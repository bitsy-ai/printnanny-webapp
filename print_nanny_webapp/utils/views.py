from rest_framework.request import Request
from print_nanny_webapp.users.models import User


class AuthenticatedHttpRequest(Request):
    user: User
