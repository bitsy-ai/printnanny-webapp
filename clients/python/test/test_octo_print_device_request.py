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
from print_nanny_client.models.octo_print_device_request import OctoPrintDeviceRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestOctoPrintDeviceRequest(unittest.TestCase):
    """OctoPrintDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoPrintDeviceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.octo_print_device_request.OctoPrintDeviceRequest()  # noqa: E501
        if include_optional :
            return OctoPrintDeviceRequest(
                name = '', 
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
                active_session = print_nanny_client.models.print_session_request.PrintSessionRequest(
                    created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    octoprint_device = 56, 
                    active = True, 
                    session = '', 
                    filepos = -2147483648, 
                    print_progress = -2147483648, 
                    time_elapsed = -2147483648, 
                    time_remaining = -2147483648, 
                    printer_profile = 56, 
                    gcode_file = 56, 
                    gcode_filename = '', 
                    octoprint_job = {
                        'key' : null
                        }, 
                    print_job_status = null, )
            )
        else :
            return OctoPrintDeviceRequest(
                name = '',
                model = '',
                platform = '',
                serial = '',
                cores = -2147483648,
                ram = -2147483648,
                python_version = '',
                pip_version = '',
                octoprint_version = '',
                plugin_version = '',
                print_nanny_client_version = '',
        )

    def testOctoPrintDeviceRequest(self):
        """Test OctoPrintDeviceRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
