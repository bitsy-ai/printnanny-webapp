import contextlib
from django.db import connections
from beeline.middleware.django import HoneyMiddlewareBase, HoneyDBWrapper


class HoneyMiddlewareIgnoreHealthCheck(HoneyMiddlewareBase):

    ignored = ["health", "static", "/"]

    def __call__(self, request):

        if any(
            [
                ignored_path in request.get_full_path_info()
                for ignored_path in self.ignored
            ]
        ):
            return self.get_response(request)
        try:
            db_wrapper = HoneyDBWrapper()
            # db instrumentation is only present in Django > 2.0
            with contextlib.ExitStack() as stack:
                for connection in connections.all():
                    stack.enter_context(connection.execute_wrapper(db_wrapper))
                response = self.create_http_event(request)
        except AttributeError:
            response = self.create_http_event(request)

        return response

    def get_context_from_request(self, request):
        trace_name = "django_http_%s" % request.method.lower()
        return {
            "name": trace_name,
            "type": "http_server",
            "request.host": request.get_host(),
            "request.method": request.method,
            "request.path": request.path,
            "request.remote_addr": request.META.get("REMOTE_ADDR"),
            "request.content_length": request.META.get("CONTENT_LENGTH", 0),
            "request.user_agent": request.META.get("HTTP_USER_AGENT"),
            "request.scheme": request.scheme,
            "request.secure": request.is_secure(),
            "request.query": request.GET.dict(),
            "request.xhr": request.headers.get("x-requested-with") == "XMLHttpRequest",
            "request.post": request.POST.dict(),
            "request.user": request.user,
        }
