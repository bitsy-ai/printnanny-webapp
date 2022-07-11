# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.nested_request import NestedRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestNestedRequest(unittest.TestCase):
    """NestedRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NestedRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.nested_request.NestedRequest()  # noqa: E501
        if include_optional :
            return NestedRequest(
                password = '0', 
                is_serviceuser = True, 
                is_superuser = True, 
                is_staff = True, 
                is_active = True, 
                date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                first_name = '', 
                last_name = '', 
                email = '0', 
                groups = [
                    56
                    ], 
                user_permissions = [
                    56
                    ]
            )
        else :
            return NestedRequest(
                password = '0',
                email = '0',
        )

    def testNestedRequest(self):
        """Test NestedRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
