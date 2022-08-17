# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.102.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.patched_pi_request import PatchedPiRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPatchedPiRequest(unittest.TestCase):
    """PatchedPiRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedPiRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.patched_pi_request.PatchedPiRequest()  # noqa: E501
        if include_optional :
            return PatchedPiRequest(
                nats_app = printnanny_api_client.models.pi_nats_app_request.PiNatsAppRequest(
                    app_name = '0', 
                    json = {
                        'key' : null
                        }, 
                    pi = 56, 
                    organization = printnanny_api_client.models.nats_organization_request.NatsOrganizationRequest(
                        name = '0', 
                        is_active = True, 
                        slug = 'z0', 
                        imports = [
                            56
                            ], 
                        exports = [
                            56
                            ], ), 
                    organization_user = 56, ), 
                sbc = 'rpi_4', 
                edition = 'octoprint_lite', 
                hostname = '0', 
                fqdn = '0', 
                favorite = True, 
                setup_finished = True
            )
        else :
            return PatchedPiRequest(
        )

    def testPatchedPiRequest(self):
        """Test PatchedPiRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
