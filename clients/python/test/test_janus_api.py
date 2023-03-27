# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.130.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.janus_api import JanusApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestJanusApi(unittest.TestCase):
    """JanusApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.janus_api.JanusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pis_webrtc_streams_create(self):
        """Test case for pis_webrtc_streams_create

        """
        pass

    def test_pis_webrtc_streams_list(self):
        """Test case for pis_webrtc_streams_list

        """
        pass

    def test_pis_webrtc_streams_partial_update(self):
        """Test case for pis_webrtc_streams_partial_update

        """
        pass

    def test_pis_webrtc_streams_retrieve(self):
        """Test case for pis_webrtc_streams_retrieve

        """
        pass

    def test_pis_webrtc_streams_update(self):
        """Test case for pis_webrtc_streams_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
