# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.120.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.dj_stripe_checkout_session import DjStripeCheckoutSession  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestDjStripeCheckoutSession(unittest.TestCase):
    """DjStripeCheckoutSession unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DjStripeCheckoutSession
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.dj_stripe_checkout_session.DjStripeCheckoutSession()  # noqa: E501
        if include_optional :
            return DjStripeCheckoutSession(
                djstripe_id = 56, 
                billing_address_collection = 'auto', 
                mode = 'payment', 
                submit_type = 'auto', 
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '', 
                livemode = True, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                metadata = {
                    'key' : null
                    }, 
                description = '', 
                cancel_url = '', 
                client_reference_id = '', 
                customer_email = '', 
                display_items = {
                    'key' : null
                    }, 
                locale = '', 
                payment_method_types = {
                    'key' : null
                    }, 
                success_url = '', 
                djstripe_owner_account = '', 
                customer = '', 
                payment_intent = '', 
                subscription = ''
            )
        else :
            return DjStripeCheckoutSession(
                djstripe_id = 56,
                billing_address_collection = 'auto',
                mode = 'payment',
                submit_type = 'auto',
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                payment_method_types = {
                    'key' : null
                    },
        )

    def testDjStripeCheckoutSession(self):
        """Test DjStripeCheckoutSession"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
