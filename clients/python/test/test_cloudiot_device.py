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
from printnanny_api_client.models.cloudiot_device import CloudiotDevice  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestCloudiotDevice(unittest.TestCase):
    """CloudiotDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CloudiotDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.cloudiot_device.CloudiotDevice()  # noqa: E501
        if include_optional :
            return CloudiotDevice(
                num_id = -9223372036854775808, 
                desired_config_topic = '', 
                current_state_topic = '', 
                gcp_project_id = '', 
                gcp_region = '', 
                gcp_cloudiot_device_registry = '', 
                mqtt_bridge_hostname = '', 
                mqtt_bridge_port = 56, 
                mqtt_client_id = '', 
                deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '', 
                id = '', 
                device = 56
            )
        else :
            return CloudiotDevice(
                num_id = -9223372036854775808,
                name = '',
                id = '',
                device = 56,
        )

    def testCloudiotDevice(self):
        """Test CloudiotDevice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
