# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class TaskRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'task_type': 'TaskType',
        'active': 'bool',
        'device': 'int'
    }

    attribute_map = {
        'task_type': 'task_type',
        'active': 'active',
        'device': 'device'
    }

    def __init__(self, task_type=None, active=True, device=None, local_vars_configuration=None):  # noqa: E501
        """TaskRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._task_type = None
        self._active = None
        self._device = None
        self.discriminator = None

        self.task_type = task_type
        if active is not None:
            self.active = active
        self.device = device

    @property
    def task_type(self):
        """Gets the task_type of this TaskRequest.  # noqa: E501


        :return: The task_type of this TaskRequest.  # noqa: E501
        :rtype: TaskType
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskRequest.


        :param task_type: The task_type of this TaskRequest.  # noqa: E501
        :type task_type: TaskType
        """
        if self.local_vars_configuration.client_side_validation and task_type is None:  # noqa: E501
            raise ValueError("Invalid value for `task_type`, must not be `None`")  # noqa: E501

        self._task_type = task_type

    @property
    def active(self):
        """Gets the active of this TaskRequest.  # noqa: E501


        :return: The active of this TaskRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this TaskRequest.


        :param active: The active of this TaskRequest.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def device(self):
        """Gets the device of this TaskRequest.  # noqa: E501


        :return: The device of this TaskRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this TaskRequest.


        :param device: The device of this TaskRequest.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskRequest):
            return True

        return self.to_dict() != other.to_dict()
