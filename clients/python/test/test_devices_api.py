# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.8
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.devices_api import DevicesApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_network_settings_create(self):
        """Test case for network_settings_create

        """
        pass

    def test_network_settings_partial_update(self):
        """Test case for network_settings_partial_update

        """
        pass

    def test_network_settings_retrieve(self):
        """Test case for network_settings_retrieve

        """
        pass

    def test_network_settings_update(self):
        """Test case for network_settings_update

        """
        pass

    def test_pi_update_or_create(self):
        """Test case for pi_update_or_create

        """
        pass

    def test_pis_create(self):
        """Test case for pis_create

        """
        pass

    def test_pis_destroy(self):
        """Test case for pis_destroy

        """
        pass

    def test_pis_license_zip_retrieve(self):
        """Test case for pis_license_zip_retrieve

        """
        pass

    def test_pis_list(self):
        """Test case for pis_list

        """
        pass

    def test_pis_partial_update(self):
        """Test case for pis_partial_update

        """
        pass

    def test_pis_retrieve(self):
        """Test case for pis_retrieve

        """
        pass

    def test_pis_system_info_create(self):
        """Test case for pis_system_info_create

        """
        pass

    def test_pis_system_info_list(self):
        """Test case for pis_system_info_list

        """
        pass

    def test_pis_system_info_partial_update(self):
        """Test case for pis_system_info_partial_update

        """
        pass

    def test_pis_system_info_retrieve(self):
        """Test case for pis_system_info_retrieve

        """
        pass

    def test_pis_system_info_update(self):
        """Test case for pis_system_info_update

        """
        pass

    def test_pis_update(self):
        """Test case for pis_update

        """
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

    def test_system_info_update_or_create(self):
        """Test case for system_info_update_or_create

        """
        pass

    def test_webrtc_stream_update_or_create(self):
        """Test case for webrtc_stream_update_or_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
