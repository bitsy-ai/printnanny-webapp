from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_info import SystemInfo
from ...models.system_info_request import SystemInfoRequest
from ...types import Response


def _get_kwargs(
    pi_id: int,
    *,
    client: AuthenticatedClient,
    form_data: SystemInfoRequest,
    multipart_data: SystemInfoRequest,
    json_body: SystemInfoRequest,
) -> Dict[str, Any]:
    url = "{}/api/pis/{pi_id}/system-info/update-or-create/".format(client.base_url, pi_id=pi_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SystemInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SystemInfo.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SystemInfo.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = SystemInfo.from_dict(response.json())

        return response_202
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SystemInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pi_id: int,
    *,
    client: AuthenticatedClient,
    form_data: SystemInfoRequest,
    multipart_data: SystemInfoRequest,
    json_body: SystemInfoRequest,
) -> Response[SystemInfo]:
    """
    Args:
        pi_id (int):
        multipart_data (SystemInfoRequest):
        json_body (SystemInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemInfo]
    """

    kwargs = _get_kwargs(
        pi_id=pi_id,
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
    pi_id: int,
    *,
    client: AuthenticatedClient,
    form_data: SystemInfoRequest,
    multipart_data: SystemInfoRequest,
    json_body: SystemInfoRequest,
) -> Optional[SystemInfo]:
    """
    Args:
        pi_id (int):
        multipart_data (SystemInfoRequest):
        json_body (SystemInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemInfo]
    """

    return sync_detailed(
        pi_id=pi_id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    pi_id: int,
    *,
    client: AuthenticatedClient,
    form_data: SystemInfoRequest,
    multipart_data: SystemInfoRequest,
    json_body: SystemInfoRequest,
) -> Response[SystemInfo]:
    """
    Args:
        pi_id (int):
        multipart_data (SystemInfoRequest):
        json_body (SystemInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemInfo]
    """

    kwargs = _get_kwargs(
        pi_id=pi_id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pi_id: int,
    *,
    client: AuthenticatedClient,
    form_data: SystemInfoRequest,
    multipart_data: SystemInfoRequest,
    json_body: SystemInfoRequest,
) -> Optional[SystemInfo]:
    """
    Args:
        pi_id (int):
        multipart_data (SystemInfoRequest):
        json_body (SystemInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemInfo]
    """

    return (
        await asyncio_detailed(
            pi_id=pi_id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
