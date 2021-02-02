from storages.backends.gcloud import GoogleCloudStorage
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


class MediaRootGoogleCloudStorage(GoogleCloudStorage):
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
        # no_signed_url = (
        #     self.default_acl == 'publicRead' or not self.querystring_auth)

        # if not self.custom_endpoint and no_signed_url:
        #     return blob.public_url
        # elif no_signed_url:
        #     return '{storage_base_url}/{quoted_name}'.format(
        #         storage_base_url=self.custom_endpoint,
        #         quoted_name=_quote(name, safe=b"/~"),
        #     )
        # elif not self.custom_endpoint:
        return blob.generate_signed_url(self.expiration, version=version)
        # else:
        #     return blob.generate_signed_url(
        #         expiration=self.expiration,
        #         api_access_endpoint=self.custom_endpoint,
        #         version=version
        #     )


class PublicGoogleCloudStorage(GoogleCloudStorage):
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
        # no_signed_url = (
        #     self.default_acl == 'publicRead' or not self.querystring_auth)

        # if not self.custom_endpoint and no_signed_url:
        #     return blob.public_url
        # elif no_signed_url:
        #     return '{storage_base_url}/{quoted_name}'.format(
        #         storage_base_url=self.custom_endpoint,
        #         quoted_name=_quote(name, safe=b"/~"),
        #     )
        # elif not self.custom_endpoint:
        return blob.generate_signed_url(self.expiration, version=version)
        # else:
        #     return blob.generate_signed_url(
        #         expiration=self.expiration,
        #         api_access_endpoint=self.custom_endpoint,
        #         version=version
        #     )
