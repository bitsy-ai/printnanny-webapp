# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.131.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_webrtc_stream_list import PaginatedWebrtcStreamList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedWebrtcStreamList(unittest.TestCase):
    """PaginatedWebrtcStreamList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedWebrtcStreamList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_webrtc_stream_list.PaginatedWebrtcStreamList()  # noqa: E501
        if include_optional :
            return PaginatedWebrtcStreamList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.webrtc_stream.WebrtcStream(
                        active = True, 
                        admin_port = 56, 
                        admin_secret = '', 
                        admin_url = '', 
                        api_domain = '', 
                        api_port = 56, 
                        api_token = '', 
                        api_url = '', 
                        config_type = 'cloud', 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 56, 
                        info = {
                            'key' : null
                            }, 
                        is_admin = True, 
                        pi = 56, 
                        pt = 56, 
                        rtp_domain = '', 
                        video_rtp_port = 56, 
                        data_rtp_port = 56, 
                        rtpmap = '', 
                        stream_pin = '', 
                        stream_secret = '', 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        ws_port = 56, 
                        ws_url = '', )
                    ]
            )
        else :
            return PaginatedWebrtcStreamList(
        )

    def testPaginatedWebrtcStreamList(self):
        """Test PaginatedWebrtcStreamList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
