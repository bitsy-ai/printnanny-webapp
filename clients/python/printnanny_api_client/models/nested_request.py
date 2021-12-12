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


class NestedRequest(object):
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
        'hostname': 'str',
        'release_channel': 'ReleaseChannelEnum',
        'user': 'int',
        'bootstrap_release': 'int'
    }

    attribute_map = {
        'hostname': 'hostname',
        'release_channel': 'release_channel',
        'user': 'user',
        'bootstrap_release': 'bootstrap_release'
    }

    def __init__(self, hostname=None, release_channel=None, user=None, bootstrap_release=None, local_vars_configuration=None):  # noqa: E501
        """NestedRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._hostname = None
        self._release_channel = None
        self._user = None
        self._bootstrap_release = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        self.release_channel = release_channel
        self.user = user
        if bootstrap_release is not None:
            self.bootstrap_release = bootstrap_release

    @property
    def hostname(self):
        """Gets the hostname of this NestedRequest.  # noqa: E501

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :return: The hostname of this NestedRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this NestedRequest.

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :param hostname: The hostname of this NestedRequest.  # noqa: E501
        :type hostname: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) < 1):
            raise ValueError("Invalid value for `hostname`, length must be greater than or equal to `1`")  # noqa: E501

        self._hostname = hostname

    @property
    def release_channel(self):
        """Gets the release_channel of this NestedRequest.  # noqa: E501

        WARNING: you should only use the nightly developer channel when guided by Print Nanny staff! This unstable channel is intended for QA and verifying bug fixes.  # noqa: E501

        :return: The release_channel of this NestedRequest.  # noqa: E501
        :rtype: ReleaseChannelEnum
        """
        return self._release_channel

    @release_channel.setter
    def release_channel(self, release_channel):
        """Sets the release_channel of this NestedRequest.

        WARNING: you should only use the nightly developer channel when guided by Print Nanny staff! This unstable channel is intended for QA and verifying bug fixes.  # noqa: E501

        :param release_channel: The release_channel of this NestedRequest.  # noqa: E501
        :type release_channel: ReleaseChannelEnum
        """

        self._release_channel = release_channel

    @property
    def user(self):
        """Gets the user of this NestedRequest.  # noqa: E501


        :return: The user of this NestedRequest.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this NestedRequest.


        :param user: The user of this NestedRequest.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def bootstrap_release(self):
        """Gets the bootstrap_release of this NestedRequest.  # noqa: E501


        :return: The bootstrap_release of this NestedRequest.  # noqa: E501
        :rtype: int
        """
        return self._bootstrap_release

    @bootstrap_release.setter
    def bootstrap_release(self, bootstrap_release):
        """Sets the bootstrap_release of this NestedRequest.


        :param bootstrap_release: The bootstrap_release of this NestedRequest.  # noqa: E501
        :type bootstrap_release: int
        """

        self._bootstrap_release = bootstrap_release

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
        if not isinstance(other, NestedRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedRequest):
            return True

        return self.to_dict() != other.to_dict()
