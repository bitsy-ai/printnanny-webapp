from django.contrib.auth import get_user_model
from django.apps import apps
from django.utils import timezone
from django.core.files.images import ImageFile, File
from django.template.loader import render_to_string
from django.conf import settings

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
import numpy as np
import socket
import imageio
import uuid
import os
from django.urls import reverse
from django.db.models import Q
from skimage.io import imread_collection
import plotly.express as px
import plotly.graph_objects as go
import shutil

from scipy import signal
import sys

from anymail.message import AnymailMessage

from config import celery_app

from print_nanny_webapp.utils import prometheus_metrics as metrics
from print_nanny_webapp.utils.predictor import ThreadLocalPredictor, predict_events_to_dataframe

TimelapseAlert = apps.get_model('alerts', 'TimelapseAlert')
DefectAlert = apps.get_model('alerts', 'DefectAlert')
AlertPlot = apps.get_model('alerts', 'AlertPlot')

PredictEvent = apps.get_model('client_events', 'PredictEvent')
PrintJob = apps.get_model('remote_control', 'PrintJob')


User = get_user_model()
logger = logging.getLogger(__name__)
pd.options.plotting.backend = "plotly"

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
        'RESUME_URL': f'http://loctask_id=str(uuid4())ail/print_alert_message_subject.txt", merge_data).strip()'
    }
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


def calc_metrics(df, framerate):

    def _seconds(value):
        if isinstance(value, str):  # value seems to be a timestamp
            _zip_ft = zip((3600, 60, 1, 1/framerate), value.split(':'))
            return sum(f * float(t) for f,t in _zip_ft)
        elif isinstance(value, (int, float)):  # frames
            return value / framerate
        else:
            return 0

    def _timecode(seconds):
        return '{h:02d}:{m:02d}:{s:02d}:{f:02d}' \
                .format(h=int(seconds/3600),
                        m=int(seconds/60%60),
                        s=int(seconds%60),
                        f=round((seconds-int(seconds))*framerate))

    def _frames(seconds):
        return seconds * framerate

    def timecode_to_frames(timecode, fps):
        return _frames(_seconds(timecode) - _seconds(start))

    def frames_to_timecode(frames, start=None):
        return _timecode(_seconds(frames) + _seconds(start))

    NUM_DETECTIONS_PER_FRAME = len(df['detection_scores'].iloc[0])
    df = df[['detection_classes', 'detection_scores']]
    df = df.reset_index()
    df = df.rename(columns={'id': 'frame_id' })
    NUM_FRAMES = len(df)
    df['timecode'] = df['frame_id'].apply(frames_to_timecode)
    # explode detection_classes and detection_scores together
    df = df.set_index(['frame_id']).apply(pd.Series.explode).reset_index()
    assert len(df) == NUM_FRAMES * NUM_DETECTIONS_PER_FRAME
 
    # add string labels
    df['label'] = df['detection_classes'].map(LABELS)

    # create a hierarchal index
    df = df.set_index(['frame_id', 'label'])


    confident_df = df[df['detection_scores'] > CONFIDENCE_THRESHOLD]
    mask = (df['detection_scores'] > CONFIDENCE_THRESHOLD) & (df['detection_classes'].isin(FAILURES))
    fail_df = df[mask]

    return df, fail_df, confident_df

@shared_task
def log_metrics(df, notify_callback=None, alert_cls=DefectAlert):
    """
        df - prediction_dataframe()
    """
    NUM_FRAMES = len(df.groupby('frame_id').count().index)
    metrics.predict_frames_per_minute.observe(NUM_FRAMES)

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

def savgol_filter(x, fps):
    logger.info(type(x))
    # assert x > window
    if len(x) <= fps:
        window = len(x)//8
    else:
        window = int(fps)
    
    # window must be an odd number
    if window % 2 == 0:
        window += 1
    
    # assert polyorder < window
    if window <= 3:
        return x
    
    return signal.savgol_filter(
        x,
        window,
        1
    )

@shared_task
def create_box_plot(confident_df, timelapse_alert_id, temp_dir):

    filename = f'{timelapse_alert_id}_boxplot'
    fig = confident_df.reset_index().plot(
        x='label',
        y='detection_scores',
        kind='box',
        title="Print Nanny's Confidence Distribution by Label",
        color='label'
    )

    html = os.path.join(temp_dir, f'{filename}.html')
    with open(html, 'w+') as f:
        fig.write_html(
            f,
            include_plotlyjs=False,
            full_html=False
        )

    png = os.path.join(temp_dir, f'{filename}.png')
    fig.write_image(png)
    
    alert_plot = create_alert_plot(
        filename,
        temp_dir,
        sys._getframe().f_code.co_name,
        'Confidence Distribution',
        'boxplot',
        timelapse_alert_id
    )

    return alert_plot

@shared_task
def create_line_subplots(confident_df, timelapse_alert_id, temp_dir, fps):
    g = confident_df.reset_index()

    y = savgol_filter(g['detection_scores'], fps)

    fig = px.line(
        g, x='frame_id', y=y, color='label', facet_col='label', line_group='label',
        height=800, width=800, facet_col_wrap=1, facet_col_spacing=0.05
    )

    fig.update_yaxes(title_text='Confidence')
    fig.update_layout(
        overwrite=True,
        title_text="Confidence over Time, Breakout by Detection Type",
        xaxis_title='Time (frame id)',
        legend_title='Detection'
    )

    filename = f'{timelapse_alert_id}_lines_subplot'
    html = os.path.join(temp_dir, f'{filename}.html')
    with open(html, 'w+') as f:
        fig.write_html(
            f,
            include_plotlyjs=False,
            full_html=False
        )

    png = os.path.join(temp_dir, f'{filename}.png')
    fig.write_image(png)

    alert_plot = create_alert_plot(
        filename,
        temp_dir,
        sys._getframe().f_code.co_name,
        'Confidence over Time',
        'Breakout by Detection Type',
        timelapse_alert_id
    )

    return alert_plot

@shared_task()
def create_health_abs_plot(confident_df, fail_df, timelapse_alert_id, temp_dir, fps):
    g = confident_df.reset_index()

    fig = go.Figure()

    print_trace = g[g['label'] == 'print']
    fail_trace = fail_df.reset_index()

    window = int(fps)

    fig.add_trace(go.Scatter(
        x=print_trace['frame_id'], 
        y=savgol_filter(print_trace['detection_scores'],fps),
        fill=None,
        mode='lines',
        name='print'

    ))

    fig.add_trace(go.Scatter(
        x=fail_trace['frame_id'], 
        y=savgol_filter(fail_trace['detection_scores'], fps),
        fill=None,
        mode='lines',
        name='defects',    
    ))

    fig.update_layout(
        overwrite=True,
        title_text="Print Health Scores (Absolute)",
        xaxis_title='Time (frame id)',
        yaxis_title='Health Score'
    )


    filename = f'{timelapse_alert_id}_health_abs_plot'
    html = os.path.join(temp_dir, f'{filename}.html')
    with open(html, 'w+') as f:
        fig.write_html(
            f,
            include_plotlyjs=False,
            full_html=False
        )

    png = os.path.join(temp_dir, f'{filename}.png')
    fig.write_image(png)

    alert_plot = create_alert_plot(
        filename,
        temp_dir,
        sys._getframe().f_code.co_name,
        'Change in Print Health Over Time',
        'Health score over time, breakout by print vs all defects',
        timelapse_alert_id
    )

    return alert_plot

@shared_task()
def create_health_rel_plot(confident_df, fail_df,timelapse_alert_id, temp_dir, fps):
    g = confident_df.reset_index()
    print_trace = g[g['label'] == 'print']
    fail_trace = fail_df.reset_index()
    split_df = pd.concat({'fail': fail_trace, 'print': print_trace}).reset_index()

    mask = split_df.level_0 == 'fail'

    y = split_df[~mask].groupby('timecode')['detection_scores'].sum().subtract(
        split_df[mask].groupby('timecode')['detection_scores'].sum(),
        fill_value=0
    )
    fig = go.Figure(go.Waterfall(
        orientation = "v",
        x = y.index,
        y =  y,
    ))

    fig.update_layout(
        overwrite=True,
        title_text="Change in Print Health Over Time",
        xaxis_title='Time (relative)',
        yaxis_title='Health Score'
    )

    fig.update_xaxes(
        nticks=20
    )

    if len(y[y < 0]) >= (fps/2):
        alert_offset = int(fps/2)

        fig.add_annotation(
            x=y[y < 0].index[alert_offset],
            y=1,
            text="Print Nanny alerts you at this time",
            showarrow=True,
            arrowhead=1
        )

        fig.add_vrect(
            x0=y[y < 0].index[alert_offset], x1=y[y < 0].index[-1],
            fillcolor="LightSalmon", opacity=0.5,
            layer="below", line_width=0,
        )

    filename = f'{timelapse_alert_id}_health_rel_plot'

    png = os.path.join(temp_dir, f'{filename}.png')
    fig.write_image(png)

    html = os.path.join(temp_dir, f'{filename}.html')
    with open(html, 'w+') as f:
        fig.write_html(
            f,
            include_plotlyjs=False,
            full_html=False
        )

    alert_plot = create_alert_plot(
        filename,
        temp_dir,
        sys._getframe().f_code.co_name,
        'Change in Print Health Over Time',
        'Relative change (waterfall) health scores over time',
        timelapse_alert_id
    )

    return alert_plot

def create_alert_plot(filename, tmp_dir, function, title, description, alert_id):
    
    with open(os.path.join(tmp_dir, filename + '.png'), 'rb') as png_f:
        wrapped_png = ImageFile(png_f)
        with open(os.path.join(tmp_dir, filename + '.html'), 'rb') as html_f:
            wrapped_html = File(html_f)
            alert_plot = AlertPlot(
                function=function,
                title=title,
                description=description,
                alert=TimelapseAlert.objects.get(id=alert_id)
            )
            alert_plot.image.save(filename + '.png', wrapped_png)
            alert_plot.html.save(filename + '.html', wrapped_html)
            alert_plot.save()
            return alert_plot
        
@shared_task
def create_report_card(df, timelapse_alert_id, temp_dir, fps):

    multi_df, fail_df, confident_df = calc_metrics(df, fps)

    filename = f'timelapse_alert_{timelapse_alert_id}_dataframe.csv'
    csv = os.path.join(temp_dir, filename)
    with open(csv, 'w+') as f:
        multi_df.to_csv(f)
    TimelapseAlert.objects.filter(id=timelapse_alert_id).update(
        dataframe=csv
    )

    workflow = group([
        create_box_plot.si(confident_df, timelapse_alert_id, temp_dir),
        create_line_subplots.si(confident_df, timelapse_alert_id, temp_dir, fps),
        create_health_abs_plot.si(confident_df, fail_df, timelapse_alert_id, temp_dir, fps),
        create_health_rel_plot.si(confident_df, fail_df, timelapse_alert_id, temp_dir, fps)
    ]) | send_timelapse_upload_email_notification.si(timelapse_alert_id, temp_dir)

    
    return workflow()

@shared_task
def render_annotated_video(timelapse_alert_id, temp_dir, fps):
    annotated_images = imread_collection(temp_dir + "/*.jpg")
    filename = f'timelapse_alert_{timelapse_alert_id}_annotated.mp4'
    file_path = os.path.join(temp_dir, filename)
    imageio.mimwrite(file_path, annotated_images, fps=fps, format='FFMPEG')

    with open(file_path, 'rb') as f:
        wrapped_file = File(f)
        timelapse_alert = TimelapseAlert.objects.get(
                id=timelapse_alert_id
        )
        timelapse_alert.annotated_video.save(filename, wrapped_file)

    logging.info(f'Updated {timelapse_alert_id} with {file_path}')
    return timelapse_alert

@shared_task
def send_timelapse_upload_email_notification(timelapse_alert_id, temp_dir):

    timelapse_alert = TimelapseAlert.objects.get(id=timelapse_alert_id)

    merge_data = {
        'REPORT_URL': reverse('dashboard:report-cards:detail', kwargs={'id': timelapse_alert_id}),
        'FIRST_NAME': timelapse_alert.user.first_name or 'Maker',
        'ORIGINAL_FILENAME': timelapse_alert.original_filename
    }

    text_body = render_to_string("email/timelapse_alert_body.txt", merge_data)
    html_body = render_to_string("email/timelapse_alert_body.html", merge_data)
    subject = render_to_string("email/timelapse_alert_subject.txt", merge_data)

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[timelapse_alert.user.email],
        tags=["default-print-alert"],  # Anymail extra in constructor
    )
    message.attach_alternative(html_body, 'text/html')
    message.send()

    return message

@shared_task
def prediction_dicts_to_dataframe(predict_dicts):
    predict_dicts = np.array(predict_dicts, dtype=np.object)
    predict_dicts = np.hstack(predict_dicts)
    df = pd.DataFrame.from_records(predict_dicts, index='id')
    df = df.dropna()
    df = df['predict_data'].apply(dict_to_series)

    return df

@shared_task
def predict_postprocess_frame(frame_id, frame, temp_dir):
    predictor = ThreadLocalPredictor()
    predict_data = predictor.predict(frame)
    annotated_image = predictor.postprocess(frame, predict_data)
    imageio.imwrite(os.path.join(
        temp_dir, str(frame_id) + '.jpg'
    ), annotated_image)
    return {'predict_data': predict_data, 'id': frame_id }

@shared_task
def rm_tmp_dir(temp_dir):
    return shutil.rmtree(temp_dir)

@shared_task
def annotate_job_success(alert_id):
    alert = TimelapseAlert.objects.filter(id=alert_id).update(
        job_status=TimelapseAlert.JobStatusChoices.SUCCESS
    )

@shared_task
def annotate_job_error(alert_id):
    logger.error(f'Marking TimelapseAlert {alert_id} as FAILURE')
    alert = TimelapseAlert.objects.filter(id=alert_id).update(
        job_status=TimelapseAlert.JobStatusChoices.FAILURE
    )

@shared_task()
def create_analyze_video_task(timelapse_alert_id, file_path):
    '''

    '''

    reader = imageio.get_reader(file_path)
    fps = reader.get_meta_data()['fps']

    CHUNKS = int(fps//2) 
    temp_dir = tempfile.mkdtemp(dir=settings.MEDIA_ROOT)
    grouped = predict_postprocess_frame.chunks( 
        ((i, frame, temp_dir) for i, frame in enumerate(reader))
        , CHUNKS).group() 
    chord1 = chord(grouped, prediction_dicts_to_dataframe.s())

    report_card_tasks = group([
        #render_annotated_gif.si(timelapse_alert_id, temp_dir, fps),
        render_annotated_video.si(timelapse_alert_id, temp_dir, fps),
        create_report_card.s(timelapse_alert_id, temp_dir, fps)
    ])


    chord1.link(report_card_tasks)
    chord1.link_error(annotate_job_error.si(timelapse_alert_id))

    report_card_tasks.link(rm_tmp_dir.si(temp_dir))
    report_card_tasks.link(annotate_job_success.si(timelapse_alert_id))
    report_card_tasks.link_error(annotate_job_error.si(timelapse_alert_id))

    return chord1()

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