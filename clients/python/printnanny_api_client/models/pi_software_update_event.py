# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.3
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


class PiSoftwareUpdateEvent(object):
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
        'source': 'SourceEnum',
        'subject': 'str',
        'payload': 'dict(str, object)',
        'version': 'str',
        'event_type': 'PiSoftwareUpdateEventType',
        'polymorphic_ctype': 'int',
        'pi': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'source': 'source',
        'subject': 'subject',
        'payload': 'payload',
        'version': 'version',
        'event_type': 'event_type',
        'polymorphic_ctype': 'polymorphic_ctype',
        'pi': 'pi'
    }

    def __init__(self, id=None, created_dt=None, source=None, subject=None, payload=None, version=None, event_type=None, polymorphic_ctype=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """PiSoftwareUpdateEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._source = None
        self._subject = None
        self._payload = None
        self._version = None
        self._event_type = None
        self._polymorphic_ctype = None
        self._pi = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.source = source
        self.subject = subject
        if payload is not None:
            self.payload = payload
        self.version = version
        self.event_type = event_type
        self.polymorphic_ctype = polymorphic_ctype
        self.pi = pi

    @property
    def id(self):
        """Gets the id of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The id of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PiSoftwareUpdateEvent.


        :param id: The id of this PiSoftwareUpdateEvent.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The created_dt of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PiSoftwareUpdateEvent.


        :param created_dt: The created_dt of this PiSoftwareUpdateEvent.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def source(self):
        """Gets the source of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The source of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: SourceEnum
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PiSoftwareUpdateEvent.


        :param source: The source of this PiSoftwareUpdateEvent.  # noqa: E501
        :type source: SourceEnum
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def subject(self):
        """Gets the subject of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The subject of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PiSoftwareUpdateEvent.


        :param subject: The subject of this PiSoftwareUpdateEvent.  # noqa: E501
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
        """Gets the payload of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The payload of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this PiSoftwareUpdateEvent.


        :param payload: The payload of this PiSoftwareUpdateEvent.  # noqa: E501
        :type payload: dict(str, object)
        """

        self._payload = payload

    @property
    def version(self):
        """Gets the version of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The version of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PiSoftwareUpdateEvent.


        :param version: The version of this PiSoftwareUpdateEvent.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 32):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `32`")  # noqa: E501

        self._version = version

    @property
    def event_type(self):
        """Gets the event_type of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The event_type of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: PiSoftwareUpdateEventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PiSoftwareUpdateEvent.


        :param event_type: The event_type of this PiSoftwareUpdateEvent.  # noqa: E501
        :type event_type: PiSoftwareUpdateEventType
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The polymorphic_ctype of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this PiSoftwareUpdateEvent.


        :param polymorphic_ctype: The polymorphic_ctype of this PiSoftwareUpdateEvent.  # noqa: E501
        :type polymorphic_ctype: int
        """
        if self.local_vars_configuration.client_side_validation and polymorphic_ctype is None:  # noqa: E501
            raise ValueError("Invalid value for `polymorphic_ctype`, must not be `None`")  # noqa: E501

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def pi(self):
        """Gets the pi of this PiSoftwareUpdateEvent.  # noqa: E501


        :return: The pi of this PiSoftwareUpdateEvent.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PiSoftwareUpdateEvent.


        :param pi: The pi of this PiSoftwareUpdateEvent.  # noqa: E501
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
        if not isinstance(other, PiSoftwareUpdateEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PiSoftwareUpdateEvent):
            return True

        return self.to_dict() != other.to_dict()
