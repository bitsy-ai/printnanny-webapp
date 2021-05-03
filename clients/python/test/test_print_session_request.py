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
from print_nanny_client.models.print_session_request import PrintSessionRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPrintSessionRequest(unittest.TestCase):
    """PrintSessionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintSessionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.print_session_request.PrintSessionRequest()  # noqa: E501
        if include_optional :
            return PrintSessionRequest(
                octoprint_device = 56, 
                session = '', 
                filepos = -2147483648, 
                print_progress = -2147483648, 
                time_elapsed = -2147483648, 
                time_remaining = -2147483648, 
                status = 'monitoring_active', 
                printer_profile = 56, 
                gcode_file = 56, 
                gcode_filename = ''
            )
        else :
            return PrintSessionRequest(
                octoprint_device = 56,
                session = '',
        )

    def testPrintSessionRequest(self):
        """Test PrintSessionRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
