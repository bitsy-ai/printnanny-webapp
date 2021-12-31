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


class ReleaseRequest(object):
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
        'name': 'str',
        'variant': 'ReleaseVariant',
        'zip_url': 'str',
        'release_channel': 'ReleaseChannelEnum'
    }

    attribute_map = {
        'name': 'name',
        'variant': 'variant',
        'zip_url': 'zip_url',
        'release_channel': 'release_channel'
    }

    def __init__(self, name=None, variant=None, zip_url=None, release_channel=None, local_vars_configuration=None):  # noqa: E501
        """ReleaseRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._variant = None
        self._zip_url = None
        self._release_channel = None
        self.discriminator = None

        self.name = name
        self.variant = variant
        self.zip_url = zip_url
        if release_channel is not None:
            self.release_channel = release_channel

    @property
    def name(self):
        """Gets the name of this ReleaseRequest.  # noqa: E501


        :return: The name of this ReleaseRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReleaseRequest.


        :param name: The name of this ReleaseRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def variant(self):
        """Gets the variant of this ReleaseRequest.  # noqa: E501


        :return: The variant of this ReleaseRequest.  # noqa: E501
        :rtype: ReleaseVariant
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this ReleaseRequest.


        :param variant: The variant of this ReleaseRequest.  # noqa: E501
        :type variant: ReleaseVariant
        """
        if self.local_vars_configuration.client_side_validation and variant is None:  # noqa: E501
            raise ValueError("Invalid value for `variant`, must not be `None`")  # noqa: E501

        self._variant = variant

    @property
    def zip_url(self):
        """Gets the zip_url of this ReleaseRequest.  # noqa: E501


        :return: The zip_url of this ReleaseRequest.  # noqa: E501
        :rtype: str
        """
        return self._zip_url

    @zip_url.setter
    def zip_url(self, zip_url):
        """Sets the zip_url of this ReleaseRequest.


        :param zip_url: The zip_url of this ReleaseRequest.  # noqa: E501
        :type zip_url: str
        """
        if self.local_vars_configuration.client_side_validation and zip_url is None:  # noqa: E501
            raise ValueError("Invalid value for `zip_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                zip_url is not None and len(zip_url) > 255):
            raise ValueError("Invalid value for `zip_url`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                zip_url is not None and len(zip_url) < 1):
            raise ValueError("Invalid value for `zip_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._zip_url = zip_url

    @property
    def release_channel(self):
        """Gets the release_channel of this ReleaseRequest.  # noqa: E501


        :return: The release_channel of this ReleaseRequest.  # noqa: E501
        :rtype: ReleaseChannelEnum
        """
        return self._release_channel

    @release_channel.setter
    def release_channel(self, release_channel):
        """Sets the release_channel of this ReleaseRequest.


        :param release_channel: The release_channel of this ReleaseRequest.  # noqa: E501
        :type release_channel: ReleaseChannelEnum
        """

        self._release_channel = release_channel

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
        if not isinstance(other, ReleaseRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReleaseRequest):
            return True

        return self.to_dict() != other.to_dict()
