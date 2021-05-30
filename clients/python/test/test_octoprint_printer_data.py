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
from print_nanny_client.models.octoprint_printer_data import OctoprintPrinterData  # noqa: E501
from print_nanny_client.rest import ApiException

class TestOctoprintPrinterData(unittest.TestCase):
    """OctoprintPrinterData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoprintPrinterData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.octoprint_printer_data.OctoprintPrinterData()  # noqa: E501
        if include_optional :
            return OctoprintPrinterData(
                job = print_nanny_client.models.octoprint_job.OctoprintJob(
                    file = print_nanny_client.models.octoprint_file.OctoprintFile(
                        name = '', 
                        path = '', 
                        display = '', 
                        origin = '', 
                        size = 56, 
                        date = 56, ), 
                    estimated_print_time = 1.337, 
                    average_print_time = 1.337, 
                    last_print_time = 1.337, 
                    filament = {
                        'key' : null
                        }, ), 
                state = print_nanny_client.models.octoprint_printer_state.OctoprintPrinterState(
                    text = '', 
                    flags = print_nanny_client.models.octoprint_printer_flags.OctoprintPrinterFlags(
                        operational = True, 
                        printing = True, 
                        cancelling = True, 
                        pausing = True, 
                        resuming = True, 
                        finishing = True, 
                        closed_or_error = True, 
                        error = True, 
                        paused = True, 
                        ready = True, 
                        sd_ready = True, ), ), 
                user = '', 
                current_z = 1.337, 
                progress = print_nanny_client.models.octoprint_progress.OctoprintProgress(
                    completion = 1.337, 
                    filepos = 56, 
                    print_time = 56, 
                    print_time_left = 56, 
                    print_time_origin = '', ), 
                resends = {
                    'key' : null
                    }
            )
        else :
            return OctoprintPrinterData(
                job = print_nanny_client.models.octoprint_job.OctoprintJob(
                    file = print_nanny_client.models.octoprint_file.OctoprintFile(
                        name = '', 
                        path = '', 
                        display = '', 
                        origin = '', 
                        size = 56, 
                        date = 56, ), 
                    estimated_print_time = 1.337, 
                    average_print_time = 1.337, 
                    last_print_time = 1.337, 
                    filament = {
                        'key' : null
                        }, ),
                state = print_nanny_client.models.octoprint_printer_state.OctoprintPrinterState(
                    text = '', 
                    flags = print_nanny_client.models.octoprint_printer_flags.OctoprintPrinterFlags(
                        operational = True, 
                        printing = True, 
                        cancelling = True, 
                        pausing = True, 
                        resuming = True, 
                        finishing = True, 
                        closed_or_error = True, 
                        error = True, 
                        paused = True, 
                        ready = True, 
                        sd_ready = True, ), ),
                user = '',
                current_z = 1.337,
                progress = print_nanny_client.models.octoprint_progress.OctoprintProgress(
                    completion = 1.337, 
                    filepos = 56, 
                    print_time = 56, 
                    print_time_left = 56, 
                    print_time_origin = '', ),
                resends = {
                    'key' : null
                    },
        )

    def testOctoprintPrinterData(self):
        """Test OctoprintPrinterData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
