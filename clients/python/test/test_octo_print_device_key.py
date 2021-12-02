# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.octo_print_device_key import OctoPrintDeviceKey  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestOctoPrintDeviceKey(unittest.TestCase):
    """OctoPrintDeviceKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoPrintDeviceKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.octo_print_device_key.OctoPrintDeviceKey()  # noqa: E501
        if include_optional :
            return OctoPrintDeviceKey(
                active_session = printnanny_api_client.models.print_session.PrintSession(
                    id = 56, 
                    created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    octoprint_device = 56, 
                    active = True, 
                    session = '', 
                    filepos = -2147483648, 
                    print_progress = -2147483648, 
                    time_elapsed = -2147483648, 
                    time_remaining = -2147483648, 
                    user = 56, 
                    printer_profile = 56, 
                    gcode_file = 56, 
                    gcode_filename = '', 
                    octoprint_job = {
                        'key' : null
                        }, 
                    print_job_status = null, 
                    url = '', 
                    datesegment = '', ), 
                ca_certs = {
                    'key' : ''
                    }, 
                cloudiot_device_configs = '', 
                cloudiot_device_name = '', 
                cloudiot_device_num_id = 56, 
                cloudiot_device_path = '', 
                cloudiot_device = {
                    'key' : null
                    }, 
                cores = -2147483648, 
                cpu_flags = [
                    ''
                    ], 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                fingerprint = '', 
                hardware = '', 
                id = 56, 
                manage_url = '', 
                model = '', 
                monitoring_active = True, 
                name = '', 
                octoprint_version = '', 
                pip_version = '', 
                platform = '', 
                plugin_version = '', 
                print_nanny_client_version = '', 
                private_key_checksum = '', 
                private_key = '', 
                public_key_checksum = '', 
                public_key = '', 
                python_version = '', 
                ram = -2147483648, 
                revision = '', 
                serial = '', 
                user = 56, 
                url = ''
            )
        else :
            return OctoPrintDeviceKey(
                ca_certs = {
                    'key' : ''
                    },
                cloudiot_device_configs = '',
                cloudiot_device_name = '',
                cloudiot_device_num_id = 56,
                cloudiot_device_path = '',
                cloudiot_device = {
                    'key' : null
                    },
                cores = -2147483648,
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                fingerprint = '',
                id = 56,
                manage_url = '',
                model = '',
                monitoring_active = True,
                name = '',
                octoprint_version = '',
                pip_version = '',
                platform = '',
                plugin_version = '',
                print_nanny_client_version = '',
                private_key_checksum = '',
                private_key = '',
                public_key_checksum = '',
                public_key = '',
                python_version = '',
                ram = -2147483648,
                serial = '',
                user = 56,
                url = '',
        )

    def testOctoPrintDeviceKey(self):
        """Test OctoPrintDeviceKey"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
