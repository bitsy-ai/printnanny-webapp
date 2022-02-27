# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
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


class WebRTCEventRequest(object):
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
        'event_type': 'WebRTCEventEventTypeEnum',
        'source': 'EventSource',
        'send_ws': 'bool',
        'event_name': 'WebRTCEventName',
        'data': 'dict(str, object)',
        'send_mqtt': 'bool',
        'device': 'int'
    }

    attribute_map = {
        'event_type': 'event_type',
        'source': 'source',
        'send_ws': 'send_ws',
        'event_name': 'event_name',
        'data': 'data',
        'send_mqtt': 'send_mqtt',
        'device': 'device'
    }

    def __init__(self, event_type=None, source=None, send_ws=None, event_name=None, data=None, send_mqtt=None, device=None, local_vars_configuration=None):  # noqa: E501
        """WebRTCEventRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._source = None
        self._send_ws = None
        self._event_name = None
        self._data = None
        self._send_mqtt = None
        self._device = None
        self.discriminator = None

        self.event_type = event_type
        self.source = source
        if send_ws is not None:
            self.send_ws = send_ws
        self.event_name = event_name
        if data is not None:
            self.data = data
        if send_mqtt is not None:
            self.send_mqtt = send_mqtt
        self.device = device

    @property
    def event_type(self):
        """Gets the event_type of this WebRTCEventRequest.  # noqa: E501


        :return: The event_type of this WebRTCEventRequest.  # noqa: E501
        :rtype: WebRTCEventEventTypeEnum
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this WebRTCEventRequest.


        :param event_type: The event_type of this WebRTCEventRequest.  # noqa: E501
        :type event_type: WebRTCEventEventTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def source(self):
        """Gets the source of this WebRTCEventRequest.  # noqa: E501


        :return: The source of this WebRTCEventRequest.  # noqa: E501
        :rtype: EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this WebRTCEventRequest.


        :param source: The source of this WebRTCEventRequest.  # noqa: E501
        :type source: EventSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def send_ws(self):
        """Gets the send_ws of this WebRTCEventRequest.  # noqa: E501

        Broadcast to events websocket: /ws/events  # noqa: E501

        :return: The send_ws of this WebRTCEventRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_ws

    @send_ws.setter
    def send_ws(self, send_ws):
        """Sets the send_ws of this WebRTCEventRequest.

        Broadcast to events websocket: /ws/events  # noqa: E501

        :param send_ws: The send_ws of this WebRTCEventRequest.  # noqa: E501
        :type send_ws: bool
        """

        self._send_ws = send_ws

    @property
    def event_name(self):
        """Gets the event_name of this WebRTCEventRequest.  # noqa: E501


        :return: The event_name of this WebRTCEventRequest.  # noqa: E501
        :rtype: WebRTCEventName
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this WebRTCEventRequest.


        :param event_name: The event_name of this WebRTCEventRequest.  # noqa: E501
        :type event_name: WebRTCEventName
        """
        if self.local_vars_configuration.client_side_validation and event_name is None:  # noqa: E501
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def data(self):
        """Gets the data of this WebRTCEventRequest.  # noqa: E501


        :return: The data of this WebRTCEventRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this WebRTCEventRequest.


        :param data: The data of this WebRTCEventRequest.  # noqa: E501
        :type data: dict(str, object)
        """

        self._data = data

    @property
    def send_mqtt(self):
        """Gets the send_mqtt of this WebRTCEventRequest.  # noqa: E501

        Broadcast to mqtt topic: /devices/{device-id}/commands/  # noqa: E501

        :return: The send_mqtt of this WebRTCEventRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_mqtt

    @send_mqtt.setter
    def send_mqtt(self, send_mqtt):
        """Sets the send_mqtt of this WebRTCEventRequest.

        Broadcast to mqtt topic: /devices/{device-id}/commands/  # noqa: E501

        :param send_mqtt: The send_mqtt of this WebRTCEventRequest.  # noqa: E501
        :type send_mqtt: bool
        """

        self._send_mqtt = send_mqtt

    @property
    def device(self):
        """Gets the device of this WebRTCEventRequest.  # noqa: E501


        :return: The device of this WebRTCEventRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this WebRTCEventRequest.


        :param device: The device of this WebRTCEventRequest.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

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
        if not isinstance(other, WebRTCEventRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebRTCEventRequest):
            return True

        return self.to_dict() != other.to_dict()
