# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.print_job_alert_request import PrintJobAlertRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPrintJobAlertRequest(unittest.TestCase):
    """PrintJobAlertRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintJobAlertRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.print_job_alert_request.PrintJobAlertRequest()  # noqa: E501
        if include_optional :
            return PrintJobAlertRequest(
                event_type = 'PrintQuality', 
                event_source = 'octoprint', 
                payload = {
                    'key' : null
                    }, 
                pi = 56
            )
        else :
            return PrintJobAlertRequest(
                event_type = 'PrintQuality',
                event_source = 'octoprint',
                pi = 56,
        )

    def testPrintJobAlertRequest(self):
        """Test PrintJobAlertRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
