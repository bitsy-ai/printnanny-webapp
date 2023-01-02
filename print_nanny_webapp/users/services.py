from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()


def get_or_create_user_by_email(email: str) -> AbstractUser:
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return User.objects.create_user(email, User.objects.make_random_password())
