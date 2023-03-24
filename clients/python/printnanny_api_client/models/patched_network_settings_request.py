# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.129.1
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


class PatchedNetworkSettingsRequest(object):
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
        'preferred_dns': 'PreferredDnsType',
        'user': 'int'
    }

    attribute_map = {
        'preferred_dns': 'preferred_dns',
        'user': 'user'
    }

    def __init__(self, preferred_dns=None, user=None, local_vars_configuration=None):  # noqa: E501
        """PatchedNetworkSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._preferred_dns = None
        self._user = None
        self.discriminator = None

        if preferred_dns is not None:
            self.preferred_dns = preferred_dns
        if user is not None:
            self.user = user

    @property
    def preferred_dns(self):
        """Gets the preferred_dns of this PatchedNetworkSettingsRequest.  # noqa: E501


        :return: The preferred_dns of this PatchedNetworkSettingsRequest.  # noqa: E501
        :rtype: PreferredDnsType
        """
        return self._preferred_dns

    @preferred_dns.setter
    def preferred_dns(self, preferred_dns):
        """Sets the preferred_dns of this PatchedNetworkSettingsRequest.


        :param preferred_dns: The preferred_dns of this PatchedNetworkSettingsRequest.  # noqa: E501
        :type preferred_dns: PreferredDnsType
        """

        self._preferred_dns = preferred_dns

    @property
    def user(self):
        """Gets the user of this PatchedNetworkSettingsRequest.  # noqa: E501


        :return: The user of this PatchedNetworkSettingsRequest.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PatchedNetworkSettingsRequest.


        :param user: The user of this PatchedNetworkSettingsRequest.  # noqa: E501
        :type user: int
        """

        self._user = user

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
        if not isinstance(other, PatchedNetworkSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedNetworkSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
