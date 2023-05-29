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


class WorkspaceInviteRemindRequest(object):
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
        'workspace_invite': 'int'
    }

    attribute_map = {
        'workspace_invite': 'workspace_invite'
    }

    def __init__(self, workspace_invite=None, local_vars_configuration=None):  # noqa: E501
        """WorkspaceInviteRemindRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._workspace_invite = None
        self.discriminator = None

        self.workspace_invite = workspace_invite

    @property
    def workspace_invite(self):
        """Gets the workspace_invite of this WorkspaceInviteRemindRequest.  # noqa: E501


        :return: The workspace_invite of this WorkspaceInviteRemindRequest.  # noqa: E501
        :rtype: int
        """
        return self._workspace_invite

    @workspace_invite.setter
    def workspace_invite(self, workspace_invite):
        """Sets the workspace_invite of this WorkspaceInviteRemindRequest.


        :param workspace_invite: The workspace_invite of this WorkspaceInviteRemindRequest.  # noqa: E501
        :type workspace_invite: int
        """
        if self.local_vars_configuration.client_side_validation and workspace_invite is None:  # noqa: E501
            raise ValueError("Invalid value for `workspace_invite`, must not be `None`")  # noqa: E501

        self._workspace_invite = workspace_invite

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
        if not isinstance(other, WorkspaceInviteRemindRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceInviteRemindRequest):
            return True

        return self.to_dict() != other.to_dict()
