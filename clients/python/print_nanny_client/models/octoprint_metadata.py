# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
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


class OctoprintMetadata(object):
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
        'environment': 'OctoprintEnvironment',
        'printer_data': 'OctoprintPrinterData',
        'temperature': 'dict(str, object)'
    }

    attribute_map = {
        'environment': 'environment',
        'printer_data': 'printer_data',
        'temperature': 'temperature'
    }

    def __init__(self, environment=None, printer_data=None, temperature=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._environment = None
        self._printer_data = None
        self._temperature = None
        self.discriminator = None

        self.environment = environment
        self.printer_data = printer_data
        self.temperature = temperature

    @property
    def environment(self):
        """Gets the environment of this OctoprintMetadata.  # noqa: E501


        :return: The environment of this OctoprintMetadata.  # noqa: E501
        :rtype: OctoprintEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this OctoprintMetadata.


        :param environment: The environment of this OctoprintMetadata.  # noqa: E501
        :type environment: OctoprintEnvironment
        """
        if self.local_vars_configuration.client_side_validation and environment is None:  # noqa: E501
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def printer_data(self):
        """Gets the printer_data of this OctoprintMetadata.  # noqa: E501


        :return: The printer_data of this OctoprintMetadata.  # noqa: E501
        :rtype: OctoprintPrinterData
        """
        return self._printer_data

    @printer_data.setter
    def printer_data(self, printer_data):
        """Sets the printer_data of this OctoprintMetadata.


        :param printer_data: The printer_data of this OctoprintMetadata.  # noqa: E501
        :type printer_data: OctoprintPrinterData
        """
        if self.local_vars_configuration.client_side_validation and printer_data is None:  # noqa: E501
            raise ValueError("Invalid value for `printer_data`, must not be `None`")  # noqa: E501

        self._printer_data = printer_data

    @property
    def temperature(self):
        """Gets the temperature of this OctoprintMetadata.  # noqa: E501


        :return: The temperature of this OctoprintMetadata.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this OctoprintMetadata.


        :param temperature: The temperature of this OctoprintMetadata.  # noqa: E501
        :type temperature: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and temperature is None:  # noqa: E501
            raise ValueError("Invalid value for `temperature`, must not be `None`")  # noqa: E501

        self._temperature = temperature

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
        if not isinstance(other, OctoprintMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintMetadata):
            return True

        return self.to_dict() != other.to_dict()
