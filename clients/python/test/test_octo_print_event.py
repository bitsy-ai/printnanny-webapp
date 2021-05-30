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
from print_nanny_client.models.octo_print_event import OctoPrintEvent  # noqa: E501
from print_nanny_client.rest import ApiException

class TestOctoPrintEvent(unittest.TestCase):
    """OctoPrintEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoPrintEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.octo_print_event.OctoPrintEvent()  # noqa: E501
        if include_optional :
            return OctoPrintEvent(
                id = 56, 
                print_session = '', 
                ts = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                event_source = 'octoprint', 
                event_data = {
                    'key' : null
                    }, 
                print_nanny_plugin_version = '', 
                print_nanny_client_version = '', 
                octoprint_version = '', 
                octoprint_job = {
                    'key' : null
                    }, 
                event_type = 'ClientAuthed', 
                polymorphic_ctype = 56, 
                octoprint_device = 56, 
                user = 56
            )
        else :
            return OctoPrintEvent(
                print_nanny_plugin_version = '',
                print_nanny_client_version = '',
                octoprint_version = '',
                event_type = 'ClientAuthed',
                octoprint_device = 56,
        )

    def testOctoPrintEvent(self):
        """Test OctoPrintEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
