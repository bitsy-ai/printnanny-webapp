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
from print_nanny_client.models.partner3_d_geeks_metadata import Partner3DGeeksMetadata  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPartner3DGeeksMetadata(unittest.TestCase):
    """Partner3DGeeksMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Partner3DGeeksMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.partner3_d_geeks_metadata.Partner3DGeeksMetadata()  # noqa: E501
        if include_optional :
            return Partner3DGeeksMetadata(
                name = '', 
                model = '', 
                platform = '', 
                octoprint_version = '', 
                print_nanny_plugin_version = '', 
                print_nanny_client_version = '', 
                verified = ''
            )
        else :
            return Partner3DGeeksMetadata(
                name = '',
                model = '',
                platform = '',
                octoprint_version = '',
                print_nanny_plugin_version = '',
                print_nanny_client_version = '',
                verified = '',
        )

    def testPartner3DGeeksMetadata(self):
        """Test Partner3DGeeksMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
