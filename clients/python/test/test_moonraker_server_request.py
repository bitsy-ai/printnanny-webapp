# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.131.9
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.moonraker_server_request import MoonrakerServerRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestMoonrakerServerRequest(unittest.TestCase):
    """MoonrakerServerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MoonrakerServerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.moonraker_server_request.MoonrakerServerRequest()  # noqa: E501
        if include_optional :
            return MoonrakerServerRequest(
                base_path = '0', 
                moonraker_version = '0', 
                pip_version = '0', 
                python_version = '0', 
                api_key = '0', 
                pi = 56
            )
        else :
            return MoonrakerServerRequest(
                base_path = '0',
                pi = 56,
        )

    def testMoonrakerServerRequest(self):
        """Test MoonrakerServerRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
