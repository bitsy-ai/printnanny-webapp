# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
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


class DeviceInfoRequest(object):
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
        'hardware': 'str',
        'revision': 'str',
        'model': 'str',
        'serial': 'str',
        'cores': 'int',
        'ram': 'int',
        'image_version': 'str',
        'device': 'int'
    }

    attribute_map = {
        'machine_id': 'machine_id',
        'hardware': 'hardware',
        'revision': 'revision',
        'model': 'model',
        'serial': 'serial',
        'cores': 'cores',
        'ram': 'ram',
        'image_version': 'image_version',
        'device': 'device'
    }

    def __init__(self, machine_id=None, hardware=None, revision=None, model=None, serial=None, cores=None, ram=None, image_version=None, device=None, local_vars_configuration=None):  # noqa: E501
        """DeviceInfoRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._machine_id = None
        self._hardware = None
        self._revision = None
        self._model = None
        self._serial = None
        self._cores = None
        self._ram = None
        self._image_version = None
        self._device = None
        self.discriminator = None

        self.machine_id = machine_id
        self.hardware = hardware
        self.revision = revision
        self.model = model
        self.serial = serial
        self.cores = cores
        self.ram = ram
        self.image_version = image_version
        self.device = device

    @property
    def machine_id(self):
        """Gets the machine_id of this DeviceInfoRequest.  # noqa: E501

        Populated from /etc/machine-id  # noqa: E501

        :return: The machine_id of this DeviceInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this DeviceInfoRequest.

        Populated from /etc/machine-id  # noqa: E501

        :param machine_id: The machine_id of this DeviceInfoRequest.  # noqa: E501
        :type machine_id: str
        """
        if self.local_vars_configuration.client_side_validation and machine_id is None:  # noqa: E501
            raise ValueError("Invalid value for `machine_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                machine_id is not None and len(machine_id) > 255):
            raise ValueError("Invalid value for `machine_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                machine_id is not None and len(machine_id) < 1):
            raise ValueError("Invalid value for `machine_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._machine_id = machine_id

    @property
    def hardware(self):
        """Gets the hardware of this DeviceInfoRequest.  # noqa: E501

        Populated from /proc/cpuinfo HARDWARE  # noqa: E501

        :return: The hardware of this DeviceInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this DeviceInfoRequest.

        Populated from /proc/cpuinfo HARDWARE  # noqa: E501

        :param hardware: The hardware of this DeviceInfoRequest.  # noqa: E501
        :type hardware: str
        """
        if self.local_vars_configuration.client_side_validation and hardware is None:  # noqa: E501
            raise ValueError("Invalid value for `hardware`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) > 255):
            raise ValueError("Invalid value for `hardware`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) < 1):
            raise ValueError("Invalid value for `hardware`, length must be greater than or equal to `1`")  # noqa: E501

        self._hardware = hardware

    @property
    def revision(self):
        """Gets the revision of this DeviceInfoRequest.  # noqa: E501

        Populated from /proc/cpuinfo REVISION  # noqa: E501

        :return: The revision of this DeviceInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this DeviceInfoRequest.

        Populated from /proc/cpuinfo REVISION  # noqa: E501

        :param revision: The revision of this DeviceInfoRequest.  # noqa: E501
        :type revision: str
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) < 1):
            raise ValueError("Invalid value for `revision`, length must be greater than or equal to `1`")  # noqa: E501

        self._revision = revision

    @property
    def model(self):
        """Gets the model of this DeviceInfoRequest.  # noqa: E501

        Populated from /proc/cpuinfo MODEL  # noqa: E501

        :return: The model of this DeviceInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DeviceInfoRequest.

        Populated from /proc/cpuinfo MODEL  # noqa: E501

        :param model: The model of this DeviceInfoRequest.  # noqa: E501
        :type model: str
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) < 1):
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `1`")  # noqa: E501

        self._model = model

    @property
    def serial(self):
        """Gets the serial of this DeviceInfoRequest.  # noqa: E501

        Populated from /proc/cpuinfo SERIAL  # noqa: E501

        :return: The serial of this DeviceInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DeviceInfoRequest.

        Populated from /proc/cpuinfo SERIAL  # noqa: E501

        :param serial: The serial of this DeviceInfoRequest.  # noqa: E501
        :type serial: str
        """
        if self.local_vars_configuration.client_side_validation and serial is None:  # noqa: E501
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 255):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) < 1):
            raise ValueError("Invalid value for `serial`, length must be greater than or equal to `1`")  # noqa: E501

        self._serial = serial

    @property
    def cores(self):
        """Gets the cores of this DeviceInfoRequest.  # noqa: E501


        :return: The cores of this DeviceInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this DeviceInfoRequest.


        :param cores: The cores of this DeviceInfoRequest.  # noqa: E501
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
        """Gets the ram of this DeviceInfoRequest.  # noqa: E501


        :return: The ram of this DeviceInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this DeviceInfoRequest.


        :param ram: The ram of this DeviceInfoRequest.  # noqa: E501
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
    def image_version(self):
        """Gets the image_version of this DeviceInfoRequest.  # noqa: E501

        Print Nanny OS version string from /boot/image_version.txt  # noqa: E501

        :return: The image_version of this DeviceInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this DeviceInfoRequest.

        Print Nanny OS version string from /boot/image_version.txt  # noqa: E501

        :param image_version: The image_version of this DeviceInfoRequest.  # noqa: E501
        :type image_version: str
        """
        if self.local_vars_configuration.client_side_validation and image_version is None:  # noqa: E501
            raise ValueError("Invalid value for `image_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_version is not None and len(image_version) > 255):
            raise ValueError("Invalid value for `image_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_version is not None and len(image_version) < 1):
            raise ValueError("Invalid value for `image_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_version = image_version

    @property
    def device(self):
        """Gets the device of this DeviceInfoRequest.  # noqa: E501


        :return: The device of this DeviceInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DeviceInfoRequest.


        :param device: The device of this DeviceInfoRequest.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

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
        if not isinstance(other, DeviceInfoRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceInfoRequest):
            return True

        return self.to_dict() != other.to_dict()
