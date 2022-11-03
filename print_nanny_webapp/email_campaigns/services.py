import logging
from typing import Dict, Optional, Union

from anymail.message import AnymailMessage
from django.apps import apps
from django.db.models.query import QuerySet

from print_nanny_webapp.email_campaigns.models import Campaign, EmailMessage
from print_nanny_webapp.users.models import User

logger = logging.getLogger(__name__)


InviteRequest = apps.get_model("users", "InviteRequest")
RemoteAccessSurvey1 = apps.get_model("surveys", "RemoteAccessSurvey1")
EmailWaitlist = apps.get_model("users", "EmailWaitlist")


def migrate_surveys_to_email_waitlist():
    already_added = EmailWaitlist.objects.all().values("email")
    surveys_to_add = InviteRequest.objects.exclude(email__in=already_added).all()
    remaining = surveys_to_add.count()
    logger.info("Found %s InviteRequest not in EmailWaitlist, adding", remaining)

    for survey in surveys_to_add:
        try:
            EmailWaitlist.objects.create(
                created_dt=survey.created_dt, email=survey.email
            )
        except Exception as e:
            logger.error("Failed to add %s to EmailWaitlist: %s", survey, e)
        remaining -= 1

        # log progress for every 100 signups
        if remaining % 100 == 0:
            logger.info("%s InviteRequest remainng", remaining)
    already_added = EmailWaitlist.objects.all().values("email")
    surveys_to_add = RemoteAccessSurvey1.objects.exclude(email__in=already_added).all()
    remaining = surveys_to_add.count()
    logger.info("Found %s RemoteAccessSurvey1 not in EmailWaitlist, adding", remaining)
    for survey in surveys_to_add:
        try:
            EmailWaitlist.objects.create(
                created_dt=survey.created_dt, email=survey.email
            )
        except Exception as e:
            logger.error("Failed to add %s to EmailWaitlist: %s", survey, e)
        remaining -= 1

        # log progress for every 100 signups
        if remaining % 100 == 0:
            logger.info("%s InviteRequest remainng", remaining)


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


def filter_email_waitlist_not_subscribed(
    campaign: Campaign, limit=10
) -> QuerySet[EmailWaitlist]:
    already_subscribed = User.objects.all().values("email")  # type: ignore[has-type]
    already_sent = EmailMessage.objects.filter(campaign=campaign).values("email")
    return (
        EmailWaitlist.objects.exclude(email__in=already_sent)
        .exclude(email__in=already_subscribed)
        .order_by("-created_dt")
        .all()[:limit]
        .values_list("email", flat=True)
    )


def send_fn_founding_member_november_2022_offer(
    campaign: Campaign, filter_fn=filter_email_waitlist_not_subscribed, limit=10
) -> AnymailMessage:
    emails = list(filter_fn(campaign, limit=limit))

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
