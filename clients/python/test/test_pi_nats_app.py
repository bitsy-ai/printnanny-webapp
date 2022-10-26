# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.109.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.pi_nats_app import PiNatsApp  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPiNatsApp(unittest.TestCase):
    """PiNatsApp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PiNatsApp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.pi_nats_app.PiNatsApp()  # noqa: E501
        if include_optional :
            return PiNatsApp(
                id = 56, 
                app_name = '', 
                json = {
                    'key' : null
                    }, 
                pi = 56, 
                organization = printnanny_api_client.models.nats_organization.NatsOrganization(
                    id = 56, 
                    name = '', 
                    is_active = True, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    slug = 'z', 
                    json = {
                        'key' : null
                        }, 
                    imports = [
                        56
                        ], 
                    exports = [
                        56
                        ], 
                    users = [
                        56
                        ], ), 
                organization_user = 56, 
                nats_server_uri = '', 
                nats_ws_uri = '', 
                nats_subject_pattern = '', 
                nats_subject_pattern_template = ''
            )
        else :
            return PiNatsApp(
                id = 56,
                pi = 56,
                organization = printnanny_api_client.models.nats_organization.NatsOrganization(
                    id = 56, 
                    name = '', 
                    is_active = True, 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    slug = 'z', 
                    json = {
                        'key' : null
                        }, 
                    imports = [
                        56
                        ], 
                    exports = [
                        56
                        ], 
                    users = [
                        56
                        ], ),
                organization_user = 56,
                nats_server_uri = '',
                nats_ws_uri = '',
                nats_subject_pattern = '',
                nats_subject_pattern_template = '',
        )

    def testPiNatsApp(self):
        """Test PiNatsApp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
