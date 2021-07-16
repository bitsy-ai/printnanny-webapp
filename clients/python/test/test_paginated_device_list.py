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
from print_nanny_client.models.paginated_device_list import PaginatedDeviceList  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPaginatedDeviceList(unittest.TestCase):
    """PaginatedDeviceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedDeviceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.paginated_device_list.PaginatedDeviceList()  # noqa: E501
        if include_optional :
            return PaginatedDeviceList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    print_nanny_client.models.device.Device(
                        id = 56, 
                        deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user = 56, 
                        name = '', 
                        public_key = '', 
                        fingerprint = '', 
                        cloudiot_device = {
                            'key' : null
                            }, 
                        cloudiot_device_name = '', 
                        cloudiot_device_path = '', 
                        cloudiot_device_num_id = 56, 
                        os_version = '', 
                        os = '', 
                        kernel_version = '', 
                        hardware = '', 
                        revision = '', 
                        model = '', 
                        serial = '', 
                        cores = -2147483648, 
                        ram = -9223372036854775808, 
                        cpu_flags = '', 
                        url = '', )
                    ]
            )
        else :
            return PaginatedDeviceList(
        )

    def testPaginatedDeviceList(self):
        """Test PaginatedDeviceList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
