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

import printnanny_api_client
from printnanny_api_client.api.tasks_api import TasksApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.tasks_api.TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_devices_tasks_create(self):
        """Test case for devices_tasks_create

        """
        pass

    def test_devices_tasks_list(self):
        """Test case for devices_tasks_list

        """
        pass

    def test_devices_tasks_status_create(self):
        """Test case for devices_tasks_status_create

        """
        pass

    def test_devices_tasks_status_list(self):
        """Test case for devices_tasks_status_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
