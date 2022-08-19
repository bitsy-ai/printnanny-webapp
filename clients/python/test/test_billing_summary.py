# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.103.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.billing_summary import BillingSummary  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestBillingSummary(unittest.TestCase):
    """BillingSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BillingSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.billing_summary.BillingSummary()  # noqa: E501
        if include_optional :
            return BillingSummary(
                subscription = printnanny_api_client.models.stripe_subscription.StripeSubscription(
                    djstripe_id = 56, 
                    plan = printnanny_api_client.models.stripe_plan.StripePlan(
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
                        active = True, 
                        amount = '-8072', 
                        amount_decimal = '-8072888', 
                        currency = '', 
                        interval = null, 
                        interval_count = 0, 
                        nickname = '', 
                        tiers = {
                            'key' : null
                            }, 
                        transform_usage = {
                            'key' : null
                            }, 
                        trial_period_days = -2147483648, 
                        usage_type = null, 
                        djstripe_owner_account = '', 
                        product = '', ), 
                    default_payment_method = printnanny_api_client.models.stripe_payment_method.StripePaymentMethod(
                        djstripe_id = 56, 
                        djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        livemode = True, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        billing_details = {
                            'key' : null
                            }, 
                        type = null, 
                        acss_debit = {
                            'key' : null
                            }, 
                        afterpay_clearpay = {
                            'key' : null
                            }, 
                        alipay = {
                            'key' : null
                            }, 
                        au_becs_debit = {
                            'key' : null
                            }, 
                        bacs_debit = {
                            'key' : null
                            }, 
                        bancontact = {
                            'key' : null
                            }, 
                        boleto = {
                            'key' : null
                            }, 
                        card = {
                            'key' : null
                            }, 
                        card_present = {
                            'key' : null
                            }, 
                        eps = {
                            'key' : null
                            }, 
                        fpx = {
                            'key' : null
                            }, 
                        giropay = {
                            'key' : null
                            }, 
                        grabpay = {
                            'key' : null
                            }, 
                        ideal = {
                            'key' : null
                            }, 
                        interac_present = {
                            'key' : null
                            }, 
                        oxxo = {
                            'key' : null
                            }, 
                        p24 = {
                            'key' : null
                            }, 
                        sepa_debit = {
                            'key' : null
                            }, 
                        sofort = {
                            'key' : null
                            }, 
                        wechat_pay = {
                            'key' : null
                            }, 
                        djstripe_owner_account = '', 
                        customer = '', ), 
                    schedule = printnanny_api_client.models.stripe_subscription_schedule.StripeSubscriptionSchedule(
                        djstripe_id = 56, 
                        djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        livemode = True, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        billing_thresholds = {
                            'key' : null
                            }, 
                        canceled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        current_phase = {
                            'key' : null
                            }, 
                        default_settings = {
                            'key' : null
                            }, 
                        end_behavior = null, 
                        phases = {
                            'key' : null
                            }, 
                        released_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = null, 
                        djstripe_owner_account = '', 
                        customer = 56, 
                        released_subscription = 56, ), 
                    is_period_current = True, 
                    is_status_current = True, 
                    is_status_temporarily_current = True, 
                    is_valid = True, 
                    djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    livemode = True, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    metadata = {
                        'key' : null
                        }, 
                    description = '', 
                    application_fee_percent = '-807', 
                    billing_cycle_anchor = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    billing_thresholds = {
                        'key' : null
                        }, 
                    cancel_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    cancel_at_period_end = True, 
                    canceled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    collection_method = null, 
                    current_period_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    current_period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    days_until_due = -2147483648, 
                    discount = {
                        'key' : null
                        }, 
                    ended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    next_pending_invoice_item_invoice = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    pending_invoice_item_interval = {
                        'key' : null
                        }, 
                    pending_update = {
                        'key' : null
                        }, 
                    quantity = -2147483648, 
                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status = null, 
                    trial_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    trial_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    djstripe_owner_account = '', 
                    customer = '', 
                    default_source = '', 
                    latest_invoice = '', 
                    pending_setup_intent = '', 
                    default_tax_rates = [
                        56
                        ], ), 
                customer = printnanny_api_client.models.stripe_customer.StripeCustomer(
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
                    tax_exempt = null, 
                    date_purged = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    djstripe_owner_account = '', 
                    default_source = '', 
                    coupon = 56, 
                    default_payment_method = '', 
                    subscriber = 56, ), 
                user = None, 
                billing_portal_url = ''
            )
        else :
            return BillingSummary(
                subscription = printnanny_api_client.models.stripe_subscription.StripeSubscription(
                    djstripe_id = 56, 
                    plan = printnanny_api_client.models.stripe_plan.StripePlan(
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
                        active = True, 
                        amount = '-8072', 
                        amount_decimal = '-8072888', 
                        currency = '', 
                        interval = null, 
                        interval_count = 0, 
                        nickname = '', 
                        tiers = {
                            'key' : null
                            }, 
                        transform_usage = {
                            'key' : null
                            }, 
                        trial_period_days = -2147483648, 
                        usage_type = null, 
                        djstripe_owner_account = '', 
                        product = '', ), 
                    default_payment_method = printnanny_api_client.models.stripe_payment_method.StripePaymentMethod(
                        djstripe_id = 56, 
                        djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        livemode = True, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        billing_details = {
                            'key' : null
                            }, 
                        type = null, 
                        acss_debit = {
                            'key' : null
                            }, 
                        afterpay_clearpay = {
                            'key' : null
                            }, 
                        alipay = {
                            'key' : null
                            }, 
                        au_becs_debit = {
                            'key' : null
                            }, 
                        bacs_debit = {
                            'key' : null
                            }, 
                        bancontact = {
                            'key' : null
                            }, 
                        boleto = {
                            'key' : null
                            }, 
                        card = {
                            'key' : null
                            }, 
                        card_present = {
                            'key' : null
                            }, 
                        eps = {
                            'key' : null
                            }, 
                        fpx = {
                            'key' : null
                            }, 
                        giropay = {
                            'key' : null
                            }, 
                        grabpay = {
                            'key' : null
                            }, 
                        ideal = {
                            'key' : null
                            }, 
                        interac_present = {
                            'key' : null
                            }, 
                        oxxo = {
                            'key' : null
                            }, 
                        p24 = {
                            'key' : null
                            }, 
                        sepa_debit = {
                            'key' : null
                            }, 
                        sofort = {
                            'key' : null
                            }, 
                        wechat_pay = {
                            'key' : null
                            }, 
                        djstripe_owner_account = '', 
                        customer = '', ), 
                    schedule = printnanny_api_client.models.stripe_subscription_schedule.StripeSubscriptionSchedule(
                        djstripe_id = 56, 
                        djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        livemode = True, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        billing_thresholds = {
                            'key' : null
                            }, 
                        canceled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        current_phase = {
                            'key' : null
                            }, 
                        default_settings = {
                            'key' : null
                            }, 
                        end_behavior = null, 
                        phases = {
                            'key' : null
                            }, 
                        released_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = null, 
                        djstripe_owner_account = '', 
                        customer = 56, 
                        released_subscription = 56, ), 
                    is_period_current = True, 
                    is_status_current = True, 
                    is_status_temporarily_current = True, 
                    is_valid = True, 
                    djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    livemode = True, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    metadata = {
                        'key' : null
                        }, 
                    description = '', 
                    application_fee_percent = '-807', 
                    billing_cycle_anchor = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    billing_thresholds = {
                        'key' : null
                        }, 
                    cancel_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    cancel_at_period_end = True, 
                    canceled_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    collection_method = null, 
                    current_period_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    current_period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    days_until_due = -2147483648, 
                    discount = {
                        'key' : null
                        }, 
                    ended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    next_pending_invoice_item_invoice = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    pending_invoice_item_interval = {
                        'key' : null
                        }, 
                    pending_update = {
                        'key' : null
                        }, 
                    quantity = -2147483648, 
                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status = null, 
                    trial_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    trial_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    djstripe_owner_account = '', 
                    customer = '', 
                    default_source = '', 
                    latest_invoice = '', 
                    pending_setup_intent = '', 
                    default_tax_rates = [
                        56
                        ], ),
                customer = printnanny_api_client.models.stripe_customer.StripeCustomer(
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
                    tax_exempt = null, 
                    date_purged = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    djstripe_owner_account = '', 
                    default_source = '', 
                    coupon = 56, 
                    default_payment_method = '', 
                    subscriber = 56, ),
                billing_portal_url = '',
        )

    def testBillingSummary(self):
        """Test BillingSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
