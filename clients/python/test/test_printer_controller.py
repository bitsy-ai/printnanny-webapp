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
from print_nanny_client.models.printer_controller import PrinterController  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPrinterController(unittest.TestCase):
    """PrinterController unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrinterController
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.printer_controller.PrinterController()  # noqa: E501
        if include_optional :
            return PrinterController(
                id = 56, 
                user = 56, 
                appliance = 56, 
                deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                software = 'OctoPrint', 
                polymorphic_ctype = 56
            )
        else :
            return PrinterController(
                software = 'OctoPrint',
        )

    def testPrinterController(self):
        """Test PrinterController"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
