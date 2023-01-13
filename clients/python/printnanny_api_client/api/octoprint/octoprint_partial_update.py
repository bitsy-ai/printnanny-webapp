from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.octo_print_server import OctoPrintServer
from ...models.patched_octo_print_server_request import PatchedOctoPrintServerRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOctoPrintServerRequest,
    multipart_data: PatchedOctoPrintServerRequest,
    json_body: PatchedOctoPrintServerRequest,
) -> Dict[str, Any]:
    url = "{}/api/octoprint/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[OctoPrintServer]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OctoPrintServer.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[OctoPrintServer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOctoPrintServerRequest,
    multipart_data: PatchedOctoPrintServerRequest,
    json_body: PatchedOctoPrintServerRequest,
) -> Response[OctoPrintServer]:
    """
    Args:
        id (int):
        multipart_data (PatchedOctoPrintServerRequest):
        json_body (PatchedOctoPrintServerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OctoPrintServer]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOctoPrintServerRequest,
    multipart_data: PatchedOctoPrintServerRequest,
    json_body: PatchedOctoPrintServerRequest,
) -> Optional[OctoPrintServer]:
    """
    Args:
        id (int):
        multipart_data (PatchedOctoPrintServerRequest):
        json_body (PatchedOctoPrintServerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OctoPrintServer]
    """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOctoPrintServerRequest,
    multipart_data: PatchedOctoPrintServerRequest,
    json_body: PatchedOctoPrintServerRequest,
) -> Response[OctoPrintServer]:
    """
    Args:
        id (int):
        multipart_data (PatchedOctoPrintServerRequest):
        json_body (PatchedOctoPrintServerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OctoPrintServer]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOctoPrintServerRequest,
    multipart_data: PatchedOctoPrintServerRequest,
    json_body: PatchedOctoPrintServerRequest,
) -> Optional[OctoPrintServer]:
    """
    Args:
        id (int):
        multipart_data (PatchedOctoPrintServerRequest):
        json_body (PatchedOctoPrintServerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OctoPrintServer]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
