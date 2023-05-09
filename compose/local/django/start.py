from django.conf import settings
from djstripe.models.api import APIKey
from djstripe.enums import APIKeyType

# djstripe now requires manual key creation via admin ui after version 2.5
# this is a workaround for CI tests
APIKey.objects.get_or_create(
    secret=settings.STRIPE_TEST_SECRET_KEY, livemode=False, type=APIKeyType.secret
)
