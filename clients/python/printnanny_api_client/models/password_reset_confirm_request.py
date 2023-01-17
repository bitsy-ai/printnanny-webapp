# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.2
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


class PasswordResetConfirmRequest(object):
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
        'new_password1': 'str',
        'new_password2': 'str',
        'uid': 'str',
        'token': 'str'
    }

    attribute_map = {
        'new_password1': 'new_password1',
        'new_password2': 'new_password2',
        'uid': 'uid',
        'token': 'token'
    }

    def __init__(self, new_password1=None, new_password2=None, uid=None, token=None, local_vars_configuration=None):  # noqa: E501
        """PasswordResetConfirmRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._new_password1 = None
        self._new_password2 = None
        self._uid = None
        self._token = None
        self.discriminator = None

        self.new_password1 = new_password1
        self.new_password2 = new_password2
        self.uid = uid
        self.token = token

    @property
    def new_password1(self):
        """Gets the new_password1 of this PasswordResetConfirmRequest.  # noqa: E501


        :return: The new_password1 of this PasswordResetConfirmRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_password1

    @new_password1.setter
    def new_password1(self, new_password1):
        """Sets the new_password1 of this PasswordResetConfirmRequest.


        :param new_password1: The new_password1 of this PasswordResetConfirmRequest.  # noqa: E501
        :type new_password1: str
        """
        if self.local_vars_configuration.client_side_validation and new_password1 is None:  # noqa: E501
            raise ValueError("Invalid value for `new_password1`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_password1 is not None and len(new_password1) > 128):
            raise ValueError("Invalid value for `new_password1`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_password1 is not None and len(new_password1) < 1):
            raise ValueError("Invalid value for `new_password1`, length must be greater than or equal to `1`")  # noqa: E501

        self._new_password1 = new_password1

    @property
    def new_password2(self):
        """Gets the new_password2 of this PasswordResetConfirmRequest.  # noqa: E501


        :return: The new_password2 of this PasswordResetConfirmRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_password2

    @new_password2.setter
    def new_password2(self, new_password2):
        """Sets the new_password2 of this PasswordResetConfirmRequest.


        :param new_password2: The new_password2 of this PasswordResetConfirmRequest.  # noqa: E501
        :type new_password2: str
        """
        if self.local_vars_configuration.client_side_validation and new_password2 is None:  # noqa: E501
            raise ValueError("Invalid value for `new_password2`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_password2 is not None and len(new_password2) > 128):
            raise ValueError("Invalid value for `new_password2`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_password2 is not None and len(new_password2) < 1):
            raise ValueError("Invalid value for `new_password2`, length must be greater than or equal to `1`")  # noqa: E501

        self._new_password2 = new_password2

    @property
    def uid(self):
        """Gets the uid of this PasswordResetConfirmRequest.  # noqa: E501


        :return: The uid of this PasswordResetConfirmRequest.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this PasswordResetConfirmRequest.


        :param uid: The uid of this PasswordResetConfirmRequest.  # noqa: E501
        :type uid: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uid is not None and len(uid) < 1):
            raise ValueError("Invalid value for `uid`, length must be greater than or equal to `1`")  # noqa: E501

        self._uid = uid

    @property
    def token(self):
        """Gets the token of this PasswordResetConfirmRequest.  # noqa: E501


        :return: The token of this PasswordResetConfirmRequest.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this PasswordResetConfirmRequest.


        :param token: The token of this PasswordResetConfirmRequest.  # noqa: E501
        :type token: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token is not None and len(token) < 1):
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `1`")  # noqa: E501

        self._token = token

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
        if not isinstance(other, PasswordResetConfirmRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PasswordResetConfirmRequest):
            return True

        return self.to_dict() != other.to_dict()
