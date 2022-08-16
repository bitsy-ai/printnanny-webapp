# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.101.2
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


class User(object):
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
        'id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'is_beta_tester': 'bool',
        'member_badges': 'list[MemberBadge]'
    }

    attribute_map = {
        'email': 'email',
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'is_beta_tester': 'is_beta_tester',
        'member_badges': 'member_badges'
    }

    def __init__(self, email=None, id=None, first_name=None, last_name=None, is_beta_tester=None, member_badges=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._id = None
        self._first_name = None
        self._last_name = None
        self._is_beta_tester = None
        self._member_badges = None
        self.discriminator = None

        self.email = email
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.is_beta_tester = is_beta_tester
        self.member_badges = member_badges

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 30):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `30`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 30):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `30`")  # noqa: E501

        self._last_name = last_name

    @property
    def is_beta_tester(self):
        """Gets the is_beta_tester of this User.  # noqa: E501


        :return: The is_beta_tester of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_beta_tester

    @is_beta_tester.setter
    def is_beta_tester(self, is_beta_tester):
        """Sets the is_beta_tester of this User.


        :param is_beta_tester: The is_beta_tester of this User.  # noqa: E501
        :type is_beta_tester: bool
        """
        if self.local_vars_configuration.client_side_validation and is_beta_tester is None:  # noqa: E501
            raise ValueError("Invalid value for `is_beta_tester`, must not be `None`")  # noqa: E501

        self._is_beta_tester = is_beta_tester

    @property
    def member_badges(self):
        """Gets the member_badges of this User.  # noqa: E501


        :return: The member_badges of this User.  # noqa: E501
        :rtype: list[MemberBadge]
        """
        return self._member_badges

    @member_badges.setter
    def member_badges(self, member_badges):
        """Sets the member_badges of this User.


        :param member_badges: The member_badges of this User.  # noqa: E501
        :type member_badges: list[MemberBadge]
        """
        if self.local_vars_configuration.client_side_validation and member_badges is None:  # noqa: E501
            raise ValueError("Invalid value for `member_badges`, must not be `None`")  # noqa: E501

        self._member_badges = member_badges

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
