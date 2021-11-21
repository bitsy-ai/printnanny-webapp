# coding: utf-8

"""
    print-nanny-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import print_nanny_client
from print_nanny_client.models.octoprint_job_request import OctoprintJobRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestOctoprintJobRequest(unittest.TestCase):
    """OctoprintJobRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoprintJobRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.octoprint_job_request.OctoprintJobRequest()  # noqa: E501
        if include_optional :
            return OctoprintJobRequest(
                file = None, 
                estimated_print_time = 1.337, 
                average_print_time = 1.337, 
                last_print_time = 1.337, 
                filament = {
                    'key' : null
                    }
            )
        else :
            return OctoprintJobRequest(
                filament = {
                    'key' : null
                    },
        )

    def testOctoprintJobRequest(self):
        """Test OctoprintJobRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
