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


class WorkspaceInvite(object):
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
        'guid': 'str',
        'invitee_identifier': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'invited_by': 'int',
        'invitee': 'int',
        'organization': 'int'
    }

    attribute_map = {
        'id': 'id',
        'guid': 'guid',
        'invitee_identifier': 'invitee_identifier',
        'created': 'created',
        'modified': 'modified',
        'invited_by': 'invited_by',
        'invitee': 'invitee',
        'organization': 'organization'
    }

    def __init__(self, id=None, guid=None, invitee_identifier=None, created=None, modified=None, invited_by=None, invitee=None, organization=None, local_vars_configuration=None):  # noqa: E501
        """WorkspaceInvite - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._guid = None
        self._invitee_identifier = None
        self._created = None
        self._modified = None
        self._invited_by = None
        self._invitee = None
        self._organization = None
        self.discriminator = None

        self.id = id
        self.guid = guid
        self.invitee_identifier = invitee_identifier
        self.created = created
        self.modified = modified
        self.invited_by = invited_by
        self.invitee = invitee
        self.organization = organization

    @property
    def id(self):
        """Gets the id of this WorkspaceInvite.  # noqa: E501


        :return: The id of this WorkspaceInvite.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceInvite.


        :param id: The id of this WorkspaceInvite.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def guid(self):
        """Gets the guid of this WorkspaceInvite.  # noqa: E501


        :return: The guid of this WorkspaceInvite.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this WorkspaceInvite.


        :param guid: The guid of this WorkspaceInvite.  # noqa: E501
        :type guid: str
        """
        if self.local_vars_configuration.client_side_validation and guid is None:  # noqa: E501
            raise ValueError("Invalid value for `guid`, must not be `None`")  # noqa: E501

        self._guid = guid

    @property
    def invitee_identifier(self):
        """Gets the invitee_identifier of this WorkspaceInvite.  # noqa: E501

        The contact identifier for the invitee, email, phone number, social media handle, etc.  # noqa: E501

        :return: The invitee_identifier of this WorkspaceInvite.  # noqa: E501
        :rtype: str
        """
        return self._invitee_identifier

    @invitee_identifier.setter
    def invitee_identifier(self, invitee_identifier):
        """Sets the invitee_identifier of this WorkspaceInvite.

        The contact identifier for the invitee, email, phone number, social media handle, etc.  # noqa: E501

        :param invitee_identifier: The invitee_identifier of this WorkspaceInvite.  # noqa: E501
        :type invitee_identifier: str
        """
        if self.local_vars_configuration.client_side_validation and invitee_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `invitee_identifier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                invitee_identifier is not None and len(invitee_identifier) > 1000):
            raise ValueError("Invalid value for `invitee_identifier`, length must be less than or equal to `1000`")  # noqa: E501

        self._invitee_identifier = invitee_identifier

    @property
    def created(self):
        """Gets the created of this WorkspaceInvite.  # noqa: E501


        :return: The created of this WorkspaceInvite.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WorkspaceInvite.


        :param created: The created of this WorkspaceInvite.  # noqa: E501
        :type created: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this WorkspaceInvite.  # noqa: E501


        :return: The modified of this WorkspaceInvite.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this WorkspaceInvite.


        :param modified: The modified of this WorkspaceInvite.  # noqa: E501
        :type modified: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified is None:  # noqa: E501
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def invited_by(self):
        """Gets the invited_by of this WorkspaceInvite.  # noqa: E501


        :return: The invited_by of this WorkspaceInvite.  # noqa: E501
        :rtype: int
        """
        return self._invited_by

    @invited_by.setter
    def invited_by(self, invited_by):
        """Sets the invited_by of this WorkspaceInvite.


        :param invited_by: The invited_by of this WorkspaceInvite.  # noqa: E501
        :type invited_by: int
        """
        if self.local_vars_configuration.client_side_validation and invited_by is None:  # noqa: E501
            raise ValueError("Invalid value for `invited_by`, must not be `None`")  # noqa: E501

        self._invited_by = invited_by

    @property
    def invitee(self):
        """Gets the invitee of this WorkspaceInvite.  # noqa: E501


        :return: The invitee of this WorkspaceInvite.  # noqa: E501
        :rtype: int
        """
        return self._invitee

    @invitee.setter
    def invitee(self, invitee):
        """Sets the invitee of this WorkspaceInvite.


        :param invitee: The invitee of this WorkspaceInvite.  # noqa: E501
        :type invitee: int
        """

        self._invitee = invitee

    @property
    def organization(self):
        """Gets the organization of this WorkspaceInvite.  # noqa: E501


        :return: The organization of this WorkspaceInvite.  # noqa: E501
        :rtype: int
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this WorkspaceInvite.


        :param organization: The organization of this WorkspaceInvite.  # noqa: E501
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
        if not isinstance(other, WorkspaceInvite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceInvite):
            return True

        return self.to_dict() != other.to_dict()
