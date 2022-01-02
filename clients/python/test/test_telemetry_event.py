# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.telemetry_event import TelemetryEvent  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestTelemetryEvent(unittest.TestCase):
    """TelemetryEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TelemetryEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.telemetry_event.TelemetryEvent()  # noqa: E501
        if include_optional :
            return TelemetryEvent(
                id = 56, 
                ts = 1.337, 
                event_source = None, 
                event_type = None, 
                octoprint_environment = printnanny_api_client.models.octoprint_environment.OctoprintEnvironment(
                    os = printnanny_api_client.models.octoprint_platform.OctoprintPlatform(
                        id = '', 
                        platform = '', 
                        bits = '', ), 
                    python = printnanny_api_client.models.octoprint_python.OctoprintPython(
                        version = '', 
                        pip = '', 
                        virtualenv = '', ), 
                    hardware = printnanny_api_client.models.octoprint_hardware.OctoprintHardware(
                        cores = 56, 
                        freq = 1.337, 
                        ram = 56, ), 
                    pi_support = printnanny_api_client.models.octoprint_pi_support.OctoprintPiSupport(
                        model = '', 
                        throttle_state = '', 
                        octopi_version = '', ), ), 
                octoprint_printer_data = printnanny_api_client.models.octoprint_printer_data.OctoprintPrinterData(
                    job = printnanny_api_client.models.octoprint_job.OctoprintJob(
                        file = null, 
                        estimated_print_time = 1.337, 
                        average_print_time = 1.337, 
                        last_print_time = 1.337, 
                        filament = {
                            'key' : null
                            }, ), 
                    state = printnanny_api_client.models.octoprint_printer_state.OctoprintPrinterState(
                        text = '', 
                        flags = printnanny_api_client.models.octoprint_printer_flags.OctoprintPrinterFlags(
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
                    progress = printnanny_api_client.models.octoprint_progress.OctoprintProgress(
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
                event_data = {
                    'key' : null
                    }, 
                temperature = {
                    'key' : null
                    }, 
                print_nanny_plugin_version = '', 
                print_nanny_client_version = '', 
                print_nanny_beta_client_version = '', 
                octoprint_version = '', 
                polymorphic_ctype = 56, 
                octoprint_device = 56, 
                user = 56, 
                print_session = 56
            )
        else :
            return TelemetryEvent(
                id = 56,
                octoprint_environment = printnanny_api_client.models.octoprint_environment.OctoprintEnvironment(
                    os = printnanny_api_client.models.octoprint_platform.OctoprintPlatform(
                        id = '', 
                        platform = '', 
                        bits = '', ), 
                    python = printnanny_api_client.models.octoprint_python.OctoprintPython(
                        version = '', 
                        pip = '', 
                        virtualenv = '', ), 
                    hardware = printnanny_api_client.models.octoprint_hardware.OctoprintHardware(
                        cores = 56, 
                        freq = 1.337, 
                        ram = 56, ), 
                    pi_support = printnanny_api_client.models.octoprint_pi_support.OctoprintPiSupport(
                        model = '', 
                        throttle_state = '', 
                        octopi_version = '', ), ),
                octoprint_printer_data = printnanny_api_client.models.octoprint_printer_data.OctoprintPrinterData(
                    job = printnanny_api_client.models.octoprint_job.OctoprintJob(
                        file = null, 
                        estimated_print_time = 1.337, 
                        average_print_time = 1.337, 
                        last_print_time = 1.337, 
                        filament = {
                            'key' : null
                            }, ), 
                    state = printnanny_api_client.models.octoprint_printer_state.OctoprintPrinterState(
                        text = '', 
                        flags = printnanny_api_client.models.octoprint_printer_flags.OctoprintPrinterFlags(
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
                    progress = printnanny_api_client.models.octoprint_progress.OctoprintProgress(
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
                print_nanny_plugin_version = '',
                print_nanny_client_version = '',
                octoprint_version = '',
                polymorphic_ctype = 56,
                octoprint_device = 56,
                user = 56,
        )

    def testTelemetryEvent(self):
        """Test TelemetryEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
