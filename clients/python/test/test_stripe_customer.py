# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.3
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.stripe_customer import StripeCustomer  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestStripeCustomer(unittest.TestCase):
    """StripeCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StripeCustomer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.stripe_customer.StripeCustomer()  # noqa: E501
        if include_optional :
            return StripeCustomer(
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
                address = {
                    'key' : null
                    }, 
                balance = -9223372036854775808, 
                currency = '', 
                delinquent = True, 
                deleted = True, 
                coupon_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                coupon_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                email = '', 
                invoice_prefix = '', 
                invoice_settings = {
                    'key' : null
                    }, 
                name = '', 
                phone = '', 
                preferred_locales = {
                    'key' : null
                    }, 
                shipping = {
                    'key' : null
                    }, 
                tax_exempt = None, 
                date_purged = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                djstripe_owner_account = '', 
                default_source = '', 
                coupon = 56, 
                default_payment_method = '', 
                subscriber = 56
            )
        else :
            return StripeCustomer(
                djstripe_id = 56,
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                coupon_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                coupon_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                date_purged = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_owner_account = '',
                subscriber = 56,
        )

    def testStripeCustomer(self):
        """Test StripeCustomer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
