# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.102.3
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.stripe_plan import StripePlan  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestStripePlan(unittest.TestCase):
    """StripePlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StripePlan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.stripe_plan.StripePlan()  # noqa: E501
        if include_optional :
            return StripePlan(
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
                interval = None, 
                interval_count = 0, 
                nickname = '', 
                tiers = {
                    'key' : null
                    }, 
                transform_usage = {
                    'key' : null
                    }, 
                trial_period_days = -2147483648, 
                usage_type = None, 
                djstripe_owner_account = '', 
                product = ''
            )
        else :
            return StripePlan(
                djstripe_id = 56,
                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                active = True,
                currency = '',
                interval = None,
        )

    def testStripePlan(self):
        """Test StripePlan"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
