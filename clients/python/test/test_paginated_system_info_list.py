# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.94.3
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_system_info_list import PaginatedSystemInfoList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedSystemInfoList(unittest.TestCase):
    """PaginatedSystemInfoList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedSystemInfoList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_system_info_list.PaginatedSystemInfoList()  # noqa: E501
        if include_optional :
            return PaginatedSystemInfoList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.system_info.SystemInfo(
                        id = 56, 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        machine_id = '', 
                        revision = '', 
                        model = '', 
                        serial = '', 
                        cores = -2147483648, 
                        ram = -9223372036854775808, 
                        os_version_id = '', 
                        os_build_id = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        os_variant_id = '', 
                        os_release_json = {
                            'key' : null
                            }, 
                        device = 56, )
                    ]
            )
        else :
            return PaginatedSystemInfoList(
        )

    def testPaginatedSystemInfoList(self):
        """Test PaginatedSystemInfoList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
