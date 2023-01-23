# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.9
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_crash_report_list import PaginatedCrashReportList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedCrashReportList(unittest.TestCase):
    """PaginatedCrashReportList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedCrashReportList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_crash_report_list.PaginatedCrashReportList()  # noqa: E501
        if include_optional :
            return PaginatedCrashReportList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.crash_report.CrashReport(
                        id = '', 
                        url = '', 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        email = '', 
                        os_version = '', 
                        os_logs = '', 
                        browser_version = '', 
                        browser_logs = '', 
                        serial = '', 
                        posthog_session = '', 
                        status = 'Investigating', 
                        support_comment = '', 
                        user = 56, 
                        pi = 56, )
                    ]
            )
        else :
            return PaginatedCrashReportList(
        )

    def testPaginatedCrashReportList(self):
        """Test PaginatedCrashReportList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
