import logging
from corsheaders.signals import check_request_enabled


logger = logging.getLogger(__name__)

# set CORS headers on non-API routes - API requests will originate from client-side javascripts running in OctoPrint, Mainsail, etc.
def cors_allow_api_to_everyone(sender, request, **kwargs):
    logger.debug(
        "cors_allow_api_to_everyone called with sender %s request %s kwargs %s",
        sender,
        request,
        kwargs,
    )
    return request.path.startswith("/api/")


check_request_enabled.connect(cors_allow_api_to_everyone)
