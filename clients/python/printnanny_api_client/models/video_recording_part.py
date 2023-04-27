# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.133.4
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


class VideoRecordingPart(object):
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
        'deleted_by_cascade': 'bool',
        'size': 'int',
        'buffer_index': 'int',
        'buffer_runningtime': 'int',
        'file_name': 'str',
        'mp4_file': 'str',
        'sync_start': 'datetime',
        'sync_end': 'datetime',
        'video_recording': 'str',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'deleted_by_cascade': 'deleted_by_cascade',
        'size': 'size',
        'buffer_index': 'buffer_index',
        'buffer_runningtime': 'buffer_runningtime',
        'file_name': 'file_name',
        'mp4_file': 'mp4_file',
        'sync_start': 'sync_start',
        'sync_end': 'sync_end',
        'video_recording': 'video_recording',
        'user': 'user'
    }

    def __init__(self, id=None, deleted_by_cascade=None, size=None, buffer_index=None, buffer_runningtime=None, file_name=None, mp4_file=None, sync_start=None, sync_end=None, video_recording=None, user=None, local_vars_configuration=None):  # noqa: E501
        """VideoRecordingPart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deleted_by_cascade = None
        self._size = None
        self._buffer_index = None
        self._buffer_runningtime = None
        self._file_name = None
        self._mp4_file = None
        self._sync_start = None
        self._sync_end = None
        self._video_recording = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.deleted_by_cascade = deleted_by_cascade
        self.size = size
        self.buffer_index = buffer_index
        self.buffer_runningtime = buffer_runningtime
        self.file_name = file_name
        self.mp4_file = mp4_file
        self.sync_start = sync_start
        self.sync_end = sync_end
        self.video_recording = video_recording
        self.user = user

    @property
    def id(self):
        """Gets the id of this VideoRecordingPart.  # noqa: E501


        :return: The id of this VideoRecordingPart.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VideoRecordingPart.


        :param id: The id of this VideoRecordingPart.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id

    @property
    def deleted_by_cascade(self):
        """Gets the deleted_by_cascade of this VideoRecordingPart.  # noqa: E501


        :return: The deleted_by_cascade of this VideoRecordingPart.  # noqa: E501
        :rtype: bool
        """
        return self._deleted_by_cascade

    @deleted_by_cascade.setter
    def deleted_by_cascade(self, deleted_by_cascade):
        """Sets the deleted_by_cascade of this VideoRecordingPart.


        :param deleted_by_cascade: The deleted_by_cascade of this VideoRecordingPart.  # noqa: E501
        :type deleted_by_cascade: bool
        """
        if self.local_vars_configuration.client_side_validation and deleted_by_cascade is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_by_cascade`, must not be `None`")  # noqa: E501

        self._deleted_by_cascade = deleted_by_cascade

    @property
    def size(self):
        """Gets the size of this VideoRecordingPart.  # noqa: E501


        :return: The size of this VideoRecordingPart.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VideoRecordingPart.


        :param size: The size of this VideoRecordingPart.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._size = size

    @property
    def buffer_index(self):
        """Gets the buffer_index of this VideoRecordingPart.  # noqa: E501


        :return: The buffer_index of this VideoRecordingPart.  # noqa: E501
        :rtype: int
        """
        return self._buffer_index

    @buffer_index.setter
    def buffer_index(self, buffer_index):
        """Sets the buffer_index of this VideoRecordingPart.


        :param buffer_index: The buffer_index of this VideoRecordingPart.  # noqa: E501
        :type buffer_index: int
        """
        if self.local_vars_configuration.client_side_validation and buffer_index is None:  # noqa: E501
            raise ValueError("Invalid value for `buffer_index`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                buffer_index is not None and buffer_index > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `buffer_index`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                buffer_index is not None and buffer_index < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `buffer_index`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._buffer_index = buffer_index

    @property
    def buffer_runningtime(self):
        """Gets the buffer_runningtime of this VideoRecordingPart.  # noqa: E501


        :return: The buffer_runningtime of this VideoRecordingPart.  # noqa: E501
        :rtype: int
        """
        return self._buffer_runningtime

    @buffer_runningtime.setter
    def buffer_runningtime(self, buffer_runningtime):
        """Sets the buffer_runningtime of this VideoRecordingPart.


        :param buffer_runningtime: The buffer_runningtime of this VideoRecordingPart.  # noqa: E501
        :type buffer_runningtime: int
        """
        if self.local_vars_configuration.client_side_validation and buffer_runningtime is None:  # noqa: E501
            raise ValueError("Invalid value for `buffer_runningtime`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                buffer_runningtime is not None and buffer_runningtime > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `buffer_runningtime`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                buffer_runningtime is not None and buffer_runningtime < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `buffer_runningtime`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._buffer_runningtime = buffer_runningtime

    @property
    def file_name(self):
        """Gets the file_name of this VideoRecordingPart.  # noqa: E501


        :return: The file_name of this VideoRecordingPart.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this VideoRecordingPart.


        :param file_name: The file_name of this VideoRecordingPart.  # noqa: E501
        :type file_name: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_name is not None and len(file_name) > 255):
            raise ValueError("Invalid value for `file_name`, length must be less than or equal to `255`")  # noqa: E501

        self._file_name = file_name

    @property
    def mp4_file(self):
        """Gets the mp4_file of this VideoRecordingPart.  # noqa: E501


        :return: The mp4_file of this VideoRecordingPart.  # noqa: E501
        :rtype: str
        """
        return self._mp4_file

    @mp4_file.setter
    def mp4_file(self, mp4_file):
        """Sets the mp4_file of this VideoRecordingPart.


        :param mp4_file: The mp4_file of this VideoRecordingPart.  # noqa: E501
        :type mp4_file: str
        """
        if self.local_vars_configuration.client_side_validation and mp4_file is None:  # noqa: E501
            raise ValueError("Invalid value for `mp4_file`, must not be `None`")  # noqa: E501

        self._mp4_file = mp4_file

    @property
    def sync_start(self):
        """Gets the sync_start of this VideoRecordingPart.  # noqa: E501


        :return: The sync_start of this VideoRecordingPart.  # noqa: E501
        :rtype: datetime
        """
        return self._sync_start

    @sync_start.setter
    def sync_start(self, sync_start):
        """Sets the sync_start of this VideoRecordingPart.


        :param sync_start: The sync_start of this VideoRecordingPart.  # noqa: E501
        :type sync_start: datetime
        """
        if self.local_vars_configuration.client_side_validation and sync_start is None:  # noqa: E501
            raise ValueError("Invalid value for `sync_start`, must not be `None`")  # noqa: E501

        self._sync_start = sync_start

    @property
    def sync_end(self):
        """Gets the sync_end of this VideoRecordingPart.  # noqa: E501


        :return: The sync_end of this VideoRecordingPart.  # noqa: E501
        :rtype: datetime
        """
        return self._sync_end

    @sync_end.setter
    def sync_end(self, sync_end):
        """Sets the sync_end of this VideoRecordingPart.


        :param sync_end: The sync_end of this VideoRecordingPart.  # noqa: E501
        :type sync_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and sync_end is None:  # noqa: E501
            raise ValueError("Invalid value for `sync_end`, must not be `None`")  # noqa: E501

        self._sync_end = sync_end

    @property
    def video_recording(self):
        """Gets the video_recording of this VideoRecordingPart.  # noqa: E501


        :return: The video_recording of this VideoRecordingPart.  # noqa: E501
        :rtype: str
        """
        return self._video_recording

    @video_recording.setter
    def video_recording(self, video_recording):
        """Sets the video_recording of this VideoRecordingPart.


        :param video_recording: The video_recording of this VideoRecordingPart.  # noqa: E501
        :type video_recording: str
        """
        if self.local_vars_configuration.client_side_validation and video_recording is None:  # noqa: E501
            raise ValueError("Invalid value for `video_recording`, must not be `None`")  # noqa: E501

        self._video_recording = video_recording

    @property
    def user(self):
        """Gets the user of this VideoRecordingPart.  # noqa: E501


        :return: The user of this VideoRecordingPart.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VideoRecordingPart.


        :param user: The user of this VideoRecordingPart.  # noqa: E501
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
        if not isinstance(other, VideoRecordingPart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VideoRecordingPart):
            return True

        return self.to_dict() != other.to_dict()
