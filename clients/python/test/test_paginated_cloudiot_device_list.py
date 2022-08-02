# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_cloudiot_device_list import PaginatedCloudiotDeviceList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedCloudiotDeviceList(unittest.TestCase):
    """PaginatedCloudiotDeviceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedCloudiotDeviceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_cloudiot_device_list.PaginatedCloudiotDeviceList()  # noqa: E501
        if include_optional :
            return PaginatedCloudiotDeviceList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.cloudiot_device.CloudiotDevice(
                        num_id = 56, 
                        command_topic = '', 
                        event_topic = '', 
                        config_topic = '', 
                        state_topic = '', 
                        gcp_resource = '', 
                        gcp_project_id = '', 
                        gcp_region = '', 
                        gcp_cloudiot_pi_registry = '', 
                        mqtt_bridge_hostname = '', 
                        mqtt_bridge_port = 56, 
                        mqtt_client_id = '', 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        id = '', 
                        pi = 56, 
                        public_key = 56, )
                    ]
            )
        else :
            return PaginatedCloudiotDeviceList(
        )

    def testPaginatedCloudiotDeviceList(self):
        """Test PaginatedCloudiotDeviceList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
