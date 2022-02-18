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


class JanusTaskRequest(object):
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
        'active': 'bool',
        'task_type': 'JanusTaskType',
        'stream': 'int'
    }

    attribute_map = {
        'active': 'active',
        'task_type': 'task_type',
        'stream': 'stream'
    }

    def __init__(self, active=None, task_type=None, stream=None, local_vars_configuration=None):  # noqa: E501
        """JanusTaskRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._task_type = None
        self._stream = None
        self.discriminator = None

        if active is not None:
            self.active = active
        self.task_type = task_type
        self.stream = stream

    @property
    def active(self):
        """Gets the active of this JanusTaskRequest.  # noqa: E501


        :return: The active of this JanusTaskRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this JanusTaskRequest.


        :param active: The active of this JanusTaskRequest.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def task_type(self):
        """Gets the task_type of this JanusTaskRequest.  # noqa: E501


        :return: The task_type of this JanusTaskRequest.  # noqa: E501
        :rtype: JanusTaskType
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this JanusTaskRequest.


        :param task_type: The task_type of this JanusTaskRequest.  # noqa: E501
        :type task_type: JanusTaskType
        """
        if self.local_vars_configuration.client_side_validation and task_type is None:  # noqa: E501
            raise ValueError("Invalid value for `task_type`, must not be `None`")  # noqa: E501

        self._task_type = task_type

    @property
    def stream(self):
        """Gets the stream of this JanusTaskRequest.  # noqa: E501


        :return: The stream of this JanusTaskRequest.  # noqa: E501
        :rtype: int
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this JanusTaskRequest.


        :param stream: The stream of this JanusTaskRequest.  # noqa: E501
        :type stream: int
        """
        if self.local_vars_configuration.client_side_validation and stream is None:  # noqa: E501
            raise ValueError("Invalid value for `stream`, must not be `None`")  # noqa: E501

        self._stream = stream

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
        if not isinstance(other, JanusTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JanusTaskRequest):
            return True

        return self.to_dict() != other.to_dict()
