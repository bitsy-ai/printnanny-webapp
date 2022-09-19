# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.108.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.nats_organization_request import NatsOrganizationRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestNatsOrganizationRequest(unittest.TestCase):
    """NatsOrganizationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NatsOrganizationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.nats_organization_request.NatsOrganizationRequest()  # noqa: E501
        if include_optional :
            return NatsOrganizationRequest(
                name = '0', 
                is_active = True, 
                slug = 'z0', 
                json = {
                    'key' : null
                    }, 
                imports = [
                    56
                    ], 
                exports = [
                    56
                    ]
            )
        else :
            return NatsOrganizationRequest(
                name = '0',
                slug = 'z0',
                imports = [
                    56
                    ],
                exports = [
                    56
                    ],
        )

    def testNatsOrganizationRequest(self):
        """Test NatsOrganizationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
