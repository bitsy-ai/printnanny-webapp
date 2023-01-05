# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.119.4
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.pi_software_update_command_request import PiSoftwareUpdateCommandRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPiSoftwareUpdateCommandRequest(unittest.TestCase):
    """PiSoftwareUpdateCommandRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PiSoftwareUpdateCommandRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.pi_software_update_command_request.PiSoftwareUpdateCommandRequest()  # noqa: E501
        if include_optional :
            return PiSoftwareUpdateCommandRequest(
                id = '', 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                payload = printnanny_api_client.models.pi_software_update_payload_request.PiSoftwareUpdatePayloadRequest(
                    wic_tarball_url = '0', 
                    wic_bmap_url = '0', 
                    manifest_url = '0', 
                    swu_url = '0', 
                    version_id = '0', 
                    version = '0', 
                    version_codename = '0', ), 
                subject_pattern = 'pi.{pi_id}.command.swupdate', 
                version = '0', 
                event_type = 'Swupdate', 
                pi = 56
            )
        else :
            return PiSoftwareUpdateCommandRequest(
                payload = printnanny_api_client.models.pi_software_update_payload_request.PiSoftwareUpdatePayloadRequest(
                    wic_tarball_url = '0', 
                    wic_bmap_url = '0', 
                    manifest_url = '0', 
                    swu_url = '0', 
                    version_id = '0', 
                    version = '0', 
                    version_codename = '0', ),
                subject_pattern = 'pi.{pi_id}.command.swupdate',
                version = '0',
                event_type = 'Swupdate',
                pi = 56,
        )

    def testPiSoftwareUpdateCommandRequest(self):
        """Test PiSoftwareUpdateCommandRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
