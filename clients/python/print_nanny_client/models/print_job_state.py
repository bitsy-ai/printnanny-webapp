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


class PrintJobState(object):
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
        'client_event_type': 'ClientEventTypeEnum',
        'event_data': 'dict(str, object)',
        'device': 'int',
        'user': 'int',
        'plugin_version': 'str',
        'octoprint_version': 'str',
        'clientevent_ptr': 'int',
        'event_type': 'PrintJobStateEventTypeEnum',
        'state': 'dict(str, object)',
        'current_z': 'float',
        'progress': 'dict(str, object)',
        'job_data_file': 'str',
        'print_job': 'int',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'polymorphic_ctype': 'polymorphic_ctype',
        'created_dt': 'created_dt',
        'client_event_type': 'client_event_type',
        'event_data': 'event_data',
        'device': 'device',
        'user': 'user',
        'plugin_version': 'plugin_version',
        'octoprint_version': 'octoprint_version',
        'clientevent_ptr': 'clientevent_ptr',
        'event_type': 'event_type',
        'state': 'state',
        'current_z': 'current_z',
        'progress': 'progress',
        'job_data_file': 'job_data_file',
        'print_job': 'print_job',
        'url': 'url'
    }

    def __init__(self, id=None, polymorphic_ctype=None, created_dt=None, client_event_type=None, event_data=None, device=None, user=None, plugin_version=None, octoprint_version=None, clientevent_ptr=None, event_type=None, state=None, current_z=None, progress=None, job_data_file=None, print_job=None, url=None, local_vars_configuration=None):  # noqa: E501
        """PrintJobState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._polymorphic_ctype = None
        self._created_dt = None
        self._client_event_type = None
        self._event_data = None
        self._device = None
        self._user = None
        self._plugin_version = None
        self._octoprint_version = None
        self._clientevent_ptr = None
        self._event_type = None
        self._state = None
        self._current_z = None
        self._progress = None
        self._job_data_file = None
        self._print_job = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if polymorphic_ctype is not None:
            self.polymorphic_ctype = polymorphic_ctype
        self.created_dt = created_dt
        self.client_event_type = client_event_type
        self.event_data = event_data
        self.device = device
        if user is not None:
            self.user = user
        self.plugin_version = plugin_version
        self.octoprint_version = octoprint_version
        if clientevent_ptr is not None:
            self.clientevent_ptr = clientevent_ptr
        self.event_type = event_type
        if state is not None:
            self.state = state
        self.current_z = current_z
        if progress is not None:
            self.progress = progress
        self.job_data_file = job_data_file
        self.print_job = print_job
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this PrintJobState.  # noqa: E501


        :return: The id of this PrintJobState.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrintJobState.


        :param id: The id of this PrintJobState.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this PrintJobState.  # noqa: E501


        :return: The polymorphic_ctype of this PrintJobState.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this PrintJobState.


        :param polymorphic_ctype: The polymorphic_ctype of this PrintJobState.  # noqa: E501
        :type polymorphic_ctype: int
        """

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def created_dt(self):
        """Gets the created_dt of this PrintJobState.  # noqa: E501


        :return: The created_dt of this PrintJobState.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PrintJobState.


        :param created_dt: The created_dt of this PrintJobState.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def client_event_type(self):
        """Gets the client_event_type of this PrintJobState.  # noqa: E501


        :return: The client_event_type of this PrintJobState.  # noqa: E501
        :rtype: ClientEventTypeEnum
        """
        return self._client_event_type

    @client_event_type.setter
    def client_event_type(self, client_event_type):
        """Sets the client_event_type of this PrintJobState.


        :param client_event_type: The client_event_type of this PrintJobState.  # noqa: E501
        :type client_event_type: ClientEventTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and client_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `client_event_type`, must not be `None`")  # noqa: E501

        self._client_event_type = client_event_type

    @property
    def event_data(self):
        """Gets the event_data of this PrintJobState.  # noqa: E501


        :return: The event_data of this PrintJobState.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        """Sets the event_data of this PrintJobState.


        :param event_data: The event_data of this PrintJobState.  # noqa: E501
        :type event_data: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and event_data is None:  # noqa: E501
            raise ValueError("Invalid value for `event_data`, must not be `None`")  # noqa: E501

        self._event_data = event_data

    @property
    def device(self):
        """Gets the device of this PrintJobState.  # noqa: E501


        :return: The device of this PrintJobState.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PrintJobState.


        :param device: The device of this PrintJobState.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def user(self):
        """Gets the user of this PrintJobState.  # noqa: E501


        :return: The user of this PrintJobState.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PrintJobState.


        :param user: The user of this PrintJobState.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def plugin_version(self):
        """Gets the plugin_version of this PrintJobState.  # noqa: E501


        :return: The plugin_version of this PrintJobState.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this PrintJobState.


        :param plugin_version: The plugin_version of this PrintJobState.  # noqa: E501
        :type plugin_version: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_version is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plugin_version is not None and len(plugin_version) > 60):
            raise ValueError("Invalid value for `plugin_version`, length must be less than or equal to `60`")  # noqa: E501

        self._plugin_version = plugin_version

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this PrintJobState.  # noqa: E501


        :return: The octoprint_version of this PrintJobState.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this PrintJobState.


        :param octoprint_version: The octoprint_version of this PrintJobState.  # noqa: E501
        :type octoprint_version: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_version is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 60):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `60`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def clientevent_ptr(self):
        """Gets the clientevent_ptr of this PrintJobState.  # noqa: E501


        :return: The clientevent_ptr of this PrintJobState.  # noqa: E501
        :rtype: int
        """
        return self._clientevent_ptr

    @clientevent_ptr.setter
    def clientevent_ptr(self, clientevent_ptr):
        """Sets the clientevent_ptr of this PrintJobState.


        :param clientevent_ptr: The clientevent_ptr of this PrintJobState.  # noqa: E501
        :type clientevent_ptr: int
        """

        self._clientevent_ptr = clientevent_ptr

    @property
    def event_type(self):
        """Gets the event_type of this PrintJobState.  # noqa: E501


        :return: The event_type of this PrintJobState.  # noqa: E501
        :rtype: PrintJobStateEventTypeEnum
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PrintJobState.


        :param event_type: The event_type of this PrintJobState.  # noqa: E501
        :type event_type: PrintJobStateEventTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def state(self):
        """Gets the state of this PrintJobState.  # noqa: E501


        :return: The state of this PrintJobState.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PrintJobState.


        :param state: The state of this PrintJobState.  # noqa: E501
        :type state: dict(str, object)
        """

        self._state = state

    @property
    def current_z(self):
        """Gets the current_z of this PrintJobState.  # noqa: E501


        :return: The current_z of this PrintJobState.  # noqa: E501
        :rtype: float
        """
        return self._current_z

    @current_z.setter
    def current_z(self, current_z):
        """Sets the current_z of this PrintJobState.


        :param current_z: The current_z of this PrintJobState.  # noqa: E501
        :type current_z: float
        """

        self._current_z = current_z

    @property
    def progress(self):
        """Gets the progress of this PrintJobState.  # noqa: E501


        :return: The progress of this PrintJobState.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this PrintJobState.


        :param progress: The progress of this PrintJobState.  # noqa: E501
        :type progress: dict(str, object)
        """

        self._progress = progress

    @property
    def job_data_file(self):
        """Gets the job_data_file of this PrintJobState.  # noqa: E501


        :return: The job_data_file of this PrintJobState.  # noqa: E501
        :rtype: str
        """
        return self._job_data_file

    @job_data_file.setter
    def job_data_file(self, job_data_file):
        """Sets the job_data_file of this PrintJobState.


        :param job_data_file: The job_data_file of this PrintJobState.  # noqa: E501
        :type job_data_file: str
        """
        if self.local_vars_configuration.client_side_validation and job_data_file is None:  # noqa: E501
            raise ValueError("Invalid value for `job_data_file`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                job_data_file is not None and len(job_data_file) > 255):
            raise ValueError("Invalid value for `job_data_file`, length must be less than or equal to `255`")  # noqa: E501

        self._job_data_file = job_data_file

    @property
    def print_job(self):
        """Gets the print_job of this PrintJobState.  # noqa: E501


        :return: The print_job of this PrintJobState.  # noqa: E501
        :rtype: int
        """
        return self._print_job

    @print_job.setter
    def print_job(self, print_job):
        """Sets the print_job of this PrintJobState.


        :param print_job: The print_job of this PrintJobState.  # noqa: E501
        :type print_job: int
        """

        self._print_job = print_job

    @property
    def url(self):
        """Gets the url of this PrintJobState.  # noqa: E501


        :return: The url of this PrintJobState.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PrintJobState.


        :param url: The url of this PrintJobState.  # noqa: E501
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
        if not isinstance(other, PrintJobState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintJobState):
            return True

        return self.to_dict() != other.to_dict()
