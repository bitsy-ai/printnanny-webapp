import logging
from typing import Dict, List

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


def format_merge_metadata(email: str) -> Dict[str, str]:
    name = "Maker"
    try:
        user = User.objects.get(email=email)
        if user.first_name:
            name = user.first_name
        return dict(user_id=str(user.id), name=name)
    except User.DoesNotExist:
        return dict(user_id=None, name=name)


def send_fn_founding_member_november_2022_offer(
    emails: List[str], campaign: Campaign
) -> AnymailMessage:

    msg = AnymailMessage(
        subject=campaign.subject,
        tags=["marketing", "founding_member"],
        from_email="beta@mail.printnanny.ai",
    )

    msg.template_id = campaign.template

    msg.to = emails
    msg.merge_metadata = {email: format_merge_metadata(email) for email in emails}
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
