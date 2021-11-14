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
from print_nanny_client.models.printer_controller_request import PrinterControllerRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPrinterControllerRequest(unittest.TestCase):
    """PrinterControllerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrinterControllerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.printer_controller_request.PrinterControllerRequest()  # noqa: E501
        if include_optional :
            return PrinterControllerRequest(
                software = None, 
                user = 56, 
                device = 56
            )
        else :
            return PrinterControllerRequest(
                user = 56,
                device = 56,
        )

    def testPrinterControllerRequest(self):
        """Test PrinterControllerRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
