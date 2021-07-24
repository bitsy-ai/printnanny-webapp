# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import print_nanny_client
from print_nanny_client.models.print_job_event_request import PrintJobEventRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPrintJobEventRequest(unittest.TestCase):
    """PrintJobEventRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintJobEventRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.print_job_event_request.PrintJobEventRequest()  # noqa: E501
        if include_optional :
            return PrintJobEventRequest(
                event_type = 'PrintCancelled', 
                event_data = {
                    'key' : null
                    }, 
                octoprint_environment = {
                    'key' : null
                    }, 
                octoprint_printer_data = {
                    'key' : null
                    }, 
                temperature = {
                    'key' : null
                    }, 
                print_nanny_plugin_version = '', 
                print_nanny_client_version = '', 
                octoprint_version = '', 
                octoprint_device = 56, 
                print_session = 56
            )
        else :
            return PrintJobEventRequest(
                event_type = 'PrintCancelled',
                print_nanny_plugin_version = '',
                print_nanny_client_version = '',
                octoprint_version = '',
                octoprint_device = 56,
        )

    def testPrintJobEventRequest(self):
        """Test PrintJobEventRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
