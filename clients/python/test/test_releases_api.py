# coding: utf-8

"""
    print-nanny-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import print_nanny_client
from print_nanny_client.api.releases_api import ReleasesApi  # noqa: E501
from print_nanny_client.rest import ApiException


class TestReleasesApi(unittest.TestCase):
    """ReleasesApi unit test stubs"""

    def setUp(self):
        self.api = print_nanny_client.api.releases_api.ReleasesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_releases_latest_retrieve(self):
        """Test case for releases_latest_retrieve

        """
        pass

    def test_releases_list(self):
        """Test case for releases_list

        """
        pass

    def test_releases_retrieve(self):
        """Test case for releases_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
