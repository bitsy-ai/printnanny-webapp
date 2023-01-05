# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.119.4
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.octo_print_server_status import OctoPrintServerStatus  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestOctoPrintServerStatus(unittest.TestCase):
    """OctoPrintServerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoPrintServerStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.octo_print_server_status.OctoPrintServerStatus()  # noqa: E501
        if include_optional :
            return OctoPrintServerStatus(
                id = '', 
                subject_pattern = 'pi.{pi_id}.octoprint.server', 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                payload = {
                    'key' : null
                    }, 
                event_type = 'Test', 
                octoprint_server = 56, 
                pi = 56
            )
        else :
            return OctoPrintServerStatus(
                id = '',
                subject_pattern = 'pi.{pi_id}.octoprint.server',
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                event_type = 'Test',
                octoprint_server = 56,
                pi = 56,
        )

    def testOctoPrintServerStatus(self):
        """Test OctoPrintServerStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
