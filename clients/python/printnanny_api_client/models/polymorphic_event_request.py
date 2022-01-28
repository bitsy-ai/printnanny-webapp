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


class PolymorphicEventRequest(object):
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
        'type': 'TestEventType',
        'status': 'EventStatus',
        'source': 'EventSource',
        'resourcetype': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'source': 'source',
        'resourcetype': 'resourcetype'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, type=None, status=None, source=None, resourcetype='TestEvent', local_vars_configuration=None):  # noqa: E501
        """PolymorphicEventRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._status = None
        self._source = None
        self._resourcetype = None
        self.discriminator = 'resourcetype'

        self.type = type
        if status is not None:
            self.status = status
        self.source = source
        if resourcetype is not None:
            self.resourcetype = resourcetype

    @property
    def type(self):
        """Gets the type of this PolymorphicEventRequest.  # noqa: E501


        :return: The type of this PolymorphicEventRequest.  # noqa: E501
        :rtype: TestEventType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolymorphicEventRequest.


        :param type: The type of this PolymorphicEventRequest.  # noqa: E501
        :type type: TestEventType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this PolymorphicEventRequest.  # noqa: E501


        :return: The status of this PolymorphicEventRequest.  # noqa: E501
        :rtype: EventStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolymorphicEventRequest.


        :param status: The status of this PolymorphicEventRequest.  # noqa: E501
        :type status: EventStatus
        """

        self._status = status

    @property
    def source(self):
        """Gets the source of this PolymorphicEventRequest.  # noqa: E501


        :return: The source of this PolymorphicEventRequest.  # noqa: E501
        :rtype: EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PolymorphicEventRequest.


        :param source: The source of this PolymorphicEventRequest.  # noqa: E501
        :type source: EventSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def resourcetype(self):
        """Gets the resourcetype of this PolymorphicEventRequest.  # noqa: E501


        :return: The resourcetype of this PolymorphicEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._resourcetype

    @resourcetype.setter
    def resourcetype(self, resourcetype):
        """Sets the resourcetype of this PolymorphicEventRequest.


        :param resourcetype: The resourcetype of this PolymorphicEventRequest.  # noqa: E501
        :type resourcetype: str
        """
        if (self.local_vars_configuration.client_side_validation and
                resourcetype is not None and len(resourcetype) < 1):
            raise ValueError("Invalid value for `resourcetype`, length must be greater than or equal to `1`")  # noqa: E501

        self._resourcetype = resourcetype

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
        if not isinstance(other, PolymorphicEventRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolymorphicEventRequest):
            return True

        return self.to_dict() != other.to_dict()
