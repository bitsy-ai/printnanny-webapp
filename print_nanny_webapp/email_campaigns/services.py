import logging
from typing import Dict, Optional, Union

from anymail.message import AnymailMessage
from django.db import models

from print_nanny_webapp.email_campaigns.models import Campaign, EmailMessage
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


def format_merge_metadata(email: str) -> Dict[str, Optional[Union[str, int]]]:
    name = "Maker"
    try:
        user = User.objects.get(email=email)  # type: ignore[has-type]
        if user.first_name:
            name = user.first_name
        return dict(user_id=str(user.id), name=name)
    except User.DoesNotExist:
        return dict(user_id=None, name=name)


def send_fn_founding_member_november_2022_offer(
    campaign: Campaign, model: models.Model, limit=10
) -> AnymailMessage:
    already_subscribed = User.objects.all().values("email")
    already_sent = EmailMessage.objects.filter(campaign=campaign).values("email")
    emails = list(
        model.objects.exclude(email__in=already_sent)
        .exclude(email__in=already_subscribed)
        .order_by("-created_dt")
        .all()[:limit]
        .values_list("email", flat=True)
    )
    msg = AnymailMessage(
        subject=campaign.subject,
        tags=["marketing", "founding_member"],
        from_email="PrintNanny <beta@mail.printnanny.ai>",
    )

    msg.template_id = campaign.template

    msg.to = emails
    msg.merge_metadata = {email: format_merge_metadata(email) for email in emails}
    msg.esp_extra = {
        # TODO: send-time optimization is only available for single recipient messages
        # "o:deliverytime-optimize-period": "24h",  # use Mailgun Send Time Optimization
        # "o:time-zone-localize": "16:00",  # use Mailgun Timezone Optimization
        "h:Reply-To": "leigh@printnanny.ai",
    }
    msg.merge_global_data = {"campaign_id": campaign.id}

    logger.info("Starting campaign %s to %s recipients", campaign.template, len(msg.to))
    msg.send(fail_silently=False)
    logger.info("Success! Started campaign %s", campaign.template)
    return msg


def send_fn_founding_member_november_2022_followup_offer(
    campaign: Campaign, model: models.Model, limit=10
) -> AnymailMessage:

    already_subscribed = User.objects.all().values("email")
    already_sent = EmailMessage.objects.filter(campaign=campaign).values("email")
    emails = list(
        model.objects.exclude(email__in=already_sent)
        .exclude(email__in=already_subscribed)
        .order_by("-created_dt")
        .all()[:limit]
        .values_list("email", flat=True)
    )
    msg = AnymailMessage(
        subject=campaign.subject,
        tags=["marketing", "founding_member"],
        from_email="PrintNanny <beta@mail.printnanny.ai>",
    )

    msg.template_id = campaign.template

    msg.to = emails
    msg.merge_metadata = {email: format_merge_metadata(email) for email in emails}
    msg.esp_extra = {
        # TODO: send-time optimization is only available for single recipient messages
        # "o:deliverytime-optimize-period": "24h",  # use Mailgun Send Time Optimization
        # "o:time-zone-localize": "16:00",  # use Mailgun Timezone Optimization
        "h:Reply-To": "leigh@printnanny.ai",
    }
    msg.merge_global_data = {"campaign_id": campaign.id}

    logger.info("Starting campaign %s to %s recipients", campaign.template, len(msg.to))
    msg.send(fail_silently=False)
    logger.info("Success! Started campaign %s", campaign.template)
    return msg
