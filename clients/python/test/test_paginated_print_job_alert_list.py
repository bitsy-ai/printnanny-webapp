# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.132.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_print_job_alert_list import PaginatedPrintJobAlertList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedPrintJobAlertList(unittest.TestCase):
    """PaginatedPrintJobAlertList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedPrintJobAlertList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_print_job_alert_list.PaginatedPrintJobAlertList()  # noqa: E501
        if include_optional :
            return PaginatedPrintJobAlertList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.print_job_alert.PrintJobAlert(
                        id = '', 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        event_type = 'PrintQuality', 
                        event_source = 'octoprint', 
                        payload = {
                            'key' : null
                            }, 
                        email_message_id = '', 
                        celery_task_id = '', 
                        user = 56, 
                        pi = 56, )
                    ]
            )
        else :
            return PaginatedPrintJobAlertList(
        )

    def testPaginatedPrintJobAlertList(self):
        """Test PaginatedPrintJobAlertList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
