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
from print_nanny_client.models.appliance_pki import AppliancePKI  # noqa: E501
from print_nanny_client.rest import ApiException

class TestAppliancePKI(unittest.TestCase):
    """AppliancePKI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AppliancePKI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.appliance_pki.AppliancePKI()  # noqa: E501
        if include_optional :
            return AppliancePKI(
                id = 56, 
                deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                public_key_path = '', 
                private_key_path = '', 
                public_key = '', 
                public_key_checksum = '', 
                fingerprint = '', 
                appliance = 56
            )
        else :
            return AppliancePKI(
                id = 56,
                deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                public_key_path = '',
                private_key_path = '',
                public_key = '',
                public_key_checksum = '',
                fingerprint = '',
                appliance = 56,
        )

    def testAppliancePKI(self):
        """Test AppliancePKI"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
