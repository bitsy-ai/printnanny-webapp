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
from print_nanny_client.models.paginated_ansible_facts_list import PaginatedAnsibleFactsList  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPaginatedAnsibleFactsList(unittest.TestCase):
    """PaginatedAnsibleFactsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedAnsibleFactsList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.paginated_ansible_facts_list.PaginatedAnsibleFactsList()  # noqa: E501
        if include_optional :
            return PaginatedAnsibleFactsList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    print_nanny_client.models.ansible_facts.AnsibleFacts(
                        id = 56, 
                        user = '', 
                        device = 56, 
                        deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        os_version = '', 
                        os = '', 
                        kernel_version = '', 
                        hardware = '', 
                        revision = '', 
                        model = '', 
                        serial = '', 
                        cores = -2147483648, 
                        ram = -9223372036854775808, 
                        cpu_flags = [
                            ''
                            ], 
                        release_channel = 'main', 
                        json = {
                            'key' : null
                            }, )
                    ]
            )
        else :
            return PaginatedAnsibleFactsList(
        )

    def testPaginatedAnsibleFactsList(self):
        """Test PaginatedAnsibleFactsList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
