# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.5
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_polymorphic_pi_event_list import PaginatedPolymorphicPiEventList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedPolymorphicPiEventList(unittest.TestCase):
    """PaginatedPolymorphicPiEventList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedPolymorphicPiEventList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_polymorphic_pi_event_list.PaginatedPolymorphicPiEventList()  # noqa: E501
        if include_optional :
            return PaginatedPolymorphicPiEventList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    null
                    ]
            )
        else :
            return PaginatedPolymorphicPiEventList(
        )

    def testPaginatedPolymorphicPiEventList(self):
        """Test PaginatedPolymorphicPiEventList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
