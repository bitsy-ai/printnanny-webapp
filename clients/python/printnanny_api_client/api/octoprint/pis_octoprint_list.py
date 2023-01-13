from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.paginated_octo_print_server_list import PaginatedOctoPrintServerList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pi_id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/pis/{pi_id}/octoprint/".format(client.base_url, pi_id=pi_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorDetail, PaginatedOctoPrintServerList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedOctoPrintServerList.from_dict(response.json())

        return response_200
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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorDetail, PaginatedOctoPrintServerList]]:
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
    page: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorDetail, PaginatedOctoPrintServerList]]:
    """
    Args:
        pi_id (int):
        page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, PaginatedOctoPrintServerList]]
    """

    kwargs = _get_kwargs(
        pi_id=pi_id,
        client=client,
        page=page,
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
    page: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorDetail, PaginatedOctoPrintServerList]]:
    """
    Args:
        pi_id (int):
        page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, PaginatedOctoPrintServerList]]
    """

    return sync_detailed(
        pi_id=pi_id,
        client=client,
        page=page,
    ).parsed


async def asyncio_detailed(
    pi_id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorDetail, PaginatedOctoPrintServerList]]:
    """
    Args:
        pi_id (int):
        page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, PaginatedOctoPrintServerList]]
    """

    kwargs = _get_kwargs(
        pi_id=pi_id,
        client=client,
        page=page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pi_id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorDetail, PaginatedOctoPrintServerList]]:
    """
    Args:
        pi_id (int):
        page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, PaginatedOctoPrintServerList]]
    """

    return (
        await asyncio_detailed(
            pi_id=pi_id,
            client=client,
            page=page,
        )
    ).parsed
