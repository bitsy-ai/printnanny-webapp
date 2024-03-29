# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.dj_stripe_price import DjStripePrice  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestDjStripePrice(unittest.TestCase):
    """DjStripePrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DjStripePrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.dj_stripe_price.DjStripePrice()  # noqa: E501
        if include_optional :
            return DjStripePrice(
                djstripe_id = 56, 
                billing_scheme = 'per_unit', 
                human_readable_price = '', 
                tiers_mode = 'graduated', 
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '', 
                livemode = True, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                metadata = {
                    'key' : null
                    }, 
                description = '', 
                active = True, 
                currency = '', 
                nickname = '', 
                recurring = {
                    'key' : null
                    }, 
                type = None, 
                unit_amount = -9223372036854775808, 
                unit_amount_decimal = '-8072888', 
                lookup_key = '', 
                tiers = {
                    'key' : null
                    }, 
                transform_quantity = {
                    'key' : null
                    }, 
                djstripe_owner_account = '', 
                product = ''
            )
        else :
            return DjStripePrice(
                djstripe_id = 56,
                billing_scheme = 'per_unit',
                human_readable_price = '',
                tiers_mode = 'graduated',
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                active = True,
                currency = '',
                type = None,
                product = '',
        )

    def testDjStripePrice(self):
        """Test DjStripePrice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
