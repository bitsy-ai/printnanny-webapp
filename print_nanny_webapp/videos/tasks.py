import logging
import io

from uuid import UUID
import tensorflow as tf
from PIL import Image
import numpy as np

from django.apps import apps
from django.conf import settings

from print_nanny_webapp.videos.services import finalize_video_recording
from config import celery_app

logger = logging.getLogger(__name__)

ChallengeCampaignLead = apps.get_model("videos", "ChallengeCampaignLead")


@celery_app.task()
def finalize_video_recording_task(video_recording_id: UUID):
    return finalize_video_recording(video_recording_id)


@celery_app.task()
def printnanny_challenge_task(challenge_id: int):
    entry = ChallengeCampaignLead.objects.get(id=challenge_id)
    logger.info("Processing ChallengeCampaignLead id=%s", entry.id)

    entry.submission.open()
    img = Image.open(entry.submission)
    tensors = tf.image.resize(
        img,
        [320, 320],
        preserve_aspect_ratio=False,
        antialias=False,
    )

    interpreter = tf.lite.Interpreter(model_path=settings.TFLITE_MODEL)
    interpreter.allocate_tensors()
    interpreter.set_tensor(0, tensors)
    interpreter.invoke()

    boxes = interpreter.result()
    colors = np.array(
        [
            [128, 255, 0],  # nozzle: green
            [255, 0, 0],  # adhesion: red
            [255, 153, 51],  # spaghetti: orange
            [178, 102, 255],  # print: purple
            [51, 255, 255],  # raft: cyan
        ]
    )
    output_tensor = tf.image.draw_bounding_boxes([tensors], boxes, colors)
    output_img = tf.keras.preprocessing.image.array_to_img(output_tensor)
    buf = io.BytesIO()
    output_img.save(buf, format="JPEG")
    entry.result.save(entry.submission.filename, buf)
    logger.info("Saved ChallengeCampaignLead.result id=%s", entry.id)
