from rest_framework.authentication import TokenAuthentication
from .models import GeeksToken


class GeeksTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"
    model = GeeksToken
