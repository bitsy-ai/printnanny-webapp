# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class PrintStatusEvent(object):
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
        'polymorphic_ctype': 'int',
        'created_dt': 'datetime',
        'event_source': 'EventSourceEnum',
        'event_data': 'dict(str, object)',
        'octoprint_device': 'int',
        'user': 'int',
        'plugin_version': 'str',
        'client_version': 'str',
        'octoprint_version': 'str',
        'metadata': 'dict(str, object)',
        'octoprint_job': 'dict(str, object)',
        'print_session': 'int',
        'telemetryevent_ptr': 'int',
        'event_type': 'PrintStatusEventEventTypeEnum',
        'state': 'dict(str, object)',
        'current_z': 'float',
        'progress': 'dict(str, object)',
        'job_data_file': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'polymorphic_ctype': 'polymorphic_ctype',
        'created_dt': 'created_dt',
        'event_source': 'event_source',
        'event_data': 'event_data',
        'octoprint_device': 'octoprint_device',
        'user': 'user',
        'plugin_version': 'plugin_version',
        'client_version': 'client_version',
        'octoprint_version': 'octoprint_version',
        'metadata': 'metadata',
        'octoprint_job': 'octoprint_job',
        'print_session': 'print_session',
        'telemetryevent_ptr': 'telemetryevent_ptr',
        'event_type': 'event_type',
        'state': 'state',
        'current_z': 'current_z',
        'progress': 'progress',
        'job_data_file': 'job_data_file',
        'url': 'url'
    }

    def __init__(self, id=None, polymorphic_ctype=None, created_dt=None, event_source=None, event_data=None, octoprint_device=None, user=None, plugin_version=None, client_version=None, octoprint_version=None, metadata=None, octoprint_job=None, print_session=None, telemetryevent_ptr=None, event_type=None, state=None, current_z=None, progress=None, job_data_file=None, url=None, local_vars_configuration=None):  # noqa: E501
        """PrintStatusEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._polymorphic_ctype = None
        self._created_dt = None
        self._event_source = None
        self._event_data = None
        self._octoprint_device = None
        self._user = None
        self._plugin_version = None
        self._client_version = None
        self._octoprint_version = None
        self._metadata = None
        self._octoprint_job = None
        self._print_session = None
        self._telemetryevent_ptr = None
        self._event_type = None
        self._state = None
        self._current_z = None
        self._progress = None
        self._job_data_file = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if polymorphic_ctype is not None:
            self.polymorphic_ctype = polymorphic_ctype
        if created_dt is not None:
            self.created_dt = created_dt
        if event_source is not None:
            self.event_source = event_source
        self.event_data = event_data
        self.octoprint_device = octoprint_device
        if user is not None:
            self.user = user
        self.plugin_version = plugin_version
        self.client_version = client_version
        self.octoprint_version = octoprint_version
        self.metadata = metadata
        self.octoprint_job = octoprint_job
        self.print_session = print_session
        if telemetryevent_ptr is not None:
            self.telemetryevent_ptr = telemetryevent_ptr
        self.event_type = event_type
        if state is not None:
            self.state = state
        self.current_z = current_z
        if progress is not None:
            self.progress = progress
        self.job_data_file = job_data_file
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this PrintStatusEvent.  # noqa: E501


        :return: The id of this PrintStatusEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrintStatusEvent.


        :param id: The id of this PrintStatusEvent.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this PrintStatusEvent.  # noqa: E501


        :return: The polymorphic_ctype of this PrintStatusEvent.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this PrintStatusEvent.


        :param polymorphic_ctype: The polymorphic_ctype of this PrintStatusEvent.  # noqa: E501
        :type polymorphic_ctype: int
        """

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def created_dt(self):
        """Gets the created_dt of this PrintStatusEvent.  # noqa: E501


        :return: The created_dt of this PrintStatusEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PrintStatusEvent.


        :param created_dt: The created_dt of this PrintStatusEvent.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def event_source(self):
        """Gets the event_source of this PrintStatusEvent.  # noqa: E501


        :return: The event_source of this PrintStatusEvent.  # noqa: E501
        :rtype: EventSourceEnum
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this PrintStatusEvent.


        :param event_source: The event_source of this PrintStatusEvent.  # noqa: E501
        :type event_source: EventSourceEnum
        """

        self._event_source = event_source

    @property
    def event_data(self):
        """Gets the event_data of this PrintStatusEvent.  # noqa: E501


        :return: The event_data of this PrintStatusEvent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        """Sets the event_data of this PrintStatusEvent.


        :param event_data: The event_data of this PrintStatusEvent.  # noqa: E501
        :type event_data: dict(str, object)
        """

        self._event_data = event_data

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this PrintStatusEvent.  # noqa: E501


        :return: The octoprint_device of this PrintStatusEvent.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this PrintStatusEvent.


        :param octoprint_device: The octoprint_device of this PrintStatusEvent.  # noqa: E501
        :type octoprint_device: int
        """
        if self.local_vars_configuration.client_side_validation and octoprint_device is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_device`, must not be `None`")  # noqa: E501

        self._octoprint_device = octoprint_device

    @property
    def user(self):
        """Gets the user of this PrintStatusEvent.  # noqa: E501


        :return: The user of this PrintStatusEvent.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PrintStatusEvent.


        :param user: The user of this PrintStatusEvent.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def plugin_version(self):
        """Gets the plugin_version of this PrintStatusEvent.  # noqa: E501


        :return: The plugin_version of this PrintStatusEvent.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this PrintStatusEvent.


        :param plugin_version: The plugin_version of this PrintStatusEvent.  # noqa: E501
        :type plugin_version: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_version is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plugin_version is not None and len(plugin_version) > 60):
            raise ValueError("Invalid value for `plugin_version`, length must be less than or equal to `60`")  # noqa: E501

        self._plugin_version = plugin_version

    @property
    def client_version(self):
        """Gets the client_version of this PrintStatusEvent.  # noqa: E501


        :return: The client_version of this PrintStatusEvent.  # noqa: E501
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this PrintStatusEvent.


        :param client_version: The client_version of this PrintStatusEvent.  # noqa: E501
        :type client_version: str
        """
        if self.local_vars_configuration.client_side_validation and client_version is None:  # noqa: E501
            raise ValueError("Invalid value for `client_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_version is not None and len(client_version) > 60):
            raise ValueError("Invalid value for `client_version`, length must be less than or equal to `60`")  # noqa: E501

        self._client_version = client_version

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this PrintStatusEvent.  # noqa: E501


        :return: The octoprint_version of this PrintStatusEvent.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this PrintStatusEvent.


        :param octoprint_version: The octoprint_version of this PrintStatusEvent.  # noqa: E501
        :type octoprint_version: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_version is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 60):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `60`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def metadata(self):
        """Gets the metadata of this PrintStatusEvent.  # noqa: E501


        :return: The metadata of this PrintStatusEvent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PrintStatusEvent.


        :param metadata: The metadata of this PrintStatusEvent.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

    @property
    def octoprint_job(self):
        """Gets the octoprint_job of this PrintStatusEvent.  # noqa: E501


        :return: The octoprint_job of this PrintStatusEvent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._octoprint_job

    @octoprint_job.setter
    def octoprint_job(self, octoprint_job):
        """Sets the octoprint_job of this PrintStatusEvent.


        :param octoprint_job: The octoprint_job of this PrintStatusEvent.  # noqa: E501
        :type octoprint_job: dict(str, object)
        """

        self._octoprint_job = octoprint_job

    @property
    def print_session(self):
        """Gets the print_session of this PrintStatusEvent.  # noqa: E501


        :return: The print_session of this PrintStatusEvent.  # noqa: E501
        :rtype: int
        """
        return self._print_session

    @print_session.setter
    def print_session(self, print_session):
        """Sets the print_session of this PrintStatusEvent.


        :param print_session: The print_session of this PrintStatusEvent.  # noqa: E501
        :type print_session: int
        """

        self._print_session = print_session

    @property
    def telemetryevent_ptr(self):
        """Gets the telemetryevent_ptr of this PrintStatusEvent.  # noqa: E501


        :return: The telemetryevent_ptr of this PrintStatusEvent.  # noqa: E501
        :rtype: int
        """
        return self._telemetryevent_ptr

    @telemetryevent_ptr.setter
    def telemetryevent_ptr(self, telemetryevent_ptr):
        """Sets the telemetryevent_ptr of this PrintStatusEvent.


        :param telemetryevent_ptr: The telemetryevent_ptr of this PrintStatusEvent.  # noqa: E501
        :type telemetryevent_ptr: int
        """

        self._telemetryevent_ptr = telemetryevent_ptr

    @property
    def event_type(self):
        """Gets the event_type of this PrintStatusEvent.  # noqa: E501


        :return: The event_type of this PrintStatusEvent.  # noqa: E501
        :rtype: PrintStatusEventEventTypeEnum
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PrintStatusEvent.


        :param event_type: The event_type of this PrintStatusEvent.  # noqa: E501
        :type event_type: PrintStatusEventEventTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def state(self):
        """Gets the state of this PrintStatusEvent.  # noqa: E501


        :return: The state of this PrintStatusEvent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PrintStatusEvent.


        :param state: The state of this PrintStatusEvent.  # noqa: E501
        :type state: dict(str, object)
        """

        self._state = state

    @property
    def current_z(self):
        """Gets the current_z of this PrintStatusEvent.  # noqa: E501


        :return: The current_z of this PrintStatusEvent.  # noqa: E501
        :rtype: float
        """
        return self._current_z

    @current_z.setter
    def current_z(self, current_z):
        """Sets the current_z of this PrintStatusEvent.


        :param current_z: The current_z of this PrintStatusEvent.  # noqa: E501
        :type current_z: float
        """

        self._current_z = current_z

    @property
    def progress(self):
        """Gets the progress of this PrintStatusEvent.  # noqa: E501


        :return: The progress of this PrintStatusEvent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this PrintStatusEvent.


        :param progress: The progress of this PrintStatusEvent.  # noqa: E501
        :type progress: dict(str, object)
        """

        self._progress = progress

    @property
    def job_data_file(self):
        """Gets the job_data_file of this PrintStatusEvent.  # noqa: E501


        :return: The job_data_file of this PrintStatusEvent.  # noqa: E501
        :rtype: str
        """
        return self._job_data_file

    @job_data_file.setter
    def job_data_file(self, job_data_file):
        """Sets the job_data_file of this PrintStatusEvent.


        :param job_data_file: The job_data_file of this PrintStatusEvent.  # noqa: E501
        :type job_data_file: str
        """
        if self.local_vars_configuration.client_side_validation and job_data_file is None:  # noqa: E501
            raise ValueError("Invalid value for `job_data_file`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                job_data_file is not None and len(job_data_file) > 255):
            raise ValueError("Invalid value for `job_data_file`, length must be less than or equal to `255`")  # noqa: E501

        self._job_data_file = job_data_file

    @property
    def url(self):
        """Gets the url of this PrintStatusEvent.  # noqa: E501


        :return: The url of this PrintStatusEvent.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PrintStatusEvent.


        :param url: The url of this PrintStatusEvent.  # noqa: E501
        :type url: str
        """

        self._url = url

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
        if not isinstance(other, PrintStatusEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintStatusEvent):
            return True

        return self.to_dict() != other.to_dict()
