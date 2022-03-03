import pytest

from print_nanny_webapp.users.models import User
from print_nanny_webapp.users.tests.factories import UserFactory
from webpack_loader.loader import WebpackLoader


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture(autouse=True)
def no_webpack_loaded(monkeypatch):
    def mockreturn(loader, bundle_name):
        return []

    monkeypatch.setattr(WebpackLoader, "get_bundle", mockreturn)
