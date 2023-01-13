from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.patched_pi_request import PatchedPiRequest
from ...models.pi import Pi
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: PatchedPiRequest,
    multipart_data: PatchedPiRequest,
    json_body: PatchedPiRequest,
) -> Dict[str, Any]:
    url = "{}/api/pis/{id}/".format(client.base_url, id=id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorDetail, Pi]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = Pi.from_dict(response.json())

        return response_202
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorDetail, Pi]]:
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
    form_data: PatchedPiRequest,
    multipart_data: PatchedPiRequest,
    json_body: PatchedPiRequest,
) -> Response[Union[ErrorDetail, Pi]]:
    """A device (Raspberry Pi) running Print Nanny OS

    Args:
        id (int):
        multipart_data (PatchedPiRequest):
        json_body (PatchedPiRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Pi]]
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
    form_data: PatchedPiRequest,
    multipart_data: PatchedPiRequest,
    json_body: PatchedPiRequest,
) -> Optional[Union[ErrorDetail, Pi]]:
    """A device (Raspberry Pi) running Print Nanny OS

    Args:
        id (int):
        multipart_data (PatchedPiRequest):
        json_body (PatchedPiRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Pi]]
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
    form_data: PatchedPiRequest,
    multipart_data: PatchedPiRequest,
    json_body: PatchedPiRequest,
) -> Response[Union[ErrorDetail, Pi]]:
    """A device (Raspberry Pi) running Print Nanny OS

    Args:
        id (int):
        multipart_data (PatchedPiRequest):
        json_body (PatchedPiRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Pi]]
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
    form_data: PatchedPiRequest,
    multipart_data: PatchedPiRequest,
    json_body: PatchedPiRequest,
) -> Optional[Union[ErrorDetail, Pi]]:
    """A device (Raspberry Pi) running Print Nanny OS

    Args:
        id (int):
        multipart_data (PatchedPiRequest):
        json_body (PatchedPiRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Pi]]
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
