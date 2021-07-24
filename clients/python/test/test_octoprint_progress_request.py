# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import print_nanny_client
from print_nanny_client.models.octoprint_progress_request import OctoprintProgressRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestOctoprintProgressRequest(unittest.TestCase):
    """OctoprintProgressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoprintProgressRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.octoprint_progress_request.OctoprintProgressRequest()  # noqa: E501
        if include_optional :
            return OctoprintProgressRequest(
                completion = 1.337, 
                filepos = 56, 
                print_time = 56, 
                print_time_left = 56, 
                print_time_origin = ''
            )
        else :
            return OctoprintProgressRequest(
                completion = 1.337,
                filepos = 56,
                print_time = 56,
                print_time_left = 56,
        )

    def testOctoprintProgressRequest(self):
        """Test OctoprintProgressRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
