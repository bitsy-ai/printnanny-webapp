# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
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


class PolymorphicEvent(object):
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
        'event_type': 'TestEventEventTypeEnum',
        'stream': 'JanusStream',
        'created_dt': 'datetime',
        'source': 'EventSource',
        'send_ws': 'bool',
        'event_name': 'TestEventName',
        'data': 'dict(str, object)',
        'send_mqtt': 'bool',
        'polymorphic_ctype': 'int',
        'user': 'int',
        'device': 'int'
    }

    attribute_map = {
        'id': 'id',
        'event_type': 'event_type',
        'stream': 'stream',
        'created_dt': 'created_dt',
        'source': 'source',
        'send_ws': 'send_ws',
        'event_name': 'event_name',
        'data': 'data',
        'send_mqtt': 'send_mqtt',
        'polymorphic_ctype': 'polymorphic_ctype',
        'user': 'user',
        'device': 'device'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, id=None, event_type=None, stream=None, created_dt=None, source=None, send_ws=None, event_name=None, data=None, send_mqtt=None, polymorphic_ctype=None, user=None, device=None, local_vars_configuration=None):  # noqa: E501
        """PolymorphicEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._event_type = None
        self._stream = None
        self._created_dt = None
        self._source = None
        self._send_ws = None
        self._event_name = None
        self._data = None
        self._send_mqtt = None
        self._polymorphic_ctype = None
        self._user = None
        self._device = None
        self.discriminator = 'event_type'

        self.id = id
        self.event_type = event_type
        self.stream = stream
        self.created_dt = created_dt
        self.source = source
        if send_ws is not None:
            self.send_ws = send_ws
        self.event_name = event_name
        if data is not None:
            self.data = data
        if send_mqtt is not None:
            self.send_mqtt = send_mqtt
        self.polymorphic_ctype = polymorphic_ctype
        self.user = user
        self.device = device

    @property
    def id(self):
        """Gets the id of this PolymorphicEvent.  # noqa: E501


        :return: The id of this PolymorphicEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolymorphicEvent.


        :param id: The id of this PolymorphicEvent.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def event_type(self):
        """Gets the event_type of this PolymorphicEvent.  # noqa: E501


        :return: The event_type of this PolymorphicEvent.  # noqa: E501
        :rtype: TestEventEventTypeEnum
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PolymorphicEvent.


        :param event_type: The event_type of this PolymorphicEvent.  # noqa: E501
        :type event_type: TestEventEventTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def stream(self):
        """Gets the stream of this PolymorphicEvent.  # noqa: E501


        :return: The stream of this PolymorphicEvent.  # noqa: E501
        :rtype: JanusStream
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this PolymorphicEvent.


        :param stream: The stream of this PolymorphicEvent.  # noqa: E501
        :type stream: JanusStream
        """

        self._stream = stream

    @property
    def created_dt(self):
        """Gets the created_dt of this PolymorphicEvent.  # noqa: E501


        :return: The created_dt of this PolymorphicEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PolymorphicEvent.


        :param created_dt: The created_dt of this PolymorphicEvent.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def source(self):
        """Gets the source of this PolymorphicEvent.  # noqa: E501


        :return: The source of this PolymorphicEvent.  # noqa: E501
        :rtype: EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PolymorphicEvent.


        :param source: The source of this PolymorphicEvent.  # noqa: E501
        :type source: EventSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def send_ws(self):
        """Gets the send_ws of this PolymorphicEvent.  # noqa: E501

        Broadcast to events websocket: /ws/events  # noqa: E501

        :return: The send_ws of this PolymorphicEvent.  # noqa: E501
        :rtype: bool
        """
        return self._send_ws

    @send_ws.setter
    def send_ws(self, send_ws):
        """Sets the send_ws of this PolymorphicEvent.

        Broadcast to events websocket: /ws/events  # noqa: E501

        :param send_ws: The send_ws of this PolymorphicEvent.  # noqa: E501
        :type send_ws: bool
        """

        self._send_ws = send_ws

    @property
    def event_name(self):
        """Gets the event_name of this PolymorphicEvent.  # noqa: E501


        :return: The event_name of this PolymorphicEvent.  # noqa: E501
        :rtype: TestEventName
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this PolymorphicEvent.


        :param event_name: The event_name of this PolymorphicEvent.  # noqa: E501
        :type event_name: TestEventName
        """
        if self.local_vars_configuration.client_side_validation and event_name is None:  # noqa: E501
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def data(self):
        """Gets the data of this PolymorphicEvent.  # noqa: E501


        :return: The data of this PolymorphicEvent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PolymorphicEvent.


        :param data: The data of this PolymorphicEvent.  # noqa: E501
        :type data: dict(str, object)
        """

        self._data = data

    @property
    def send_mqtt(self):
        """Gets the send_mqtt of this PolymorphicEvent.  # noqa: E501

        Broadcast to mqtt topic: /devices/{device-id}/commands/  # noqa: E501

        :return: The send_mqtt of this PolymorphicEvent.  # noqa: E501
        :rtype: bool
        """
        return self._send_mqtt

    @send_mqtt.setter
    def send_mqtt(self, send_mqtt):
        """Sets the send_mqtt of this PolymorphicEvent.

        Broadcast to mqtt topic: /devices/{device-id}/commands/  # noqa: E501

        :param send_mqtt: The send_mqtt of this PolymorphicEvent.  # noqa: E501
        :type send_mqtt: bool
        """

        self._send_mqtt = send_mqtt

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this PolymorphicEvent.  # noqa: E501


        :return: The polymorphic_ctype of this PolymorphicEvent.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this PolymorphicEvent.


        :param polymorphic_ctype: The polymorphic_ctype of this PolymorphicEvent.  # noqa: E501
        :type polymorphic_ctype: int
        """
        if self.local_vars_configuration.client_side_validation and polymorphic_ctype is None:  # noqa: E501
            raise ValueError("Invalid value for `polymorphic_ctype`, must not be `None`")  # noqa: E501

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def user(self):
        """Gets the user of this PolymorphicEvent.  # noqa: E501


        :return: The user of this PolymorphicEvent.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PolymorphicEvent.


        :param user: The user of this PolymorphicEvent.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def device(self):
        """Gets the device of this PolymorphicEvent.  # noqa: E501


        :return: The device of this PolymorphicEvent.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PolymorphicEvent.


        :param device: The device of this PolymorphicEvent.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

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
        if not isinstance(other, PolymorphicEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolymorphicEvent):
            return True

        return self.to_dict() != other.to_dict()
