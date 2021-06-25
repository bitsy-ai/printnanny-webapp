import pytest

from print_nanny_webapp.users.models import User
from print_nanny_webapp.users.tests.factories import UserFactory

# pytest_plugins = ("celery.contrib.pytest",)


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture(scope="session")
def celery_config():
    return {
        "broker_url": "redis://localhost:6379/0",
        "result_backend": "redis://localhost:6379/0",
    }
