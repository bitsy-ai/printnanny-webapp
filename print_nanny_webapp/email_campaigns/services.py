import logging
from typing import Dict
from django.db.models.query import QuerySet

from anymail.message import AnymailMessage

from print_nanny_webapp.email_campaigns.models import Campaign
from print_nanny_webapp.users.models import User

logger = logging.getLogger(__name__)


def format_email(user) -> str:
    result = ""
    if user.first_name is not None:
        result += user.first_name
        result += " "
    if user.last_name is not None:
        result += user.last_name
        result += " "
    if result == "":
        return user.email
    return f"{result} <{user.email}>"


def format_merge_data(user) -> Dict[str, str]:
    if user.first_name:
        return dict(name=user.first_name)
    return dict(name="Maker")


def format_merge_metadata(user: User) -> Dict[str, str]:
    return dict(user_id=str(user.id))


def send_fn_founding_member_november_2022_offer(
    queryset: QuerySet[User], campaign: Campaign
) -> AnymailMessage:

    msg = AnymailMessage(
        subject=campaign.subject,
        tags=["marketing", "founding_member"],
        from_email="beta@mail.printnanny.ai",
        to=[u.email for u in queryset],
    )

    msg.template_id = campaign.template

    msg.to = [u.email for u in queryset]
    msg.merge_data = {u.email: format_merge_data(u) for u in queryset}
    msg.merge_metadata = {u.email: format_merge_metadata(u) for u in queryset}
    msg.esp_extra = {
        "o:deliverytime-optimize-period": "24h",  # use Mailgun Send Time Optimization
        "o:time-zone-localize": "16:00",  # use Mailgun Timezone Optimization
        "h:Reply-To": "leigh@printnanny.ai",
    }
    msg.merge_global_data = {"campaign_id": campaign.id}

    logger.info("Starting campaign %s to %s recipients", campaign.template, len(msg.to))
    msg.send(fail_silently=False)
    logger.info("Success! Started campaign %s", campaign.template)
    return msg
