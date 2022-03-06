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
from printnanny_api_client.models.paginated_octo_print_device_list import PaginatedOctoPrintDeviceList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedOctoPrintDeviceList(unittest.TestCase):
    """PaginatedOctoPrintDeviceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedOctoPrintDeviceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_octo_print_device_list.PaginatedOctoPrintDeviceList()  # noqa: E501
        if include_optional :
            return PaginatedOctoPrintDeviceList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.octo_print_device.OctoPrintDevice(
                        id = 56, 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        user = 56, 
                        public_key = '', 
                        fingerprint = '', 
                        cloudiot_device = {
                            'key' : null
                            }, 
                        cloudiot_device_name = '', 
                        cloudiot_device_path = '', 
                        cloudiot_device_num_id = 56, 
                        model = '', 
                        platform = '', 
                        cpu_flags = [
                            ''
                            ], 
                        hardware = '', 
                        revision = '', 
                        serial = '', 
                        cores = -2147483648, 
                        ram = -2147483648, 
                        python_version = '', 
                        pip_version = '', 
                        virtualenv = '', 
                        octoprint_version = '', 
                        plugin_version = '', 
                        print_nanny_client_version = '', 
                        print_nanny_beta_client_version = '', 
                        cloudiot_device_configs = '', 
                        manage_url = '', 
                        monitoring_active = True, 
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
                            datesegment = '', ), )
                    ]
            )
        else :
            return PaginatedOctoPrintDeviceList(
        )

    def testPaginatedOctoPrintDeviceList(self):
        """Test PaginatedOctoPrintDeviceList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
