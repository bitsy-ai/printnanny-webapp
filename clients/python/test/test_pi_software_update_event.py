# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.pi_software_update_event import PiSoftwareUpdateEvent  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPiSoftwareUpdateEvent(unittest.TestCase):
    """PiSoftwareUpdateEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PiSoftwareUpdateEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.pi_software_update_event.PiSoftwareUpdateEvent()  # noqa: E501
        if include_optional :
            return PiSoftwareUpdateEvent(
                id = 56, 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                source = 'octoprint', 
                subject = '', 
                payload = {
                    'key' : null
                    }, 
                version = '', 
                event_type = 'Started', 
                polymorphic_ctype = 56, 
                pi = 56
            )
        else :
            return PiSoftwareUpdateEvent(
                id = 56,
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                source = 'octoprint',
                subject = '',
                version = '',
                event_type = 'Started',
                polymorphic_ctype = 56,
                pi = 56,
        )

    def testPiSoftwareUpdateEvent(self):
        """Test PiSoftwareUpdateEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
