# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.120.1
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


class PatchedSystemInfoRequest(object):
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
        'machine_id': 'str',
        'revision': 'str',
        'model': 'str',
        'serial': 'str',
        'cores': 'int',
        'ram': 'int',
        'os_version_id': 'str',
        'os_build_id': 'datetime',
        'os_release_json': 'dict(str, object)',
        'uptime': 'int',
        'rootfs_size': 'int',
        'rootfs_used': 'int',
        'bootfs_size': 'int',
        'bootfs_used': 'int',
        'datafs_size': 'int',
        'datafs_used': 'int',
        'pi': 'int'
    }

    attribute_map = {
        'machine_id': 'machine_id',
        'revision': 'revision',
        'model': 'model',
        'serial': 'serial',
        'cores': 'cores',
        'ram': 'ram',
        'os_version_id': 'os_version_id',
        'os_build_id': 'os_build_id',
        'os_release_json': 'os_release_json',
        'uptime': 'uptime',
        'rootfs_size': 'rootfs_size',
        'rootfs_used': 'rootfs_used',
        'bootfs_size': 'bootfs_size',
        'bootfs_used': 'bootfs_used',
        'datafs_size': 'datafs_size',
        'datafs_used': 'datafs_used',
        'pi': 'pi'
    }

    def __init__(self, machine_id=None, revision=None, model=None, serial=None, cores=None, ram=None, os_version_id=None, os_build_id=None, os_release_json=None, uptime=None, rootfs_size=None, rootfs_used=None, bootfs_size=None, bootfs_used=None, datafs_size=None, datafs_used=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """PatchedSystemInfoRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._machine_id = None
        self._revision = None
        self._model = None
        self._serial = None
        self._cores = None
        self._ram = None
        self._os_version_id = None
        self._os_build_id = None
        self._os_release_json = None
        self._uptime = None
        self._rootfs_size = None
        self._rootfs_used = None
        self._bootfs_size = None
        self._bootfs_used = None
        self._datafs_size = None
        self._datafs_used = None
        self._pi = None
        self.discriminator = None

        if machine_id is not None:
            self.machine_id = machine_id
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
        if os_version_id is not None:
            self.os_version_id = os_version_id
        if os_build_id is not None:
            self.os_build_id = os_build_id
        if os_release_json is not None:
            self.os_release_json = os_release_json
        if uptime is not None:
            self.uptime = uptime
        if rootfs_size is not None:
            self.rootfs_size = rootfs_size
        if rootfs_used is not None:
            self.rootfs_used = rootfs_used
        if bootfs_size is not None:
            self.bootfs_size = bootfs_size
        if bootfs_used is not None:
            self.bootfs_used = bootfs_used
        if datafs_size is not None:
            self.datafs_size = datafs_size
        if datafs_used is not None:
            self.datafs_used = datafs_used
        if pi is not None:
            self.pi = pi

    @property
    def machine_id(self):
        """Gets the machine_id of this PatchedSystemInfoRequest.  # noqa: E501

        Populated from /etc/machine-id  # noqa: E501

        :return: The machine_id of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this PatchedSystemInfoRequest.

        Populated from /etc/machine-id  # noqa: E501

        :param machine_id: The machine_id of this PatchedSystemInfoRequest.  # noqa: E501
        :type machine_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                machine_id is not None and len(machine_id) > 255):
            raise ValueError("Invalid value for `machine_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                machine_id is not None and len(machine_id) < 1):
            raise ValueError("Invalid value for `machine_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._machine_id = machine_id

    @property
    def revision(self):
        """Gets the revision of this PatchedSystemInfoRequest.  # noqa: E501

        Populated from /proc/cpuinfo REVISION  # noqa: E501

        :return: The revision of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this PatchedSystemInfoRequest.

        Populated from /proc/cpuinfo REVISION  # noqa: E501

        :param revision: The revision of this PatchedSystemInfoRequest.  # noqa: E501
        :type revision: str
        """
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) < 1):
            raise ValueError("Invalid value for `revision`, length must be greater than or equal to `1`")  # noqa: E501

        self._revision = revision

    @property
    def model(self):
        """Gets the model of this PatchedSystemInfoRequest.  # noqa: E501

        Populated from /proc/cpuinfo MODEL  # noqa: E501

        :return: The model of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PatchedSystemInfoRequest.

        Populated from /proc/cpuinfo MODEL  # noqa: E501

        :param model: The model of this PatchedSystemInfoRequest.  # noqa: E501
        :type model: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) < 1):
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `1`")  # noqa: E501

        self._model = model

    @property
    def serial(self):
        """Gets the serial of this PatchedSystemInfoRequest.  # noqa: E501

        Populated from /proc/cpuinfo SERIAL  # noqa: E501

        :return: The serial of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this PatchedSystemInfoRequest.

        Populated from /proc/cpuinfo SERIAL  # noqa: E501

        :param serial: The serial of this PatchedSystemInfoRequest.  # noqa: E501
        :type serial: str
        """
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 255):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) < 1):
            raise ValueError("Invalid value for `serial`, length must be greater than or equal to `1`")  # noqa: E501

        self._serial = serial

    @property
    def cores(self):
        """Gets the cores of this PatchedSystemInfoRequest.  # noqa: E501


        :return: The cores of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this PatchedSystemInfoRequest.


        :param cores: The cores of this PatchedSystemInfoRequest.  # noqa: E501
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
        """Gets the ram of this PatchedSystemInfoRequest.  # noqa: E501


        :return: The ram of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this PatchedSystemInfoRequest.


        :param ram: The ram of this PatchedSystemInfoRequest.  # noqa: E501
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
    def os_version_id(self):
        """Gets the os_version_id of this PatchedSystemInfoRequest.  # noqa: E501

        PrintNanny OS VERSION_ID from /etc/os-release  # noqa: E501

        :return: The os_version_id of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._os_version_id

    @os_version_id.setter
    def os_version_id(self, os_version_id):
        """Sets the os_version_id of this PatchedSystemInfoRequest.

        PrintNanny OS VERSION_ID from /etc/os-release  # noqa: E501

        :param os_version_id: The os_version_id of this PatchedSystemInfoRequest.  # noqa: E501
        :type os_version_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                os_version_id is not None and len(os_version_id) > 255):
            raise ValueError("Invalid value for `os_version_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                os_version_id is not None and len(os_version_id) < 1):
            raise ValueError("Invalid value for `os_version_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._os_version_id = os_version_id

    @property
    def os_build_id(self):
        """Gets the os_build_id of this PatchedSystemInfoRequest.  # noqa: E501

        PrintNanny OS BUILD_ID from /etc/os-release  # noqa: E501

        :return: The os_build_id of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._os_build_id

    @os_build_id.setter
    def os_build_id(self, os_build_id):
        """Sets the os_build_id of this PatchedSystemInfoRequest.

        PrintNanny OS BUILD_ID from /etc/os-release  # noqa: E501

        :param os_build_id: The os_build_id of this PatchedSystemInfoRequest.  # noqa: E501
        :type os_build_id: datetime
        """

        self._os_build_id = os_build_id

    @property
    def os_release_json(self):
        """Gets the os_release_json of this PatchedSystemInfoRequest.  # noqa: E501

        Full contents of /etc/os-release in key:value format  # noqa: E501

        :return: The os_release_json of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._os_release_json

    @os_release_json.setter
    def os_release_json(self, os_release_json):
        """Sets the os_release_json of this PatchedSystemInfoRequest.

        Full contents of /etc/os-release in key:value format  # noqa: E501

        :param os_release_json: The os_release_json of this PatchedSystemInfoRequest.  # noqa: E501
        :type os_release_json: dict(str, object)
        """

        self._os_release_json = os_release_json

    @property
    def uptime(self):
        """Gets the uptime of this PatchedSystemInfoRequest.  # noqa: E501

        system uptime (in seconds)  # noqa: E501

        :return: The uptime of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this PatchedSystemInfoRequest.

        system uptime (in seconds)  # noqa: E501

        :param uptime: The uptime of this PatchedSystemInfoRequest.  # noqa: E501
        :type uptime: int
        """
        if (self.local_vars_configuration.client_side_validation and
                uptime is not None and uptime > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `uptime`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uptime is not None and uptime < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `uptime`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._uptime = uptime

    @property
    def rootfs_size(self):
        """Gets the rootfs_size of this PatchedSystemInfoRequest.  # noqa: E501

        Size of /dev/root filesystem in bytes  # noqa: E501

        :return: The rootfs_size of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._rootfs_size

    @rootfs_size.setter
    def rootfs_size(self, rootfs_size):
        """Sets the rootfs_size of this PatchedSystemInfoRequest.

        Size of /dev/root filesystem in bytes  # noqa: E501

        :param rootfs_size: The rootfs_size of this PatchedSystemInfoRequest.  # noqa: E501
        :type rootfs_size: int
        """
        if (self.local_vars_configuration.client_side_validation and
                rootfs_size is not None and rootfs_size > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `rootfs_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rootfs_size is not None and rootfs_size < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `rootfs_size`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._rootfs_size = rootfs_size

    @property
    def rootfs_used(self):
        """Gets the rootfs_used of this PatchedSystemInfoRequest.  # noqa: E501

        Space used in /dev/root filesystem in bytes  # noqa: E501

        :return: The rootfs_used of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._rootfs_used

    @rootfs_used.setter
    def rootfs_used(self, rootfs_used):
        """Sets the rootfs_used of this PatchedSystemInfoRequest.

        Space used in /dev/root filesystem in bytes  # noqa: E501

        :param rootfs_used: The rootfs_used of this PatchedSystemInfoRequest.  # noqa: E501
        :type rootfs_used: int
        """
        if (self.local_vars_configuration.client_side_validation and
                rootfs_used is not None and rootfs_used > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `rootfs_used`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rootfs_used is not None and rootfs_used < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `rootfs_used`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._rootfs_used = rootfs_used

    @property
    def bootfs_size(self):
        """Gets the bootfs_size of this PatchedSystemInfoRequest.  # noqa: E501

        Size of /dev/mmcblk0p1 filesystem in bytes  # noqa: E501

        :return: The bootfs_size of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._bootfs_size

    @bootfs_size.setter
    def bootfs_size(self, bootfs_size):
        """Sets the bootfs_size of this PatchedSystemInfoRequest.

        Size of /dev/mmcblk0p1 filesystem in bytes  # noqa: E501

        :param bootfs_size: The bootfs_size of this PatchedSystemInfoRequest.  # noqa: E501
        :type bootfs_size: int
        """
        if (self.local_vars_configuration.client_side_validation and
                bootfs_size is not None and bootfs_size > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `bootfs_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bootfs_size is not None and bootfs_size < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `bootfs_size`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._bootfs_size = bootfs_size

    @property
    def bootfs_used(self):
        """Gets the bootfs_used of this PatchedSystemInfoRequest.  # noqa: E501

        Space used in /dev/mmcblk0p1 filesystem in bytes  # noqa: E501

        :return: The bootfs_used of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._bootfs_used

    @bootfs_used.setter
    def bootfs_used(self, bootfs_used):
        """Sets the bootfs_used of this PatchedSystemInfoRequest.

        Space used in /dev/mmcblk0p1 filesystem in bytes  # noqa: E501

        :param bootfs_used: The bootfs_used of this PatchedSystemInfoRequest.  # noqa: E501
        :type bootfs_used: int
        """
        if (self.local_vars_configuration.client_side_validation and
                bootfs_used is not None and bootfs_used > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `bootfs_used`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bootfs_used is not None and bootfs_used < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `bootfs_used`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._bootfs_used = bootfs_used

    @property
    def datafs_size(self):
        """Gets the datafs_size of this PatchedSystemInfoRequest.  # noqa: E501

        Size of /dev/mmcblk0p4 filesystem in bytes  # noqa: E501

        :return: The datafs_size of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._datafs_size

    @datafs_size.setter
    def datafs_size(self, datafs_size):
        """Sets the datafs_size of this PatchedSystemInfoRequest.

        Size of /dev/mmcblk0p4 filesystem in bytes  # noqa: E501

        :param datafs_size: The datafs_size of this PatchedSystemInfoRequest.  # noqa: E501
        :type datafs_size: int
        """
        if (self.local_vars_configuration.client_side_validation and
                datafs_size is not None and datafs_size > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `datafs_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                datafs_size is not None and datafs_size < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `datafs_size`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._datafs_size = datafs_size

    @property
    def datafs_used(self):
        """Gets the datafs_used of this PatchedSystemInfoRequest.  # noqa: E501

        Space used in /dev/mmcblk0p4 filesystem in bytes  # noqa: E501

        :return: The datafs_used of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._datafs_used

    @datafs_used.setter
    def datafs_used(self, datafs_used):
        """Sets the datafs_used of this PatchedSystemInfoRequest.

        Space used in /dev/mmcblk0p4 filesystem in bytes  # noqa: E501

        :param datafs_used: The datafs_used of this PatchedSystemInfoRequest.  # noqa: E501
        :type datafs_used: int
        """
        if (self.local_vars_configuration.client_side_validation and
                datafs_used is not None and datafs_used > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `datafs_used`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                datafs_used is not None and datafs_used < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `datafs_used`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._datafs_used = datafs_used

    @property
    def pi(self):
        """Gets the pi of this PatchedSystemInfoRequest.  # noqa: E501


        :return: The pi of this PatchedSystemInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PatchedSystemInfoRequest.


        :param pi: The pi of this PatchedSystemInfoRequest.  # noqa: E501
        :type pi: int
        """

        self._pi = pi

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
        if not isinstance(other, PatchedSystemInfoRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedSystemInfoRequest):
            return True

        return self.to_dict() != other.to_dict()
