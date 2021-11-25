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


class SystemTaskRequest(object):
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
        'status': 'SystemTaskStatus',
        'type': 'SystemTaskType',
        'ansible_facts': 'dict(str, object)',
        'ansible_extra_vars': 'dict(str, object)',
        'device': 'int'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'ansible_facts': 'ansible_facts',
        'ansible_extra_vars': 'ansible_extra_vars',
        'device': 'device'
    }

    def __init__(self, status=None, type=None, ansible_facts=None, ansible_extra_vars=None, device=None, local_vars_configuration=None):  # noqa: E501
        """SystemTaskRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._type = None
        self._ansible_facts = None
        self._ansible_extra_vars = None
        self._device = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if ansible_facts is not None:
            self.ansible_facts = ansible_facts
        if ansible_extra_vars is not None:
            self.ansible_extra_vars = ansible_extra_vars
        self.device = device

    @property
    def status(self):
        """Gets the status of this SystemTaskRequest.  # noqa: E501


        :return: The status of this SystemTaskRequest.  # noqa: E501
        :rtype: SystemTaskStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SystemTaskRequest.


        :param status: The status of this SystemTaskRequest.  # noqa: E501
        :type status: SystemTaskStatus
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this SystemTaskRequest.  # noqa: E501


        :return: The type of this SystemTaskRequest.  # noqa: E501
        :rtype: SystemTaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemTaskRequest.


        :param type: The type of this SystemTaskRequest.  # noqa: E501
        :type type: SystemTaskType
        """

        self._type = type

    @property
    def ansible_facts(self):
        """Gets the ansible_facts of this SystemTaskRequest.  # noqa: E501


        :return: The ansible_facts of this SystemTaskRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._ansible_facts

    @ansible_facts.setter
    def ansible_facts(self, ansible_facts):
        """Sets the ansible_facts of this SystemTaskRequest.


        :param ansible_facts: The ansible_facts of this SystemTaskRequest.  # noqa: E501
        :type ansible_facts: dict(str, object)
        """

        self._ansible_facts = ansible_facts

    @property
    def ansible_extra_vars(self):
        """Gets the ansible_extra_vars of this SystemTaskRequest.  # noqa: E501


        :return: The ansible_extra_vars of this SystemTaskRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._ansible_extra_vars

    @ansible_extra_vars.setter
    def ansible_extra_vars(self, ansible_extra_vars):
        """Sets the ansible_extra_vars of this SystemTaskRequest.


        :param ansible_extra_vars: The ansible_extra_vars of this SystemTaskRequest.  # noqa: E501
        :type ansible_extra_vars: dict(str, object)
        """

        self._ansible_extra_vars = ansible_extra_vars

    @property
    def device(self):
        """Gets the device of this SystemTaskRequest.  # noqa: E501


        :return: The device of this SystemTaskRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this SystemTaskRequest.


        :param device: The device of this SystemTaskRequest.  # noqa: E501
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
        if not isinstance(other, SystemTaskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemTaskRequest):
            return True

        return self.to_dict() != other.to_dict()
