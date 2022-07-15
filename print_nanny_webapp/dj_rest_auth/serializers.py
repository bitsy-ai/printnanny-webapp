from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from dj_rest_auth.registration.serializers import (
    RegisterSerializer as BaseRegisterSerializer,
)


class LoginSerializer(BaseLoginSerializer):
    # override username field in LoginSerializer
    username = None
    # set email to required
    email = serializers.EmailField(required=True)


class RegisterSerializer(BaseRegisterSerializer):
    # override username field in LoginSerializer
    username = None
    email = serializers.EmailField(required=True)
