from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.password_reset_request import PasswordResetRequest
from ...models.rest_auth_detail import RestAuthDetail
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: PasswordResetRequest,
    multipart_data: PasswordResetRequest,
    json_body: PasswordResetRequest,
) -> Dict[str, Any]:
    url = "{}/api/accounts/password/reset/".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RestAuthDetail]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestAuthDetail.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RestAuthDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: PasswordResetRequest,
    multipart_data: PasswordResetRequest,
    json_body: PasswordResetRequest,
) -> Response[RestAuthDetail]:
    """Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.

    Args:
        multipart_data (PasswordResetRequest): Serializer for requesting a password reset e-mail.
        json_body (PasswordResetRequest): Serializer for requesting a password reset e-mail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAuthDetail]
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
    form_data: PasswordResetRequest,
    multipart_data: PasswordResetRequest,
    json_body: PasswordResetRequest,
) -> Optional[RestAuthDetail]:
    """Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.

    Args:
        multipart_data (PasswordResetRequest): Serializer for requesting a password reset e-mail.
        json_body (PasswordResetRequest): Serializer for requesting a password reset e-mail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAuthDetail]
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
    form_data: PasswordResetRequest,
    multipart_data: PasswordResetRequest,
    json_body: PasswordResetRequest,
) -> Response[RestAuthDetail]:
    """Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.

    Args:
        multipart_data (PasswordResetRequest): Serializer for requesting a password reset e-mail.
        json_body (PasswordResetRequest): Serializer for requesting a password reset e-mail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAuthDetail]
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
    form_data: PasswordResetRequest,
    multipart_data: PasswordResetRequest,
    json_body: PasswordResetRequest,
) -> Optional[RestAuthDetail]:
    """Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.

    Args:
        multipart_data (PasswordResetRequest): Serializer for requesting a password reset e-mail.
        json_body (PasswordResetRequest): Serializer for requesting a password reset e-mail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAuthDetail]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
