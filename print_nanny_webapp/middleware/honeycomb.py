import contextlib
from django.db import connections
import logging
from beeline.middleware.django import HoneyMiddlewareBase, HoneyDBWrapper


class HoneyMiddlewareIgnoreHealthCheck(HoneyMiddlewareBase):

    ignored = ["health", "static"]

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
