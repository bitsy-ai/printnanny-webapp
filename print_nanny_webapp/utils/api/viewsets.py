from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin


class MetadataModelMixin:
    """
    See: https://www.mnot.net/blog/2012/10/29/NO_OPTIONS

    The purpose of this mixin is to provide a self-contained schema response for form-building
    """

    # @action(methods=["GET"], detail=False)
    # def metadata(self, request):
    #     meta = self.metadata_class()

    #     # build fake OPTIONS request for parent endpoint
    #     # copy request
    #     fake_options_req = request._request
    #     fake_options_req.path = fake_options_req.path.replace("metadata/", "")
    #     fake_options_req.method = "OPTIONS"
    #     res = self.options(fake_options_req)
    #     # data = meta.determine_metadata(fake_options_req, self)

    #     return Response(data)

    def metadata(self, *args, **kwargs):
        import pdb

        pdb.set_trace()

        return super().options(*args, **kwargs)
