import prometheus_client
from .models import PrintJob
print_job_status = prometheus_client.Enum(
    'print_job_status',
    'Last seen status of a print job',
    states=PrintJob.StatusChoices.values
)