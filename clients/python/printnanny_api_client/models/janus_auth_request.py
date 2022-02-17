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


class JanusAuthRequest(object):
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
        'admin_secret': 'str',
        'api_token': 'str',
        'config_type': 'JanusConfigType',
        'user': 'int'
    }

    attribute_map = {
        'admin_secret': 'admin_secret',
        'api_token': 'api_token',
        'config_type': 'config_type',
        'user': 'user'
    }

    def __init__(self, admin_secret=None, api_token=None, config_type=None, user=None, local_vars_configuration=None):  # noqa: E501
        """JanusAuthRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._admin_secret = None
        self._api_token = None
        self._config_type = None
        self._user = None
        self.discriminator = None

        self.admin_secret = admin_secret
        if api_token is not None:
            self.api_token = api_token
        if config_type is not None:
            self.config_type = config_type
        self.user = user

    @property
    def admin_secret(self):
        """Gets the admin_secret of this JanusAuthRequest.  # noqa: E501


        :return: The admin_secret of this JanusAuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._admin_secret

    @admin_secret.setter
    def admin_secret(self, admin_secret):
        """Sets the admin_secret of this JanusAuthRequest.


        :param admin_secret: The admin_secret of this JanusAuthRequest.  # noqa: E501
        :type admin_secret: str
        """
        if (self.local_vars_configuration.client_side_validation and
                admin_secret is not None and len(admin_secret) > 255):
            raise ValueError("Invalid value for `admin_secret`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                admin_secret is not None and len(admin_secret) < 1):
            raise ValueError("Invalid value for `admin_secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._admin_secret = admin_secret

    @property
    def api_token(self):
        """Gets the api_token of this JanusAuthRequest.  # noqa: E501


        :return: The api_token of this JanusAuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this JanusAuthRequest.


        :param api_token: The api_token of this JanusAuthRequest.  # noqa: E501
        :type api_token: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_token is not None and len(api_token) > 255):
            raise ValueError("Invalid value for `api_token`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                api_token is not None and len(api_token) < 1):
            raise ValueError("Invalid value for `api_token`, length must be greater than or equal to `1`")  # noqa: E501

        self._api_token = api_token

    @property
    def config_type(self):
        """Gets the config_type of this JanusAuthRequest.  # noqa: E501


        :return: The config_type of this JanusAuthRequest.  # noqa: E501
        :rtype: JanusConfigType
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this JanusAuthRequest.


        :param config_type: The config_type of this JanusAuthRequest.  # noqa: E501
        :type config_type: JanusConfigType
        """

        self._config_type = config_type

    @property
    def user(self):
        """Gets the user of this JanusAuthRequest.  # noqa: E501


        :return: The user of this JanusAuthRequest.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this JanusAuthRequest.


        :param user: The user of this JanusAuthRequest.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, JanusAuthRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JanusAuthRequest):
            return True

        return self.to_dict() != other.to_dict()
