# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.127.2
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.shop_api import ShopApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestShopApi(unittest.TestCase):
    """ShopApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.shop_api.ShopApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cloud_plans_retrieve(self):
        """Test case for cloud_plans_retrieve

        """
        pass

    def test_shop_checkout_success_retrieve(self):
        """Test case for shop_checkout_success_retrieve

        """
        pass

    def test_shop_orders_create(self):
        """Test case for shop_orders_create

        """
        pass

    def test_shop_products_list(self):
        """Test case for shop_products_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
