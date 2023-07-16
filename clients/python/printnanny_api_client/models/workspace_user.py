# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
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


class WorkspaceUser(object):
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
        'id': 'int',
        'user': 'User',
        'created': 'datetime',
        'modified': 'datetime',
        'is_admin': 'bool',
        'organization': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'created': 'created',
        'modified': 'modified',
        'is_admin': 'is_admin',
        'organization': 'organization'
    }

    def __init__(self, id=None, user=None, created=None, modified=None, is_admin=None, organization=None, local_vars_configuration=None):  # noqa: E501
        """WorkspaceUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user = None
        self._created = None
        self._modified = None
        self._is_admin = None
        self._organization = None
        self.discriminator = None

        self.id = id
        self.user = user
        self.created = created
        self.modified = modified
        if is_admin is not None:
            self.is_admin = is_admin
        self.organization = organization

    @property
    def id(self):
        """Gets the id of this WorkspaceUser.  # noqa: E501


        :return: The id of this WorkspaceUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceUser.


        :param id: The id of this WorkspaceUser.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user(self):
        """Gets the user of this WorkspaceUser.  # noqa: E501


        :return: The user of this WorkspaceUser.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WorkspaceUser.


        :param user: The user of this WorkspaceUser.  # noqa: E501
        :type user: User
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def created(self):
        """Gets the created of this WorkspaceUser.  # noqa: E501


        :return: The created of this WorkspaceUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WorkspaceUser.


        :param created: The created of this WorkspaceUser.  # noqa: E501
        :type created: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this WorkspaceUser.  # noqa: E501


        :return: The modified of this WorkspaceUser.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this WorkspaceUser.


        :param modified: The modified of this WorkspaceUser.  # noqa: E501
        :type modified: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified is None:  # noqa: E501
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def is_admin(self):
        """Gets the is_admin of this WorkspaceUser.  # noqa: E501


        :return: The is_admin of this WorkspaceUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this WorkspaceUser.


        :param is_admin: The is_admin of this WorkspaceUser.  # noqa: E501
        :type is_admin: bool
        """

        self._is_admin = is_admin

    @property
    def organization(self):
        """Gets the organization of this WorkspaceUser.  # noqa: E501


        :return: The organization of this WorkspaceUser.  # noqa: E501
        :rtype: int
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this WorkspaceUser.


        :param organization: The organization of this WorkspaceUser.  # noqa: E501
        :type organization: int
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

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
        if not isinstance(other, WorkspaceUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceUser):
            return True

        return self.to_dict() != other.to_dict()