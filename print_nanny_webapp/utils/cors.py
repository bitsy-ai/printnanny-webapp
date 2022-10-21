from corsheaders.signals import check_request_enabled


# set CORS headers on non-API routes - API requests will originate from client-side javascripts running in OctoPrint, Mainsail, etc.
def cors_allow_api_to_everyone(_sender, request, **_kwargs):
    return request.path.startswith("/api/")


check_request_enabled.connect(cors_allow_api_to_everyone)
