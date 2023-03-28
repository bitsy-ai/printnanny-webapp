# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.131.5
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.dj_stripe_product import DjStripeProduct  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestDjStripeProduct(unittest.TestCase):
    """DjStripeProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DjStripeProduct
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.dj_stripe_product.DjStripeProduct()  # noqa: E501
        if include_optional :
            return DjStripeProduct(
                djstripe_id = 56, 
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '', 
                livemode = True, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                metadata = {
                    'key' : null
                    }, 
                description = '', 
                name = '', 
                type = None, 
                active = True, 
                attributes = {
                    'key' : null
                    }, 
                caption = '', 
                deactivate_on = {
                    'key' : null
                    }, 
                images = {
                    'key' : null
                    }, 
                package_dimensions = {
                    'key' : null
                    }, 
                shippable = True, 
                url = '', 
                statement_descriptor = '', 
                unit_label = '', 
                djstripe_owner_account = ''
            )
        else :
            return DjStripeProduct(
                djstripe_id = 56,
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                name = '',
                type = None,
        )

    def testDjStripeProduct(self):
        """Test DjStripeProduct"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
