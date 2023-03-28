from tempfile import TemporaryDirectory, NamedTemporaryFile
import logging
import subprocess

from django.apps import apps
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)
VideoRecording = apps.get_model("videos", "VideoRecording")


def gsutil_download_paths(
    video_recording: VideoRecording, tmpdir: TemporaryDirectory
) -> str:
    # -m flag performs paallel multi-threaded copy
    # -r recursively downloads
    cmd = [
        "gsutil",
        "-m",
        "-r",
        f"gs://{settings.GS_BUCKET_NAME}/{video_recording.gsutil_pattern()}",
        tmpdir.name,
    ]
    logger.info("Running command: %s", cmd)
    subprocess.run(cmd, capture_output=True, encoding="utf8", check=True)
    return tmpdir.name


def gst_combine_mp4_parts(src: TemporaryDirectory, dest: NamedTemporaryFile):
    cmd = [
        "gst-launch-1.0",
        "playbin",
        f'uri="splitmux://{src.name}/*.mp4"',
        "!",
        "filesink",
        f"location={dest.name}",
    ]
    subprocess.run(cmd, capture_output=True, encoding="utf8", check=True)


def finalize_video_recording(video_recording_id: int):
    finalize_start = timezone.now()
    video_recording = VideoRecording.get(id=video_recording_id)
    video_recording.finalize_start = finalize_start
    video_recording.save()

    tmpdir = TemporaryDirectory()
    tmpfile = NamedTemporaryFile()
    logger.info(
        "Preparing to finalize VideoRecording id=%s count_parts=%s, downloading parts to %s",
        video_recording.id,
        video_recording.video_recording_parts_set.count(),
        tmpdir,
    )
    gsutil_download_paths(video_recording, tmpdir)
    gst_combine_mp4_parts(tmpdir, tmpfile)

    if video_recording.mp4_file is not None:
        raise FileExistsError(
            f"VideoRecording id={video_recording_id} already has mp4_file={video_recording.mp4_file}",
        )
    video_recording.mp4_file.save("final.mp4", tmpfile)
    finalize_end = timezone.now()
    video_recording.finalize_end = finalize_end
    video_recording.save()
    return True
