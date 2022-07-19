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


class AlertRequest(object):
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
        'octoprint_device': 'int',
        'event_type': 'EventTypeEnum',
        'seen': 'bool',
        'sent': 'bool'
    }

    attribute_map = {
        'octoprint_device': 'octoprint_device',
        'event_type': 'event_type',
        'seen': 'seen',
        'sent': 'sent'
    }

    def __init__(self, octoprint_device=None, event_type=None, seen=None, sent=None, local_vars_configuration=None):  # noqa: E501
        """AlertRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._octoprint_device = None
        self._event_type = None
        self._seen = None
        self._sent = None
        self.discriminator = None

        self.octoprint_device = octoprint_device
        self.event_type = event_type
        if seen is not None:
            self.seen = seen
        if sent is not None:
            self.sent = sent

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this AlertRequest.  # noqa: E501


        :return: The octoprint_device of this AlertRequest.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this AlertRequest.


        :param octoprint_device: The octoprint_device of this AlertRequest.  # noqa: E501
        :type octoprint_device: int
        """

        self._octoprint_device = octoprint_device

    @property
    def event_type(self):
        """Gets the event_type of this AlertRequest.  # noqa: E501


        :return: The event_type of this AlertRequest.  # noqa: E501
        :rtype: EventTypeEnum
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this AlertRequest.


        :param event_type: The event_type of this AlertRequest.  # noqa: E501
        :type event_type: EventTypeEnum
        """

        self._event_type = event_type

    @property
    def seen(self):
        """Gets the seen of this AlertRequest.  # noqa: E501


        :return: The seen of this AlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this AlertRequest.


        :param seen: The seen of this AlertRequest.  # noqa: E501
        :type seen: bool
        """

        self._seen = seen

    @property
    def sent(self):
        """Gets the sent of this AlertRequest.  # noqa: E501


        :return: The sent of this AlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this AlertRequest.


        :param sent: The sent of this AlertRequest.  # noqa: E501
        :type sent: bool
        """

        self._sent = sent

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
        if not isinstance(other, AlertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertRequest):
            return True

        return self.to_dict() != other.to_dict()
