# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.6
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.videos_api import VideosApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestVideosApi(unittest.TestCase):
    """VideosApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.videos_api.VideosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_video_recordings_create(self):
        """Test case for video_recordings_create

        """
        pass

    def test_video_recordings_get_or_create(self):
        """Test case for video_recordings_get_or_create

        """
        pass

    def test_video_recordings_list(self):
        """Test case for video_recordings_list

        """
        pass

    def test_video_recordings_partial_update(self):
        """Test case for video_recordings_partial_update

        """
        pass

    def test_video_recordings_retrieve(self):
        """Test case for video_recordings_retrieve

        """
        pass

    def test_video_recordings_update(self):
        """Test case for video_recordings_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
