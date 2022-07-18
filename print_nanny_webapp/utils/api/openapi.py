from drf_spectacular.openapi import AutoSchema


def drf_spectacular_preprocessor(endpoints):
    orig_endpoints = endpoints.copy()
    for (path, path_regex, method, callback) in orig_endpoints:
        # add OPTIONS to any viewset with POST (create) method, exclude update-or-create actions
        # OPTIONS response is used to build forms and ui elements
        if method == "POST" and "update-or-create" not in path:
            endpoints.append([path, path_regex, "OPTIONS", callback])
    return endpoints


# extend drf_spectacular's AutoSchema class with options -> metadata mapping
class CustomAutoSchema(AutoSchema):
    method_mapping = {
        "get": "retrieve",
        "post": "create",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
        "options": "metadata",
    }
