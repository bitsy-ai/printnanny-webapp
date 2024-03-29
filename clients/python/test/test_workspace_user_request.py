# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.workspace_user_request import WorkspaceUserRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestWorkspaceUserRequest(unittest.TestCase):
    """WorkspaceUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkspaceUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.workspace_user_request.WorkspaceUserRequest()  # noqa: E501
        if include_optional :
            return WorkspaceUserRequest(
                user = printnanny_api_client.models.user_request.UserRequest(
                    email = '0', 
                    first_name = '', 
                    last_name = '', ), 
                is_admin = True, 
                organization = 56
            )
        else :
            return WorkspaceUserRequest(
                user = printnanny_api_client.models.user_request.UserRequest(
                    email = '0', 
                    first_name = '', 
                    last_name = '', ),
                organization = 56,
        )

    def testWorkspaceUserRequest(self):
        """Test WorkspaceUserRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
