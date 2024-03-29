# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_video_recording_part_list import PaginatedVideoRecordingPartList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedVideoRecordingPartList(unittest.TestCase):
    """PaginatedVideoRecordingPartList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedVideoRecordingPartList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_video_recording_part_list.PaginatedVideoRecordingPartList()  # noqa: E501
        if include_optional :
            return PaginatedVideoRecordingPartList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.video_recording_part.VideoRecordingPart(
                        id = '', 
                        deleted_by_cascade = True, 
                        size = -9223372036854775808, 
                        buffer_index = -9223372036854775808, 
                        buffer_runningtime = -9223372036854775808, 
                        file_name = '', 
                        mp4_file = '', 
                        sync_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sync_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        video_recording = '', 
                        user = 56, )
                    ]
            )
        else :
            return PaginatedVideoRecordingPartList(
        )

    def testPaginatedVideoRecordingPartList(self):
        """Test PaginatedVideoRecordingPartList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
