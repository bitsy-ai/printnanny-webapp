# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.octo_print_settings_request import OctoPrintSettingsRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestOctoPrintSettingsRequest(unittest.TestCase):
    """OctoPrintSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoPrintSettingsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.octo_print_settings_request.OctoPrintSettingsRequest()  # noqa: E501
        if include_optional :
            return OctoPrintSettingsRequest(
                sync_gcode = True, 
                sync_printer_profiles = True, 
                sync_backups = True, 
                monitoring_auto_start = True, 
                monitoring_auto_pause = True
            )
        else :
            return OctoPrintSettingsRequest(
        )

    def testOctoPrintSettingsRequest(self):
        """Test OctoPrintSettingsRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
