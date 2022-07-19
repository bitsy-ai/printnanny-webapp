# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.95.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_alert_list import PaginatedAlertList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedAlertList(unittest.TestCase):
    """PaginatedAlertList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedAlertList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_alert_list.PaginatedAlertList()  # noqa: E501
        if include_optional :
            return PaginatedAlertList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.alert.Alert(
                        id = 56, 
                        time = '', 
                        gcode_file = '', 
                        print_progress = '', 
                        time_elapsed = '', 
                        time_remaining = '', 
                        manage_device_url = '', 
                        user = 56, 
                        octoprint_device = 56, 
                        event_type = null, 
                        seen = True, 
                        sent = True, 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', )
                    ]
            )
        else :
            return PaginatedAlertList(
        )

    def testPaginatedAlertList(self):
        """Test PaginatedAlertList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
