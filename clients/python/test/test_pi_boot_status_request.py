# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.120.2
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.pi_boot_status_request import PiBootStatusRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPiBootStatusRequest(unittest.TestCase):
    """PiBootStatusRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PiBootStatusRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.pi_boot_status_request.PiBootStatusRequest()  # noqa: E501
        if include_optional :
            return PiBootStatusRequest(
                id = '', 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                subject_pattern = 'pi.{pi_id}.status.boot', 
                payload = {
                    'key' : null
                    }, 
                event_type = 'SystemctlShow', 
                pi = 56
            )
        else :
            return PiBootStatusRequest(
                subject_pattern = 'pi.{pi_id}.status.boot',
                event_type = 'SystemctlShow',
                pi = 56,
        )

    def testPiBootStatusRequest(self):
        """Test PiBootStatusRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
