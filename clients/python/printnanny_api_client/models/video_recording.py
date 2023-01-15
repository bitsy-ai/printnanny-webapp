# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.1
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


class VideoRecording(object):
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
        'mjr_upload_url': 'str',
        'start_dt': 'datetime',
        'end_dt': 'datetime',
        'name': 'str',
        'mjr_recording': 'str',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'mjr_upload_url': 'mjr_upload_url',
        'start_dt': 'start_dt',
        'end_dt': 'end_dt',
        'name': 'name',
        'mjr_recording': 'mjr_recording',
        'user': 'user'
    }

    def __init__(self, id=None, mjr_upload_url=None, start_dt=None, end_dt=None, name=None, mjr_recording=None, user=None, local_vars_configuration=None):  # noqa: E501
        """VideoRecording - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._mjr_upload_url = None
        self._start_dt = None
        self._end_dt = None
        self._name = None
        self._mjr_recording = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.mjr_upload_url = mjr_upload_url
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.name = name
        self.mjr_recording = mjr_recording
        self.user = user

    @property
    def id(self):
        """Gets the id of this VideoRecording.  # noqa: E501


        :return: The id of this VideoRecording.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VideoRecording.


        :param id: The id of this VideoRecording.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def mjr_upload_url(self):
        """Gets the mjr_upload_url of this VideoRecording.  # noqa: E501


        :return: The mjr_upload_url of this VideoRecording.  # noqa: E501
        :rtype: str
        """
        return self._mjr_upload_url

    @mjr_upload_url.setter
    def mjr_upload_url(self, mjr_upload_url):
        """Sets the mjr_upload_url of this VideoRecording.


        :param mjr_upload_url: The mjr_upload_url of this VideoRecording.  # noqa: E501
        :type mjr_upload_url: str
        """
        if self.local_vars_configuration.client_side_validation and mjr_upload_url is None:  # noqa: E501
            raise ValueError("Invalid value for `mjr_upload_url`, must not be `None`")  # noqa: E501

        self._mjr_upload_url = mjr_upload_url

    @property
    def start_dt(self):
        """Gets the start_dt of this VideoRecording.  # noqa: E501


        :return: The start_dt of this VideoRecording.  # noqa: E501
        :rtype: datetime
        """
        return self._start_dt

    @start_dt.setter
    def start_dt(self, start_dt):
        """Sets the start_dt of this VideoRecording.


        :param start_dt: The start_dt of this VideoRecording.  # noqa: E501
        :type start_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `start_dt`, must not be `None`")  # noqa: E501

        self._start_dt = start_dt

    @property
    def end_dt(self):
        """Gets the end_dt of this VideoRecording.  # noqa: E501


        :return: The end_dt of this VideoRecording.  # noqa: E501
        :rtype: datetime
        """
        return self._end_dt

    @end_dt.setter
    def end_dt(self, end_dt):
        """Sets the end_dt of this VideoRecording.


        :param end_dt: The end_dt of this VideoRecording.  # noqa: E501
        :type end_dt: datetime
        """

        self._end_dt = end_dt

    @property
    def name(self):
        """Gets the name of this VideoRecording.  # noqa: E501


        :return: The name of this VideoRecording.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VideoRecording.


        :param name: The name of this VideoRecording.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def mjr_recording(self):
        """Gets the mjr_recording of this VideoRecording.  # noqa: E501


        :return: The mjr_recording of this VideoRecording.  # noqa: E501
        :rtype: str
        """
        return self._mjr_recording

    @mjr_recording.setter
    def mjr_recording(self, mjr_recording):
        """Sets the mjr_recording of this VideoRecording.


        :param mjr_recording: The mjr_recording of this VideoRecording.  # noqa: E501
        :type mjr_recording: str
        """

        self._mjr_recording = mjr_recording

    @property
    def user(self):
        """Gets the user of this VideoRecording.  # noqa: E501


        :return: The user of this VideoRecording.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VideoRecording.


        :param user: The user of this VideoRecording.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, VideoRecording):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VideoRecording):
            return True

        return self.to_dict() != other.to_dict()
