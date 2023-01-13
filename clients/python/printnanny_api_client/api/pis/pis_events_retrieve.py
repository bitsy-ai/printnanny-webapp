from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.pi_boot_command import PiBootCommand
from ...models.pi_boot_status import PiBootStatus
from ...models.pi_cam_command import PiCamCommand
from ...models.pi_cam_status import PiCamStatus
from ...models.pi_software_update_command import PiSoftwareUpdateCommand
from ...models.pi_software_update_status import PiSoftwareUpdateStatus
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/pis/events/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        ErrorDetail,
        Union[
            "PiBootCommand",
            "PiBootStatus",
            "PiCamCommand",
            "PiCamStatus",
            "PiSoftwareUpdateCommand",
            "PiSoftwareUpdateStatus",
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "PiBootCommand",
            "PiBootStatus",
            "PiCamCommand",
            "PiCamStatus",
            "PiSoftwareUpdateCommand",
            "PiSoftwareUpdateStatus",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_pi_event_type_0 = PiCamStatus.from_dict(data)

                return componentsschemas_polymorphic_pi_event_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_pi_event_type_1 = PiSoftwareUpdateStatus.from_dict(data)

                return componentsschemas_polymorphic_pi_event_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_pi_event_type_2 = PiBootStatus.from_dict(data)

                return componentsschemas_polymorphic_pi_event_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_pi_event_type_3 = PiCamCommand.from_dict(data)

                return componentsschemas_polymorphic_pi_event_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_pi_event_type_4 = PiSoftwareUpdateCommand.from_dict(data)

                return componentsschemas_polymorphic_pi_event_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_polymorphic_pi_event_type_5 = PiBootCommand.from_dict(data)

            return componentsschemas_polymorphic_pi_event_type_5

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorDetail.from_dict(response.json())

        return response_404
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
) -> Response[
    Union[
        ErrorDetail,
        Union[
            "PiBootCommand",
            "PiBootStatus",
            "PiCamCommand",
            "PiCamStatus",
            "PiSoftwareUpdateCommand",
            "PiSoftwareUpdateStatus",
        ],
    ]
]:
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
) -> Response[
    Union[
        ErrorDetail,
        Union[
            "PiBootCommand",
            "PiBootStatus",
            "PiCamCommand",
            "PiCamStatus",
            "PiSoftwareUpdateCommand",
            "PiSoftwareUpdateStatus",
        ],
    ]
]:
    """Interact with all events inheriting from BasePiEvent

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Union['PiBootCommand', 'PiBootStatus', 'PiCamCommand', 'PiCamStatus', 'PiSoftwareUpdateCommand', 'PiSoftwareUpdateStatus']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
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
) -> Optional[
    Union[
        ErrorDetail,
        Union[
            "PiBootCommand",
            "PiBootStatus",
            "PiCamCommand",
            "PiCamStatus",
            "PiSoftwareUpdateCommand",
            "PiSoftwareUpdateStatus",
        ],
    ]
]:
    """Interact with all events inheriting from BasePiEvent

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Union['PiBootCommand', 'PiBootStatus', 'PiCamCommand', 'PiCamStatus', 'PiSoftwareUpdateCommand', 'PiSoftwareUpdateStatus']]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        ErrorDetail,
        Union[
            "PiBootCommand",
            "PiBootStatus",
            "PiCamCommand",
            "PiCamStatus",
            "PiSoftwareUpdateCommand",
            "PiSoftwareUpdateStatus",
        ],
    ]
]:
    """Interact with all events inheriting from BasePiEvent

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Union['PiBootCommand', 'PiBootStatus', 'PiCamCommand', 'PiCamStatus', 'PiSoftwareUpdateCommand', 'PiSoftwareUpdateStatus']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        ErrorDetail,
        Union[
            "PiBootCommand",
            "PiBootStatus",
            "PiCamCommand",
            "PiCamStatus",
            "PiSoftwareUpdateCommand",
            "PiSoftwareUpdateStatus",
        ],
    ]
]:
    """Interact with all events inheriting from BasePiEvent

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Union['PiBootCommand', 'PiBootStatus', 'PiCamCommand', 'PiCamStatus', 'PiSoftwareUpdateCommand', 'PiSoftwareUpdateStatus']]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
