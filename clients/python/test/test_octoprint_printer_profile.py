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
from print_nanny_client.models.octoprint_printer_profile import OctoprintPrinterProfile  # noqa: E501
from print_nanny_client.rest import ApiException

class TestOctoprintPrinterProfile(unittest.TestCase):
    """OctoprintPrinterProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoprintPrinterProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.octoprint_printer_profile.OctoprintPrinterProfile()  # noqa: E501
        if include_optional :
            return OctoprintPrinterProfile(
                id = 56, 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '', 
                axes_e_inverted = True, 
                axes_e_speed = -2147483648, 
                axes_x_speed = -2147483648, 
                axes_x_inverted = True, 
                axes_y_inverted = True, 
                axes_y_speed = -2147483648, 
                axes_z_inverted = True, 
                axes_z_speed = -2147483648, 
                extruder_count = -2147483648, 
                extruder_nozzle_diameter = 1.337, 
                extruder_shared_nozzle = True, 
                heated_bed = True, 
                heated_chamber = True, 
                model = '', 
                volume_custom_box = {
                    'key' : null
                    }, 
                volume_depth = 1.337, 
                volume_formfactor = '', 
                volume_height = 1.337, 
                volume_origin = '', 
                volume_width = 1.337, 
                polymorphic_ctype = 56, 
                user = 56, 
                controller = 56, 
                device = 56, 
                octoprint_controller = 56
            )
        else :
            return OctoprintPrinterProfile(
                id = 56,
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                polymorphic_ctype = 56,
                user = 56,
                controller = 56,
                device = 56,
                octoprint_controller = 56,
        )

    def testOctoprintPrinterProfile(self):
        """Test OctoprintPrinterProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
