# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.109.1
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


class PiSettingsRequest(object):
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
        'cloud_video_enabled': 'bool',
        'telemetry_enabled': 'bool',
        'pi': 'int'
    }

    attribute_map = {
        'cloud_video_enabled': 'cloud_video_enabled',
        'telemetry_enabled': 'telemetry_enabled',
        'pi': 'pi'
    }

    def __init__(self, cloud_video_enabled=None, telemetry_enabled=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """PiSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_video_enabled = None
        self._telemetry_enabled = None
        self._pi = None
        self.discriminator = None

        if cloud_video_enabled is not None:
            self.cloud_video_enabled = cloud_video_enabled
        if telemetry_enabled is not None:
            self.telemetry_enabled = telemetry_enabled
        self.pi = pi

    @property
    def cloud_video_enabled(self):
        """Gets the cloud_video_enabled of this PiSettingsRequest.  # noqa: E501

        Send camera stream to PrintNanny Cloud  # noqa: E501

        :return: The cloud_video_enabled of this PiSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_video_enabled

    @cloud_video_enabled.setter
    def cloud_video_enabled(self, cloud_video_enabled):
        """Sets the cloud_video_enabled of this PiSettingsRequest.

        Send camera stream to PrintNanny Cloud  # noqa: E501

        :param cloud_video_enabled: The cloud_video_enabled of this PiSettingsRequest.  # noqa: E501
        :type cloud_video_enabled: bool
        """

        self._cloud_video_enabled = cloud_video_enabled

    @property
    def telemetry_enabled(self):
        """Gets the telemetry_enabled of this PiSettingsRequest.  # noqa: E501

        Send telemetry and performance profiling data to PrintNanny Cloud  # noqa: E501

        :return: The telemetry_enabled of this PiSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._telemetry_enabled

    @telemetry_enabled.setter
    def telemetry_enabled(self, telemetry_enabled):
        """Sets the telemetry_enabled of this PiSettingsRequest.

        Send telemetry and performance profiling data to PrintNanny Cloud  # noqa: E501

        :param telemetry_enabled: The telemetry_enabled of this PiSettingsRequest.  # noqa: E501
        :type telemetry_enabled: bool
        """

        self._telemetry_enabled = telemetry_enabled

    @property
    def pi(self):
        """Gets the pi of this PiSettingsRequest.  # noqa: E501


        :return: The pi of this PiSettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PiSettingsRequest.


        :param pi: The pi of this PiSettingsRequest.  # noqa: E501
        :type pi: int
        """
        if self.local_vars_configuration.client_side_validation and pi is None:  # noqa: E501
            raise ValueError("Invalid value for `pi`, must not be `None`")  # noqa: E501

        self._pi = pi

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
        if not isinstance(other, PiSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PiSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
