from anymail.message import AnymailMessage


def send_fn_founding_member_november_2022_offer():
    msg = AnymailMessage(
        headers={
            "X-Example-Header": "myapp",
        },
        tags=["marketing", "founding_member"],
    )
