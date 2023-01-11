# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.121.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.pi_boot_status_type import PiBootStatusType  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPiBootStatusType(unittest.TestCase):
    """PiBootStatusType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PiBootStatusType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.pi_boot_status_type.PiBootStatusType()  # noqa: E501
        if include_optional :
            return PiBootStatusType(
            )
        else :
            return PiBootStatusType(
        )

    def testPiBootStatusType(self):
        """Test PiBootStatusType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
