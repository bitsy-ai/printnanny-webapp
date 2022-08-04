# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.7
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


class PiGstreamerCommand(object):
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
        'subject': 'str',
        'payload': 'dict(str, object)',
        'event_type': 'PiGstreamerCommandType',
        'polymorphic_ctype': 'int',
        'pi': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'subject': 'subject',
        'payload': 'payload',
        'event_type': 'event_type',
        'polymorphic_ctype': 'polymorphic_ctype',
        'pi': 'pi'
    }

    def __init__(self, id=None, created_dt=None, subject=None, payload=None, event_type=None, polymorphic_ctype=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """PiGstreamerCommand - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._subject = None
        self._payload = None
        self._event_type = None
        self._polymorphic_ctype = None
        self._pi = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.subject = subject
        if payload is not None:
            self.payload = payload
        self.event_type = event_type
        self.polymorphic_ctype = polymorphic_ctype
        self.pi = pi

    @property
    def id(self):
        """Gets the id of this PiGstreamerCommand.  # noqa: E501


        :return: The id of this PiGstreamerCommand.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PiGstreamerCommand.


        :param id: The id of this PiGstreamerCommand.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this PiGstreamerCommand.  # noqa: E501


        :return: The created_dt of this PiGstreamerCommand.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PiGstreamerCommand.


        :param created_dt: The created_dt of this PiGstreamerCommand.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def subject(self):
        """Gets the subject of this PiGstreamerCommand.  # noqa: E501


        :return: The subject of this PiGstreamerCommand.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PiGstreamerCommand.


        :param subject: The subject of this PiGstreamerCommand.  # noqa: E501
        :type subject: str
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) > 255):
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `255`")  # noqa: E501

        self._subject = subject

    @property
    def payload(self):
        """Gets the payload of this PiGstreamerCommand.  # noqa: E501


        :return: The payload of this PiGstreamerCommand.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this PiGstreamerCommand.


        :param payload: The payload of this PiGstreamerCommand.  # noqa: E501
        :type payload: dict(str, object)
        """

        self._payload = payload

    @property
    def event_type(self):
        """Gets the event_type of this PiGstreamerCommand.  # noqa: E501


        :return: The event_type of this PiGstreamerCommand.  # noqa: E501
        :rtype: PiGstreamerCommandType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PiGstreamerCommand.


        :param event_type: The event_type of this PiGstreamerCommand.  # noqa: E501
        :type event_type: PiGstreamerCommandType
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this PiGstreamerCommand.  # noqa: E501


        :return: The polymorphic_ctype of this PiGstreamerCommand.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this PiGstreamerCommand.


        :param polymorphic_ctype: The polymorphic_ctype of this PiGstreamerCommand.  # noqa: E501
        :type polymorphic_ctype: int
        """
        if self.local_vars_configuration.client_side_validation and polymorphic_ctype is None:  # noqa: E501
            raise ValueError("Invalid value for `polymorphic_ctype`, must not be `None`")  # noqa: E501

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def pi(self):
        """Gets the pi of this PiGstreamerCommand.  # noqa: E501


        :return: The pi of this PiGstreamerCommand.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PiGstreamerCommand.


        :param pi: The pi of this PiGstreamerCommand.  # noqa: E501
        :type pi: int
        """
        if self.local_vars_configuration.client_side_validation and pi is None:  # noqa: E501
            raise ValueError("Invalid value for `pi`, must not be `None`")  # noqa: E501

        self._pi = pi

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
        if not isinstance(other, PiGstreamerCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PiGstreamerCommand):
            return True

        return self.to_dict() != other.to_dict()
