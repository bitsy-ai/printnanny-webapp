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
from printnanny_api_client.models.pi import Pi  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPi(unittest.TestCase):
    """Pi unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Pi
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.pi.Pi()  # noqa: E501
        if include_optional :
            return Pi(
                id = 56, 
                last_boot = '', 
                settings = None, 
                user = None, 
                system_info = None, 
                webrtc_edge = None, 
                webrtc_cloud = None, 
                octoprint_server = None, 
                urls = printnanny_api_client.models.pi_urls.Pi_urls(
                    octoprint = '', 
                    swupdate = '', 
                    syncthing = '', ), 
                nats_app = None, 
                sbc = 'rpi_4', 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                hostname = '', 
                fqdn = '', 
                favorite = True, 
                setup_finished = True
            )
        else :
            return Pi(
                id = 56,
                last_boot = '',
                settings = None,
                user = None,
                system_info = None,
                webrtc_edge = None,
                webrtc_cloud = None,
                octoprint_server = None,
                urls = printnanny_api_client.models.pi_urls.Pi_urls(
                    octoprint = '', 
                    swupdate = '', 
                    syncthing = '', ),
                nats_app = None,
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testPi(self):
        """Test Pi"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
