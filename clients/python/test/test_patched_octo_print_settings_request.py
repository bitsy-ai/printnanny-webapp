# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.131.3
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.patched_octo_print_settings_request import PatchedOctoPrintSettingsRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPatchedOctoPrintSettingsRequest(unittest.TestCase):
    """PatchedOctoPrintSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedOctoPrintSettingsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.patched_octo_print_settings_request.PatchedOctoPrintSettingsRequest()  # noqa: E501
        if include_optional :
            return PatchedOctoPrintSettingsRequest(
                octoprint_enabled = True, 
                events_enabled = True, 
                sync_gcode = True, 
                sync_printer_profiles = True, 
                sync_backups = True, 
                auto_backup = '0', 
                octoprint_server = 56
            )
        else :
            return PatchedOctoPrintSettingsRequest(
        )

    def testPatchedOctoPrintSettingsRequest(self):
        """Test PatchedOctoPrintSettingsRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
