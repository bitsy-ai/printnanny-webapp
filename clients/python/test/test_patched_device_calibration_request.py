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
from printnanny_api_client.models.patched_device_calibration_request import PatchedDeviceCalibrationRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPatchedDeviceCalibrationRequest(unittest.TestCase):
    """PatchedDeviceCalibrationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedDeviceCalibrationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.patched_device_calibration_request.PatchedDeviceCalibrationRequest()  # noqa: E501
        if include_optional :
            return PatchedDeviceCalibrationRequest(
                octoprint_device = 56, 
                fps = 1.337, 
                xy = {
                    'key' : null
                    }, 
                height = -2147483648, 
                width = -2147483648
            )
        else :
            return PatchedDeviceCalibrationRequest(
        )

    def testPatchedDeviceCalibrationRequest(self):
        """Test PatchedDeviceCalibrationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
