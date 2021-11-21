# coding: utf-8

"""
    print-nanny-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import print_nanny_client
from print_nanny_client.models.release_channel_enum import ReleaseChannelEnum  # noqa: E501
from print_nanny_client.rest import ApiException

class TestReleaseChannelEnum(unittest.TestCase):
    """ReleaseChannelEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReleaseChannelEnum
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.release_channel_enum.ReleaseChannelEnum()  # noqa: E501
        if include_optional :
            return ReleaseChannelEnum(
            )
        else :
            return ReleaseChannelEnum(
        )

    def testReleaseChannelEnum(self):
        """Test ReleaseChannelEnum"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
