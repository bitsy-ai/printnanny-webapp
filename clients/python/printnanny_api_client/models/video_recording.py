# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.132.1
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
        'id': 'str',
        'mp4_size': 'int',
        'cloud_sync_done': 'bool',
        'finalize_start': 'datetime',
        'finalize_end': 'datetime',
        'finalize_task_id': 'str',
        'recording_start': 'datetime',
        'recording_end': 'datetime',
        'gcode_file_name': 'str',
        'mp4_file': 'str',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'mp4_size': 'mp4_size',
        'cloud_sync_done': 'cloud_sync_done',
        'finalize_start': 'finalize_start',
        'finalize_end': 'finalize_end',
        'finalize_task_id': 'finalize_task_id',
        'recording_start': 'recording_start',
        'recording_end': 'recording_end',
        'gcode_file_name': 'gcode_file_name',
        'mp4_file': 'mp4_file',
        'user': 'user'
    }

    def __init__(self, id=None, mp4_size=None, cloud_sync_done=None, finalize_start=None, finalize_end=None, finalize_task_id=None, recording_start=None, recording_end=None, gcode_file_name=None, mp4_file=None, user=None, local_vars_configuration=None):  # noqa: E501
        """VideoRecording - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._mp4_size = None
        self._cloud_sync_done = None
        self._finalize_start = None
        self._finalize_end = None
        self._finalize_task_id = None
        self._recording_start = None
        self._recording_end = None
        self._gcode_file_name = None
        self._mp4_file = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.mp4_size = mp4_size
        if cloud_sync_done is not None:
            self.cloud_sync_done = cloud_sync_done
        self.finalize_start = finalize_start
        self.finalize_end = finalize_end
        self.finalize_task_id = finalize_task_id
        self.recording_start = recording_start
        self.recording_end = recording_end
        self.gcode_file_name = gcode_file_name
        self.mp4_file = mp4_file
        self.user = user

    @property
    def id(self):
        """Gets the id of this VideoRecording.  # noqa: E501


        :return: The id of this VideoRecording.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VideoRecording.


        :param id: The id of this VideoRecording.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def mp4_size(self):
        """Gets the mp4_size of this VideoRecording.  # noqa: E501


        :return: The mp4_size of this VideoRecording.  # noqa: E501
        :rtype: int
        """
        return self._mp4_size

    @mp4_size.setter
    def mp4_size(self, mp4_size):
        """Sets the mp4_size of this VideoRecording.


        :param mp4_size: The mp4_size of this VideoRecording.  # noqa: E501
        :type mp4_size: int
        """

        self._mp4_size = mp4_size

    @property
    def cloud_sync_done(self):
        """Gets the cloud_sync_done of this VideoRecording.  # noqa: E501


        :return: The cloud_sync_done of this VideoRecording.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_sync_done

    @cloud_sync_done.setter
    def cloud_sync_done(self, cloud_sync_done):
        """Sets the cloud_sync_done of this VideoRecording.


        :param cloud_sync_done: The cloud_sync_done of this VideoRecording.  # noqa: E501
        :type cloud_sync_done: bool
        """

        self._cloud_sync_done = cloud_sync_done

    @property
    def finalize_start(self):
        """Gets the finalize_start of this VideoRecording.  # noqa: E501


        :return: The finalize_start of this VideoRecording.  # noqa: E501
        :rtype: datetime
        """
        return self._finalize_start

    @finalize_start.setter
    def finalize_start(self, finalize_start):
        """Sets the finalize_start of this VideoRecording.


        :param finalize_start: The finalize_start of this VideoRecording.  # noqa: E501
        :type finalize_start: datetime
        """

        self._finalize_start = finalize_start

    @property
    def finalize_end(self):
        """Gets the finalize_end of this VideoRecording.  # noqa: E501


        :return: The finalize_end of this VideoRecording.  # noqa: E501
        :rtype: datetime
        """
        return self._finalize_end

    @finalize_end.setter
    def finalize_end(self, finalize_end):
        """Sets the finalize_end of this VideoRecording.


        :param finalize_end: The finalize_end of this VideoRecording.  # noqa: E501
        :type finalize_end: datetime
        """

        self._finalize_end = finalize_end

    @property
    def finalize_task_id(self):
        """Gets the finalize_task_id of this VideoRecording.  # noqa: E501


        :return: The finalize_task_id of this VideoRecording.  # noqa: E501
        :rtype: str
        """
        return self._finalize_task_id

    @finalize_task_id.setter
    def finalize_task_id(self, finalize_task_id):
        """Sets the finalize_task_id of this VideoRecording.


        :param finalize_task_id: The finalize_task_id of this VideoRecording.  # noqa: E501
        :type finalize_task_id: str
        """

        self._finalize_task_id = finalize_task_id

    @property
    def recording_start(self):
        """Gets the recording_start of this VideoRecording.  # noqa: E501


        :return: The recording_start of this VideoRecording.  # noqa: E501
        :rtype: datetime
        """
        return self._recording_start

    @recording_start.setter
    def recording_start(self, recording_start):
        """Sets the recording_start of this VideoRecording.


        :param recording_start: The recording_start of this VideoRecording.  # noqa: E501
        :type recording_start: datetime
        """

        self._recording_start = recording_start

    @property
    def recording_end(self):
        """Gets the recording_end of this VideoRecording.  # noqa: E501


        :return: The recording_end of this VideoRecording.  # noqa: E501
        :rtype: datetime
        """
        return self._recording_end

    @recording_end.setter
    def recording_end(self, recording_end):
        """Sets the recording_end of this VideoRecording.


        :param recording_end: The recording_end of this VideoRecording.  # noqa: E501
        :type recording_end: datetime
        """

        self._recording_end = recording_end

    @property
    def gcode_file_name(self):
        """Gets the gcode_file_name of this VideoRecording.  # noqa: E501


        :return: The gcode_file_name of this VideoRecording.  # noqa: E501
        :rtype: str
        """
        return self._gcode_file_name

    @gcode_file_name.setter
    def gcode_file_name(self, gcode_file_name):
        """Sets the gcode_file_name of this VideoRecording.


        :param gcode_file_name: The gcode_file_name of this VideoRecording.  # noqa: E501
        :type gcode_file_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                gcode_file_name is not None and len(gcode_file_name) > 255):
            raise ValueError("Invalid value for `gcode_file_name`, length must be less than or equal to `255`")  # noqa: E501

        self._gcode_file_name = gcode_file_name

    @property
    def mp4_file(self):
        """Gets the mp4_file of this VideoRecording.  # noqa: E501


        :return: The mp4_file of this VideoRecording.  # noqa: E501
        :rtype: str
        """
        return self._mp4_file

    @mp4_file.setter
    def mp4_file(self, mp4_file):
        """Sets the mp4_file of this VideoRecording.


        :param mp4_file: The mp4_file of this VideoRecording.  # noqa: E501
        :type mp4_file: str
        """

        self._mp4_file = mp4_file

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
