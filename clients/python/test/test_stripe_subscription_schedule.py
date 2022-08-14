# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.101.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.stripe_subscription_schedule import StripeSubscriptionSchedule  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestStripeSubscriptionSchedule(unittest.TestCase):
    """StripeSubscriptionSchedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StripeSubscriptionSchedule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.stripe_subscription_schedule.StripeSubscriptionSchedule()  # noqa: E501
        if include_optional :
            return StripeSubscriptionSchedule(
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
                end_behavior = None, 
                phases = {
                    'key' : null
                    }, 
                released_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = None, 
                djstripe_owner_account = '', 
                customer = 56, 
                released_subscription = 56
            )
        else :
            return StripeSubscriptionSchedule(
                djstripe_id = 56,
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                end_behavior = None,
                status = None,
                customer = 56,
        )

    def testStripeSubscriptionSchedule(self):
        """Test StripeSubscriptionSchedule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
