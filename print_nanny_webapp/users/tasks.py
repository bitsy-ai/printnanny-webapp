# Request URL: https://help.print-nanny.com/ghost/api/v3/admin/members/?include=labels%2Cemail_recipients
# Request Method: POST

# query params
# include=labels%2Cemail_recipients

# {"members":[{"name":"Leigh Johnson","email":"leigh@bitsy.ai","note":"","subscribed":true,"comped":false,"email_count":0,"email_opened_count":0,"email_open_rate":null,"labels":[]}]}
from celery import shared_task
from django.apps import apps
import logging
import requests  # pip install requests
import jwt  # pip install pyjwt
from datetime import datetime as date
from celery import group, chord, shared_task
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()
GhostMember = apps.get_model("users", "GhostMember")
InviteRequest = apps.get_model("users", "InviteRequest")

logger = logging.getLogger(__name__)


@shared_task
def create_ghost_member(ghost_member):
    logger.info(f"create_ghost_member task called with ghost_members={ghost_member}")
    # Split the key into ID and SECRET
    api_id, secret = settings.GHOST_ADMIN_API_KEY.split(":")

    # Prepare header and payload
    iat = int(date.now().timestamp())

    header = {"alg": "HS256", "typ": "JWT", "kid": api_id}
    payload = {"iat": iat, "exp": iat + 5 * 60, "aud": "/v3/admin/"}

    # Create the token (including decoding secret)
    token = jwt.encode(
        payload, bytes.fromhex(secret), algorithm="HS256", headers=header
    )

    # Make an authenticated request to create a post
    url = "https://blog.print-nanny.com/ghost/api/v3/admin/members/"
    headers = {"Authorization": "Ghost {}".format(token)}
    body = {"members": [ghost_member]}
    r = requests.post(url, json=body, headers=headers)

    # if user already exists, raises
    # celeryworker       | requests.exceptions.HTTPError: 422 Client Error: Unprocessable Entity for url: https://help.print-nanny.com/ghost/api/v3/admin/members/
    try:
        r.raise_for_status()
    except Exception as e:
        logger.warning(
            {
                "msg": "Attempting to retreive user after POST /ghost/api/v3/admin/members/",
                "error": e,
            }
        )
        r = requests.get(url, headers=headers, params={"search": body.get("email")})
    data = r.json()

    for member in data.get("members"):

        user = User.objects.filter(email=member["email"]).first()
        invite_request = InviteRequest.objects.filter(email=member["email"]).first()
        try:
            obj = GhostMember.objects.filter(email=member["email"]).first()

            if obj is not None:
                obj.email = member["email"]
                obj.uuid = member["uuid"]
                obj.user = user
                obj.invite_request = invite_request
                obj.email_count = member["email_count"]
                obj.email_open_rate = member["email_open_rate"]
                obj.email_opened_count = member["email_opened_count"]
                obj.save()
            else:
                obj = GhostMember.objects.create(
                    email=member["email"],
                    uuid=member["uuid"],
                    user=user,
                    invite_request=invite_request,
                    email_count=member["email_count"],
                    email_open_rate=member["email_open_rate"],
                    email_opened_count=member["email_opened_count"],
                    site=GhostMember.SiteChoices.BLOG,
                )
                logger.info(f"Created GhostMember id={obj.id}")
        except Exception as e:
            logger.error(e)
    return r.json()


@shared_task
def push_ghost_members():
    """
    One-time only task to create ghost members
    user / invite request manager should handle this going forward
    """

    invite_requests = InviteRequest.objects.all()

    create_tasks = group(
        [create_ghost_member.si(i.to_ghost_member()) for i in invite_requests]
    )

    return create_tasks()
