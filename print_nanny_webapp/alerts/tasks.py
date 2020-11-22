from django.contrib.auth import get_user_model
from django.apps import apps
from django.utils import timezone
import logging
import datetime
import json
import io
import tempfile
from prometheus_client import Info
from prometheus_client import Counter
from celery import shared_task
from celery import group, chain, chord
import pandas as pd
import socket
import imageio
import uuid
from django.db.models import Q

from anymail.message import AnymailMessage

from config import celery_app

from print_nanny_webapp.utils import prometheus_metrics as metrics
from print_nanny_webapp.utils.predictor import ThreadLocalPredictor, predict_events_to_dataframe

TimelapseAlert = apps.get_model('alerts', 'TimelapseAlert')
DefectAlert = apps.get_model('alerts', 'DefectAlert')
PredictEvent = apps.get_model('client_events', 'PredictEvent')
PrintJob = apps.get_model('remote_control', 'PrintJob')


User = get_user_model()
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
    'CONFIDENCE_THRESHOLD': str(CONFIDENCE_THRESHOLD),
    'FAILURE_NOTIFY_THRESHOLD': str(FAILURE_NOTIFY_THRESHOLD),
    'HOSTNAME': socket.gethostname(),
})

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
    df = predict_events_to_dataframe(predict_events)
    

    # NUM_DETECTIONS_PER_FRAME = len(df['detection_scores'].iloc[0])

    # df = df[['detection_classes', 'detection_scores']]
    # df = df.reset_index()
    # df = df.rename(columns={'id': 'frame_id' })
    # NUM_FRAMES = len(df)

    # # explode detection_classes and detection_scores together
    # df = df.set_index(['frame_id']).apply(pd.Series.explode).reset_index()
    # assert len(df) == NUM_FRAMES * NUM_DETECTIONS_PER_FRAME
 
    # # add string labels
    # df['label'] = df['detection_classes'].map(LABELS)

    # # create a hierarchal index
    # df = df.set_index(['frame_id', 'label'])
    return df

@shared_task
def download_annotated_image(url):
    return imageio.imread(url)

@shared_task
def send_timelapse_upload_email_notification(annotated_video, timelapse_alert_id, ratio, fps):

    # https://github.com/imageio/imageio-ffmpeg/issues/28
    # ffmpeg is opened in a subprocess, which does not support io.BytesIO()
    # with tempfile.NamedTemporaryFile() as f:

    #     imageio.mimwrite(f, annotated_images, fps=fps, format='FFMPEG')
    #     f.seek(0)
    #     img_file = ImageFile(f, name=buff.name)

    alert_message = TimelapseAlert.objects.filter(
            id=timelapse_alert_id
        ).update(
            annotated_video = annotated_video,
            ratio = ratio, 
            dataframe = df.to_json(orient='records')
    )

    merge_data = {
        'RATIO': '{:.2%}'.format(ratio),
        'ORIGINAL_VIDEO': alert_message.original_video.url,
        'VIDEO_URL': alert_message.annotated_video.url,
        # 'FEEDBACK_POSITIVE': reverse('view_name', 
        # 'FEEDBACK_NEGATIVE': 
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
def send_print_job_failure_notification(df, ratio):
    if ratio <= FAILURE_NOTIFY_THRESHOLD:
        return
    logging.info(f'Calling {notify_callback} in worker thread')

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
def log_metrics(df, notify_callback=None, alert_cls=DefectAlert):
    """
        df - prediction_dataframe()
    """

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

    if notify_callback is not None:
        logging.info(f'Calling {notify_callback} in worker thread')
        notify_callback(fail_df, ratio=ratio)

    ### Log metrics
    for label, num_detections in confident_df.groupby(level='label').size().items():
        metrics.detections_per_minute.labels(
            detection_class=label,
            alert_type=alert_cls.__name__
            ).observe(num_detections)
    
    for (frame_id, label), num_detections in confident_df.groupby(['frame_id', 'label']).size().items():
        metrics.detections_per_frame.labels(
            detection_class=label,
            alert_type=alert_cls.__name__
            ).observe(num_detections)
 
    for (frame_id, label), (_, score) in confident_df.iterrows():
        metrics.detections_confidence_per_label.labels(
            detection_class=label,
            alert_type=alert_cls.__name__
            ).observe(score)

    return fail_df, ratio

@shared_task
def predict_postprocess_frame(frame_id, frame):
    predictor = ThreadLocalPredictor()
    predict_data = predictor.predict(frame)
    predict_data['annotated_image'] = predictor.postprocess(frame, predict_data)
    return {'predict_data': predict_data, 'id': frame_id }

@shared_task
def save_annotated_video(df, timelapse_alert_id):

    buff = io.BytesIO()
    imageio.mimwrite(buff, df['annotated_images'], format='GIF-PIL')
    buff.seek(0)
    filename = f'timelapse_alert_{timelapse_alert_id}_annotated.gif'
    img_file = ImageFile(buff, name=filename)
    return TimelapseAlert.objects.filter(id=timelapse_alert_id).update(
        annotated_video=img_file
    )

@shared_task
def prediction_dicts_to_dataframe(predict_dicts):
    logger.info(predict_dicts)
    df = pd.DataFrame.from_records(predict_dicts, index='id')
    df = df.dropna()
    df = df['predict_data'].apply(dict_to_series)
    return df


@shared_task(soft_time_limit=300, time_limit=400)
def analyze_timelapse_video(timelapse_alert_id, file_path):
    reader = imageio.get_reader(file_path)
    fps = reader.get_meta_data()['fps']

    logger.info(reader.get_meta_data())

    # https://github.com/imageio/imageio-ffmpeg/issues/28
    # ffmpeg is opened in a subprocess, which does not support io.BytesIO()

    # df_workflow = chord(
    #     predict_postprocess_frame.chunks(enumerate(reader),5),
    #     prediction_dicts_to_dataframe.s()
    # )
    return group(
        predict_postprocess_frame.si(i, frame) for i, frame in enumerate(reader)
    )

    # return chain(
    #     prediction_dicts_s,
    #     prediction_dicts_to_dataframe.s(),
    #     group(
    #         save_annotated_video.s(timelapse_alert_id),
    #         log_metrics.s(notify_callback=None, alert_cls=TimelapseAlert)
    #     )
    # )()

    # with tempfile.NamedTemporaryFile() as f:
    #     with imageio.get_writer(f, format='GIF-PIL', fps=fps) as w:
    #         predictor = ThreadLocalPredictor()
    #         prediction_data = [
    #             predict_postprocess_frame(i, image)
    #             for i, image in enumerate(reader)
    #         ]
    #         img_file = ImageFile(f)

    # df = predict_events_to_dataframe(prediction_data)


    # fail_df, ratio = log_metrics(
    #     df, 
    #     notify_callback=None,
    #     alert_cls=TimelapseAlert
    # )

    #send_timelapse_upload_email_notification(img_file, timelapse_alert_id, ratio, fps)

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
                notify_callback=send_email_failure_notification
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