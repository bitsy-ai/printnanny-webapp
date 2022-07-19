# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.95.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.octoprint_api import OctoprintApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestOctoprintApi(unittest.TestCase):
    """OctoprintApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.octoprint_api.OctoprintApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_devices_octoprint_list(self):
        """Test case for devices_octoprint_list

        """
        pass

    def test_octoprint_backups_create(self):
        """Test case for octoprint_backups_create

        """
        pass

    def test_octoprint_backups_list(self):
        """Test case for octoprint_backups_list

        """
        pass

    def test_octoprint_backups_retrieve(self):
        """Test case for octoprint_backups_retrieve

        """
        pass

    def test_octoprint_create(self):
        """Test case for octoprint_create

        """
        pass

    def test_octoprint_gcode_files_create(self):
        """Test case for octoprint_gcode_files_create

        """
        pass

    def test_octoprint_gcode_files_list(self):
        """Test case for octoprint_gcode_files_list

        """
        pass

    def test_octoprint_gcode_files_retrieve(self):
        """Test case for octoprint_gcode_files_retrieve

        """
        pass

    def test_octoprint_list(self):
        """Test case for octoprint_list

        """
        pass

    def test_octoprint_partial_update(self):
        """Test case for octoprint_partial_update

        """
        pass

    def test_octoprint_printer_profiles_create(self):
        """Test case for octoprint_printer_profiles_create

        """
        pass

    def test_octoprint_printer_profiles_list(self):
        """Test case for octoprint_printer_profiles_list

        """
        pass

    def test_octoprint_printer_profiles_partial_update(self):
        """Test case for octoprint_printer_profiles_partial_update

        """
        pass

    def test_octoprint_printer_profiles_update(self):
        """Test case for octoprint_printer_profiles_update

        """
        pass

    def test_octoprint_profile_update_or_create(self):
        """Test case for octoprint_profile_update_or_create

        """
        pass

    def test_octoprint_server_update_or_create(self):
        """Test case for octoprint_server_update_or_create

        """
        pass

    def test_octoprint_settings_create(self):
        """Test case for octoprint_settings_create

        """
        pass

    def test_octoprint_settings_list(self):
        """Test case for octoprint_settings_list

        """
        pass

    def test_octoprint_settings_partial_update(self):
        """Test case for octoprint_settings_partial_update

        """
        pass

    def test_octoprint_settings_update(self):
        """Test case for octoprint_settings_update

        """
        pass

    def test_octoprint_settings_update_or_create(self):
        """Test case for octoprint_settings_update_or_create

        """
        pass

    def test_octoprint_update(self):
        """Test case for octoprint_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
