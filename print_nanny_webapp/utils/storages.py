from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import safe_join


class StaticRootGoogleCloudStorage(GoogleCloudStorage):
    location = "static"
    default_acl = "publicRead"


class MediaRootGoogleCloudStorage(GoogleCloudStorage):
    location = "media"
    file_overwrite = False

    def _normalize_name(self, name):
        """
        Normalizes the name so that paths like /path/to/ignored/../something.txt
        and ./file.txt work.  Note that clean_name adds ./ to some paths so
        they need to be fixed here. We check to make sure that the path pointed
        to is not outside the directory specified by the LOCATION setting.
        """
        try:
            return safe_join(self.location, name)
        except ValueError:
            pass
        # celeryworker       | [2020-11-24 20:37:53,210: INFO/ForkPoolWorker-32] Uploading to path
        # celeryworker       | [2020-11-24 20:37:53,263: WARNING/ForkPoolWorker-32] ******
        # celeryworker       | [2020-11-24 20:37:53,263: WARNING/ForkPoolWorker-32] media
        # celeryworker       | [2020-11-24 20:37:53,263: WARNING/ForkPoolWorker-32] uploads/TimelapseAlert/2020/Nov/25/timelapse_alert_551_annotated.mp4
        # celeryworker       | [2020-11-24 20:37:53,565: WARNING/ForkPoolWorker-32] ******
        # celeryworker       | [2020-11-24 20:37:53,565: WARNING/ForkPoolWorker-32] media
        # celeryworker       | [2020-11-24 20:37:53,565: WARNING/ForkPoolWorker-32] uploads/TimelapseAlert/2020/Nov/25/timelapse_alert_551_annotated.mp4
        # celeryworker       | [2020-11-24 20:37:55,736: INFO/ForkPoolWorker-32] Updated 551 with /tmp/tmptlt4j77a/timelapse_alert_551_annotated.mp4
        # celeryworker       | [2020-11-24 20:37:55,763: INFO/MainProcess] Received task: print_nanny_webapp.alerts.tasks.rm_tmp_dir[1e25cff2-f0e1-4a7a-b66c-2fd6716ce2a
        # except ValueError:
        #     raise SuspiciousOperation("Attempted access to '%s' denied." %
        #                               name)
