# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.2
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.video_recordings_api import VideoRecordingsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestVideoRecordingsApi(unittest.TestCase):
    """VideoRecordingsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.video_recordings_api.VideoRecordingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_video_recordings_retrieve(self):
        """Test case for video_recordings_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
