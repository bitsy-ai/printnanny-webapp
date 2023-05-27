# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.dj_stripe_charge import DjStripeCharge  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestDjStripeCharge(unittest.TestCase):
    """DjStripeCharge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DjStripeCharge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.dj_stripe_charge.DjStripeCharge()  # noqa: E501
        if include_optional :
            return DjStripeCharge(
                djstripe_id = 56, 
                failure_code = 'account_already_exists', 
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '', 
                livemode = True, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                metadata = {
                    'key' : null
                    }, 
                description = '', 
                amount = '-8072', 
                amount_captured = '-8072', 
                amount_refunded = '-8072', 
                application = '', 
                application_fee_amount = '-8072', 
                billing_details = {
                    'key' : null
                    }, 
                calculated_statement_descriptor = '', 
                captured = True, 
                currency = '', 
                disputed = True, 
                failure_message = '', 
                fraud_details = {
                    'key' : null
                    }, 
                outcome = {
                    'key' : null
                    }, 
                paid = True, 
                payment_method_details = {
                    'key' : null
                    }, 
                receipt_email = '', 
                receipt_number = '', 
                receipt_url = '', 
                refunded = True, 
                shipping = {
                    'key' : null
                    }, 
                statement_descriptor = '', 
                statement_descriptor_suffix = '', 
                status = None, 
                transfer_data = {
                    'key' : null
                    }, 
                transfer_group = '', 
                djstripe_owner_account = '', 
                application_fee = '', 
                balance_transaction = '', 
                customer = '', 
                dispute = '', 
                invoice = '', 
                on_behalf_of = '', 
                payment_intent = '', 
                payment_method = '', 
                source = '', 
                source_transfer = '', 
                transfer = ''
            )
        else :
            return DjStripeCharge(
                djstripe_id = 56,
                failure_code = 'account_already_exists',
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                amount = '-8072',
                amount_refunded = '-8072',
                currency = '',
                status = None,
        )

    def testDjStripeCharge(self):
        """Test DjStripeCharge"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
