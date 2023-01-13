# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.123.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.video_recording import VideoRecording  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestVideoRecording(unittest.TestCase):
    """VideoRecording unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VideoRecording
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.video_recording.VideoRecording()  # noqa: E501
        if include_optional :
            return VideoRecording(
                id = 56, 
                mjr_upload_url = '', 
                start_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                end_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '', 
                mjr_recording = '', 
                user = 56
            )
        else :
            return VideoRecording(
                id = 56,
                mjr_upload_url = '',
                start_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                user = 56,
        )

    def testVideoRecording(self):
        """Test VideoRecording"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
