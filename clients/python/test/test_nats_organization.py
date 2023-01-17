# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.3
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.nats_organization import NatsOrganization  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestNatsOrganization(unittest.TestCase):
    """NatsOrganization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NatsOrganization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.nats_organization.NatsOrganization()  # noqa: E501
        if include_optional :
            return NatsOrganization(
                id = 56, 
                name = '', 
                is_active = True, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                slug = 'z', 
                json = {
                    'key' : null
                    }, 
                jetstream_enabled = True, 
                jetstream_max_mem = '', 
                jetstream_max_file = '', 
                jetstream_max_streams = 0, 
                jetstream_max_consumers = 0, 
                imports = [
                    56
                    ], 
                exports = [
                    56
                    ], 
                users = [
                    56
                    ]
            )
        else :
            return NatsOrganization(
                id = 56,
                name = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                slug = 'z',
                imports = [
                    56
                    ],
                exports = [
                    56
                    ],
                users = [
                    56
                    ],
        )

    def testNatsOrganization(self):
        """Test NatsOrganization"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
