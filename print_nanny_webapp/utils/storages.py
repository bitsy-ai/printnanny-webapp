from storages.backends.gcloud import GoogleCloudStorage
from google.cloud import storage
from datetime import datetime, timedelta
from typing import Dict, Any
import google.auth

credentials, project_id = google.auth.default()

# Perform a refresh request to get the access token of the current credentials (Else, it's None)
from google.auth.transport import requests
from storages.utils import (
    check_location,
    clean_name,
    get_available_overwrite_name,
    safe_join,
    setting,
)


class StaticRootGoogleCloudStorage(GoogleCloudStorage):
    location = "static"
    default_acl = "publicRead"


# based on: https://stackoverflow.com/questions/64234214/how-to-generate-a-blob-signed-url-in-google-cloud-run
class SignBlob:
    def get_sign_kwargs(self) -> Dict[str, Any]:
        r = requests.Request()
        credentials.refresh(r)
        return {
            "service_account_email": credentials.service_account_email,
            "access_token": credentials.token,
        }


class MediaRootGoogleCloudStorage(GoogleCloudStorage, SignBlob):
    location = "media"
    file_overwrite = True
    default_acl = "projectPrivate"

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

    def url(self, name, version="v4"):
        """
        Return public url or a signed url for the Blob.
        This DOES NOT check for existance of Blob - that makes codes too slow
        for many use cases.
        """
        name = self._normalize_name(clean_name(name))
        blob = self.bucket.blob(name)
        sign_kwargs = self.get_sign_kwargs()
        return blob.generate_signed_url(
            expiration=self.expiration, version=version, **sign_kwargs
        )


class PublicGoogleCloudStorage(GoogleCloudStorage, SignBlob):
    location = "public"
    file_overwrite = True
    default_acl = "publicRead"

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

    def url(self, name, version="v4"):
        """
        Return public url or a signed url for the Blob.
        This DOES NOT check for existance of Blob - that makes codes too slow
        for many use cases.
        """
        name = self._normalize_name(clean_name(name))
        blob = self.bucket.blob(name)
        sign_kwargs = self.get_sign_kwargs()
        return blob.generate_signed_url(
            expiration=self.expiration, version=version, **sign_kwargs
        )
