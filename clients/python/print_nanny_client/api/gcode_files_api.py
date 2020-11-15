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
from print_nanny_client.model.gcode_file import GcodeFile


class GcodeFilesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __gcode_files_create(
            self,
            name,
            file,
            file_hash,
            **kwargs
        ):
            """gcode_files_create  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.gcode_files_create(name, file, file_hash, async_req=True)
            >>> result = thread.get()

            Args:
                name (str):
                file (file_type):
                file_hash (str):

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
                GcodeFile
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
            kwargs['name'] = \
                name
            kwargs['file'] = \
                file
            kwargs['file_hash'] = \
                file_hash
            return self.call_with_http_info(**kwargs)

        self.gcode_files_create = Endpoint(
            settings={
                'response_type': (GcodeFile,),
                'auth': [
                    'cookieAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/api/gcode_files/',
                'operation_id': 'gcode_files_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'file',
                    'file_hash',
                ],
                'required': [
                    'name',
                    'file',
                    'file_hash',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'name',
                    'file_hash',
                ]
            },
            root_map={
                'validations': {
                    ('name',): {
                        'max_length': 255,
                    },
                    ('file_hash',): {
                        'max_length': 255,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'file':
                        (file_type,),
                    'file_hash':
                        (str,),
                },
                'attribute_map': {
                    'name': 'name',
                    'file': 'file',
                    'file_hash': 'file_hash',
                },
                'location_map': {
                    'name': 'form',
                    'file': 'form',
                    'file_hash': 'form',
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
            callable=__gcode_files_create
        )

        def __gcode_files_list(
            self,
            **kwargs
        ):
            """gcode_files_list  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.gcode_files_list(async_req=True)
            >>> result = thread.get()


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
                [GcodeFile]
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
            return self.call_with_http_info(**kwargs)

        self.gcode_files_list = Endpoint(
            settings={
                'response_type': ([GcodeFile],),
                'auth': [
                    'cookieAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/api/gcode_files/',
                'operation_id': 'gcode_files_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
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
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__gcode_files_list
        )

        def __gcode_files_partial_update(
            self,
            id,
            **kwargs
        ):
            """gcode_files_partial_update  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.gcode_files_partial_update(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): A unique integer value identifying this gcode file.

            Keyword Args:
                name (str): [optional]
                file (file_type): [optional]
                file_hash (str): [optional]
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
                GcodeFile
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.gcode_files_partial_update = Endpoint(
            settings={
                'response_type': (GcodeFile,),
                'auth': [
                    'cookieAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/api/gcode_files/{id}/',
                'operation_id': 'gcode_files_partial_update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'name',
                    'file',
                    'file_hash',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'name',
                    'file_hash',
                ]
            },
            root_map={
                'validations': {
                    ('name',): {
                        'max_length': 255,
                    },
                    ('file_hash',): {
                        'max_length': 255,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'name':
                        (str,),
                    'file':
                        (file_type,),
                    'file_hash':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'name': 'name',
                    'file': 'file',
                    'file_hash': 'file_hash',
                },
                'location_map': {
                    'id': 'path',
                    'name': 'form',
                    'file': 'form',
                    'file_hash': 'form',
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
            callable=__gcode_files_partial_update
        )

        def __gcode_files_retrieve(
            self,
            id,
            **kwargs
        ):
            """gcode_files_retrieve  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.gcode_files_retrieve(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): A unique integer value identifying this gcode file.

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
                GcodeFile
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.gcode_files_retrieve = Endpoint(
            settings={
                'response_type': (GcodeFile,),
                'auth': [
                    'cookieAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/api/gcode_files/{id}/',
                'operation_id': 'gcode_files_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
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
                    'id':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__gcode_files_retrieve
        )

        def __gcode_files_update(
            self,
            id,
            name,
            file,
            file_hash,
            **kwargs
        ):
            """gcode_files_update  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.gcode_files_update(id, name, file, file_hash, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): A unique integer value identifying this gcode file.
                name (str):
                file (file_type):
                file_hash (str):

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
                GcodeFile
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
            kwargs['id'] = \
                id
            kwargs['name'] = \
                name
            kwargs['file'] = \
                file
            kwargs['file_hash'] = \
                file_hash
            return self.call_with_http_info(**kwargs)

        self.gcode_files_update = Endpoint(
            settings={
                'response_type': (GcodeFile,),
                'auth': [
                    'cookieAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/api/gcode_files/{id}/',
                'operation_id': 'gcode_files_update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'name',
                    'file',
                    'file_hash',
                ],
                'required': [
                    'id',
                    'name',
                    'file',
                    'file_hash',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'name',
                    'file_hash',
                ]
            },
            root_map={
                'validations': {
                    ('name',): {
                        'max_length': 255,
                    },
                    ('file_hash',): {
                        'max_length': 255,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'name':
                        (str,),
                    'file':
                        (file_type,),
                    'file_hash':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'name': 'name',
                    'file': 'file',
                    'file_hash': 'file_hash',
                },
                'location_map': {
                    'id': 'path',
                    'name': 'form',
                    'file': 'form',
                    'file_hash': 'form',
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
            callable=__gcode_files_update
        )

        def __gcode_files_update_or_create(
            self,
            name,
            file,
            file_hash,
            **kwargs
        ):
            """gcode_files_update_or_create  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.gcode_files_update_or_create(name, file, file_hash, async_req=True)
            >>> result = thread.get()

            Args:
                name (str):
                file (file_type):
                file_hash (str):

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
                GcodeFile
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
            kwargs['name'] = \
                name
            kwargs['file'] = \
                file
            kwargs['file_hash'] = \
                file_hash
            return self.call_with_http_info(**kwargs)

        self.gcode_files_update_or_create = Endpoint(
            settings={
                'response_type': (GcodeFile,),
                'auth': [
                    'cookieAuth',
                    'tokenAuth'
                ],
                'endpoint_path': '/api/gcode_files/update_or_create/',
                'operation_id': 'gcode_files_update_or_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'file',
                    'file_hash',
                ],
                'required': [
                    'name',
                    'file',
                    'file_hash',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'name',
                    'file_hash',
                ]
            },
            root_map={
                'validations': {
                    ('name',): {
                        'max_length': 255,
                    },
                    ('file_hash',): {
                        'max_length': 255,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'file':
                        (file_type,),
                    'file_hash':
                        (str,),
                },
                'attribute_map': {
                    'name': 'name',
                    'file': 'file',
                    'file_hash': 'file_hash',
                },
                'location_map': {
                    'name': 'form',
                    'file': 'form',
                    'file_hash': 'form',
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
            callable=__gcode_files_update_or_create
        )
