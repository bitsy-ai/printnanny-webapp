# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.8
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


class PrintNannyApiConfig(object):
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
        'bearer_access_token': 'str',
        'base_path': 'str'
    }

    attribute_map = {
        'bearer_access_token': 'bearer_access_token',
        'base_path': 'base_path'
    }

    def __init__(self, bearer_access_token=None, base_path=None, local_vars_configuration=None):  # noqa: E501
        """PrintNannyApiConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bearer_access_token = None
        self._base_path = None
        self.discriminator = None

        self.bearer_access_token = bearer_access_token
        self.base_path = base_path

    @property
    def bearer_access_token(self):
        """Gets the bearer_access_token of this PrintNannyApiConfig.  # noqa: E501


        :return: The bearer_access_token of this PrintNannyApiConfig.  # noqa: E501
        :rtype: str
        """
        return self._bearer_access_token

    @bearer_access_token.setter
    def bearer_access_token(self, bearer_access_token):
        """Sets the bearer_access_token of this PrintNannyApiConfig.


        :param bearer_access_token: The bearer_access_token of this PrintNannyApiConfig.  # noqa: E501
        :type bearer_access_token: str
        """

        self._bearer_access_token = bearer_access_token

    @property
    def base_path(self):
        """Gets the base_path of this PrintNannyApiConfig.  # noqa: E501


        :return: The base_path of this PrintNannyApiConfig.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this PrintNannyApiConfig.


        :param base_path: The base_path of this PrintNannyApiConfig.  # noqa: E501
        :type base_path: str
        """
        if self.local_vars_configuration.client_side_validation and base_path is None:  # noqa: E501
            raise ValueError("Invalid value for `base_path`, must not be `None`")  # noqa: E501

        self._base_path = base_path

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
        if not isinstance(other, PrintNannyApiConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintNannyApiConfig):
            return True

        return self.to_dict() != other.to_dict()
