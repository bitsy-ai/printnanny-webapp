from django.contrib.auth import get_user_model
from django.apps import apps
from django.utils import timezone
import logging
import datetime
import json
import io
from prometheus_client import Info
from prometheus_client import Counter
from celery import shared_task
from celery import group, chain
import pandas as pd
import socket
import imageio
import uuid
from django.db.models import Q

from anymail.message import AnymailMessage

from config import celery_app
from .models import PredictEvent, PrintJob
User = get_user_model()


from print_nanny_webapp.client_events import metrics

logger = logging.getLogger(__name__)

EVERY_N_SECONDS = 60.0

# minimum confidence score for detection to be accepted for post-processing
CONFIDENCE_THRESHOLD = 0.5
# minimum ratio of failed:neutral detections required to send email
FAILURE_NOTIFY_THRESHOLD = 0.5
# small number added to ratio denominator
FAILURE_EPSILON = 1e-7

LABELS = {
    1: 'nozzle',
    2: 'adhesion',
    3: 'spaghetti',
    4: 'print',
    5: 'raft',
}

FAILURES = {
    2: 'adhesion',
    3: 'spaghetti',  
}

metrics.build_version.info({
    'CONFIDENCE_THRESHOLD': CONFIDENCE_THRESHOLD,
    'FAILURE_NOTIFY_THRESHOLD': FAILURE_NOTIFY_THRESHOLD,
    'HOSTNAME': socket.gethostname(),
})

def dict_to_series(data):
    return pd.Series(data.values(), index=data.keys())

@shared_task
def predict_events_dataframe(print_job_id, start=None, stop=None):
    '''
        notify-exploration.ipynb
    '''

    if start and stop:
        predict_events = PredictEvent.objects.filter(
            print_job=print_job_id,
            dt__range=(start, stop)
        ).order_by('-dt').values('id','predict_data').all()
    elif start:
        predict_events = PredictEvent.objects.filter(
            print_job=print_job_id,
            dt__gte=start
        ).order_by('-dt').values('id','predict_data').all()
    elif stop:
        predict_events = PredictEvent.objects.filter(
            print_job=print_job_id,
            dt__gte=start
        ).order_by('-dt').values('id','predict_data').all()
    else:
        predict_events = PredictEvent.objects.filter(
            print_job=print_job_id,
        ).order_by('-dt').values('id','predict_data').all()   

    if predict_events.count() == 0:
        logger.error(f'0 predict_events for print_job {print_job_id}')
        return

    logger.info(f'Analyzing {predict_events.count()} predict_events for print_job {print_job_id}')

    # project predict_data JSONField to Series columns
    df = pd.DataFrame.from_records(predict_events, index='id')
    df = df.dropna()
    df = df['predict_data'].apply(dict_to_series)

    NUM_DETECTIONS_PER_FRAME = len(df['detection_scores'].iloc[0])

    df = df[['detection_classes', 'detection_scores']]
    df = df.reset_index()
    df = df.rename(columns={'id': 'frame_id' })
    NUM_FRAMES = len(df)

    # explode detection_classes and detection_scores together
    df = df.set_index(['frame_id']).apply(pd.Series.explode).reset_index()
    assert len(df) == NUM_FRAMES * NUM_DETECTIONS_PER_FRAME
 
    # add string labels
    df['label'] = df['detection_classes'].map(LABELS)

    # create a hierarchal index
    df = df.set_index(['frame_id', 'label'])
    return df

@shared_task
def download_annotated_image(url):
    return imageio.imread(url)

@shared_task
def send_email_notification(df, ratio=FAILURE_NOTIFY_THRESHOLD):
    frame_ids = [frame_id for frame_id, _ in df.index]

    predict_events = PredictEvent.objects.filter(
        id__in=frame_ids,
        print_job=4        
    ).order_by('dt').all()

    print_job = predict_events[0].print_job

    # assert no previous alert messages, or all alert messages are in the "RESUMED" state 
    last_alert_message = AlertMessage.objects.filter(
        print_job=print_job.id,
    ).order_by('-created_dt').first()
    if last_alert_message is not None:
        logging.warning('Alert for print job {print_job} already sent at {alert_message.created_dt}, skipping')
        return

    # images = [ 
    #     imageio.imread(event.files.annotated_image.file.location)
    #     for event in predict_events
    # ]

    images = []

    for i, event in enumerate(predict_events):
        images.append(imageio.imread(event.files.annotated_image.file))
        print(f'finished {i}/{len(predict_events)}')
    buff = io.BytesIO()
    imageio.mimwrite(buff, images, fps=20, format='GIF-PIL')
    buff.seek(0)
    
    filename= f'print_job_{print_job.id}_alert_message_{predict_events[0].dt}_{predict_events[len(predict_events)-1].dt}'
    img_file = ImageFile(buff, name=filename)
    alert_message = AlertMessage.objects.create(
        user=print_job.user,
        print_job=print_job,
        video=img_file,
        dataframe=df.to_json(orient='records')
    )
    
    
    merge_data = {
        'RATIO': '{:.2%}'.format(ratio),
        'GCODE_FILE': print_job.gcode_file.name,
        'VIDEO_URL': alert_message.video.url,
        'STOP_URL': f'http://localhost/feedback/{alert_message.id}?action=stop_print',
        'SILENCE_URL': f'http://localhost/feedback/{alert_message.id}?action=silence',
        'RESUME_URL': f'http://localhost/feedback/{alert_message.id}?action=resume',
        'FIRST_NAME': print_job.user.first_name or 'Maker',
    }

    subject = render_to_string("email/print_alert_message_subject.txt", merge_data).strip()
    text_body = render_to_string("email/print_alert_message_body.txt", merge_data)
    html_body = render_to_string("email/print_alert_message_body.html", merge_data)

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[predict_events[0].user.email],
        tags=["default-print-alert"],  # Anymail extra in constructor
    )
    message.attach_alternative(html_body, 'text/html')
    return message.send()

@shared_task
def log_metrics(df, print_job, notify_callback=None):
    """
        df - prediction_dataframe()
    """

    NUM_FRAMES = len(df.groupby('frame_id').count().index)
    metrics.predict_frames_per_minute.observe(NUM_FRAMES)

    confident_df = df[df['detection_scores'] > CONFIDENCE_THRESHOLD]
    mask = (df['detection_scores'] > CONFIDENCE_THRESHOLD) & (df['detection_classes'].isin(FAILURES))
    fail_df = df[mask]

    mask = (df['detection_scores'] > CONFIDENCE_THRESHOLD) & (~df['detection_classes'].isin(FAILURES))
    neutral_df = df[mask]

    # at least 1 neutral detection in the frame
    num_neutral = len(neutral_df.groupby('frame_id'))
    # at least 1 failed detection in the frame
    num_failed = len(fail_df.groupby('frame_id'))

    # compare failed:neutral detection ratio
    ratio = num_failed / (num_neutral + FAILURE_EPSILON)
    metrics.detections_failure_ratio.observe(ratio)
    logging.info(f'num_failed:num_neutral ratio {ratio}')
    if ratio > FAILURE_NOTIFY_THRESHOLD:
        logging.info(f'Calling {notify_callback} in worker thread')
        if notify_callback:
            notify_callback(fail_df)


    ### Log metrics

    for label, num_detections in confident_df.groupby(level='label').size().items():
        metrics.detections_per_minute.labels(detection_class=label).observe(num_detections)
    
    for (frame_id, label), num_detections in confident_df.groupby(['frame_id', 'label']).size().items():
        metrics.detections_per_frame.labels(detection_class=label).observe(num_detections)
 
    for (frame_id, label), (_, score) in confident_df.iterrows():
        metrics.detections_confidence_per_label.labels(detection_class=label).observe(score)

    logging.info(f'Finished log_metrics_and_notify for print_job {print_job.id}')
    

@shared_task
def debug_jobs_analysis():
    """schedules ananlysis job for each recently-ish seen print job. Useful for debugging analyze task"""

    now = timezone.now()
    earlier = now - datetime.timedelta(seconds=EVERY_N_SECONDS*10000)
    print_jobs = PrintJob.objects.filter(
        last_seen__range=(earlier,now)
    )

    workflow_per_print_job = [
        chain(
            predict_events_dataframe.si(print_job.id,start=earlier, stop=now),
            log_metrics.s(
                print_job, 
                notify_callback=send_email_failure_notification.s()
            )
        )
        for print_job in print_jobs
    ]
    logger.info(f'Scheduling analysis for {print_jobs.count()} active print jobs')
    job = group(workflow_per_print_job)
    return job()

@shared_task
def schedule_active_jobs_analysis():
    """schedules ananlysis job for each active print job"""
    pass
    # now = timezone.now()
    # earlier = now - datetime.timedelta(seconds=EVERY_N_SECONDS)
    # active_print_jobs = PrintJob.objects.filter(
    #     last_status=PrintJob.StatusChoices.STARTED,
    #     last_seen__range=(earlier,now)
    # )

    # logger.info(f'Scheduling analysis for {active_print_jobs.count()} active print jobs')
    # job = group([
    #     prediction_dataframe.si(print_job.id,earlier, now)
    # ] for print_job in active_print_jobs)
    # return job()

# @celery_app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):

#     sender.add_periodic_task(EVERY_N_SECONDS, schedule_active_jobs_analysis.s(), name='active job analysis')