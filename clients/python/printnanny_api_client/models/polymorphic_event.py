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
        'type': 'TestEventType',
        'status': 'EventStatus',
        'resourcetype': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'resourcetype': 'resourcetype'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, id=None, type=None, status=None, resourcetype='TestEvent', local_vars_configuration=None):  # noqa: E501
        """PolymorphicEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._status = None
        self._resourcetype = None
        self.discriminator = 'resourcetype'

        self.id = id
        self.type = type
        if status is not None:
            self.status = status
        if resourcetype is not None:
            self.resourcetype = resourcetype

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
    def type(self):
        """Gets the type of this PolymorphicEvent.  # noqa: E501


        :return: The type of this PolymorphicEvent.  # noqa: E501
        :rtype: TestEventType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolymorphicEvent.


        :param type: The type of this PolymorphicEvent.  # noqa: E501
        :type type: TestEventType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this PolymorphicEvent.  # noqa: E501


        :return: The status of this PolymorphicEvent.  # noqa: E501
        :rtype: EventStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolymorphicEvent.


        :param status: The status of this PolymorphicEvent.  # noqa: E501
        :type status: EventStatus
        """

        self._status = status

    @property
    def resourcetype(self):
        """Gets the resourcetype of this PolymorphicEvent.  # noqa: E501


        :return: The resourcetype of this PolymorphicEvent.  # noqa: E501
        :rtype: str
        """
        return self._resourcetype

    @resourcetype.setter
    def resourcetype(self, resourcetype):
        """Sets the resourcetype of this PolymorphicEvent.


        :param resourcetype: The resourcetype of this PolymorphicEvent.  # noqa: E501
        :type resourcetype: str
        """

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
        if not isinstance(other, PolymorphicEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolymorphicEvent):
            return True

        return self.to_dict() != other.to_dict()
