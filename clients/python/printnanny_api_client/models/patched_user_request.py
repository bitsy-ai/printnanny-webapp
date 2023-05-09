# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.134.2
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


class PatchedUserRequest(object):
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
        'first_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name'
    }

    def __init__(self, email=None, first_name=None, last_name=None, local_vars_configuration=None):  # noqa: E501
        """PatchedUserRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._first_name = None
        self._last_name = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name

    @property
    def email(self):
        """Gets the email of this PatchedUserRequest.  # noqa: E501


        :return: The email of this PatchedUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PatchedUserRequest.


        :param email: The email of this PatchedUserRequest.  # noqa: E501
        :type email: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this PatchedUserRequest.  # noqa: E501


        :return: The first_name of this PatchedUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PatchedUserRequest.


        :param first_name: The first_name of this PatchedUserRequest.  # noqa: E501
        :type first_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 150):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `150`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PatchedUserRequest.  # noqa: E501


        :return: The last_name of this PatchedUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PatchedUserRequest.


        :param last_name: The last_name of this PatchedUserRequest.  # noqa: E501
        :type last_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 150):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `150`")  # noqa: E501

        self._last_name = last_name

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
        if not isinstance(other, PatchedUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedUserRequest):
            return True

        return self.to_dict() != other.to_dict()
