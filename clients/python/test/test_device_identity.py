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
from print_nanny_client.models.device_identity import DeviceIdentity  # noqa: E501
from print_nanny_client.rest import ApiException

class TestDeviceIdentity(unittest.TestCase):
    """DeviceIdentity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceIdentity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.device_identity.DeviceIdentity()  # noqa: E501
        if include_optional :
            return DeviceIdentity(
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = 56, 
                name = '', 
                fingerprint = '', 
                cloudiot_device_name = '', 
                cloudiot_device_num_id = 56, 
                cloudiot_device_path = '', 
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
                url = '', 
                private_key = '', 
                private_key_checksum = '', 
                public_key = '', 
                public_key_checksum = '', 
                ca_certs = print_nanny_client.models.device_identity_ca_certs.DeviceIdentity_ca_certs(
                    primary = '', 
                    primary_checksum = '', 
                    backup = '', 
                    backup_checksum = '', )
            )
        else :
            return DeviceIdentity(
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = 56,
                name = '',
                fingerprint = '',
                cloudiot_device_name = '',
                cloudiot_device_num_id = 56,
                cloudiot_device_path = '',
                os_version = '',
                os = '',
                kernel_version = '',
                cores = -2147483648,
                ram = -9223372036854775808,
                cpu_flags = [
                    ''
                    ],
                url = '',
                private_key = '',
                private_key_checksum = '',
                public_key = '',
                public_key_checksum = '',
                ca_certs = print_nanny_client.models.device_identity_ca_certs.DeviceIdentity_ca_certs(
                    primary = '', 
                    primary_checksum = '', 
                    backup = '', 
                    backup_checksum = '', ),
        )

    def testDeviceIdentity(self):
        """Test DeviceIdentity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
