from django_nats_nkeys.models import NatsOrganizationUser
from django_nats_nkeys.services import create_nats_account_org
from print_nanny_webapp.users.models import User


def get_or_create_nats_organization_user(user: User) -> NatsOrganizationUser:
    # is user already member of an organization?
    try:
        org_user = NatsOrganizationUser.objects.get(user=user)
    except NatsOrganizationUser.DoesNotExist:
        # if not, create a new organization and set user as org owner
        org = create_nats_account_org(user)
        org_user = org.owner.organization_user
    return org_user
