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


class OctoPrintDeviceKeyRequest(object):
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
        'name': 'str',
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
        'octoprint_version': 'str',
        'plugin_version': 'str',
        'print_nanny_client_version': 'str'
    }

    attribute_map = {
        'name': 'name',
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
        'octoprint_version': 'octoprint_version',
        'plugin_version': 'plugin_version',
        'print_nanny_client_version': 'print_nanny_client_version'
    }

    def __init__(self, name=None, model=None, platform=None, cpu_flags=None, hardware=None, revision=None, serial=None, cores=None, ram=None, python_version=None, pip_version=None, virtualenv=None, monitoring_active=None, octoprint_version=None, plugin_version=None, print_nanny_client_version=None, local_vars_configuration=None):  # noqa: E501
        """OctoPrintDeviceKeyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
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
        self._octoprint_version = None
        self._plugin_version = None
        self._print_nanny_client_version = None
        self.discriminator = None

        self.name = name
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
        self.octoprint_version = octoprint_version
        self.plugin_version = plugin_version
        self.print_nanny_client_version = print_nanny_client_version

    @property
    def name(self):
        """Gets the name of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The name of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OctoPrintDeviceKeyRequest.


        :param name: The name of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def model(self):
        """Gets the model of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The model of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this OctoPrintDeviceKeyRequest.


        :param model: The model of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the platform of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The platform of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this OctoPrintDeviceKeyRequest.


        :param platform: The platform of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the cpu_flags of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The cpu_flags of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cpu_flags

    @cpu_flags.setter
    def cpu_flags(self, cpu_flags):
        """Sets the cpu_flags of this OctoPrintDeviceKeyRequest.


        :param cpu_flags: The cpu_flags of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :type cpu_flags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and cpu_flags is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu_flags`, must not be `None`")  # noqa: E501

        self._cpu_flags = cpu_flags

    @property
    def hardware(self):
        """Gets the hardware of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The hardware of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this OctoPrintDeviceKeyRequest.


        :param hardware: The hardware of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :type hardware: str
        """
        if self.local_vars_configuration.client_side_validation and hardware is None:  # noqa: E501
            raise ValueError("Invalid value for `hardware`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) > 255):
            raise ValueError("Invalid value for `hardware`, length must be less than or equal to `255`")  # noqa: E501

        self._hardware = hardware

    @property
    def revision(self):
        """Gets the revision of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The revision of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this OctoPrintDeviceKeyRequest.


        :param revision: The revision of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :type revision: str
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501

        self._revision = revision

    @property
    def serial(self):
        """Gets the serial of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The serial of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this OctoPrintDeviceKeyRequest.


        :param serial: The serial of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the cores of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The cores of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this OctoPrintDeviceKeyRequest.


        :param cores: The cores of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the ram of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The ram of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this OctoPrintDeviceKeyRequest.


        :param ram: The ram of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the python_version of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The python_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this OctoPrintDeviceKeyRequest.


        :param python_version: The python_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the pip_version of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The pip_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._pip_version

    @pip_version.setter
    def pip_version(self, pip_version):
        """Sets the pip_version of this OctoPrintDeviceKeyRequest.


        :param pip_version: The pip_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the virtualenv of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The virtualenv of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtualenv

    @virtualenv.setter
    def virtualenv(self, virtualenv):
        """Sets the virtualenv of this OctoPrintDeviceKeyRequest.


        :param virtualenv: The virtualenv of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :type virtualenv: str
        """
        if self.local_vars_configuration.client_side_validation and virtualenv is None:  # noqa: E501
            raise ValueError("Invalid value for `virtualenv`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                virtualenv is not None and len(virtualenv) > 255):
            raise ValueError("Invalid value for `virtualenv`, length must be less than or equal to `255`")  # noqa: E501

        self._virtualenv = virtualenv

    @property
    def monitoring_active(self):
        """Gets the monitoring_active of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The monitoring_active of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._monitoring_active

    @monitoring_active.setter
    def monitoring_active(self, monitoring_active):
        """Sets the monitoring_active of this OctoPrintDeviceKeyRequest.


        :param monitoring_active: The monitoring_active of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :type monitoring_active: bool
        """

        self._monitoring_active = monitoring_active

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The octoprint_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this OctoPrintDeviceKeyRequest.


        :param octoprint_version: The octoprint_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the plugin_version of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The plugin_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this OctoPrintDeviceKeyRequest.


        :param plugin_version: The plugin_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
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
        """Gets the print_nanny_client_version of this OctoPrintDeviceKeyRequest.  # noqa: E501


        :return: The print_nanny_client_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_client_version

    @print_nanny_client_version.setter
    def print_nanny_client_version(self, print_nanny_client_version):
        """Sets the print_nanny_client_version of this OctoPrintDeviceKeyRequest.


        :param print_nanny_client_version: The print_nanny_client_version of this OctoPrintDeviceKeyRequest.  # noqa: E501
        :type print_nanny_client_version: str
        """
        if self.local_vars_configuration.client_side_validation and print_nanny_client_version is None:  # noqa: E501
            raise ValueError("Invalid value for `print_nanny_client_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_client_version is not None and len(print_nanny_client_version) > 255):
            raise ValueError("Invalid value for `print_nanny_client_version`, length must be less than or equal to `255`")  # noqa: E501

        self._print_nanny_client_version = print_nanny_client_version

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
        if not isinstance(other, OctoPrintDeviceKeyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoPrintDeviceKeyRequest):
            return True

        return self.to_dict() != other.to_dict()
