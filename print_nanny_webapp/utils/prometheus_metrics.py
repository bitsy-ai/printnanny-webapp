from django.apps import apps
import prometheus_client

PrintJob = apps.get_model('remote_control', 'PrintJob')


print_job_status = prometheus_client.Enum(
    'print_job_status',
    'Last seen status of a print job',
    states=PrintJob.StatusChoices.values
)

predict_frames_per_minute = prometheus_client.Summary(
    'predict_events_per_minute',
    'Raw number of events seen. Calculated via schedule_active_jobs_analysis() periodic runs'
)

detections_per_minute = prometheus_client.Summary(
    'detections_per_minute',
    'Number of detections above confidence threshold. Calculated via schedule_active_jobs_analysis() periodic run',
    ['detection_class']
)

detections_per_frame = prometheus_client.Summary(
    'detections_per_frame',
    'Number of detections above confidence threshold. Calculated via schedule_active_jobs_analysis() periodic run',
    ['detection_class']   
)

detections_confidence_per_label = prometheus_client.Summary(
    'confidence_per_label',
    'Raw confidence score per detection per label',
    ['detection_class']
)

detections_failure_ratio = prometheus_client.Summary(
    'detections_failure_ratio',
    'Num detected failure / num detected neutral frames',
)

build_version = prometheus_client.Info(
    'build_version', 
    'key:value of deployment and build configuration'
)