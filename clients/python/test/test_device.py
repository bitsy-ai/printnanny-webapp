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
from printnanny_api_client.models.device import Device  # noqa: E501
from printnanny_api_client.rest import ApiException

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
        # model = printnanny_api_client.models.device.Device()  # noqa: E501
        if include_optional :
            return Device(
                id = 56, 
                cloudiot_device = None, 
                dashboard_url = '', 
                video_test_url = '', 
                janus_auth = None, 
                janus_local_url = '', 
                monitoring_active = True, 
                setup_complete = True, 
                user = None, 
                release_channel = None, 
                system_info = None, 
                public_key = None, 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                hostname = ''
            )
        else :
            return Device(
                id = 56,
                cloudiot_device = None,
                dashboard_url = '',
                video_test_url = '',
                janus_auth = None,
                janus_local_url = '',
                user = None,
                system_info = None,
                public_key = None,
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testDevice(self):
        """Test Device"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
