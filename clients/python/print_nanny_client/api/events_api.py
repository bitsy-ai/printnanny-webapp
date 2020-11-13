# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from print_nanny_client.api_client import ApiClient, Endpoint
from print_nanny_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from print_nanny_client.model.octo_print_event import OctoPrintEvent
from print_nanny_client.model.octo_print_event_request import OctoPrintEventRequest
from print_nanny_client.model.predict_event import PredictEvent


class EventsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __events_octoprint_create(
            self,
            octo_print_event_request,
            **kwargs
        ):
            """events_octoprint_create  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.events_octoprint_create(octo_print_event_request, async_req=True)
            >>> result = thread.get()

            Args:
                octo_print_event_request (OctoPrintEventRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                OctoPrintEvent
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['octo_print_event_request'] = \
                octo_print_event_request
            return self.call_with_http_info(**kwargs)

        self.events_octoprint_create = Endpoint(
            settings={
                'response_type': (OctoPrintEvent,),
                'auth': [
                    'cookieAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/api/events/octoprint/',
                'operation_id': 'events_octoprint_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'octo_print_event_request',
                ],
                'required': [
                    'octo_print_event_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'octo_print_event_request':
                        (OctoPrintEventRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'octo_print_event_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__events_octoprint_create
        )

        def __events_predict_create(
            self,
            dt,
            original_image,
            annotated_image,
            event_data,
            plugin_version,
            octoprint_version,
            **kwargs
        ):
            """events_predict_create  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.events_predict_create(dt, original_image, annotated_image, event_data, plugin_version, octoprint_version, async_req=True)
            >>> result = thread.get()

            Args:
                dt (datetime):
                original_image (file_type):
                annotated_image (file_type):
                event_data (str):
                plugin_version (str):
                octoprint_version (str):

            Keyword Args:
                print_job (int, none_type): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PredictEvent
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dt'] = \
                dt
            kwargs['original_image'] = \
                original_image
            kwargs['annotated_image'] = \
                annotated_image
            kwargs['event_data'] = \
                event_data
            kwargs['plugin_version'] = \
                plugin_version
            kwargs['octoprint_version'] = \
                octoprint_version
            return self.call_with_http_info(**kwargs)

        self.events_predict_create = Endpoint(
            settings={
                'response_type': (PredictEvent,),
                'auth': [
                    'cookieAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/api/events/predict/',
                'operation_id': 'events_predict_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dt',
                    'original_image',
                    'annotated_image',
                    'event_data',
                    'plugin_version',
                    'octoprint_version',
                    'print_job',
                ],
                'required': [
                    'dt',
                    'original_image',
                    'annotated_image',
                    'event_data',
                    'plugin_version',
                    'octoprint_version',
                ],
                'nullable': [
                    'print_job',
                ],
                'enum': [
                ],
                'validation': [
                    'plugin_version',
                    'octoprint_version',
                ]
            },
            root_map={
                'validations': {
                    ('plugin_version',): {
                        'max_length': 30,
                    },
                    ('octoprint_version',): {
                        'max_length': 30,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dt':
                        (datetime,),
                    'original_image':
                        (file_type,),
                    'annotated_image':
                        (file_type,),
                    'event_data':
                        (str,),
                    'plugin_version':
                        (str,),
                    'octoprint_version':
                        (str,),
                    'print_job':
                        (int, none_type,),
                },
                'attribute_map': {
                    'dt': 'dt',
                    'original_image': 'original_image',
                    'annotated_image': 'annotated_image',
                    'event_data': 'event_data',
                    'plugin_version': 'plugin_version',
                    'octoprint_version': 'octoprint_version',
                    'print_job': 'print_job',
                },
                'location_map': {
                    'dt': 'form',
                    'original_image': 'form',
                    'annotated_image': 'form',
                    'event_data': 'form',
                    'plugin_version': 'form',
                    'octoprint_version': 'form',
                    'print_job': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data',
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client,
            callable=__events_predict_create
        )
