# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class PatchedAlertPolymorphicRequest(object):
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
        'dismissed': 'bool',
        'alert_subtype': 'AlertSubtypeEnum',
        'alert_methods': 'list[AlertMethodsEnum]',
        'alert_type': 'AlertTypeEnum',
        'color': 'str',
        'icon': 'str',
        'description': 'str',
        'seen': 'bool',
        'title': 'str',
        'sent': 'bool',
        'progress_percent': 'int',
        'octoprint_device': 'int',
        'device': 'int',
        'print_session': 'int'
    }

    attribute_map = {
        'dismissed': 'dismissed',
        'alert_subtype': 'alert_subtype',
        'alert_methods': 'alert_methods',
        'alert_type': 'alert_type',
        'color': 'color',
        'icon': 'icon',
        'description': 'description',
        'seen': 'seen',
        'title': 'title',
        'sent': 'sent',
        'progress_percent': 'progress_percent',
        'octoprint_device': 'octoprint_device',
        'device': 'device',
        'print_session': 'print_session'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, dismissed=None, alert_subtype=None, alert_methods=None, alert_type=None, color=None, icon=None, description=None, seen=None, title=None, sent=None, progress_percent=None, octoprint_device=None, device=None, print_session=None, local_vars_configuration=None):  # noqa: E501
        """PatchedAlertPolymorphicRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dismissed = None
        self._alert_subtype = None
        self._alert_methods = None
        self._alert_type = None
        self._color = None
        self._icon = None
        self._description = None
        self._seen = None
        self._title = None
        self._sent = None
        self._progress_percent = None
        self._octoprint_device = None
        self._device = None
        self._print_session = None
        self.discriminator = 'type'

        if dismissed is not None:
            self.dismissed = dismissed
        if alert_subtype is not None:
            self.alert_subtype = alert_subtype
        if alert_methods is not None:
            self.alert_methods = alert_methods
        if alert_type is not None:
            self.alert_type = alert_type
        if color is not None:
            self.color = color
        if icon is not None:
            self.icon = icon
        if description is not None:
            self.description = description
        if seen is not None:
            self.seen = seen
        if title is not None:
            self.title = title
        if sent is not None:
            self.sent = sent
        if progress_percent is not None:
            self.progress_percent = progress_percent
        self.octoprint_device = octoprint_device
        if device is not None:
            self.device = device
        if print_session is not None:
            self.print_session = print_session

    @property
    def dismissed(self):
        """Gets the dismissed of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The dismissed of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dismissed

    @dismissed.setter
    def dismissed(self, dismissed):
        """Sets the dismissed of this PatchedAlertPolymorphicRequest.


        :param dismissed: The dismissed of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type dismissed: bool
        """

        self._dismissed = dismissed

    @property
    def alert_subtype(self):
        """Gets the alert_subtype of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The alert_subtype of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: AlertSubtypeEnum
        """
        return self._alert_subtype

    @alert_subtype.setter
    def alert_subtype(self, alert_subtype):
        """Sets the alert_subtype of this PatchedAlertPolymorphicRequest.


        :param alert_subtype: The alert_subtype of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type alert_subtype: AlertSubtypeEnum
        """

        self._alert_subtype = alert_subtype

    @property
    def alert_methods(self):
        """Gets the alert_methods of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The alert_methods of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: list[AlertMethodsEnum]
        """
        return self._alert_methods

    @alert_methods.setter
    def alert_methods(self, alert_methods):
        """Sets the alert_methods of this PatchedAlertPolymorphicRequest.


        :param alert_methods: The alert_methods of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type alert_methods: list[AlertMethodsEnum]
        """

        self._alert_methods = alert_methods

    @property
    def alert_type(self):
        """Gets the alert_type of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The alert_type of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: AlertTypeEnum
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this PatchedAlertPolymorphicRequest.


        :param alert_type: The alert_type of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type alert_type: AlertTypeEnum
        """

        self._alert_type = alert_type

    @property
    def color(self):
        """Gets the color of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The color of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this PatchedAlertPolymorphicRequest.


        :param color: The color of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type color: str
        """

        self._color = color

    @property
    def icon(self):
        """Gets the icon of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The icon of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this PatchedAlertPolymorphicRequest.


        :param icon: The icon of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def description(self):
        """Gets the description of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The description of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatchedAlertPolymorphicRequest.


        :param description: The description of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def seen(self):
        """Gets the seen of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The seen of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this PatchedAlertPolymorphicRequest.


        :param seen: The seen of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type seen: bool
        """

        self._seen = seen

    @property
    def title(self):
        """Gets the title of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The title of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PatchedAlertPolymorphicRequest.


        :param title: The title of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def sent(self):
        """Gets the sent of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The sent of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this PatchedAlertPolymorphicRequest.


        :param sent: The sent of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type sent: bool
        """

        self._sent = sent

    @property
    def progress_percent(self):
        """Gets the progress_percent of this PatchedAlertPolymorphicRequest.  # noqa: E501

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :return: The progress_percent of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: int
        """
        return self._progress_percent

    @progress_percent.setter
    def progress_percent(self, progress_percent):
        """Sets the progress_percent of this PatchedAlertPolymorphicRequest.

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :param progress_percent: The progress_percent of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type progress_percent: int
        """
        if (self.local_vars_configuration.client_side_validation and
                progress_percent is not None and progress_percent > 100):  # noqa: E501
            raise ValueError("Invalid value for `progress_percent`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                progress_percent is not None and progress_percent < 1):  # noqa: E501
            raise ValueError("Invalid value for `progress_percent`, must be a value greater than or equal to `1`")  # noqa: E501

        self._progress_percent = progress_percent

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The octoprint_device of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this PatchedAlertPolymorphicRequest.


        :param octoprint_device: The octoprint_device of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type octoprint_device: int
        """

        self._octoprint_device = octoprint_device

    @property
    def device(self):
        """Gets the device of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The device of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PatchedAlertPolymorphicRequest.


        :param device: The device of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type device: int
        """

        self._device = device

    @property
    def print_session(self):
        """Gets the print_session of this PatchedAlertPolymorphicRequest.  # noqa: E501


        :return: The print_session of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :rtype: int
        """
        return self._print_session

    @print_session.setter
    def print_session(self, print_session):
        """Sets the print_session of this PatchedAlertPolymorphicRequest.


        :param print_session: The print_session of this PatchedAlertPolymorphicRequest.  # noqa: E501
        :type print_session: int
        """

        self._print_session = print_session

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, PatchedAlertPolymorphicRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedAlertPolymorphicRequest):
            return True

        return self.to_dict() != other.to_dict()
