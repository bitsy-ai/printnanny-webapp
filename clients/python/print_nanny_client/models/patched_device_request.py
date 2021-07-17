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


class PatchedDeviceRequest(object):
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
        'os_version': 'str',
        'os': 'str',
        'kernel_version': 'str',
        'hardware': 'str',
        'revision': 'str',
        'model': 'str',
        'serial': 'str',
        'cores': 'int',
        'ram': 'int',
        'cpu_flags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'os_version': 'os_version',
        'os': 'os',
        'kernel_version': 'kernel_version',
        'hardware': 'hardware',
        'revision': 'revision',
        'model': 'model',
        'serial': 'serial',
        'cores': 'cores',
        'ram': 'ram',
        'cpu_flags': 'cpu_flags'
    }

    def __init__(self, name=None, os_version=None, os=None, kernel_version=None, hardware=None, revision=None, model=None, serial=None, cores=None, ram=None, cpu_flags=None, local_vars_configuration=None):  # noqa: E501
        """PatchedDeviceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._os_version = None
        self._os = None
        self._kernel_version = None
        self._hardware = None
        self._revision = None
        self._model = None
        self._serial = None
        self._cores = None
        self._ram = None
        self._cpu_flags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if os_version is not None:
            self.os_version = os_version
        if os is not None:
            self.os = os
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if hardware is not None:
            self.hardware = hardware
        if revision is not None:
            self.revision = revision
        if model is not None:
            self.model = model
        if serial is not None:
            self.serial = serial
        if cores is not None:
            self.cores = cores
        if ram is not None:
            self.ram = ram
        if cpu_flags is not None:
            self.cpu_flags = cpu_flags

    @property
    def name(self):
        """Gets the name of this PatchedDeviceRequest.  # noqa: E501


        :return: The name of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedDeviceRequest.


        :param name: The name of this PatchedDeviceRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def os_version(self):
        """Gets the os_version of this PatchedDeviceRequest.  # noqa: E501


        :return: The os_version of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this PatchedDeviceRequest.


        :param os_version: The os_version of this PatchedDeviceRequest.  # noqa: E501
        :type os_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                os_version is not None and len(os_version) > 255):
            raise ValueError("Invalid value for `os_version`, length must be less than or equal to `255`")  # noqa: E501

        self._os_version = os_version

    @property
    def os(self):
        """Gets the os of this PatchedDeviceRequest.  # noqa: E501


        :return: The os of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this PatchedDeviceRequest.


        :param os: The os of this PatchedDeviceRequest.  # noqa: E501
        :type os: str
        """
        if (self.local_vars_configuration.client_side_validation and
                os is not None and len(os) > 255):
            raise ValueError("Invalid value for `os`, length must be less than or equal to `255`")  # noqa: E501

        self._os = os

    @property
    def kernel_version(self):
        """Gets the kernel_version of this PatchedDeviceRequest.  # noqa: E501


        :return: The kernel_version of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this PatchedDeviceRequest.


        :param kernel_version: The kernel_version of this PatchedDeviceRequest.  # noqa: E501
        :type kernel_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                kernel_version is not None and len(kernel_version) > 255):
            raise ValueError("Invalid value for `kernel_version`, length must be less than or equal to `255`")  # noqa: E501

        self._kernel_version = kernel_version

    @property
    def hardware(self):
        """Gets the hardware of this PatchedDeviceRequest.  # noqa: E501


        :return: The hardware of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this PatchedDeviceRequest.


        :param hardware: The hardware of this PatchedDeviceRequest.  # noqa: E501
        :type hardware: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) > 255):
            raise ValueError("Invalid value for `hardware`, length must be less than or equal to `255`")  # noqa: E501

        self._hardware = hardware

    @property
    def revision(self):
        """Gets the revision of this PatchedDeviceRequest.  # noqa: E501


        :return: The revision of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this PatchedDeviceRequest.


        :param revision: The revision of this PatchedDeviceRequest.  # noqa: E501
        :type revision: str
        """
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501

        self._revision = revision

    @property
    def model(self):
        """Gets the model of this PatchedDeviceRequest.  # noqa: E501


        :return: The model of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PatchedDeviceRequest.


        :param model: The model of this PatchedDeviceRequest.  # noqa: E501
        :type model: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def serial(self):
        """Gets the serial of this PatchedDeviceRequest.  # noqa: E501


        :return: The serial of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this PatchedDeviceRequest.


        :param serial: The serial of this PatchedDeviceRequest.  # noqa: E501
        :type serial: str
        """
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 255):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `255`")  # noqa: E501

        self._serial = serial

    @property
    def cores(self):
        """Gets the cores of this PatchedDeviceRequest.  # noqa: E501


        :return: The cores of this PatchedDeviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this PatchedDeviceRequest.


        :param cores: The cores of this PatchedDeviceRequest.  # noqa: E501
        :type cores: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._cores = cores

    @property
    def ram(self):
        """Gets the ram of this PatchedDeviceRequest.  # noqa: E501


        :return: The ram of this PatchedDeviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this PatchedDeviceRequest.


        :param ram: The ram of this PatchedDeviceRequest.  # noqa: E501
        :type ram: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._ram = ram

    @property
    def cpu_flags(self):
        """Gets the cpu_flags of this PatchedDeviceRequest.  # noqa: E501


        :return: The cpu_flags of this PatchedDeviceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cpu_flags

    @cpu_flags.setter
    def cpu_flags(self, cpu_flags):
        """Sets the cpu_flags of this PatchedDeviceRequest.


        :param cpu_flags: The cpu_flags of this PatchedDeviceRequest.  # noqa: E501
        :type cpu_flags: list[str]
        """

        self._cpu_flags = cpu_flags

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
        if not isinstance(other, PatchedDeviceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedDeviceRequest):
            return True

        return self.to_dict() != other.to_dict()
