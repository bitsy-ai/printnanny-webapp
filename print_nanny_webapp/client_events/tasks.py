from django.contrib.auth import get_user_model
from django.apps import apps
from django.utils import timezone
import logging

import timeit

from config import celery_app
from .models import PredictEvent, PrintJob
User = get_user_model()


logger = logging.getLogger(__name__)

EVERY_N_SECONDS = 60.0

CONFIDENCE_THRESHOLD = 0.5


def dict_to_pd_series(data):
    return pd.Series(data.values(), index=data.keys())

@celery_app.task()
def analyze_predictions_over_window(print_job, start, stop):
    '''
        notify-exploration.ipynb
    '''
    predict_events = PredictEvent.objects.all().order_by('-dt').values('id','predict_data')

    
    df = pd.DataFrame.from_records(predict_events, index='id')
    # drop null
    df = df.dropna()
    # project hierarchal data to series
    df = df['predict_data'].apply(json_to_series)
    # explode num_detections dimension
    df = df[['detection_classes', 'detection_scores']]
    df = df.explode('detection_classes')

    loss = loss(df)
    

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