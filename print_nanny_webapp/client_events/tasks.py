from django.contrib.auth import get_user_model
from django.apps import apps
from django.utils import timezone
import logging
import json
from prometheus_client import Info
from prometheus_client import Counter

import timeit

from config import celery_app
from .models import PredictEvent, PrintJob
User = get_user_model()


logger = logging.getLogger(__name__)

EVERY_N_SECONDS = 60.0

CONFIDENCE_THRESHOLD = 0.5

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

i = Info('my_build_version', 'Description of info')
i.info({'version': '1.2.3', 'buildhost': 'foo@bar'})

def dict_to_series(data):
    return pd.Series(data.values(), index=data.keys())

def publish_metrics(print_job):
    i = Info('my_build_version', 'Description of info')

@celery_app.task()
def analyze_predictions_over_window(print_job, start, stop):
    '''
        notify-exploration.ipynb
    '''

    predict_events = PredictEvent.objects.filter(
        print_job=print_job.id,
        dt__range=(start, stop)
    ).order_by('-dt').values('id','predict_data')

    # project predict_data JSONField to Series columns
    df = pd.DataFrame.from_records(predict_events, index='id')
    df = df.dropna()
    df = df['predict_data'].apply(json_to_series)

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



@celery_app.task()
def schedule_active_jobs_analysis():
    """schedules ananlysis job for each active print job"""

    now = timezone.now()
    earlier = now - datetime.timedelta(seconds=EVERY_N_SECONDS)
    active_print_jobs = PrintJob.objects.filter(
        status=PrintJob.StatusChoices.STARTED,
        last_seen__range=(earlier,now)
    )

    logger.info(f'Scheduling analysis for {active_print_jobs.count()} active print jobs')
    job = group([
        
    ])

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(EVERY_N_SECONDS, schedule_active_jobs_analysis.s(), name='active job analysis')