import io
import tempfile

from celery import group, shared_task, chain
import imageio
from PIL import Image
from django.core.files.images import File
from django.conf import settings
from django.apps import apps
from django.template.loader import render_to_string

ObjectDetectEvent = apps.get_model("events", "ObjectDetectEvent")
ProgressAlert = apps.get_model("alerts", "ProgressAlert")


@shared_task
def download_frame(predict_event):
    return predict_event.files.annotated_image.read()


@shared_task
def create_video(annotated_images, alert_id):
    file = io.BytesIO()
    filename = f"alert_id_{alert_id}.mp4"
    file.name = filename
    imageio.imwrite(file, [Image(img_bytes) for img_bytes in annotated_images])

    file.seek(0)
    wrapped_file = File(f)
    alert = ProgressAlert.objects.get(id=alert_id)
    alert.annotated_video.save(filename, wrapped_file)


@shared_task
def send_progress_email_notification(alert_id, progress):

    alert = ProgressAlert.objects.get(id=alert_id)

    merge_data = {
        "REPORT_URL": reverse("dashboard:report-cards:detail", kwargs={"id": alert_id}),
        "FIRST_NAME": alert.user.first_name or "Maker",
        "FILENAME": alert.print_job.filename,
        "PROGRESS": progress,
    }

    text_body = render_to_string("email/progress_alert_body.txt", merge_data)
    html_body = render_to_string("email/progress_alert_body.html", merge_data)
    subject = render_to_string("email/progress_alert_subject.txt", merge_data)

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[alert.user.email],
        tags=alert.tags,  # Anymail extra in constructor
    )
    message.attach_alternative(html_body, "text/html")
    message.send()

    return message


@shared_task
def create_progress_video_task(print_job_id, user_id, progress, fps=10):
    logger.info(f"Processing progress for print_job_id {print_job_id} @ {progress}%")

    alert = ProgressAlert.objects.create(
        print_job=print_job_id, user=user_id, progress=progress
    )

    predict_events = ObjectDetectEvent.objects.filter(print_job=print_job_id).order_by("dt")

    temp_dir = tempfile.mkdtemp(dir=settings.MEDIA_ROOT)

    video_task = group([download_frame.si(e) for e in predict_events]) | create_video.s(
        alert.id
    )

    df = prediction_dicts_to_dataframe([p.predict_data for p in predict_events])

    workflow = group(
        video_task, create_report_card.si(df, alert.id, temp_dir, fps, callback)
    )
