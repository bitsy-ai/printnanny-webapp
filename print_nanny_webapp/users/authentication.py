from .models import GeeksToken
from rest_framework.authentication import TokenAuthentication


class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"


class GeeksTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"
    model = GeeksToken
