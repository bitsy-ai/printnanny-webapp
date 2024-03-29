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
from printnanny_api_client.models.workspace_owner import WorkspaceOwner  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestWorkspaceOwner(unittest.TestCase):
    """WorkspaceOwner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkspaceOwner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.workspace_owner.WorkspaceOwner()  # noqa: E501
        if include_optional :
            return WorkspaceOwner(
                id = 56, 
                organization_user = printnanny_api_client.models.workspace_user.WorkspaceUser(
                    id = 56, 
                    user = printnanny_api_client.models.user.User(
                        email = '', 
                        id = 56, 
                        first_name = '', 
                        last_name = '', 
                        is_beta_tester = True, ), 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_admin = True, 
                    organization = 56, ), 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                organization = 56
            )
        else :
            return WorkspaceOwner(
                id = 56,
                organization_user = printnanny_api_client.models.workspace_user.WorkspaceUser(
                    id = 56, 
                    user = printnanny_api_client.models.user.User(
                        email = '', 
                        id = 56, 
                        first_name = '', 
                        last_name = '', 
                        is_beta_tester = True, ), 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_admin = True, 
                    organization = 56, ),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization = 56,
        )

    def testWorkspaceOwner(self):
        """Test WorkspaceOwner"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
