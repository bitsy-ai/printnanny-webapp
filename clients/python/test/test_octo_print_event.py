# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.octo_print_event import OctoPrintEvent  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestOctoPrintEvent(unittest.TestCase):
    """OctoPrintEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoPrintEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.octo_print_event.OctoPrintEvent()  # noqa: E501
        if include_optional :
            return OctoPrintEvent(
                id = 56, 
                model = 'OctoPrintEvent', 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                source = 'octoprint', 
                event_name = 'Startup', 
                payload = {
                    'key' : null
                    }, 
                polymorphic_ctype = 56, 
                user = 56, 
                octoprint_install = 56, 
                device = 56
            )
        else :
            return OctoPrintEvent(
                id = 56,
                model = 'OctoPrintEvent',
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                source = 'octoprint',
                event_name = 'Startup',
                polymorphic_ctype = 56,
                user = 56,
                octoprint_install = 56,
                device = 56,
        )

    def testOctoPrintEvent(self):
        """Test OctoPrintEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
