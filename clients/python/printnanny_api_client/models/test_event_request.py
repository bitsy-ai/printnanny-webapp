# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.95.0
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


class TestEventRequest(object):
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
        'model': 'TestEventModel',
        'source': 'EventSource',
        'event_name': 'TestEventName',
        'device': 'int'
    }

    attribute_map = {
        'model': 'model',
        'source': 'source',
        'event_name': 'event_name',
        'device': 'device'
    }

    def __init__(self, model=None, source=None, event_name=None, device=None, local_vars_configuration=None):  # noqa: E501
        """TestEventRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._model = None
        self._source = None
        self._event_name = None
        self._device = None
        self.discriminator = None

        self.model = model
        self.source = source
        self.event_name = event_name
        self.device = device

    @property
    def model(self):
        """Gets the model of this TestEventRequest.  # noqa: E501


        :return: The model of this TestEventRequest.  # noqa: E501
        :rtype: TestEventModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this TestEventRequest.


        :param model: The model of this TestEventRequest.  # noqa: E501
        :type model: TestEventModel
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def source(self):
        """Gets the source of this TestEventRequest.  # noqa: E501


        :return: The source of this TestEventRequest.  # noqa: E501
        :rtype: EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TestEventRequest.


        :param source: The source of this TestEventRequest.  # noqa: E501
        :type source: EventSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def event_name(self):
        """Gets the event_name of this TestEventRequest.  # noqa: E501


        :return: The event_name of this TestEventRequest.  # noqa: E501
        :rtype: TestEventName
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this TestEventRequest.


        :param event_name: The event_name of this TestEventRequest.  # noqa: E501
        :type event_name: TestEventName
        """
        if self.local_vars_configuration.client_side_validation and event_name is None:  # noqa: E501
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def device(self):
        """Gets the device of this TestEventRequest.  # noqa: E501


        :return: The device of this TestEventRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this TestEventRequest.


        :param device: The device of this TestEventRequest.  # noqa: E501
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
        if not isinstance(other, TestEventRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestEventRequest):
            return True

        return self.to_dict() != other.to_dict()
