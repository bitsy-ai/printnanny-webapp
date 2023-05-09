# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.134.2
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


class PrintJobAlert(object):
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
        'id': 'str',
        'created_dt': 'datetime',
        'event_type': 'EventTypeEnum',
        'event_source': 'EventSourceEnum',
        'payload': 'dict(str, object)',
        'email_message_id': 'str',
        'celery_task_id': 'str',
        'user': 'int',
        'pi': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'event_type': 'event_type',
        'event_source': 'event_source',
        'payload': 'payload',
        'email_message_id': 'email_message_id',
        'celery_task_id': 'celery_task_id',
        'user': 'user',
        'pi': 'pi'
    }

    def __init__(self, id=None, created_dt=None, event_type=None, event_source=None, payload=None, email_message_id=None, celery_task_id=None, user=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """PrintJobAlert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._event_type = None
        self._event_source = None
        self._payload = None
        self._email_message_id = None
        self._celery_task_id = None
        self._user = None
        self._pi = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.event_type = event_type
        self.event_source = event_source
        self.payload = payload
        self.email_message_id = email_message_id
        self.celery_task_id = celery_task_id
        self.user = user
        self.pi = pi

    @property
    def id(self):
        """Gets the id of this PrintJobAlert.  # noqa: E501


        :return: The id of this PrintJobAlert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrintJobAlert.


        :param id: The id of this PrintJobAlert.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this PrintJobAlert.  # noqa: E501


        :return: The created_dt of this PrintJobAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PrintJobAlert.


        :param created_dt: The created_dt of this PrintJobAlert.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def event_type(self):
        """Gets the event_type of this PrintJobAlert.  # noqa: E501


        :return: The event_type of this PrintJobAlert.  # noqa: E501
        :rtype: EventTypeEnum
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PrintJobAlert.


        :param event_type: The event_type of this PrintJobAlert.  # noqa: E501
        :type event_type: EventTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def event_source(self):
        """Gets the event_source of this PrintJobAlert.  # noqa: E501


        :return: The event_source of this PrintJobAlert.  # noqa: E501
        :rtype: EventSourceEnum
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this PrintJobAlert.


        :param event_source: The event_source of this PrintJobAlert.  # noqa: E501
        :type event_source: EventSourceEnum
        """
        if self.local_vars_configuration.client_side_validation and event_source is None:  # noqa: E501
            raise ValueError("Invalid value for `event_source`, must not be `None`")  # noqa: E501

        self._event_source = event_source

    @property
    def payload(self):
        """Gets the payload of this PrintJobAlert.  # noqa: E501


        :return: The payload of this PrintJobAlert.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this PrintJobAlert.


        :param payload: The payload of this PrintJobAlert.  # noqa: E501
        :type payload: dict(str, object)
        """

        self._payload = payload

    @property
    def email_message_id(self):
        """Gets the email_message_id of this PrintJobAlert.  # noqa: E501


        :return: The email_message_id of this PrintJobAlert.  # noqa: E501
        :rtype: str
        """
        return self._email_message_id

    @email_message_id.setter
    def email_message_id(self, email_message_id):
        """Sets the email_message_id of this PrintJobAlert.


        :param email_message_id: The email_message_id of this PrintJobAlert.  # noqa: E501
        :type email_message_id: str
        """

        self._email_message_id = email_message_id

    @property
    def celery_task_id(self):
        """Gets the celery_task_id of this PrintJobAlert.  # noqa: E501


        :return: The celery_task_id of this PrintJobAlert.  # noqa: E501
        :rtype: str
        """
        return self._celery_task_id

    @celery_task_id.setter
    def celery_task_id(self, celery_task_id):
        """Sets the celery_task_id of this PrintJobAlert.


        :param celery_task_id: The celery_task_id of this PrintJobAlert.  # noqa: E501
        :type celery_task_id: str
        """

        self._celery_task_id = celery_task_id

    @property
    def user(self):
        """Gets the user of this PrintJobAlert.  # noqa: E501


        :return: The user of this PrintJobAlert.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PrintJobAlert.


        :param user: The user of this PrintJobAlert.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def pi(self):
        """Gets the pi of this PrintJobAlert.  # noqa: E501


        :return: The pi of this PrintJobAlert.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PrintJobAlert.


        :param pi: The pi of this PrintJobAlert.  # noqa: E501
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
        if not isinstance(other, PrintJobAlert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintJobAlert):
            return True

        return self.to_dict() != other.to_dict()
