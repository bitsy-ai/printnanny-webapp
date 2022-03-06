# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@printnanny.ai
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


class OctoprintHardwareRequest(object):
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
        'cores': 'int',
        'freq': 'float',
        'ram': 'int'
    }

    attribute_map = {
        'cores': 'cores',
        'freq': 'freq',
        'ram': 'ram'
    }

    def __init__(self, cores=None, freq=None, ram=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintHardwareRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cores = None
        self._freq = None
        self._ram = None
        self.discriminator = None

        self.cores = cores
        self.freq = freq
        self.ram = ram

    @property
    def cores(self):
        """Gets the cores of this OctoprintHardwareRequest.  # noqa: E501


        :return: The cores of this OctoprintHardwareRequest.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this OctoprintHardwareRequest.


        :param cores: The cores of this OctoprintHardwareRequest.  # noqa: E501
        :type cores: int
        """
        if self.local_vars_configuration.client_side_validation and cores is None:  # noqa: E501
            raise ValueError("Invalid value for `cores`, must not be `None`")  # noqa: E501

        self._cores = cores

    @property
    def freq(self):
        """Gets the freq of this OctoprintHardwareRequest.  # noqa: E501


        :return: The freq of this OctoprintHardwareRequest.  # noqa: E501
        :rtype: float
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this OctoprintHardwareRequest.


        :param freq: The freq of this OctoprintHardwareRequest.  # noqa: E501
        :type freq: float
        """
        if self.local_vars_configuration.client_side_validation and freq is None:  # noqa: E501
            raise ValueError("Invalid value for `freq`, must not be `None`")  # noqa: E501

        self._freq = freq

    @property
    def ram(self):
        """Gets the ram of this OctoprintHardwareRequest.  # noqa: E501


        :return: The ram of this OctoprintHardwareRequest.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this OctoprintHardwareRequest.


        :param ram: The ram of this OctoprintHardwareRequest.  # noqa: E501
        :type ram: int
        """
        if self.local_vars_configuration.client_side_validation and ram is None:  # noqa: E501
            raise ValueError("Invalid value for `ram`, must not be `None`")  # noqa: E501

        self._ram = ram

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
        if not isinstance(other, OctoprintHardwareRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintHardwareRequest):
            return True

        return self.to_dict() != other.to_dict()
