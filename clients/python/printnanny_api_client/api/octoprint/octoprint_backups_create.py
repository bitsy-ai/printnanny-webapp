from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.octo_print_backup import OctoPrintBackup
from ...models.octo_print_backup_request import OctoPrintBackupRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    multipart_data: OctoPrintBackupRequest,
) -> Dict[str, Any]:
    url = "{}/api/octoprint/backups/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorDetail, OctoPrintBackup]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = OctoPrintBackup.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ErrorDetail.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorDetail.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorDetail.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorDetail.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorDetail.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorDetail, OctoPrintBackup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: OctoPrintBackupRequest,
) -> Response[Union[ErrorDetail, OctoPrintBackup]]:
    """
    Args:
        multipart_data (OctoPrintBackupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, OctoPrintBackup]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: OctoPrintBackupRequest,
) -> Optional[Union[ErrorDetail, OctoPrintBackup]]:
    """
    Args:
        multipart_data (OctoPrintBackupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, OctoPrintBackup]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: OctoPrintBackupRequest,
) -> Response[Union[ErrorDetail, OctoPrintBackup]]:
    """
    Args:
        multipart_data (OctoPrintBackupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, OctoPrintBackup]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: OctoPrintBackupRequest,
) -> Optional[Union[ErrorDetail, OctoPrintBackup]]:
    """
    Args:
        multipart_data (OctoPrintBackupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, OctoPrintBackup]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
