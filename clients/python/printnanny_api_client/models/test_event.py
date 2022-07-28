# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.97.0
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


class TestEvent(object):
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
        'model': 'TestEventModel',
        'created_dt': 'datetime',
        'source': 'EventSource',
        'event_name': 'TestEventName',
        'polymorphic_ctype': 'int',
        'user': 'int',
        'pi': 'int'
    }

    attribute_map = {
        'id': 'id',
        'model': 'model',
        'created_dt': 'created_dt',
        'source': 'source',
        'event_name': 'event_name',
        'polymorphic_ctype': 'polymorphic_ctype',
        'user': 'user',
        'pi': 'pi'
    }

    def __init__(self, id=None, model=None, created_dt=None, source=None, event_name=None, polymorphic_ctype=None, user=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """TestEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._model = None
        self._created_dt = None
        self._source = None
        self._event_name = None
        self._polymorphic_ctype = None
        self._user = None
        self._pi = None
        self.discriminator = None

        self.id = id
        self.model = model
        self.created_dt = created_dt
        self.source = source
        self.event_name = event_name
        self.polymorphic_ctype = polymorphic_ctype
        self.user = user
        self.pi = pi

    @property
    def id(self):
        """Gets the id of this TestEvent.  # noqa: E501


        :return: The id of this TestEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestEvent.


        :param id: The id of this TestEvent.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def model(self):
        """Gets the model of this TestEvent.  # noqa: E501


        :return: The model of this TestEvent.  # noqa: E501
        :rtype: TestEventModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this TestEvent.


        :param model: The model of this TestEvent.  # noqa: E501
        :type model: TestEventModel
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def created_dt(self):
        """Gets the created_dt of this TestEvent.  # noqa: E501


        :return: The created_dt of this TestEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this TestEvent.


        :param created_dt: The created_dt of this TestEvent.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def source(self):
        """Gets the source of this TestEvent.  # noqa: E501


        :return: The source of this TestEvent.  # noqa: E501
        :rtype: EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TestEvent.


        :param source: The source of this TestEvent.  # noqa: E501
        :type source: EventSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def event_name(self):
        """Gets the event_name of this TestEvent.  # noqa: E501


        :return: The event_name of this TestEvent.  # noqa: E501
        :rtype: TestEventName
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this TestEvent.


        :param event_name: The event_name of this TestEvent.  # noqa: E501
        :type event_name: TestEventName
        """
        if self.local_vars_configuration.client_side_validation and event_name is None:  # noqa: E501
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this TestEvent.  # noqa: E501


        :return: The polymorphic_ctype of this TestEvent.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this TestEvent.


        :param polymorphic_ctype: The polymorphic_ctype of this TestEvent.  # noqa: E501
        :type polymorphic_ctype: int
        """
        if self.local_vars_configuration.client_side_validation and polymorphic_ctype is None:  # noqa: E501
            raise ValueError("Invalid value for `polymorphic_ctype`, must not be `None`")  # noqa: E501

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def user(self):
        """Gets the user of this TestEvent.  # noqa: E501


        :return: The user of this TestEvent.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TestEvent.


        :param user: The user of this TestEvent.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def pi(self):
        """Gets the pi of this TestEvent.  # noqa: E501


        :return: The pi of this TestEvent.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this TestEvent.


        :param pi: The pi of this TestEvent.  # noqa: E501
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
        if not isinstance(other, TestEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestEvent):
            return True

        return self.to_dict() != other.to_dict()
