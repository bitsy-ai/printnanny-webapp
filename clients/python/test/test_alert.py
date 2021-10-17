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
from print_nanny_client.models.alert import Alert  # noqa: E501
from print_nanny_client.rest import ApiException

class TestAlert(unittest.TestCase):
    """Alert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Alert
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.alert.Alert()  # noqa: E501
        if include_optional :
            return Alert(
                id = 56, 
                time = '', 
                gcode_file = '', 
                print_progress = '', 
                time_elapsed = '', 
                time_remaining = '', 
                manage_device_url = '', 
                user = 56, 
                octoprint_device = 56, 
                event_type = None, 
                seen = True, 
                sent = True, 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = ''
            )
        else :
            return Alert(
        )

    def testAlert(self):
        """Test Alert"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
