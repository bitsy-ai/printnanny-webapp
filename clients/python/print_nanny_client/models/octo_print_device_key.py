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


class OctoPrintDeviceKey(object):
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
        'deleted': 'datetime',
        'created_dt': 'datetime',
        'name': 'str',
        'user': 'int',
        'active_session': 'int',
        'public_key': 'str',
        'fingerprint': 'str',
        'cloudiot_device': 'dict(str, object)',
        'cloudiot_device_name': 'str',
        'cloudiot_device_path': 'str',
        'cloudiot_device_num_id': 'int',
        'model': 'str',
        'platform': 'str',
        'cpu_flags': 'list[str]',
        'hardware': 'str',
        'revision': 'str',
        'serial': 'str',
        'cores': 'int',
        'ram': 'int',
        'python_version': 'str',
        'pip_version': 'str',
        'virtualenv': 'str',
        'monitoring_active': 'bool',
        'monitoring_mode': 'MonitoringModeEnum',
        'octoprint_version': 'str',
        'plugin_version': 'str',
        'print_nanny_client_version': 'str',
        'url': 'str',
        'private_key': 'str',
        'private_key_checksum': 'str',
        'public_key_checksum': 'str',
        'cloudiot_device_configs': 'str',
        'ca_certs': 'dict(str, str)',
        'manage_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'deleted': 'deleted',
        'created_dt': 'created_dt',
        'name': 'name',
        'user': 'user',
        'active_session': 'active_session',
        'public_key': 'public_key',
        'fingerprint': 'fingerprint',
        'cloudiot_device': 'cloudiot_device',
        'cloudiot_device_name': 'cloudiot_device_name',
        'cloudiot_device_path': 'cloudiot_device_path',
        'cloudiot_device_num_id': 'cloudiot_device_num_id',
        'model': 'model',
        'platform': 'platform',
        'cpu_flags': 'cpu_flags',
        'hardware': 'hardware',
        'revision': 'revision',
        'serial': 'serial',
        'cores': 'cores',
        'ram': 'ram',
        'python_version': 'python_version',
        'pip_version': 'pip_version',
        'virtualenv': 'virtualenv',
        'monitoring_active': 'monitoring_active',
        'monitoring_mode': 'monitoring_mode',
        'octoprint_version': 'octoprint_version',
        'plugin_version': 'plugin_version',
        'print_nanny_client_version': 'print_nanny_client_version',
        'url': 'url',
        'private_key': 'private_key',
        'private_key_checksum': 'private_key_checksum',
        'public_key_checksum': 'public_key_checksum',
        'cloudiot_device_configs': 'cloudiot_device_configs',
        'ca_certs': 'ca_certs',
        'manage_url': 'manage_url'
    }

    def __init__(self, id=None, deleted=None, created_dt=None, name=None, user=None, active_session=None, public_key=None, fingerprint=None, cloudiot_device=None, cloudiot_device_name=None, cloudiot_device_path=None, cloudiot_device_num_id=None, model=None, platform=None, cpu_flags=None, hardware=None, revision=None, serial=None, cores=None, ram=None, python_version=None, pip_version=None, virtualenv=None, monitoring_active=None, monitoring_mode=None, octoprint_version=None, plugin_version=None, print_nanny_client_version=None, url=None, private_key=None, private_key_checksum=None, public_key_checksum=None, cloudiot_device_configs=None, ca_certs=None, manage_url=None, local_vars_configuration=None):  # noqa: E501
        """OctoPrintDeviceKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deleted = None
        self._created_dt = None
        self._name = None
        self._user = None
        self._active_session = None
        self._public_key = None
        self._fingerprint = None
        self._cloudiot_device = None
        self._cloudiot_device_name = None
        self._cloudiot_device_path = None
        self._cloudiot_device_num_id = None
        self._model = None
        self._platform = None
        self._cpu_flags = None
        self._hardware = None
        self._revision = None
        self._serial = None
        self._cores = None
        self._ram = None
        self._python_version = None
        self._pip_version = None
        self._virtualenv = None
        self._monitoring_active = None
        self._monitoring_mode = None
        self._octoprint_version = None
        self._plugin_version = None
        self._print_nanny_client_version = None
        self._url = None
        self._private_key = None
        self._private_key_checksum = None
        self._public_key_checksum = None
        self._cloudiot_device_configs = None
        self._ca_certs = None
        self._manage_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if deleted is not None:
            self.deleted = deleted
        if created_dt is not None:
            self.created_dt = created_dt
        self.name = name
        if user is not None:
            self.user = user
        self.active_session = active_session
        if public_key is not None:
            self.public_key = public_key
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if cloudiot_device is not None:
            self.cloudiot_device = cloudiot_device
        if cloudiot_device_name is not None:
            self.cloudiot_device_name = cloudiot_device_name
        if cloudiot_device_path is not None:
            self.cloudiot_device_path = cloudiot_device_path
        if cloudiot_device_num_id is not None:
            self.cloudiot_device_num_id = cloudiot_device_num_id
        self.model = model
        self.platform = platform
        self.cpu_flags = cpu_flags
        self.hardware = hardware
        self.revision = revision
        self.serial = serial
        self.cores = cores
        self.ram = ram
        self.python_version = python_version
        self.pip_version = pip_version
        self.virtualenv = virtualenv
        if monitoring_active is not None:
            self.monitoring_active = monitoring_active
        if monitoring_mode is not None:
            self.monitoring_mode = monitoring_mode
        self.octoprint_version = octoprint_version
        self.plugin_version = plugin_version
        self.print_nanny_client_version = print_nanny_client_version
        if url is not None:
            self.url = url
        if private_key is not None:
            self.private_key = private_key
        if private_key_checksum is not None:
            self.private_key_checksum = private_key_checksum
        self.public_key_checksum = public_key_checksum
        if cloudiot_device_configs is not None:
            self.cloudiot_device_configs = cloudiot_device_configs
        self.ca_certs = ca_certs
        if manage_url is not None:
            self.manage_url = manage_url

    @property
    def id(self):
        """Gets the id of this OctoPrintDeviceKey.  # noqa: E501


        :return: The id of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OctoPrintDeviceKey.


        :param id: The id of this OctoPrintDeviceKey.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def deleted(self):
        """Gets the deleted of this OctoPrintDeviceKey.  # noqa: E501


        :return: The deleted of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this OctoPrintDeviceKey.


        :param deleted: The deleted of this OctoPrintDeviceKey.  # noqa: E501
        :type deleted: datetime
        """

        self._deleted = deleted

    @property
    def created_dt(self):
        """Gets the created_dt of this OctoPrintDeviceKey.  # noqa: E501


        :return: The created_dt of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OctoPrintDeviceKey.


        :param created_dt: The created_dt of this OctoPrintDeviceKey.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def name(self):
        """Gets the name of this OctoPrintDeviceKey.  # noqa: E501


        :return: The name of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OctoPrintDeviceKey.


        :param name: The name of this OctoPrintDeviceKey.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def user(self):
        """Gets the user of this OctoPrintDeviceKey.  # noqa: E501


        :return: The user of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OctoPrintDeviceKey.


        :param user: The user of this OctoPrintDeviceKey.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def active_session(self):
        """Gets the active_session of this OctoPrintDeviceKey.  # noqa: E501


        :return: The active_session of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: int
        """
        return self._active_session

    @active_session.setter
    def active_session(self, active_session):
        """Sets the active_session of this OctoPrintDeviceKey.


        :param active_session: The active_session of this OctoPrintDeviceKey.  # noqa: E501
        :type active_session: int
        """

        self._active_session = active_session

    @property
    def public_key(self):
        """Gets the public_key of this OctoPrintDeviceKey.  # noqa: E501


        :return: The public_key of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this OctoPrintDeviceKey.


        :param public_key: The public_key of this OctoPrintDeviceKey.  # noqa: E501
        :type public_key: str
        """

        self._public_key = public_key

    @property
    def fingerprint(self):
        """Gets the fingerprint of this OctoPrintDeviceKey.  # noqa: E501


        :return: The fingerprint of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this OctoPrintDeviceKey.


        :param fingerprint: The fingerprint of this OctoPrintDeviceKey.  # noqa: E501
        :type fingerprint: str
        """

        self._fingerprint = fingerprint

    @property
    def cloudiot_device(self):
        """Gets the cloudiot_device of this OctoPrintDeviceKey.  # noqa: E501


        :return: The cloudiot_device of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._cloudiot_device

    @cloudiot_device.setter
    def cloudiot_device(self, cloudiot_device):
        """Sets the cloudiot_device of this OctoPrintDeviceKey.


        :param cloudiot_device: The cloudiot_device of this OctoPrintDeviceKey.  # noqa: E501
        :type cloudiot_device: dict(str, object)
        """

        self._cloudiot_device = cloudiot_device

    @property
    def cloudiot_device_name(self):
        """Gets the cloudiot_device_name of this OctoPrintDeviceKey.  # noqa: E501


        :return: The cloudiot_device_name of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._cloudiot_device_name

    @cloudiot_device_name.setter
    def cloudiot_device_name(self, cloudiot_device_name):
        """Sets the cloudiot_device_name of this OctoPrintDeviceKey.


        :param cloudiot_device_name: The cloudiot_device_name of this OctoPrintDeviceKey.  # noqa: E501
        :type cloudiot_device_name: str
        """

        self._cloudiot_device_name = cloudiot_device_name

    @property
    def cloudiot_device_path(self):
        """Gets the cloudiot_device_path of this OctoPrintDeviceKey.  # noqa: E501


        :return: The cloudiot_device_path of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._cloudiot_device_path

    @cloudiot_device_path.setter
    def cloudiot_device_path(self, cloudiot_device_path):
        """Sets the cloudiot_device_path of this OctoPrintDeviceKey.


        :param cloudiot_device_path: The cloudiot_device_path of this OctoPrintDeviceKey.  # noqa: E501
        :type cloudiot_device_path: str
        """

        self._cloudiot_device_path = cloudiot_device_path

    @property
    def cloudiot_device_num_id(self):
        """Gets the cloudiot_device_num_id of this OctoPrintDeviceKey.  # noqa: E501


        :return: The cloudiot_device_num_id of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: int
        """
        return self._cloudiot_device_num_id

    @cloudiot_device_num_id.setter
    def cloudiot_device_num_id(self, cloudiot_device_num_id):
        """Sets the cloudiot_device_num_id of this OctoPrintDeviceKey.


        :param cloudiot_device_num_id: The cloudiot_device_num_id of this OctoPrintDeviceKey.  # noqa: E501
        :type cloudiot_device_num_id: int
        """

        self._cloudiot_device_num_id = cloudiot_device_num_id

    @property
    def model(self):
        """Gets the model of this OctoPrintDeviceKey.  # noqa: E501


        :return: The model of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this OctoPrintDeviceKey.


        :param model: The model of this OctoPrintDeviceKey.  # noqa: E501
        :type model: str
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def platform(self):
        """Gets the platform of this OctoPrintDeviceKey.  # noqa: E501


        :return: The platform of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this OctoPrintDeviceKey.


        :param platform: The platform of this OctoPrintDeviceKey.  # noqa: E501
        :type platform: str
        """
        if self.local_vars_configuration.client_side_validation and platform is None:  # noqa: E501
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                platform is not None and len(platform) > 255):
            raise ValueError("Invalid value for `platform`, length must be less than or equal to `255`")  # noqa: E501

        self._platform = platform

    @property
    def cpu_flags(self):
        """Gets the cpu_flags of this OctoPrintDeviceKey.  # noqa: E501


        :return: The cpu_flags of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._cpu_flags

    @cpu_flags.setter
    def cpu_flags(self, cpu_flags):
        """Sets the cpu_flags of this OctoPrintDeviceKey.


        :param cpu_flags: The cpu_flags of this OctoPrintDeviceKey.  # noqa: E501
        :type cpu_flags: list[str]
        """

        self._cpu_flags = cpu_flags

    @property
    def hardware(self):
        """Gets the hardware of this OctoPrintDeviceKey.  # noqa: E501


        :return: The hardware of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this OctoPrintDeviceKey.


        :param hardware: The hardware of this OctoPrintDeviceKey.  # noqa: E501
        :type hardware: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) > 255):
            raise ValueError("Invalid value for `hardware`, length must be less than or equal to `255`")  # noqa: E501

        self._hardware = hardware

    @property
    def revision(self):
        """Gets the revision of this OctoPrintDeviceKey.  # noqa: E501


        :return: The revision of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this OctoPrintDeviceKey.


        :param revision: The revision of this OctoPrintDeviceKey.  # noqa: E501
        :type revision: str
        """
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501

        self._revision = revision

    @property
    def serial(self):
        """Gets the serial of this OctoPrintDeviceKey.  # noqa: E501


        :return: The serial of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this OctoPrintDeviceKey.


        :param serial: The serial of this OctoPrintDeviceKey.  # noqa: E501
        :type serial: str
        """
        if self.local_vars_configuration.client_side_validation and serial is None:  # noqa: E501
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 255):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `255`")  # noqa: E501

        self._serial = serial

    @property
    def cores(self):
        """Gets the cores of this OctoPrintDeviceKey.  # noqa: E501


        :return: The cores of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this OctoPrintDeviceKey.


        :param cores: The cores of this OctoPrintDeviceKey.  # noqa: E501
        :type cores: int
        """
        if self.local_vars_configuration.client_side_validation and cores is None:  # noqa: E501
            raise ValueError("Invalid value for `cores`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._cores = cores

    @property
    def ram(self):
        """Gets the ram of this OctoPrintDeviceKey.  # noqa: E501


        :return: The ram of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this OctoPrintDeviceKey.


        :param ram: The ram of this OctoPrintDeviceKey.  # noqa: E501
        :type ram: int
        """
        if self.local_vars_configuration.client_side_validation and ram is None:  # noqa: E501
            raise ValueError("Invalid value for `ram`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._ram = ram

    @property
    def python_version(self):
        """Gets the python_version of this OctoPrintDeviceKey.  # noqa: E501


        :return: The python_version of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this OctoPrintDeviceKey.


        :param python_version: The python_version of this OctoPrintDeviceKey.  # noqa: E501
        :type python_version: str
        """
        if self.local_vars_configuration.client_side_validation and python_version is None:  # noqa: E501
            raise ValueError("Invalid value for `python_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                python_version is not None and len(python_version) > 255):
            raise ValueError("Invalid value for `python_version`, length must be less than or equal to `255`")  # noqa: E501

        self._python_version = python_version

    @property
    def pip_version(self):
        """Gets the pip_version of this OctoPrintDeviceKey.  # noqa: E501


        :return: The pip_version of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._pip_version

    @pip_version.setter
    def pip_version(self, pip_version):
        """Sets the pip_version of this OctoPrintDeviceKey.


        :param pip_version: The pip_version of this OctoPrintDeviceKey.  # noqa: E501
        :type pip_version: str
        """
        if self.local_vars_configuration.client_side_validation and pip_version is None:  # noqa: E501
            raise ValueError("Invalid value for `pip_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pip_version is not None and len(pip_version) > 255):
            raise ValueError("Invalid value for `pip_version`, length must be less than or equal to `255`")  # noqa: E501

        self._pip_version = pip_version

    @property
    def virtualenv(self):
        """Gets the virtualenv of this OctoPrintDeviceKey.  # noqa: E501


        :return: The virtualenv of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._virtualenv

    @virtualenv.setter
    def virtualenv(self, virtualenv):
        """Sets the virtualenv of this OctoPrintDeviceKey.


        :param virtualenv: The virtualenv of this OctoPrintDeviceKey.  # noqa: E501
        :type virtualenv: str
        """
        if (self.local_vars_configuration.client_side_validation and
                virtualenv is not None and len(virtualenv) > 255):
            raise ValueError("Invalid value for `virtualenv`, length must be less than or equal to `255`")  # noqa: E501

        self._virtualenv = virtualenv

    @property
    def monitoring_active(self):
        """Gets the monitoring_active of this OctoPrintDeviceKey.  # noqa: E501


        :return: The monitoring_active of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: bool
        """
        return self._monitoring_active

    @monitoring_active.setter
    def monitoring_active(self, monitoring_active):
        """Sets the monitoring_active of this OctoPrintDeviceKey.


        :param monitoring_active: The monitoring_active of this OctoPrintDeviceKey.  # noqa: E501
        :type monitoring_active: bool
        """

        self._monitoring_active = monitoring_active

    @property
    def monitoring_mode(self):
        """Gets the monitoring_mode of this OctoPrintDeviceKey.  # noqa: E501


        :return: The monitoring_mode of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: MonitoringModeEnum
        """
        return self._monitoring_mode

    @monitoring_mode.setter
    def monitoring_mode(self, monitoring_mode):
        """Sets the monitoring_mode of this OctoPrintDeviceKey.


        :param monitoring_mode: The monitoring_mode of this OctoPrintDeviceKey.  # noqa: E501
        :type monitoring_mode: MonitoringModeEnum
        """

        self._monitoring_mode = monitoring_mode

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this OctoPrintDeviceKey.  # noqa: E501


        :return: The octoprint_version of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this OctoPrintDeviceKey.


        :param octoprint_version: The octoprint_version of this OctoPrintDeviceKey.  # noqa: E501
        :type octoprint_version: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_version is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 255):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `255`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def plugin_version(self):
        """Gets the plugin_version of this OctoPrintDeviceKey.  # noqa: E501


        :return: The plugin_version of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this OctoPrintDeviceKey.


        :param plugin_version: The plugin_version of this OctoPrintDeviceKey.  # noqa: E501
        :type plugin_version: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_version is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plugin_version is not None and len(plugin_version) > 255):
            raise ValueError("Invalid value for `plugin_version`, length must be less than or equal to `255`")  # noqa: E501

        self._plugin_version = plugin_version

    @property
    def print_nanny_client_version(self):
        """Gets the print_nanny_client_version of this OctoPrintDeviceKey.  # noqa: E501


        :return: The print_nanny_client_version of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_client_version

    @print_nanny_client_version.setter
    def print_nanny_client_version(self, print_nanny_client_version):
        """Sets the print_nanny_client_version of this OctoPrintDeviceKey.


        :param print_nanny_client_version: The print_nanny_client_version of this OctoPrintDeviceKey.  # noqa: E501
        :type print_nanny_client_version: str
        """
        if self.local_vars_configuration.client_side_validation and print_nanny_client_version is None:  # noqa: E501
            raise ValueError("Invalid value for `print_nanny_client_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_client_version is not None and len(print_nanny_client_version) > 255):
            raise ValueError("Invalid value for `print_nanny_client_version`, length must be less than or equal to `255`")  # noqa: E501

        self._print_nanny_client_version = print_nanny_client_version

    @property
    def url(self):
        """Gets the url of this OctoPrintDeviceKey.  # noqa: E501


        :return: The url of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OctoPrintDeviceKey.


        :param url: The url of this OctoPrintDeviceKey.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def private_key(self):
        """Gets the private_key of this OctoPrintDeviceKey.  # noqa: E501


        :return: The private_key of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this OctoPrintDeviceKey.


        :param private_key: The private_key of this OctoPrintDeviceKey.  # noqa: E501
        :type private_key: str
        """

        self._private_key = private_key

    @property
    def private_key_checksum(self):
        """Gets the private_key_checksum of this OctoPrintDeviceKey.  # noqa: E501


        :return: The private_key_checksum of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._private_key_checksum

    @private_key_checksum.setter
    def private_key_checksum(self, private_key_checksum):
        """Sets the private_key_checksum of this OctoPrintDeviceKey.


        :param private_key_checksum: The private_key_checksum of this OctoPrintDeviceKey.  # noqa: E501
        :type private_key_checksum: str
        """

        self._private_key_checksum = private_key_checksum

    @property
    def public_key_checksum(self):
        """Gets the public_key_checksum of this OctoPrintDeviceKey.  # noqa: E501


        :return: The public_key_checksum of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._public_key_checksum

    @public_key_checksum.setter
    def public_key_checksum(self, public_key_checksum):
        """Sets the public_key_checksum of this OctoPrintDeviceKey.


        :param public_key_checksum: The public_key_checksum of this OctoPrintDeviceKey.  # noqa: E501
        :type public_key_checksum: str
        """
        if self.local_vars_configuration.client_side_validation and public_key_checksum is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key_checksum`, must not be `None`")  # noqa: E501

        self._public_key_checksum = public_key_checksum

    @property
    def cloudiot_device_configs(self):
        """Gets the cloudiot_device_configs of this OctoPrintDeviceKey.  # noqa: E501


        :return: The cloudiot_device_configs of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._cloudiot_device_configs

    @cloudiot_device_configs.setter
    def cloudiot_device_configs(self, cloudiot_device_configs):
        """Sets the cloudiot_device_configs of this OctoPrintDeviceKey.


        :param cloudiot_device_configs: The cloudiot_device_configs of this OctoPrintDeviceKey.  # noqa: E501
        :type cloudiot_device_configs: str
        """

        self._cloudiot_device_configs = cloudiot_device_configs

    @property
    def ca_certs(self):
        """Gets the ca_certs of this OctoPrintDeviceKey.  # noqa: E501


        :return: The ca_certs of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._ca_certs

    @ca_certs.setter
    def ca_certs(self, ca_certs):
        """Sets the ca_certs of this OctoPrintDeviceKey.


        :param ca_certs: The ca_certs of this OctoPrintDeviceKey.  # noqa: E501
        :type ca_certs: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and ca_certs is None:  # noqa: E501
            raise ValueError("Invalid value for `ca_certs`, must not be `None`")  # noqa: E501

        self._ca_certs = ca_certs

    @property
    def manage_url(self):
        """Gets the manage_url of this OctoPrintDeviceKey.  # noqa: E501


        :return: The manage_url of this OctoPrintDeviceKey.  # noqa: E501
        :rtype: str
        """
        return self._manage_url

    @manage_url.setter
    def manage_url(self, manage_url):
        """Sets the manage_url of this OctoPrintDeviceKey.


        :param manage_url: The manage_url of this OctoPrintDeviceKey.  # noqa: E501
        :type manage_url: str
        """

        self._manage_url = manage_url

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
        if not isinstance(other, OctoPrintDeviceKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoPrintDeviceKey):
            return True

        return self.to_dict() != other.to_dict()
