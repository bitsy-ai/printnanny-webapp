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
from printnanny_api_client.models.janus_cloud_stream import JanusCloudStream  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestJanusCloudStream(unittest.TestCase):
    """JanusCloudStream unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JanusCloudStream
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.janus_cloud_stream.JanusCloudStream()  # noqa: E501
        if include_optional :
            return JanusCloudStream(
                id = 56, 
                auth = None, 
                api_domain = '', 
                api_port = 56, 
                api_url = '', 
                admin_url = '', 
                admin_port = 56, 
                rtp_port = 56, 
                rtp_domain = '', 
                websocket_url = '', 
                websocket_port = 56, 
                config_type = '', 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                active = True, 
                secret = '', 
                pin = '', 
                info = {
                    'key' : null
                    }, 
                ws_port = -2147483648, 
                device = 56
            )
        else :
            return JanusCloudStream(
                id = 56,
                auth = None,
                api_domain = '',
                api_port = 56,
                api_url = '',
                admin_url = '',
                admin_port = 56,
                rtp_port = 56,
                rtp_domain = '',
                websocket_url = '',
                websocket_port = 56,
                config_type = '',
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                device = 56,
        )

    def testJanusCloudStream(self):
        """Test JanusCloudStream"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
