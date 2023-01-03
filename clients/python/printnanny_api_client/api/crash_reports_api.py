# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.119.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from printnanny_api_client.api_client import ApiClient
from printnanny_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CrashReportsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def crash_reports_create(self, **kwargs):  # noqa: E501
        """crash_reports_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.crash_reports_create(async_req=True)
        >>> result = thread.get()

        :param email:
        :type email: str
        :param os_version:
        :type os_version: str
        :param os_logs:
        :type os_logs: file
        :param browser_version:
        :type browser_version: str
        :param browser_logs:
        :type browser_logs: file
        :param serial:
        :type serial: str
        :param posthog_session:
        :type posthog_session: str
        :param user:
        :type user: int
        :param pi:
        :type pi: int
        :param related_crash_report:
        :type related_crash_report: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CrashReport
        """
        kwargs['_return_http_data_only'] = True
        return self.crash_reports_create_with_http_info(**kwargs)  # noqa: E501

    def crash_reports_create_with_http_info(self, **kwargs):  # noqa: E501
        """crash_reports_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.crash_reports_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param email:
        :type email: str
        :param os_version:
        :type os_version: str
        :param os_logs:
        :type os_logs: file
        :param browser_version:
        :type browser_version: str
        :param browser_logs:
        :type browser_logs: file
        :param serial:
        :type serial: str
        :param posthog_session:
        :type posthog_session: str
        :param user:
        :type user: int
        :param pi:
        :type pi: int
        :param related_crash_report:
        :type related_crash_report: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CrashReport, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'email',
            'os_version',
            'os_logs',
            'browser_version',
            'browser_logs',
            'serial',
            'posthog_session',
            'user',
            'pi',
            'related_crash_report'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method crash_reports_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('email' in local_var_params and  # noqa: E501
                                                        len(local_var_params['email']) > 254):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `email` when calling `crash_reports_create`, length must be less than or equal to `254`")  # noqa: E501
        if self.api_client.client_side_validation and ('email' in local_var_params and  # noqa: E501
                                                        len(local_var_params['email']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `email` when calling `crash_reports_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('os_version' in local_var_params and  # noqa: E501
                                                        len(local_var_params['os_version']) > 255):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `os_version` when calling `crash_reports_create`, length must be less than or equal to `255`")  # noqa: E501
        if self.api_client.client_side_validation and ('os_version' in local_var_params and  # noqa: E501
                                                        len(local_var_params['os_version']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `os_version` when calling `crash_reports_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('browser_version' in local_var_params and  # noqa: E501
                                                        len(local_var_params['browser_version']) > 255):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `browser_version` when calling `crash_reports_create`, length must be less than or equal to `255`")  # noqa: E501
        if self.api_client.client_side_validation and ('browser_version' in local_var_params and  # noqa: E501
                                                        len(local_var_params['browser_version']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `browser_version` when calling `crash_reports_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('serial' in local_var_params and  # noqa: E501
                                                        len(local_var_params['serial']) > 255):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `serial` when calling `crash_reports_create`, length must be less than or equal to `255`")  # noqa: E501
        if self.api_client.client_side_validation and ('serial' in local_var_params and  # noqa: E501
                                                        len(local_var_params['serial']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `serial` when calling `crash_reports_create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('posthog_session' in local_var_params and  # noqa: E501
                                                        len(local_var_params['posthog_session']) > 255):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `posthog_session` when calling `crash_reports_create`, length must be less than or equal to `255`")  # noqa: E501
        if self.api_client.client_side_validation and ('posthog_session' in local_var_params and  # noqa: E501
                                                        len(local_var_params['posthog_session']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `posthog_session` when calling `crash_reports_create`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}
        if 'email' in local_var_params:
            form_params.append(('email', local_var_params['email']))  # noqa: E501
        if 'os_version' in local_var_params:
            form_params.append(('os_version', local_var_params['os_version']))  # noqa: E501
        if 'os_logs' in local_var_params:
            local_var_files['os_logs'] = local_var_params['os_logs']  # noqa: E501
        if 'browser_version' in local_var_params:
            form_params.append(('browser_version', local_var_params['browser_version']))  # noqa: E501
        if 'browser_logs' in local_var_params:
            local_var_files['browser_logs'] = local_var_params['browser_logs']  # noqa: E501
        if 'serial' in local_var_params:
            form_params.append(('serial', local_var_params['serial']))  # noqa: E501
        if 'posthog_session' in local_var_params:
            form_params.append(('posthog_session', local_var_params['posthog_session']))  # noqa: E501
        if 'user' in local_var_params:
            form_params.append(('user', local_var_params['user']))  # noqa: E501
        if 'pi' in local_var_params:
            form_params.append(('pi', local_var_params['pi']))  # noqa: E501
        if 'related_crash_report' in local_var_params:
            form_params.append(('related_crash_report', local_var_params['related_crash_report']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/x-www-form-urlencoded', 'multipart/form-data'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'tokenAuth']  # noqa: E501

        response_types_map = {
            201: "CrashReport",
            409: "ErrorDetail",
            400: "ErrorDetail",
            401: "ErrorDetail",
            403: "ErrorDetail",
            500: "ErrorDetail",
        }

        return self.api_client.call_api(
            '/api/crash-reports/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
