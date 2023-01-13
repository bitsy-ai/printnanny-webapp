from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_detail import ErrorDetail
from ...models.octo_print_gcode_event import OctoPrintGcodeEvent
from ...models.octo_print_gcode_event_request import OctoPrintGcodeEventRequest
from ...models.octo_print_print_job_status import OctoPrintPrintJobStatus
from ...models.octo_print_print_job_status_request import OctoPrintPrintJobStatusRequest
from ...models.octo_print_printer_status import OctoPrintPrinterStatus
from ...models.octo_print_printer_status_request import OctoPrintPrinterStatusRequest
from ...models.octo_print_server_status import OctoPrintServerStatus
from ...models.octo_print_server_status_request import OctoPrintServerStatusRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    multipart_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    json_body: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
) -> Dict[str, Any]:
    url = "{}/api/octoprint/events/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body: Dict[str, Any]

    if isinstance(json_body, OctoPrintPrintJobStatusRequest):
        json_body.to_dict()

    elif isinstance(json_body, OctoPrintPrinterStatusRequest):
        json_body.to_dict()

    elif isinstance(json_body, OctoPrintServerStatusRequest):
        json_body.to_dict()

    else:
        json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        ErrorDetail,
        Union["OctoPrintGcodeEvent", "OctoPrintPrintJobStatus", "OctoPrintPrinterStatus", "OctoPrintServerStatus"],
    ]
]:
    if response.status_code == HTTPStatus.CREATED:

        def _parse_response_201(
            data: object,
        ) -> Union["OctoPrintGcodeEvent", "OctoPrintPrintJobStatus", "OctoPrintPrinterStatus", "OctoPrintServerStatus"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_octo_print_event_type_0 = OctoPrintPrintJobStatus.from_dict(data)

                return componentsschemas_polymorphic_octo_print_event_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_octo_print_event_type_1 = OctoPrintPrinterStatus.from_dict(data)

                return componentsschemas_polymorphic_octo_print_event_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_octo_print_event_type_2 = OctoPrintServerStatus.from_dict(data)

                return componentsschemas_polymorphic_octo_print_event_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_polymorphic_octo_print_event_type_3 = OctoPrintGcodeEvent.from_dict(data)

            return componentsschemas_polymorphic_octo_print_event_type_3

        response_201 = _parse_response_201(response.json())

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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        ErrorDetail,
        Union["OctoPrintGcodeEvent", "OctoPrintPrintJobStatus", "OctoPrintPrinterStatus", "OctoPrintServerStatus"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    multipart_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    json_body: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
) -> Response[
    Union[
        ErrorDetail,
        Union["OctoPrintGcodeEvent", "OctoPrintPrintJobStatus", "OctoPrintPrinterStatus", "OctoPrintServerStatus"],
    ]
]:
    """Interact with all events inheriting from BasePiEvent

    Args:
        multipart_data (Union['OctoPrintGcodeEventRequest', 'OctoPrintPrintJobStatusRequest',
            'OctoPrintPrinterStatusRequest', 'OctoPrintServerStatusRequest']):
        json_body (Union['OctoPrintGcodeEventRequest', 'OctoPrintPrintJobStatusRequest',
            'OctoPrintPrinterStatusRequest', 'OctoPrintServerStatusRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Union['OctoPrintGcodeEvent', 'OctoPrintPrintJobStatus', 'OctoPrintPrinterStatus', 'OctoPrintServerStatus']]]
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
    form_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    multipart_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    json_body: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
) -> Optional[
    Union[
        ErrorDetail,
        Union["OctoPrintGcodeEvent", "OctoPrintPrintJobStatus", "OctoPrintPrinterStatus", "OctoPrintServerStatus"],
    ]
]:
    """Interact with all events inheriting from BasePiEvent

    Args:
        multipart_data (Union['OctoPrintGcodeEventRequest', 'OctoPrintPrintJobStatusRequest',
            'OctoPrintPrinterStatusRequest', 'OctoPrintServerStatusRequest']):
        json_body (Union['OctoPrintGcodeEventRequest', 'OctoPrintPrintJobStatusRequest',
            'OctoPrintPrinterStatusRequest', 'OctoPrintServerStatusRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Union['OctoPrintGcodeEvent', 'OctoPrintPrintJobStatus', 'OctoPrintPrinterStatus', 'OctoPrintServerStatus']]]
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
    form_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    multipart_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    json_body: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
) -> Response[
    Union[
        ErrorDetail,
        Union["OctoPrintGcodeEvent", "OctoPrintPrintJobStatus", "OctoPrintPrinterStatus", "OctoPrintServerStatus"],
    ]
]:
    """Interact with all events inheriting from BasePiEvent

    Args:
        multipart_data (Union['OctoPrintGcodeEventRequest', 'OctoPrintPrintJobStatusRequest',
            'OctoPrintPrinterStatusRequest', 'OctoPrintServerStatusRequest']):
        json_body (Union['OctoPrintGcodeEventRequest', 'OctoPrintPrintJobStatusRequest',
            'OctoPrintPrinterStatusRequest', 'OctoPrintServerStatusRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Union['OctoPrintGcodeEvent', 'OctoPrintPrintJobStatus', 'OctoPrintPrinterStatus', 'OctoPrintServerStatus']]]
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
    form_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    multipart_data: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
    json_body: Union[
        "OctoPrintGcodeEventRequest",
        "OctoPrintPrintJobStatusRequest",
        "OctoPrintPrinterStatusRequest",
        "OctoPrintServerStatusRequest",
    ],
) -> Optional[
    Union[
        ErrorDetail,
        Union["OctoPrintGcodeEvent", "OctoPrintPrintJobStatus", "OctoPrintPrinterStatus", "OctoPrintServerStatus"],
    ]
]:
    """Interact with all events inheriting from BasePiEvent

    Args:
        multipart_data (Union['OctoPrintGcodeEventRequest', 'OctoPrintPrintJobStatusRequest',
            'OctoPrintPrinterStatusRequest', 'OctoPrintServerStatusRequest']):
        json_body (Union['OctoPrintGcodeEventRequest', 'OctoPrintPrintJobStatusRequest',
            'OctoPrintPrinterStatusRequest', 'OctoPrintServerStatusRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorDetail, Union['OctoPrintGcodeEvent', 'OctoPrintPrintJobStatus', 'OctoPrintPrinterStatus', 'OctoPrintServerStatus']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
