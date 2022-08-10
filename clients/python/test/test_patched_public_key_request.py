# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.2
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.patched_public_key_request import PatchedPublicKeyRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPatchedPublicKeyRequest(unittest.TestCase):
    """PatchedPublicKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedPublicKeyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.patched_public_key_request.PatchedPublicKeyRequest()  # noqa: E501
        if include_optional :
            return PatchedPublicKeyRequest(
                pem = '0', 
                cipher = '0', 
                length = -2147483648, 
                fingerprint = '0', 
                pi = 56
            )
        else :
            return PatchedPublicKeyRequest(
        )

    def testPatchedPublicKeyRequest(self):
        """Test PatchedPublicKeyRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
