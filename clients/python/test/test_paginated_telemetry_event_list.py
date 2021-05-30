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
from print_nanny_client.models.paginated_telemetry_event_list import PaginatedTelemetryEventList  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPaginatedTelemetryEventList(unittest.TestCase):
    """PaginatedTelemetryEventList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedTelemetryEventList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.paginated_telemetry_event_list.PaginatedTelemetryEventList()  # noqa: E501
        if include_optional :
            return PaginatedTelemetryEventList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    print_nanny_client.models.telemetry_event.TelemetryEvent(
                        id = 56, 
                        print_session = '', 
                        event_type = 'plugin_octoprint_nanny_monitoring_start', 
                        environment = print_nanny_client.models.octoprint_environment.OctoprintEnvironment(
                            os = print_nanny_client.models.octoprint_platform.OctoprintPlatform(
                                id = '', 
                                platform = '', 
                                bits = '', ), 
                            python = print_nanny_client.models.octoprint_python.OctoprintPython(
                                version = '', 
                                pip = '', 
                                virtualenv = '', ), 
                            hardware = print_nanny_client.models.octoprint_hardware.OctoprintHardware(
                                cores = 56, 
                                freq = 1.337, 
                                ram = 56, ), 
                            pi_support = print_nanny_client.models.octoprint_pi_support.OctoprintPiSupport(
                                model = '', 
                                throttle_state = '', 
                                octopi_version = '', ), ), 
                        printer_data = print_nanny_client.models.octoprint_printer_data.OctoprintPrinterData(
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
                            offsets = {
                                'key' : null
                                }, ), 
                        temperature = {
                            'key' : null
                            }, 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        event_source = 'octoprint', 
                        event_data = {
                            'key' : null
                            }, 
                        plugin_version = '', 
                        client_version = '', 
                        octoprint_version = '', 
                        metadata = {
                            'key' : null
                            }, 
                        octoprint_job = {
                            'key' : null
                            }, 
                        polymorphic_ctype = 56, 
                        octoprint_device = 56, 
                        user = 56, )
                    ]
            )
        else :
            return PaginatedTelemetryEventList(
        )

    def testPaginatedTelemetryEventList(self):
        """Test PaginatedTelemetryEventList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
