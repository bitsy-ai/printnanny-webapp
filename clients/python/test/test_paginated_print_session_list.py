# coding: utf-8

"""
    print-nanny-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import print_nanny_client
from print_nanny_client.models.paginated_print_session_list import PaginatedPrintSessionList  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPaginatedPrintSessionList(unittest.TestCase):
    """PaginatedPrintSessionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedPrintSessionList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.paginated_print_session_list.PaginatedPrintSessionList()  # noqa: E501
        if include_optional :
            return PaginatedPrintSessionList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    print_nanny_client.models.print_session.PrintSession(
                        id = 56, 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        octoprint_device = 56, 
                        active = True, 
                        session = '', 
                        filepos = -2147483648, 
                        print_progress = -2147483648, 
                        time_elapsed = -2147483648, 
                        time_remaining = -2147483648, 
                        user = 56, 
                        printer_profile = 56, 
                        gcode_file = 56, 
                        gcode_filename = '', 
                        octoprint_job = {
                            'key' : null
                            }, 
                        print_job_status = null, 
                        url = '', 
                        datesegment = '', )
                    ]
            )
        else :
            return PaginatedPrintSessionList(
        )

    def testPaginatedPrintSessionList(self):
        """Test PaginatedPrintSessionList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
