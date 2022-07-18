# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

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


class PolymorphicCommandCreateRequest(object):
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
        'model': 'WebRTCCommandModel',
        'source': 'EventSource',
        'event_name': 'WebRTCCommandName',
        'data': 'dict(str, object)',
        'device': 'int',
        'stream': 'int'
    }

    attribute_map = {
        'model': 'model',
        'source': 'source',
        'event_name': 'event_name',
        'data': 'data',
        'device': 'device',
        'stream': 'stream'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, model=None, source=None, event_name=None, data=None, device=None, stream=None, local_vars_configuration=None):  # noqa: E501
        """PolymorphicCommandCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._model = None
        self._source = None
        self._event_name = None
        self._data = None
        self._device = None
        self._stream = None
        self.discriminator = 'model'

        self.model = model
        self.source = source
        self.event_name = event_name
        if data is not None:
            self.data = data
        self.device = device
        self.stream = stream

    @property
    def model(self):
        """Gets the model of this PolymorphicCommandCreateRequest.  # noqa: E501


        :return: The model of this PolymorphicCommandCreateRequest.  # noqa: E501
        :rtype: WebRTCCommandModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PolymorphicCommandCreateRequest.


        :param model: The model of this PolymorphicCommandCreateRequest.  # noqa: E501
        :type model: WebRTCCommandModel
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def source(self):
        """Gets the source of this PolymorphicCommandCreateRequest.  # noqa: E501


        :return: The source of this PolymorphicCommandCreateRequest.  # noqa: E501
        :rtype: EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PolymorphicCommandCreateRequest.


        :param source: The source of this PolymorphicCommandCreateRequest.  # noqa: E501
        :type source: EventSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def event_name(self):
        """Gets the event_name of this PolymorphicCommandCreateRequest.  # noqa: E501


        :return: The event_name of this PolymorphicCommandCreateRequest.  # noqa: E501
        :rtype: WebRTCCommandName
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this PolymorphicCommandCreateRequest.


        :param event_name: The event_name of this PolymorphicCommandCreateRequest.  # noqa: E501
        :type event_name: WebRTCCommandName
        """
        if self.local_vars_configuration.client_side_validation and event_name is None:  # noqa: E501
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def data(self):
        """Gets the data of this PolymorphicCommandCreateRequest.  # noqa: E501


        :return: The data of this PolymorphicCommandCreateRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PolymorphicCommandCreateRequest.


        :param data: The data of this PolymorphicCommandCreateRequest.  # noqa: E501
        :type data: dict(str, object)
        """

        self._data = data

    @property
    def device(self):
        """Gets the device of this PolymorphicCommandCreateRequest.  # noqa: E501


        :return: The device of this PolymorphicCommandCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PolymorphicCommandCreateRequest.


        :param device: The device of this PolymorphicCommandCreateRequest.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def stream(self):
        """Gets the stream of this PolymorphicCommandCreateRequest.  # noqa: E501


        :return: The stream of this PolymorphicCommandCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this PolymorphicCommandCreateRequest.


        :param stream: The stream of this PolymorphicCommandCreateRequest.  # noqa: E501
        :type stream: int
        """
        if self.local_vars_configuration.client_side_validation and stream is None:  # noqa: E501
            raise ValueError("Invalid value for `stream`, must not be `None`")  # noqa: E501

        self._stream = stream

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
        if not isinstance(other, PolymorphicCommandCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolymorphicCommandCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
