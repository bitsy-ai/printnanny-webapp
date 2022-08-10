# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.2
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


class RegisterRequest(object):
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
        'email': 'str',
        'password1': 'str',
        'password2': 'str'
    }

    attribute_map = {
        'email': 'email',
        'password1': 'password1',
        'password2': 'password2'
    }

    def __init__(self, email=None, password1=None, password2=None, local_vars_configuration=None):  # noqa: E501
        """RegisterRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._password1 = None
        self._password2 = None
        self.discriminator = None

        self.email = email
        self.password1 = password1
        self.password2 = password2

    @property
    def email(self):
        """Gets the email of this RegisterRequest.  # noqa: E501


        :return: The email of this RegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RegisterRequest.


        :param email: The email of this RegisterRequest.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def password1(self):
        """Gets the password1 of this RegisterRequest.  # noqa: E501


        :return: The password1 of this RegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._password1

    @password1.setter
    def password1(self, password1):
        """Sets the password1 of this RegisterRequest.


        :param password1: The password1 of this RegisterRequest.  # noqa: E501
        :type password1: str
        """
        if self.local_vars_configuration.client_side_validation and password1 is None:  # noqa: E501
            raise ValueError("Invalid value for `password1`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password1 is not None and len(password1) < 1):
            raise ValueError("Invalid value for `password1`, length must be greater than or equal to `1`")  # noqa: E501

        self._password1 = password1

    @property
    def password2(self):
        """Gets the password2 of this RegisterRequest.  # noqa: E501


        :return: The password2 of this RegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._password2

    @password2.setter
    def password2(self, password2):
        """Sets the password2 of this RegisterRequest.


        :param password2: The password2 of this RegisterRequest.  # noqa: E501
        :type password2: str
        """
        if self.local_vars_configuration.client_side_validation and password2 is None:  # noqa: E501
            raise ValueError("Invalid value for `password2`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password2 is not None and len(password2) < 1):
            raise ValueError("Invalid value for `password2`, length must be greater than or equal to `1`")  # noqa: E501

        self._password2 = password2

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
        if not isinstance(other, RegisterRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterRequest):
            return True

        return self.to_dict() != other.to_dict()
