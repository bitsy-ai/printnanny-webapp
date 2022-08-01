# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.pi_settings_request import PiSettingsRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPiSettingsRequest(unittest.TestCase):
    """PiSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PiSettingsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.pi_settings_request.PiSettingsRequest()  # noqa: E501
        if include_optional :
            return PiSettingsRequest(
                cloud_video_enabled = True, 
                telemetry_enabled = True, 
                pi = 56
            )
        else :
            return PiSettingsRequest(
                pi = 56,
        )

    def testPiSettingsRequest(self):
        """Test PiSettingsRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
