import logging
import io

from uuid import UUID
import tensorflow as tf
from PIL import Image
import numpy as np

from django.apps import apps
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from print_nanny_webapp.videos.services import finalize_video_recording
from print_nanny_webapp.utils.tf_object_detection.visualization_utils import (
    draw_bounding_boxes_on_image_tensors,
)
from config import celery_app

logger = logging.getLogger(__name__)

DemoSubmission = apps.get_model("videos", "DemoSubmission")


@celery_app.task()
def finalize_video_recording_task(video_recording_id: UUID):
    return finalize_video_recording(video_recording_id)


@celery_app.task()
def demo_task(challenge_id: UUID):
    entry = DemoSubmission.objects.get(id=challenge_id)
    logger.info("Processing ChallengeCampaignLead id=%s", entry.id)

    entry.submission.open()
    img = Image.open(entry.submission)
    img_arr = np.array(img)
    tensors = tf.image.resize(
        img_arr,
        [320, 320],
        preserve_aspect_ratio=False,
        antialias=False,
    )

    quantized, _output_max, _output_min = tf.quantization.quantize(
        tensors,
        0,
        256,
        tf.quint8,
    )
    batched = tf.expand_dims(quantized, axis=0)
    interpreter = tf.lite.Interpreter(model_path=settings.TFLITE_MODEL)
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.allocate_tensors()
    interpreter.set_tensor(input_details[0]["index"], batched)
    interpreter.invoke()

    boxes = interpreter.get_tensor(output_details[0]["index"])
    classes = interpreter.get_tensor(output_details[1]["index"])
    scores = interpreter.get_tensor(output_details[2]["index"])

    output_tensor = draw_bounding_boxes_on_image_tensors(
        tf.expand_dims(img_arr, axis=0),
        boxes,
        classes,
        scores,
        settings.TFLITE_CATEGORY_INDEX,
        min_score_thresh=0.66,
    )
    output_img = tf.keras.preprocessing.image.array_to_img(tf.squeeze(output_tensor))
    buf = io.BytesIO()
    output_img.save(buf, format="JPEG")
    entry.result.save(entry.submission.name, buf)
    logger.info("Saved ChallengeCampaignLead.result id=%s", entry.id)

    msg = EmailMultiAlternatives(
        subject="[PrintNanny] Your results are in 🔮",
        body=f"You can view/share your results: https://printnanny.ai/demo/{entry.id}",
        from_email="PrintNanny <noreply@mail.printnanny.ai>",
        to=[entry.email],
        reply_to=["Support <support@printnanny.ai>"],
    )
    msg.metadata = {"tflite_model_version": "20201101015829"}  # type: ignore[attr-defined]
    msg.tags = ["marketing", "demo"]  # type: ignore[attr-defined]
    msg.track_clicks = True  # type: ignore[attr-defined]
    msg.send()
