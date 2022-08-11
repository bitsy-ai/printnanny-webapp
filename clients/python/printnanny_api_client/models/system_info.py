# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.8
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


class SystemInfo(object):
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
        'machine_id': 'str',
        'revision': 'str',
        'model': 'str',
        'serial': 'str',
        'cores': 'int',
        'ram': 'int',
        'os_version_id': 'str',
        'os_build_id': 'datetime',
        'os_variant_id': 'str',
        'os_release_json': 'dict(str, object)',
        'pi': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'machine_id': 'machine_id',
        'revision': 'revision',
        'model': 'model',
        'serial': 'serial',
        'cores': 'cores',
        'ram': 'ram',
        'os_version_id': 'os_version_id',
        'os_build_id': 'os_build_id',
        'os_variant_id': 'os_variant_id',
        'os_release_json': 'os_release_json',
        'pi': 'pi'
    }

    def __init__(self, id=None, created_dt=None, updated_dt=None, machine_id=None, revision=None, model=None, serial=None, cores=None, ram=None, os_version_id=None, os_build_id=None, os_variant_id=None, os_release_json=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """SystemInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._updated_dt = None
        self._machine_id = None
        self._revision = None
        self._model = None
        self._serial = None
        self._cores = None
        self._ram = None
        self._os_version_id = None
        self._os_build_id = None
        self._os_variant_id = None
        self._os_release_json = None
        self._pi = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.machine_id = machine_id
        self.revision = revision
        self.model = model
        self.serial = serial
        self.cores = cores
        self.ram = ram
        self.os_version_id = os_version_id
        self.os_build_id = os_build_id
        self.os_variant_id = os_variant_id
        if os_release_json is not None:
            self.os_release_json = os_release_json
        self.pi = pi

    @property
    def id(self):
        """Gets the id of this SystemInfo.  # noqa: E501


        :return: The id of this SystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SystemInfo.


        :param id: The id of this SystemInfo.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this SystemInfo.  # noqa: E501


        :return: The created_dt of this SystemInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this SystemInfo.


        :param created_dt: The created_dt of this SystemInfo.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this SystemInfo.  # noqa: E501


        :return: The updated_dt of this SystemInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this SystemInfo.


        :param updated_dt: The updated_dt of this SystemInfo.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def machine_id(self):
        """Gets the machine_id of this SystemInfo.  # noqa: E501

        Populated from /etc/machine-id  # noqa: E501

        :return: The machine_id of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this SystemInfo.

        Populated from /etc/machine-id  # noqa: E501

        :param machine_id: The machine_id of this SystemInfo.  # noqa: E501
        :type machine_id: str
        """
        if self.local_vars_configuration.client_side_validation and machine_id is None:  # noqa: E501
            raise ValueError("Invalid value for `machine_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                machine_id is not None and len(machine_id) > 255):
            raise ValueError("Invalid value for `machine_id`, length must be less than or equal to `255`")  # noqa: E501

        self._machine_id = machine_id

    @property
    def revision(self):
        """Gets the revision of this SystemInfo.  # noqa: E501

        Populated from /proc/cpuinfo REVISION  # noqa: E501

        :return: The revision of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this SystemInfo.

        Populated from /proc/cpuinfo REVISION  # noqa: E501

        :param revision: The revision of this SystemInfo.  # noqa: E501
        :type revision: str
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501

        self._revision = revision

    @property
    def model(self):
        """Gets the model of this SystemInfo.  # noqa: E501

        Populated from /proc/cpuinfo MODEL  # noqa: E501

        :return: The model of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this SystemInfo.

        Populated from /proc/cpuinfo MODEL  # noqa: E501

        :param model: The model of this SystemInfo.  # noqa: E501
        :type model: str
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def serial(self):
        """Gets the serial of this SystemInfo.  # noqa: E501

        Populated from /proc/cpuinfo SERIAL  # noqa: E501

        :return: The serial of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this SystemInfo.

        Populated from /proc/cpuinfo SERIAL  # noqa: E501

        :param serial: The serial of this SystemInfo.  # noqa: E501
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
        """Gets the cores of this SystemInfo.  # noqa: E501


        :return: The cores of this SystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this SystemInfo.


        :param cores: The cores of this SystemInfo.  # noqa: E501
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
        """Gets the ram of this SystemInfo.  # noqa: E501


        :return: The ram of this SystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this SystemInfo.


        :param ram: The ram of this SystemInfo.  # noqa: E501
        :type ram: int
        """
        if self.local_vars_configuration.client_side_validation and ram is None:  # noqa: E501
            raise ValueError("Invalid value for `ram`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._ram = ram

    @property
    def os_version_id(self):
        """Gets the os_version_id of this SystemInfo.  # noqa: E501

        PrintNanny OS VERSION_ID from /etc/os-release  # noqa: E501

        :return: The os_version_id of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._os_version_id

    @os_version_id.setter
    def os_version_id(self, os_version_id):
        """Sets the os_version_id of this SystemInfo.

        PrintNanny OS VERSION_ID from /etc/os-release  # noqa: E501

        :param os_version_id: The os_version_id of this SystemInfo.  # noqa: E501
        :type os_version_id: str
        """
        if self.local_vars_configuration.client_side_validation and os_version_id is None:  # noqa: E501
            raise ValueError("Invalid value for `os_version_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                os_version_id is not None and len(os_version_id) > 255):
            raise ValueError("Invalid value for `os_version_id`, length must be less than or equal to `255`")  # noqa: E501

        self._os_version_id = os_version_id

    @property
    def os_build_id(self):
        """Gets the os_build_id of this SystemInfo.  # noqa: E501

        PrintNanny OS BUILD_ID from /etc/os-release  # noqa: E501

        :return: The os_build_id of this SystemInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._os_build_id

    @os_build_id.setter
    def os_build_id(self, os_build_id):
        """Sets the os_build_id of this SystemInfo.

        PrintNanny OS BUILD_ID from /etc/os-release  # noqa: E501

        :param os_build_id: The os_build_id of this SystemInfo.  # noqa: E501
        :type os_build_id: datetime
        """
        if self.local_vars_configuration.client_side_validation and os_build_id is None:  # noqa: E501
            raise ValueError("Invalid value for `os_build_id`, must not be `None`")  # noqa: E501

        self._os_build_id = os_build_id

    @property
    def os_variant_id(self):
        """Gets the os_variant_id of this SystemInfo.  # noqa: E501

        PrintNanny OS VARIANT_ID from /etc/os-release  # noqa: E501

        :return: The os_variant_id of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._os_variant_id

    @os_variant_id.setter
    def os_variant_id(self, os_variant_id):
        """Sets the os_variant_id of this SystemInfo.

        PrintNanny OS VARIANT_ID from /etc/os-release  # noqa: E501

        :param os_variant_id: The os_variant_id of this SystemInfo.  # noqa: E501
        :type os_variant_id: str
        """
        if self.local_vars_configuration.client_side_validation and os_variant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `os_variant_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                os_variant_id is not None and len(os_variant_id) > 255):
            raise ValueError("Invalid value for `os_variant_id`, length must be less than or equal to `255`")  # noqa: E501

        self._os_variant_id = os_variant_id

    @property
    def os_release_json(self):
        """Gets the os_release_json of this SystemInfo.  # noqa: E501

        Full contents of /etc/os-release in key:value format  # noqa: E501

        :return: The os_release_json of this SystemInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._os_release_json

    @os_release_json.setter
    def os_release_json(self, os_release_json):
        """Sets the os_release_json of this SystemInfo.

        Full contents of /etc/os-release in key:value format  # noqa: E501

        :param os_release_json: The os_release_json of this SystemInfo.  # noqa: E501
        :type os_release_json: dict(str, object)
        """

        self._os_release_json = os_release_json

    @property
    def pi(self):
        """Gets the pi of this SystemInfo.  # noqa: E501


        :return: The pi of this SystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this SystemInfo.


        :param pi: The pi of this SystemInfo.  # noqa: E501
        :type pi: int
        """
        if self.local_vars_configuration.client_side_validation and pi is None:  # noqa: E501
            raise ValueError("Invalid value for `pi`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, SystemInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemInfo):
            return True

        return self.to_dict() != other.to_dict()
