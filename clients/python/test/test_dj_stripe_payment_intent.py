# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.129.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.dj_stripe_payment_intent import DjStripePaymentIntent  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestDjStripePaymentIntent(unittest.TestCase):
    """DjStripePaymentIntent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DjStripePaymentIntent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.dj_stripe_payment_intent.DjStripePaymentIntent()  # noqa: E501
        if include_optional :
            return DjStripePaymentIntent(
                djstripe_id = 56, 
                cancellation_reason = 'abandoned', 
                charges = [
                    printnanny_api_client.models.dj_stripe_charge.DjStripeCharge(
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
                        status = null, 
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
                        transfer = '', )
                    ], 
                setup_future_usage = 'off_session', 
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '', 
                livemode = True, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                metadata = {
                    'key' : null
                    }, 
                amount = -9223372036854775808, 
                amount_capturable = -9223372036854775808, 
                amount_received = -9223372036854775808, 
                canceled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                capture_method = None, 
                client_secret = '', 
                confirmation_method = None, 
                currency = '', 
                description = '', 
                last_payment_error = {
                    'key' : null
                    }, 
                next_action = {
                    'key' : null
                    }, 
                payment_method_types = {
                    'key' : null
                    }, 
                receipt_email = '', 
                shipping = {
                    'key' : null
                    }, 
                statement_descriptor = '', 
                status = None, 
                transfer_data = {
                    'key' : null
                    }, 
                transfer_group = '', 
                djstripe_owner_account = '', 
                customer = '', 
                on_behalf_of = '', 
                payment_method = ''
            )
        else :
            return DjStripePaymentIntent(
                djstripe_id = 56,
                cancellation_reason = 'abandoned',
                charges = [
                    printnanny_api_client.models.dj_stripe_charge.DjStripeCharge(
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
                        status = null, 
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
                        transfer = '', )
                    ],
                setup_future_usage = 'off_session',
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                amount = -9223372036854775808,
                amount_capturable = -9223372036854775808,
                amount_received = -9223372036854775808,
                capture_method = None,
                client_secret = '',
                confirmation_method = None,
                currency = '',
                payment_method_types = {
                    'key' : null
                    },
                status = None,
        )

    def testDjStripePaymentIntent(self):
        """Test DjStripePaymentIntent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
