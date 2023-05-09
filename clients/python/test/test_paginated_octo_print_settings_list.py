# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.134.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_octo_print_settings_list import PaginatedOctoPrintSettingsList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedOctoPrintSettingsList(unittest.TestCase):
    """PaginatedOctoPrintSettingsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedOctoPrintSettingsList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_octo_print_settings_list.PaginatedOctoPrintSettingsList()  # noqa: E501
        if include_optional :
            return PaginatedOctoPrintSettingsList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.octo_print_settings.OctoPrintSettings(
                        id = 56, 
                        octoprint_enabled = True, 
                        events_enabled = True, 
                        sync_gcode = True, 
                        sync_printer_profiles = True, 
                        sync_backups = True, 
                        auto_backup = '', 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        octoprint_server = 56, 
                        user = 56, )
                    ]
            )
        else :
            return PaginatedOctoPrintSettingsList(
        )

    def testPaginatedOctoPrintSettingsList(self):
        """Test PaginatedOctoPrintSettingsList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
