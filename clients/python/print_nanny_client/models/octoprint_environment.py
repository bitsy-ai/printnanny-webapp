# coding: utf-8

"""
    print-nanny-client

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

from print_nanny_client.configuration import Configuration


class OctoprintEnvironment(object):
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
        'os': 'OctoprintPlatform',
        'python': 'OctoprintPython',
        'hardware': 'OctoprintHardware',
        'pi_support': 'OctoprintPiSupport'
    }

    attribute_map = {
        'os': 'os',
        'python': 'python',
        'hardware': 'hardware',
        'pi_support': 'pi_support'
    }

    def __init__(self, os=None, python=None, hardware=None, pi_support=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintEnvironment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._os = None
        self._python = None
        self._hardware = None
        self._pi_support = None
        self.discriminator = None

        self.os = os
        self.python = python
        self.hardware = hardware
        self.pi_support = pi_support

    @property
    def os(self):
        """Gets the os of this OctoprintEnvironment.  # noqa: E501


        :return: The os of this OctoprintEnvironment.  # noqa: E501
        :rtype: OctoprintPlatform
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this OctoprintEnvironment.


        :param os: The os of this OctoprintEnvironment.  # noqa: E501
        :type os: OctoprintPlatform
        """
        if self.local_vars_configuration.client_side_validation and os is None:  # noqa: E501
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def python(self):
        """Gets the python of this OctoprintEnvironment.  # noqa: E501


        :return: The python of this OctoprintEnvironment.  # noqa: E501
        :rtype: OctoprintPython
        """
        return self._python

    @python.setter
    def python(self, python):
        """Sets the python of this OctoprintEnvironment.


        :param python: The python of this OctoprintEnvironment.  # noqa: E501
        :type python: OctoprintPython
        """
        if self.local_vars_configuration.client_side_validation and python is None:  # noqa: E501
            raise ValueError("Invalid value for `python`, must not be `None`")  # noqa: E501

        self._python = python

    @property
    def hardware(self):
        """Gets the hardware of this OctoprintEnvironment.  # noqa: E501


        :return: The hardware of this OctoprintEnvironment.  # noqa: E501
        :rtype: OctoprintHardware
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this OctoprintEnvironment.


        :param hardware: The hardware of this OctoprintEnvironment.  # noqa: E501
        :type hardware: OctoprintHardware
        """
        if self.local_vars_configuration.client_side_validation and hardware is None:  # noqa: E501
            raise ValueError("Invalid value for `hardware`, must not be `None`")  # noqa: E501

        self._hardware = hardware

    @property
    def pi_support(self):
        """Gets the pi_support of this OctoprintEnvironment.  # noqa: E501


        :return: The pi_support of this OctoprintEnvironment.  # noqa: E501
        :rtype: OctoprintPiSupport
        """
        return self._pi_support

    @pi_support.setter
    def pi_support(self, pi_support):
        """Sets the pi_support of this OctoprintEnvironment.


        :param pi_support: The pi_support of this OctoprintEnvironment.  # noqa: E501
        :type pi_support: OctoprintPiSupport
        """
        if self.local_vars_configuration.client_side_validation and pi_support is None:  # noqa: E501
            raise ValueError("Invalid value for `pi_support`, must not be `None`")  # noqa: E501

        self._pi_support = pi_support

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
        if not isinstance(other, OctoprintEnvironment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintEnvironment):
            return True

        return self.to_dict() != other.to_dict()
