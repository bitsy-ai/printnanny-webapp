# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.94.2
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


class AlertSettings(object):
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
        'alert_methods': 'list[AlertMethodsEnum]',
        'event_types': 'list[EventTypesEnum]',
        'discord_webhook': 'str',
        'print_progress_percent': 'int',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'alert_methods': 'alert_methods',
        'event_types': 'event_types',
        'discord_webhook': 'discord_webhook',
        'print_progress_percent': 'print_progress_percent',
        'user': 'user'
    }

    def __init__(self, id=None, created_dt=None, updated_dt=None, alert_methods=None, event_types=None, discord_webhook=None, print_progress_percent=None, user=None, local_vars_configuration=None):  # noqa: E501
        """AlertSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._updated_dt = None
        self._alert_methods = None
        self._event_types = None
        self._discord_webhook = None
        self._print_progress_percent = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        if alert_methods is not None:
            self.alert_methods = alert_methods
        if event_types is not None:
            self.event_types = event_types
        self.discord_webhook = discord_webhook
        if print_progress_percent is not None:
            self.print_progress_percent = print_progress_percent
        self.user = user

    @property
    def id(self):
        """Gets the id of this AlertSettings.  # noqa: E501


        :return: The id of this AlertSettings.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertSettings.


        :param id: The id of this AlertSettings.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this AlertSettings.  # noqa: E501


        :return: The created_dt of this AlertSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this AlertSettings.


        :param created_dt: The created_dt of this AlertSettings.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this AlertSettings.  # noqa: E501


        :return: The updated_dt of this AlertSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this AlertSettings.


        :param updated_dt: The updated_dt of this AlertSettings.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def alert_methods(self):
        """Gets the alert_methods of this AlertSettings.  # noqa: E501


        :return: The alert_methods of this AlertSettings.  # noqa: E501
        :rtype: list[AlertMethodsEnum]
        """
        return self._alert_methods

    @alert_methods.setter
    def alert_methods(self, alert_methods):
        """Sets the alert_methods of this AlertSettings.


        :param alert_methods: The alert_methods of this AlertSettings.  # noqa: E501
        :type alert_methods: list[AlertMethodsEnum]
        """

        self._alert_methods = alert_methods

    @property
    def event_types(self):
        """Gets the event_types of this AlertSettings.  # noqa: E501


        :return: The event_types of this AlertSettings.  # noqa: E501
        :rtype: list[EventTypesEnum]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this AlertSettings.


        :param event_types: The event_types of this AlertSettings.  # noqa: E501
        :type event_types: list[EventTypesEnum]
        """

        self._event_types = event_types

    @property
    def discord_webhook(self):
        """Gets the discord_webhook of this AlertSettings.  # noqa: E501

        Send notifications to a Discord channel. Please check out this guide to <a href='https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks'>generate a webhook</a> url and paste it here.  # noqa: E501

        :return: The discord_webhook of this AlertSettings.  # noqa: E501
        :rtype: str
        """
        return self._discord_webhook

    @discord_webhook.setter
    def discord_webhook(self, discord_webhook):
        """Sets the discord_webhook of this AlertSettings.

        Send notifications to a Discord channel. Please check out this guide to <a href='https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks'>generate a webhook</a> url and paste it here.  # noqa: E501

        :param discord_webhook: The discord_webhook of this AlertSettings.  # noqa: E501
        :type discord_webhook: str
        """
        if (self.local_vars_configuration.client_side_validation and
                discord_webhook is not None and len(discord_webhook) > 255):
            raise ValueError("Invalid value for `discord_webhook`, length must be less than or equal to `255`")  # noqa: E501

        self._discord_webhook = discord_webhook

    @property
    def print_progress_percent(self):
        """Gets the print_progress_percent of this AlertSettings.  # noqa: E501

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :return: The print_progress_percent of this AlertSettings.  # noqa: E501
        :rtype: int
        """
        return self._print_progress_percent

    @print_progress_percent.setter
    def print_progress_percent(self, print_progress_percent):
        """Sets the print_progress_percent of this AlertSettings.

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :param print_progress_percent: The print_progress_percent of this AlertSettings.  # noqa: E501
        :type print_progress_percent: int
        """
        if (self.local_vars_configuration.client_side_validation and
                print_progress_percent is not None and print_progress_percent > 100):  # noqa: E501
            raise ValueError("Invalid value for `print_progress_percent`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_progress_percent is not None and print_progress_percent < 1):  # noqa: E501
            raise ValueError("Invalid value for `print_progress_percent`, must be a value greater than or equal to `1`")  # noqa: E501

        self._print_progress_percent = print_progress_percent

    @property
    def user(self):
        """Gets the user of this AlertSettings.  # noqa: E501


        :return: The user of this AlertSettings.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AlertSettings.


        :param user: The user of this AlertSettings.  # noqa: E501
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
        if not isinstance(other, AlertSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertSettings):
            return True

        return self.to_dict() != other.to_dict()
