from django.http import HttpResponsePermanentRedirect


class DomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().partition(":")[0]
        if "print-nanny.com" in host:
            return HttpResponsePermanentRedirect("https://printnanny.ai" + request.path)
        else:
            return self.get_response(request)
