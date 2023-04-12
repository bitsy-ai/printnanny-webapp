# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.132.3
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

    def test_pis_camera_snapshots_create(self):
        """Test case for pis_camera_snapshots_create

        """
        pass

    def test_pis_camera_snapshots_list(self):
        """Test case for pis_camera_snapshots_list

        """
        pass

    def test_pis_camera_snapshots_retrieve(self):
        """Test case for pis_camera_snapshots_retrieve

        """
        pass

    def test_video_parts_create(self):
        """Test case for video_parts_create

        """
        pass

    def test_video_parts_list(self):
        """Test case for video_parts_list

        """
        pass

    def test_video_parts_retrieve(self):
        """Test case for video_parts_retrieve

        """
        pass

    def test_video_recordings_finalize(self):
        """Test case for video_recordings_finalize

        """
        pass

    def test_video_recordings_update_or_create(self):
        """Test case for video_recordings_update_or_create

        """
        pass

    def test_videos_create(self):
        """Test case for videos_create

        """
        pass

    def test_videos_list(self):
        """Test case for videos_list

        """
        pass

    def test_videos_partial_update(self):
        """Test case for videos_partial_update

        """
        pass

    def test_videos_retrieve(self):
        """Test case for videos_retrieve

        """
        pass

    def test_videos_update(self):
        """Test case for videos_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
