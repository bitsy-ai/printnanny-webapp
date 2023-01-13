# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_octo_print_backup_list import PaginatedOctoPrintBackupList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedOctoPrintBackupList(unittest.TestCase):
    """PaginatedOctoPrintBackupList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedOctoPrintBackupList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_octo_print_backup_list.PaginatedOctoPrintBackupList()  # noqa: E501
        if include_optional :
            return PaginatedOctoPrintBackupList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.octo_print_backup.OctoPrintBackup(
                        id = 56, 
                        deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        hostname = '', 
                        name = '', 
                        octoprint_version = '', 
                        file = '', 
                        user = 56, )
                    ]
            )
        else :
            return PaginatedOctoPrintBackupList(
        )

    def testPaginatedOctoPrintBackupList(self):
        """Test PaginatedOctoPrintBackupList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
