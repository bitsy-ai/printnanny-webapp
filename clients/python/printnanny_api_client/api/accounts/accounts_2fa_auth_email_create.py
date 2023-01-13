from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_auth import EmailAuth
from ...models.email_auth_request import EmailAuthRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: EmailAuthRequest,
    multipart_data: EmailAuthRequest,
    json_body: EmailAuthRequest,
) -> Dict[str, Any]:
    url = "{}/accounts/2fa-auth/email/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[EmailAuth]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EmailAuth.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[EmailAuth]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: EmailAuthRequest,
    multipart_data: EmailAuthRequest,
    json_body: EmailAuthRequest,
) -> Response[EmailAuth]:
    """This returns a 6-digit callback token we can trade for a user's Auth Token.

    Args:
        multipart_data (EmailAuthRequest): Abstract class that returns a callback token based on
            the field given
            Returns a token if valid, None or a message if not.
        json_body (EmailAuthRequest): Abstract class that returns a callback token based on the
            field given
            Returns a token if valid, None or a message if not.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailAuth]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: EmailAuthRequest,
    multipart_data: EmailAuthRequest,
    json_body: EmailAuthRequest,
) -> Optional[EmailAuth]:
    """This returns a 6-digit callback token we can trade for a user's Auth Token.

    Args:
        multipart_data (EmailAuthRequest): Abstract class that returns a callback token based on
            the field given
            Returns a token if valid, None or a message if not.
        json_body (EmailAuthRequest): Abstract class that returns a callback token based on the
            field given
            Returns a token if valid, None or a message if not.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailAuth]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: EmailAuthRequest,
    multipart_data: EmailAuthRequest,
    json_body: EmailAuthRequest,
) -> Response[EmailAuth]:
    """This returns a 6-digit callback token we can trade for a user's Auth Token.

    Args:
        multipart_data (EmailAuthRequest): Abstract class that returns a callback token based on
            the field given
            Returns a token if valid, None or a message if not.
        json_body (EmailAuthRequest): Abstract class that returns a callback token based on the
            field given
            Returns a token if valid, None or a message if not.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailAuth]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: EmailAuthRequest,
    multipart_data: EmailAuthRequest,
    json_body: EmailAuthRequest,
) -> Optional[EmailAuth]:
    """This returns a 6-digit callback token we can trade for a user's Auth Token.

    Args:
        multipart_data (EmailAuthRequest): Abstract class that returns a callback token based on
            the field given
            Returns a token if valid, None or a message if not.
        json_body (EmailAuthRequest): Abstract class that returns a callback token based on the
            field given
            Returns a token if valid, None or a message if not.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailAuth]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
