# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class PrintSession(object):
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
        'updated_dt': 'datetime',
        'octoprint_device': 'int',
        'session': 'str',
        'progress': 'dict(str, object)',
        'status': 'StatusEnum',
        'user': 'int',
        'printer_profile': 'int',
        'gcode_file': 'int',
        'gcode_filename': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'octoprint_device': 'octoprint_device',
        'session': 'session',
        'progress': 'progress',
        'status': 'status',
        'user': 'user',
        'printer_profile': 'printer_profile',
        'gcode_file': 'gcode_file',
        'gcode_filename': 'gcode_filename',
        'url': 'url'
    }

    def __init__(self, id=None, created_dt=None, updated_dt=None, octoprint_device=None, session=None, progress=None, status=None, user=None, printer_profile=None, gcode_file=None, gcode_filename=None, url=None, local_vars_configuration=None):  # noqa: E501
        """PrintSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._updated_dt = None
        self._octoprint_device = None
        self._session = None
        self._progress = None
        self._status = None
        self._user = None
        self._printer_profile = None
        self._gcode_file = None
        self._gcode_filename = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_dt is not None:
            self.created_dt = created_dt
        if updated_dt is not None:
            self.updated_dt = updated_dt
        self.octoprint_device = octoprint_device
        self.session = session
        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status
        if user is not None:
            self.user = user
        self.printer_profile = printer_profile
        self.gcode_file = gcode_file
        self.gcode_filename = gcode_filename
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this PrintSession.  # noqa: E501


        :return: The id of this PrintSession.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrintSession.


        :param id: The id of this PrintSession.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this PrintSession.  # noqa: E501


        :return: The created_dt of this PrintSession.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PrintSession.


        :param created_dt: The created_dt of this PrintSession.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this PrintSession.  # noqa: E501


        :return: The updated_dt of this PrintSession.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this PrintSession.


        :param updated_dt: The updated_dt of this PrintSession.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this PrintSession.  # noqa: E501


        :return: The octoprint_device of this PrintSession.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this PrintSession.


        :param octoprint_device: The octoprint_device of this PrintSession.  # noqa: E501
        :type octoprint_device: int
        """
        if self.local_vars_configuration.client_side_validation and octoprint_device is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_device`, must not be `None`")  # noqa: E501

        self._octoprint_device = octoprint_device

    @property
    def session(self):
        """Gets the session of this PrintSession.  # noqa: E501


        :return: The session of this PrintSession.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this PrintSession.


        :param session: The session of this PrintSession.  # noqa: E501
        :type session: str
        """
        if self.local_vars_configuration.client_side_validation and session is None:  # noqa: E501
            raise ValueError("Invalid value for `session`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                session is not None and len(session) > 255):
            raise ValueError("Invalid value for `session`, length must be less than or equal to `255`")  # noqa: E501

        self._session = session

    @property
    def progress(self):
        """Gets the progress of this PrintSession.  # noqa: E501


        :return: The progress of this PrintSession.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this PrintSession.


        :param progress: The progress of this PrintSession.  # noqa: E501
        :type progress: dict(str, object)
        """

        self._progress = progress

    @property
    def status(self):
        """Gets the status of this PrintSession.  # noqa: E501


        :return: The status of this PrintSession.  # noqa: E501
        :rtype: StatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PrintSession.


        :param status: The status of this PrintSession.  # noqa: E501
        :type status: StatusEnum
        """

        self._status = status

    @property
    def user(self):
        """Gets the user of this PrintSession.  # noqa: E501


        :return: The user of this PrintSession.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PrintSession.


        :param user: The user of this PrintSession.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def printer_profile(self):
        """Gets the printer_profile of this PrintSession.  # noqa: E501


        :return: The printer_profile of this PrintSession.  # noqa: E501
        :rtype: int
        """
        return self._printer_profile

    @printer_profile.setter
    def printer_profile(self, printer_profile):
        """Sets the printer_profile of this PrintSession.


        :param printer_profile: The printer_profile of this PrintSession.  # noqa: E501
        :type printer_profile: int
        """

        self._printer_profile = printer_profile

    @property
    def gcode_file(self):
        """Gets the gcode_file of this PrintSession.  # noqa: E501


        :return: The gcode_file of this PrintSession.  # noqa: E501
        :rtype: int
        """
        return self._gcode_file

    @gcode_file.setter
    def gcode_file(self, gcode_file):
        """Sets the gcode_file of this PrintSession.


        :param gcode_file: The gcode_file of this PrintSession.  # noqa: E501
        :type gcode_file: int
        """

        self._gcode_file = gcode_file

    @property
    def gcode_filename(self):
        """Gets the gcode_filename of this PrintSession.  # noqa: E501


        :return: The gcode_filename of this PrintSession.  # noqa: E501
        :rtype: str
        """
        return self._gcode_filename

    @gcode_filename.setter
    def gcode_filename(self, gcode_filename):
        """Sets the gcode_filename of this PrintSession.


        :param gcode_filename: The gcode_filename of this PrintSession.  # noqa: E501
        :type gcode_filename: str
        """
        if (self.local_vars_configuration.client_side_validation and
                gcode_filename is not None and len(gcode_filename) > 255):
            raise ValueError("Invalid value for `gcode_filename`, length must be less than or equal to `255`")  # noqa: E501

        self._gcode_filename = gcode_filename

    @property
    def url(self):
        """Gets the url of this PrintSession.  # noqa: E501


        :return: The url of this PrintSession.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PrintSession.


        :param url: The url of this PrintSession.  # noqa: E501
        :type url: str
        """

        self._url = url

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, PrintSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintSession):
            return True

        return self.to_dict() != other.to_dict()
