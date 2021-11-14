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
from print_nanny_client.models.device import Device  # noqa: E501
from print_nanny_client.rest import ApiException

class TestDevice(unittest.TestCase):
    """Device unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Device
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.device.Device()  # noqa: E501
        if include_optional :
            return Device(
                id = 56, 
                cloudiot_device = None, 
                cameras = [
                    print_nanny_client.models.camera.Camera(
                        id = 56, 
                        deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user = 56, 
                        device = 56, 
                        name = '', 
                        camera_type = null, 
                        camera_source = '', 
                        url = '', )
                    ], 
                dashboard_url = '', 
                bootstrap_release = None, 
                printer_controllers = [
                    print_nanny_client.models.printer_controller.PrinterController(
                        id = 56, 
                        software = null, 
                        deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        polymorphic_ctype = 56, 
                        user = 56, 
                        device = 56, )
                    ], 
                release_channel = None, 
                user = None, 
                license = None, 
                deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                hostname = ''
            )
        else :
            return Device(
        )

    def testDevice(self):
        """Test Device"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
