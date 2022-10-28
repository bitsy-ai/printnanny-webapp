import logging
from typing import Dict
from django.db.models.query import QuerySet

from anymail.message import AnymailMessage

from print_nanny_webapp.email_campaigns.models import Campaign
from print_nanny_webapp.users.models import User

logger = logging.getLogger(__name__)


def format_email(user: User) -> str:
    result = ""
    if user.first_name is not None:
        result += user.first_name
        result += " "
    if user.last_name is not None:
        result += user.last_name
        result += " "
    if result == "":
        return user.email
    else:
        return f"{result} <{user.email}>"


def format_merge_data(user: User) -> Dict[str, str]:
    if user.first_name:
        return dict(name=user.first_name)
    return dict(name="Maker")


def format_merge_metadata(user: User, campaign: Campaign) -> Dict[str, str]:
    return dict(user_id=str(user.id), campaign_id=str(campaign.id))


def send_fn_founding_member_november_2022_offer(
    queryset: QuerySet[User], campaign: Campaign
):

    msg = AnymailMessage(
        subject=campaign.subject,
        tags=["marketing", "founding_member"],
        from_email="beta@mail.printnanny.ai",
    )

    msg.track_clicks = True
    msg.track_opens = True

    msg.to = [format_email(u) for u in queryset]
    msg.merge_data = [format_merge_data(u) for u in queryset]
    msg.merge_metadata = [format_merge_metadata(u, campaign) for u in queryset]
    msg.esp_extra = {
        "o:deliverytime-optimize-period": "24h",  # use Mailgun Send Time Optimization
        "o:time-zone-localize": "16:00",  # use Mailgun Timezone Optimization
        "h:Reply-To": "leigh@printnanny.ai",
    }

    logger.info("Starting campaign %s to %s recipients", campaign.template, len(msg.to))
    msg.send()
    logger.info("Success! Started campaign %s", campaign.template)
