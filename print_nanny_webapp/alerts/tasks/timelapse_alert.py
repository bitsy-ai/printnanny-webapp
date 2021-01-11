import imageio
import logging
import tempfile
import os
import socket

from anymail.message import AnymailMessage
from celery import group, chord, shared_task
from django.apps import apps
from django.template.loader import render_to_string
from django.conf import settings

from print_nanny_webapp.utils.predictor import ThreadLocalPredictor
from .common import (
    prediction_dicts_to_dataframe,
    render_alert_annotated_video,
    create_report_card,
    rm_tmp_dir,
)

logger = logging.getLogger(__name__)

# ManualVideoUploadAlert = apps.get_model("alerts", "ManualVideoUploadAlert")


@shared_task
def annotate_job_success(alert_id):
    alert = ManualVideoUploadAlert.objects.filter(id=alert_id).update(
        job_status=ManualVideoUploadAlert.JobStatusChoices.SUCCESS
    )


@shared_task
def annotate_job_error(alert_id):
    logger.error(f"Marking ManualVideoUploadAlert {alert_id} as FAILURE")
    alert = ManualVideoUploadAlert.objects.filter(id=alert_id).update(
        job_status=ManualVideoUploadAlert.JobStatusChoices.FAILURE
    )


@shared_task
def send_timelapse_upload_email_notification(timelapse_alert_id):

    timelapse_alert = ManualVideoUploadAlert.objects.get(id=timelapse_alert_id)

    merge_data = {
        "REPORT_URL": reverse(
            "dashboard:report-cards:detail", kwargs={"id": timelapse_alert_id}
        ),
        "FIRST_NAME": timelapse_alert.user.first_name or "Maker",
        "ORIGINAL_FILENAME": timelapse_alert.original_filename,
        "NOTIFY_TIMECODE": timelapse_alert.notify_timecode,
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
    message.attach_alternative(html_body, "text/html")
    message.send()

    return message


@shared_task
def predict_postprocess_frame(frame_id, frame, temp_dir):
    predictor = ThreadLocalPredictor()
    predict_data = predictor.predict(frame)
    annotated_image = predictor.postprocess(frame, predict_data)
    imageio.imwrite(os.path.join(temp_dir, str(frame_id) + ".jpg"), annotated_image)
    return {"predict_data": predict_data, "id": frame_id}


@shared_task()
def create_analyze_video_task(timelapse_alert_id):
    logger.info(f"Processing video for timelapse_alert_id {timelapse_alert_id}")
    alert = ManualVideoUploadAlert.objects.get(id=timelapse_alert_id)

    filename, ext = os.path.splitext(alert.original_video.name)
    reader = imageio.get_reader(alert.original_video.read(), ext)
    metadata = reader.get_meta_data()

    fps = metadata["fps"]

    alert.fps = fps
    alert.length = metadata["duration"]
    alert.save()

    CHUNKS = int(fps)
    temp_dir = tempfile.mkdtemp(dir=settings.MEDIA_ROOT)

    grouped = predict_postprocess_frame.chunks(
        ((i, frame, temp_dir) for i, frame in enumerate(reader)), CHUNKS
    ).group()

    chord1 = chord(grouped, prediction_dicts_to_dataframe.s())

    report_card_tasks = group(
        [
            # render_annotated_gif.si(timelapse_alert_id, temp_dir, fps),
            render_alert_annotated_video.si(timelapse_alert_id, temp_dir, fps),
            create_report_card.s(
                timelapse_alert_id,
                temp_dir,
                fps,
                send_timelapse_upload_email_notification,
            ),
        ]
    )

    chord1.link(report_card_tasks)
    chord1.link_error(annotate_job_error.si(timelapse_alert_id))

    report_card_tasks.link(rm_tmp_dir.si(temp_dir))
    report_card_tasks.link(annotate_job_success.si(timelapse_alert_id))
    report_card_tasks.link_error(annotate_job_error.si(timelapse_alert_id))

    chord1.set(queue=socket.gethostname())
    report_card_tasks.set(queue=socket.gethostname())
    return chord1()
