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
from print_nanny_client.models.create_defect_alert_request import CreateDefectAlertRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestCreateDefectAlertRequest(unittest.TestCase):
    """CreateDefectAlertRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateDefectAlertRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.create_defect_alert_request.CreateDefectAlertRequest()  # noqa: E501
        if include_optional :
            return CreateDefectAlertRequest(
                print_session = ''
            )
        else :
            return CreateDefectAlertRequest(
                print_session = '',
        )

    def testCreateDefectAlertRequest(self):
        """Test CreateDefectAlertRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
