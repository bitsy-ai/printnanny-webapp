# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.127.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.video_recording_part import VideoRecordingPart  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestVideoRecordingPart(unittest.TestCase):
    """VideoRecordingPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VideoRecordingPart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.video_recording_part.VideoRecordingPart()  # noqa: E501
        if include_optional :
            return VideoRecordingPart(
                id = '', 
                mp4_upload_url = '', 
                part = -2147483648, 
                size = -9223372036854775808, 
                mp4_file = '', 
                video_recording = ''
            )
        else :
            return VideoRecordingPart(
                id = '',
                mp4_upload_url = '',
                part = -2147483648,
                size = -9223372036854775808,
                mp4_file = '',
                video_recording = '',
        )

    def testVideoRecordingPart(self):
        """Test VideoRecordingPart"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
