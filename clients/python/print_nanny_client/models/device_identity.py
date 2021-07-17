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


class DeviceIdentity(object):
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
        'updated_dt': 'datetime',
        'user': 'int',
        'name': 'str',
        'public_key': 'str',
        'fingerprint': 'str',
        'cloudiot_device': 'dict(str, object)',
        'cloudiot_device_name': 'str',
        'cloudiot_device_path': 'str',
        'cloudiot_device_num_id': 'int',
        'os_version': 'str',
        'os': 'str',
        'kernel_version': 'str',
        'hardware': 'str',
        'revision': 'str',
        'model': 'str',
        'serial': 'str',
        'cores': 'int',
        'ram': 'int',
        'cpu_flags': 'list[str]',
        'url': 'str',
        'private_key': 'str',
        'private_key_checksum': 'str',
        'public_key_checksum': 'str',
        'cloudiot_device_configs': 'str',
        'ca_certs': 'DeviceIdentityCaCerts'
    }

    attribute_map = {
        'id': 'id',
        'deleted': 'deleted',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'user': 'user',
        'name': 'name',
        'public_key': 'public_key',
        'fingerprint': 'fingerprint',
        'cloudiot_device': 'cloudiot_device',
        'cloudiot_device_name': 'cloudiot_device_name',
        'cloudiot_device_path': 'cloudiot_device_path',
        'cloudiot_device_num_id': 'cloudiot_device_num_id',
        'os_version': 'os_version',
        'os': 'os',
        'kernel_version': 'kernel_version',
        'hardware': 'hardware',
        'revision': 'revision',
        'model': 'model',
        'serial': 'serial',
        'cores': 'cores',
        'ram': 'ram',
        'cpu_flags': 'cpu_flags',
        'url': 'url',
        'private_key': 'private_key',
        'private_key_checksum': 'private_key_checksum',
        'public_key_checksum': 'public_key_checksum',
        'cloudiot_device_configs': 'cloudiot_device_configs',
        'ca_certs': 'ca_certs'
    }

    def __init__(self, id=None, deleted=None, created_dt=None, updated_dt=None, user=None, name=None, public_key=None, fingerprint=None, cloudiot_device=None, cloudiot_device_name=None, cloudiot_device_path=None, cloudiot_device_num_id=None, os_version=None, os=None, kernel_version=None, hardware=None, revision=None, model=None, serial=None, cores=None, ram=None, cpu_flags=None, url=None, private_key=None, private_key_checksum=None, public_key_checksum=None, cloudiot_device_configs=None, ca_certs=None, local_vars_configuration=None):  # noqa: E501
        """DeviceIdentity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deleted = None
        self._created_dt = None
        self._updated_dt = None
        self._user = None
        self._name = None
        self._public_key = None
        self._fingerprint = None
        self._cloudiot_device = None
        self._cloudiot_device_name = None
        self._cloudiot_device_path = None
        self._cloudiot_device_num_id = None
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
        self._url = None
        self._private_key = None
        self._private_key_checksum = None
        self._public_key_checksum = None
        self._cloudiot_device_configs = None
        self._ca_certs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if deleted is not None:
            self.deleted = deleted
        if created_dt is not None:
            self.created_dt = created_dt
        if updated_dt is not None:
            self.updated_dt = updated_dt
        if user is not None:
            self.user = user
        self.name = name
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
        self.os_version = os_version
        self.os = os
        self.kernel_version = kernel_version
        self.hardware = hardware
        self.revision = revision
        self.model = model
        self.serial = serial
        self.cores = cores
        self.ram = ram
        self.cpu_flags = cpu_flags
        if url is not None:
            self.url = url
        if private_key is not None:
            self.private_key = private_key
        if private_key_checksum is not None:
            self.private_key_checksum = private_key_checksum
        if public_key_checksum is not None:
            self.public_key_checksum = public_key_checksum
        if cloudiot_device_configs is not None:
            self.cloudiot_device_configs = cloudiot_device_configs
        if ca_certs is not None:
            self.ca_certs = ca_certs

    @property
    def id(self):
        """Gets the id of this DeviceIdentity.  # noqa: E501


        :return: The id of this DeviceIdentity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceIdentity.


        :param id: The id of this DeviceIdentity.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def deleted(self):
        """Gets the deleted of this DeviceIdentity.  # noqa: E501


        :return: The deleted of this DeviceIdentity.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DeviceIdentity.


        :param deleted: The deleted of this DeviceIdentity.  # noqa: E501
        :type deleted: datetime
        """

        self._deleted = deleted

    @property
    def created_dt(self):
        """Gets the created_dt of this DeviceIdentity.  # noqa: E501


        :return: The created_dt of this DeviceIdentity.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this DeviceIdentity.


        :param created_dt: The created_dt of this DeviceIdentity.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this DeviceIdentity.  # noqa: E501


        :return: The updated_dt of this DeviceIdentity.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this DeviceIdentity.


        :param updated_dt: The updated_dt of this DeviceIdentity.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def user(self):
        """Gets the user of this DeviceIdentity.  # noqa: E501


        :return: The user of this DeviceIdentity.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DeviceIdentity.


        :param user: The user of this DeviceIdentity.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def name(self):
        """Gets the name of this DeviceIdentity.  # noqa: E501


        :return: The name of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceIdentity.


        :param name: The name of this DeviceIdentity.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def public_key(self):
        """Gets the public_key of this DeviceIdentity.  # noqa: E501


        :return: The public_key of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this DeviceIdentity.


        :param public_key: The public_key of this DeviceIdentity.  # noqa: E501
        :type public_key: str
        """

        self._public_key = public_key

    @property
    def fingerprint(self):
        """Gets the fingerprint of this DeviceIdentity.  # noqa: E501


        :return: The fingerprint of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this DeviceIdentity.


        :param fingerprint: The fingerprint of this DeviceIdentity.  # noqa: E501
        :type fingerprint: str
        """

        self._fingerprint = fingerprint

    @property
    def cloudiot_device(self):
        """Gets the cloudiot_device of this DeviceIdentity.  # noqa: E501


        :return: The cloudiot_device of this DeviceIdentity.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._cloudiot_device

    @cloudiot_device.setter
    def cloudiot_device(self, cloudiot_device):
        """Sets the cloudiot_device of this DeviceIdentity.


        :param cloudiot_device: The cloudiot_device of this DeviceIdentity.  # noqa: E501
        :type cloudiot_device: dict(str, object)
        """

        self._cloudiot_device = cloudiot_device

    @property
    def cloudiot_device_name(self):
        """Gets the cloudiot_device_name of this DeviceIdentity.  # noqa: E501


        :return: The cloudiot_device_name of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._cloudiot_device_name

    @cloudiot_device_name.setter
    def cloudiot_device_name(self, cloudiot_device_name):
        """Sets the cloudiot_device_name of this DeviceIdentity.


        :param cloudiot_device_name: The cloudiot_device_name of this DeviceIdentity.  # noqa: E501
        :type cloudiot_device_name: str
        """

        self._cloudiot_device_name = cloudiot_device_name

    @property
    def cloudiot_device_path(self):
        """Gets the cloudiot_device_path of this DeviceIdentity.  # noqa: E501


        :return: The cloudiot_device_path of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._cloudiot_device_path

    @cloudiot_device_path.setter
    def cloudiot_device_path(self, cloudiot_device_path):
        """Sets the cloudiot_device_path of this DeviceIdentity.


        :param cloudiot_device_path: The cloudiot_device_path of this DeviceIdentity.  # noqa: E501
        :type cloudiot_device_path: str
        """

        self._cloudiot_device_path = cloudiot_device_path

    @property
    def cloudiot_device_num_id(self):
        """Gets the cloudiot_device_num_id of this DeviceIdentity.  # noqa: E501


        :return: The cloudiot_device_num_id of this DeviceIdentity.  # noqa: E501
        :rtype: int
        """
        return self._cloudiot_device_num_id

    @cloudiot_device_num_id.setter
    def cloudiot_device_num_id(self, cloudiot_device_num_id):
        """Sets the cloudiot_device_num_id of this DeviceIdentity.


        :param cloudiot_device_num_id: The cloudiot_device_num_id of this DeviceIdentity.  # noqa: E501
        :type cloudiot_device_num_id: int
        """

        self._cloudiot_device_num_id = cloudiot_device_num_id

    @property
    def os_version(self):
        """Gets the os_version of this DeviceIdentity.  # noqa: E501


        :return: The os_version of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this DeviceIdentity.


        :param os_version: The os_version of this DeviceIdentity.  # noqa: E501
        :type os_version: str
        """
        if self.local_vars_configuration.client_side_validation and os_version is None:  # noqa: E501
            raise ValueError("Invalid value for `os_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                os_version is not None and len(os_version) > 255):
            raise ValueError("Invalid value for `os_version`, length must be less than or equal to `255`")  # noqa: E501

        self._os_version = os_version

    @property
    def os(self):
        """Gets the os of this DeviceIdentity.  # noqa: E501


        :return: The os of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this DeviceIdentity.


        :param os: The os of this DeviceIdentity.  # noqa: E501
        :type os: str
        """
        if self.local_vars_configuration.client_side_validation and os is None:  # noqa: E501
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                os is not None and len(os) > 255):
            raise ValueError("Invalid value for `os`, length must be less than or equal to `255`")  # noqa: E501

        self._os = os

    @property
    def kernel_version(self):
        """Gets the kernel_version of this DeviceIdentity.  # noqa: E501


        :return: The kernel_version of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this DeviceIdentity.


        :param kernel_version: The kernel_version of this DeviceIdentity.  # noqa: E501
        :type kernel_version: str
        """
        if self.local_vars_configuration.client_side_validation and kernel_version is None:  # noqa: E501
            raise ValueError("Invalid value for `kernel_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                kernel_version is not None and len(kernel_version) > 255):
            raise ValueError("Invalid value for `kernel_version`, length must be less than or equal to `255`")  # noqa: E501

        self._kernel_version = kernel_version

    @property
    def hardware(self):
        """Gets the hardware of this DeviceIdentity.  # noqa: E501


        :return: The hardware of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this DeviceIdentity.


        :param hardware: The hardware of this DeviceIdentity.  # noqa: E501
        :type hardware: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) > 255):
            raise ValueError("Invalid value for `hardware`, length must be less than or equal to `255`")  # noqa: E501

        self._hardware = hardware

    @property
    def revision(self):
        """Gets the revision of this DeviceIdentity.  # noqa: E501


        :return: The revision of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this DeviceIdentity.


        :param revision: The revision of this DeviceIdentity.  # noqa: E501
        :type revision: str
        """
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501

        self._revision = revision

    @property
    def model(self):
        """Gets the model of this DeviceIdentity.  # noqa: E501


        :return: The model of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DeviceIdentity.


        :param model: The model of this DeviceIdentity.  # noqa: E501
        :type model: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def serial(self):
        """Gets the serial of this DeviceIdentity.  # noqa: E501


        :return: The serial of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DeviceIdentity.


        :param serial: The serial of this DeviceIdentity.  # noqa: E501
        :type serial: str
        """
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 255):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `255`")  # noqa: E501

        self._serial = serial

    @property
    def cores(self):
        """Gets the cores of this DeviceIdentity.  # noqa: E501


        :return: The cores of this DeviceIdentity.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this DeviceIdentity.


        :param cores: The cores of this DeviceIdentity.  # noqa: E501
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
        """Gets the ram of this DeviceIdentity.  # noqa: E501


        :return: The ram of this DeviceIdentity.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this DeviceIdentity.


        :param ram: The ram of this DeviceIdentity.  # noqa: E501
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
    def cpu_flags(self):
        """Gets the cpu_flags of this DeviceIdentity.  # noqa: E501


        :return: The cpu_flags of this DeviceIdentity.  # noqa: E501
        :rtype: list[str]
        """
        return self._cpu_flags

    @cpu_flags.setter
    def cpu_flags(self, cpu_flags):
        """Sets the cpu_flags of this DeviceIdentity.


        :param cpu_flags: The cpu_flags of this DeviceIdentity.  # noqa: E501
        :type cpu_flags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and cpu_flags is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu_flags`, must not be `None`")  # noqa: E501

        self._cpu_flags = cpu_flags

    @property
    def url(self):
        """Gets the url of this DeviceIdentity.  # noqa: E501


        :return: The url of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DeviceIdentity.


        :param url: The url of this DeviceIdentity.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def private_key(self):
        """Gets the private_key of this DeviceIdentity.  # noqa: E501


        :return: The private_key of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this DeviceIdentity.


        :param private_key: The private_key of this DeviceIdentity.  # noqa: E501
        :type private_key: str
        """

        self._private_key = private_key

    @property
    def private_key_checksum(self):
        """Gets the private_key_checksum of this DeviceIdentity.  # noqa: E501


        :return: The private_key_checksum of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._private_key_checksum

    @private_key_checksum.setter
    def private_key_checksum(self, private_key_checksum):
        """Sets the private_key_checksum of this DeviceIdentity.


        :param private_key_checksum: The private_key_checksum of this DeviceIdentity.  # noqa: E501
        :type private_key_checksum: str
        """

        self._private_key_checksum = private_key_checksum

    @property
    def public_key_checksum(self):
        """Gets the public_key_checksum of this DeviceIdentity.  # noqa: E501


        :return: The public_key_checksum of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._public_key_checksum

    @public_key_checksum.setter
    def public_key_checksum(self, public_key_checksum):
        """Sets the public_key_checksum of this DeviceIdentity.


        :param public_key_checksum: The public_key_checksum of this DeviceIdentity.  # noqa: E501
        :type public_key_checksum: str
        """

        self._public_key_checksum = public_key_checksum

    @property
    def cloudiot_device_configs(self):
        """Gets the cloudiot_device_configs of this DeviceIdentity.  # noqa: E501


        :return: The cloudiot_device_configs of this DeviceIdentity.  # noqa: E501
        :rtype: str
        """
        return self._cloudiot_device_configs

    @cloudiot_device_configs.setter
    def cloudiot_device_configs(self, cloudiot_device_configs):
        """Sets the cloudiot_device_configs of this DeviceIdentity.


        :param cloudiot_device_configs: The cloudiot_device_configs of this DeviceIdentity.  # noqa: E501
        :type cloudiot_device_configs: str
        """

        self._cloudiot_device_configs = cloudiot_device_configs

    @property
    def ca_certs(self):
        """Gets the ca_certs of this DeviceIdentity.  # noqa: E501


        :return: The ca_certs of this DeviceIdentity.  # noqa: E501
        :rtype: DeviceIdentityCaCerts
        """
        return self._ca_certs

    @ca_certs.setter
    def ca_certs(self, ca_certs):
        """Sets the ca_certs of this DeviceIdentity.


        :param ca_certs: The ca_certs of this DeviceIdentity.  # noqa: E501
        :type ca_certs: DeviceIdentityCaCerts
        """

        self._ca_certs = ca_certs

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
        if not isinstance(other, DeviceIdentity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceIdentity):
            return True

        return self.to_dict() != other.to_dict()
