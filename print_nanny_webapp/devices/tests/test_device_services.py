import hashlib
import pytest
import tempfile
from django.conf import settings
from django.test import TestCase
import google.api_core.exceptions
from django.contrib.auth import get_user_model


class MockDevice(object):
    num_id = 1
    id = "1"
    name = "1"


@pytest.mark.django_db
def test_first_available_port(mocker, user):
    pass
