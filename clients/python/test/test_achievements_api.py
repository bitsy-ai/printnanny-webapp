# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.127.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.achievements_api import AchievementsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestAchievementsApi(unittest.TestCase):
    """AchievementsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.achievements_api.AchievementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_achievements_list(self):
        """Test case for achievements_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
