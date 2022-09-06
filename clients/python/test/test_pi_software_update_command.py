# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.107.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.pi_software_update_command import PiSoftwareUpdateCommand  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPiSoftwareUpdateCommand(unittest.TestCase):
    """PiSoftwareUpdateCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PiSoftwareUpdateCommand
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.pi_software_update_command.PiSoftwareUpdateCommand()  # noqa: E501
        if include_optional :
            return PiSoftwareUpdateCommand(
                id = '', 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                payload = printnanny_api_client.models.pi_software_update_payload.PiSoftwareUpdatePayload(
                    wic_tarball_url = '', 
                    wic_bmap_url = '', 
                    manifest_url = '', 
                    swu_url = '', 
                    version_id = '', 
                    version = '', 
                    version_codename = '', ), 
                subject_pattern = 'pi.{pi_id}.command.swupdate', 
                version = '', 
                event_type = 'Swupdate', 
                pi = 56
            )
        else :
            return PiSoftwareUpdateCommand(
                payload = printnanny_api_client.models.pi_software_update_payload.PiSoftwareUpdatePayload(
                    wic_tarball_url = '', 
                    wic_bmap_url = '', 
                    manifest_url = '', 
                    swu_url = '', 
                    version_id = '', 
                    version = '', 
                    version_codename = '', ),
                subject_pattern = 'pi.{pi_id}.command.swupdate',
                version = '',
                event_type = 'Swupdate',
                pi = 56,
        )

    def testPiSoftwareUpdateCommand(self):
        """Test PiSoftwareUpdateCommand"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
