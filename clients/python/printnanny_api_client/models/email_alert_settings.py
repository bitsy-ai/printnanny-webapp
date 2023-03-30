# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.132.1
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


class EmailAlertSettings(object):
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
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'progress_percent': 'int',
        'enabled': 'bool',
        'event_types': 'list[EventTypesEnum]',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'progress_percent': 'progress_percent',
        'enabled': 'enabled',
        'event_types': 'event_types',
        'user': 'user'
    }

    def __init__(self, id=None, created_dt=None, updated_dt=None, progress_percent=None, enabled=None, event_types=None, user=None, local_vars_configuration=None):  # noqa: E501
        """EmailAlertSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._updated_dt = None
        self._progress_percent = None
        self._enabled = None
        self._event_types = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        if progress_percent is not None:
            self.progress_percent = progress_percent
        if enabled is not None:
            self.enabled = enabled
        if event_types is not None:
            self.event_types = event_types
        self.user = user

    @property
    def id(self):
        """Gets the id of this EmailAlertSettings.  # noqa: E501


        :return: The id of this EmailAlertSettings.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmailAlertSettings.


        :param id: The id of this EmailAlertSettings.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this EmailAlertSettings.  # noqa: E501


        :return: The created_dt of this EmailAlertSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this EmailAlertSettings.


        :param created_dt: The created_dt of this EmailAlertSettings.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this EmailAlertSettings.  # noqa: E501


        :return: The updated_dt of this EmailAlertSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this EmailAlertSettings.


        :param updated_dt: The updated_dt of this EmailAlertSettings.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def progress_percent(self):
        """Gets the progress_percent of this EmailAlertSettings.  # noqa: E501


        :return: The progress_percent of this EmailAlertSettings.  # noqa: E501
        :rtype: int
        """
        return self._progress_percent

    @progress_percent.setter
    def progress_percent(self, progress_percent):
        """Sets the progress_percent of this EmailAlertSettings.


        :param progress_percent: The progress_percent of this EmailAlertSettings.  # noqa: E501
        :type progress_percent: int
        """
        if (self.local_vars_configuration.client_side_validation and
                progress_percent is not None and progress_percent > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `progress_percent`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                progress_percent is not None and progress_percent < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `progress_percent`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._progress_percent = progress_percent

    @property
    def enabled(self):
        """Gets the enabled of this EmailAlertSettings.  # noqa: E501


        :return: The enabled of this EmailAlertSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this EmailAlertSettings.


        :param enabled: The enabled of this EmailAlertSettings.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def event_types(self):
        """Gets the event_types of this EmailAlertSettings.  # noqa: E501


        :return: The event_types of this EmailAlertSettings.  # noqa: E501
        :rtype: list[EventTypesEnum]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this EmailAlertSettings.


        :param event_types: The event_types of this EmailAlertSettings.  # noqa: E501
        :type event_types: list[EventTypesEnum]
        """

        self._event_types = event_types

    @property
    def user(self):
        """Gets the user of this EmailAlertSettings.  # noqa: E501


        :return: The user of this EmailAlertSettings.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this EmailAlertSettings.


        :param user: The user of this EmailAlertSettings.  # noqa: E501
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
        if not isinstance(other, EmailAlertSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailAlertSettings):
            return True

        return self.to_dict() != other.to_dict()
