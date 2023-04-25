# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.133.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.callback_token_auth_request import CallbackTokenAuthRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestCallbackTokenAuthRequest(unittest.TestCase):
    """CallbackTokenAuthRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CallbackTokenAuthRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.callback_token_auth_request.CallbackTokenAuthRequest()  # noqa: E501
        if include_optional :
            return CallbackTokenAuthRequest(
                email = '0', 
                mobile = '+6807288800150', 
                token = '012345'
            )
        else :
            return CallbackTokenAuthRequest(
                token = '012345',
        )

    def testCallbackTokenAuthRequest(self):
        """Test CallbackTokenAuthRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
