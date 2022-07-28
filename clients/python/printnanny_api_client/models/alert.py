# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.98.0
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


class Alert(object):
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
        'time': 'str',
        'gcode_file': 'str',
        'print_progress': 'str',
        'time_elapsed': 'str',
        'time_remaining': 'str',
        'manage_device_url': 'str',
        'user': 'int',
        'octoprint_device': 'int',
        'event_type': 'EventTypeEnum',
        'seen': 'bool',
        'sent': 'bool',
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'gcode_file': 'gcode_file',
        'print_progress': 'print_progress',
        'time_elapsed': 'time_elapsed',
        'time_remaining': 'time_remaining',
        'manage_device_url': 'manage_device_url',
        'user': 'user',
        'octoprint_device': 'octoprint_device',
        'event_type': 'event_type',
        'seen': 'seen',
        'sent': 'sent',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'message': 'message'
    }

    def __init__(self, id=None, time=None, gcode_file=None, print_progress=None, time_elapsed=None, time_remaining=None, manage_device_url=None, user=None, octoprint_device=None, event_type=None, seen=None, sent=None, created_dt=None, updated_dt=None, message=None, local_vars_configuration=None):  # noqa: E501
        """Alert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._time = None
        self._gcode_file = None
        self._print_progress = None
        self._time_elapsed = None
        self._time_remaining = None
        self._manage_device_url = None
        self._user = None
        self._octoprint_device = None
        self._event_type = None
        self._seen = None
        self._sent = None
        self._created_dt = None
        self._updated_dt = None
        self._message = None
        self.discriminator = None

        self.id = id
        self.time = time
        self.gcode_file = gcode_file
        self.print_progress = print_progress
        self.time_elapsed = time_elapsed
        self.time_remaining = time_remaining
        self.manage_device_url = manage_device_url
        self.user = user
        self.octoprint_device = octoprint_device
        self.event_type = event_type
        if seen is not None:
            self.seen = seen
        if sent is not None:
            self.sent = sent
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.message = message

    @property
    def id(self):
        """Gets the id of this Alert.  # noqa: E501


        :return: The id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alert.


        :param id: The id of this Alert.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def time(self):
        """Gets the time of this Alert.  # noqa: E501


        :return: The time of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Alert.


        :param time: The time of this Alert.  # noqa: E501
        :type time: str
        """
        if self.local_vars_configuration.client_side_validation and time is None:  # noqa: E501
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def gcode_file(self):
        """Gets the gcode_file of this Alert.  # noqa: E501


        :return: The gcode_file of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._gcode_file

    @gcode_file.setter
    def gcode_file(self, gcode_file):
        """Sets the gcode_file of this Alert.


        :param gcode_file: The gcode_file of this Alert.  # noqa: E501
        :type gcode_file: str
        """
        if self.local_vars_configuration.client_side_validation and gcode_file is None:  # noqa: E501
            raise ValueError("Invalid value for `gcode_file`, must not be `None`")  # noqa: E501

        self._gcode_file = gcode_file

    @property
    def print_progress(self):
        """Gets the print_progress of this Alert.  # noqa: E501


        :return: The print_progress of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._print_progress

    @print_progress.setter
    def print_progress(self, print_progress):
        """Sets the print_progress of this Alert.


        :param print_progress: The print_progress of this Alert.  # noqa: E501
        :type print_progress: str
        """
        if self.local_vars_configuration.client_side_validation and print_progress is None:  # noqa: E501
            raise ValueError("Invalid value for `print_progress`, must not be `None`")  # noqa: E501

        self._print_progress = print_progress

    @property
    def time_elapsed(self):
        """Gets the time_elapsed of this Alert.  # noqa: E501


        :return: The time_elapsed of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._time_elapsed

    @time_elapsed.setter
    def time_elapsed(self, time_elapsed):
        """Sets the time_elapsed of this Alert.


        :param time_elapsed: The time_elapsed of this Alert.  # noqa: E501
        :type time_elapsed: str
        """
        if self.local_vars_configuration.client_side_validation and time_elapsed is None:  # noqa: E501
            raise ValueError("Invalid value for `time_elapsed`, must not be `None`")  # noqa: E501

        self._time_elapsed = time_elapsed

    @property
    def time_remaining(self):
        """Gets the time_remaining of this Alert.  # noqa: E501


        :return: The time_remaining of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this Alert.


        :param time_remaining: The time_remaining of this Alert.  # noqa: E501
        :type time_remaining: str
        """
        if self.local_vars_configuration.client_side_validation and time_remaining is None:  # noqa: E501
            raise ValueError("Invalid value for `time_remaining`, must not be `None`")  # noqa: E501

        self._time_remaining = time_remaining

    @property
    def manage_device_url(self):
        """Gets the manage_device_url of this Alert.  # noqa: E501


        :return: The manage_device_url of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._manage_device_url

    @manage_device_url.setter
    def manage_device_url(self, manage_device_url):
        """Sets the manage_device_url of this Alert.


        :param manage_device_url: The manage_device_url of this Alert.  # noqa: E501
        :type manage_device_url: str
        """

        self._manage_device_url = manage_device_url

    @property
    def user(self):
        """Gets the user of this Alert.  # noqa: E501


        :return: The user of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Alert.


        :param user: The user of this Alert.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this Alert.  # noqa: E501


        :return: The octoprint_device of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this Alert.


        :param octoprint_device: The octoprint_device of this Alert.  # noqa: E501
        :type octoprint_device: int
        """

        self._octoprint_device = octoprint_device

    @property
    def event_type(self):
        """Gets the event_type of this Alert.  # noqa: E501


        :return: The event_type of this Alert.  # noqa: E501
        :rtype: EventTypeEnum
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Alert.


        :param event_type: The event_type of this Alert.  # noqa: E501
        :type event_type: EventTypeEnum
        """

        self._event_type = event_type

    @property
    def seen(self):
        """Gets the seen of this Alert.  # noqa: E501


        :return: The seen of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this Alert.


        :param seen: The seen of this Alert.  # noqa: E501
        :type seen: bool
        """

        self._seen = seen

    @property
    def sent(self):
        """Gets the sent of this Alert.  # noqa: E501


        :return: The sent of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this Alert.


        :param sent: The sent of this Alert.  # noqa: E501
        :type sent: bool
        """

        self._sent = sent

    @property
    def created_dt(self):
        """Gets the created_dt of this Alert.  # noqa: E501


        :return: The created_dt of this Alert.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Alert.


        :param created_dt: The created_dt of this Alert.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this Alert.  # noqa: E501


        :return: The updated_dt of this Alert.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this Alert.


        :param updated_dt: The updated_dt of this Alert.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def message(self):
        """Gets the message of this Alert.  # noqa: E501


        :return: The message of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Alert.


        :param message: The message of this Alert.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, Alert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Alert):
            return True

        return self.to_dict() != other.to_dict()
