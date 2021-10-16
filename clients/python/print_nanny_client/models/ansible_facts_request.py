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


class AnsibleFactsRequest(object):
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
        'release_channel': 'ReleaseChannelEnum',
        'json': 'dict(str, object)'
    }

    attribute_map = {
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
        'release_channel': 'release_channel',
        'json': 'json'
    }

    def __init__(self, os_version=None, os=None, kernel_version=None, hardware=None, revision=None, model=None, serial=None, cores=None, ram=None, cpu_flags=None, release_channel=None, json=None, local_vars_configuration=None):  # noqa: E501
        """AnsibleFactsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

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
        self._release_channel = None
        self._json = None
        self.discriminator = None

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
        if release_channel is not None:
            self.release_channel = release_channel
        self.json = json

    @property
    def os_version(self):
        """Gets the os_version of this AnsibleFactsRequest.  # noqa: E501


        :return: The os_version of this AnsibleFactsRequest.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this AnsibleFactsRequest.


        :param os_version: The os_version of this AnsibleFactsRequest.  # noqa: E501
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
        """Gets the os of this AnsibleFactsRequest.  # noqa: E501


        :return: The os of this AnsibleFactsRequest.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this AnsibleFactsRequest.


        :param os: The os of this AnsibleFactsRequest.  # noqa: E501
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
        """Gets the kernel_version of this AnsibleFactsRequest.  # noqa: E501


        :return: The kernel_version of this AnsibleFactsRequest.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this AnsibleFactsRequest.


        :param kernel_version: The kernel_version of this AnsibleFactsRequest.  # noqa: E501
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
        """Gets the hardware of this AnsibleFactsRequest.  # noqa: E501


        :return: The hardware of this AnsibleFactsRequest.  # noqa: E501
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this AnsibleFactsRequest.


        :param hardware: The hardware of this AnsibleFactsRequest.  # noqa: E501
        :type hardware: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) > 255):
            raise ValueError("Invalid value for `hardware`, length must be less than or equal to `255`")  # noqa: E501

        self._hardware = hardware

    @property
    def revision(self):
        """Gets the revision of this AnsibleFactsRequest.  # noqa: E501


        :return: The revision of this AnsibleFactsRequest.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this AnsibleFactsRequest.


        :param revision: The revision of this AnsibleFactsRequest.  # noqa: E501
        :type revision: str
        """
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501

        self._revision = revision

    @property
    def model(self):
        """Gets the model of this AnsibleFactsRequest.  # noqa: E501


        :return: The model of this AnsibleFactsRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this AnsibleFactsRequest.


        :param model: The model of this AnsibleFactsRequest.  # noqa: E501
        :type model: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def serial(self):
        """Gets the serial of this AnsibleFactsRequest.  # noqa: E501


        :return: The serial of this AnsibleFactsRequest.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this AnsibleFactsRequest.


        :param serial: The serial of this AnsibleFactsRequest.  # noqa: E501
        :type serial: str
        """
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 255):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `255`")  # noqa: E501

        self._serial = serial

    @property
    def cores(self):
        """Gets the cores of this AnsibleFactsRequest.  # noqa: E501


        :return: The cores of this AnsibleFactsRequest.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this AnsibleFactsRequest.


        :param cores: The cores of this AnsibleFactsRequest.  # noqa: E501
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
        """Gets the ram of this AnsibleFactsRequest.  # noqa: E501


        :return: The ram of this AnsibleFactsRequest.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this AnsibleFactsRequest.


        :param ram: The ram of this AnsibleFactsRequest.  # noqa: E501
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
        """Gets the cpu_flags of this AnsibleFactsRequest.  # noqa: E501


        :return: The cpu_flags of this AnsibleFactsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cpu_flags

    @cpu_flags.setter
    def cpu_flags(self, cpu_flags):
        """Sets the cpu_flags of this AnsibleFactsRequest.


        :param cpu_flags: The cpu_flags of this AnsibleFactsRequest.  # noqa: E501
        :type cpu_flags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and cpu_flags is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu_flags`, must not be `None`")  # noqa: E501

        self._cpu_flags = cpu_flags

    @property
    def release_channel(self):
        """Gets the release_channel of this AnsibleFactsRequest.  # noqa: E501


        :return: The release_channel of this AnsibleFactsRequest.  # noqa: E501
        :rtype: ReleaseChannelEnum
        """
        return self._release_channel

    @release_channel.setter
    def release_channel(self, release_channel):
        """Sets the release_channel of this AnsibleFactsRequest.


        :param release_channel: The release_channel of this AnsibleFactsRequest.  # noqa: E501
        :type release_channel: ReleaseChannelEnum
        """

        self._release_channel = release_channel

    @property
    def json(self):
        """Gets the json of this AnsibleFactsRequest.  # noqa: E501


        :return: The json of this AnsibleFactsRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this AnsibleFactsRequest.


        :param json: The json of this AnsibleFactsRequest.  # noqa: E501
        :type json: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and json is None:  # noqa: E501
            raise ValueError("Invalid value for `json`, must not be `None`")  # noqa: E501

        self._json = json

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
        if not isinstance(other, AnsibleFactsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnsibleFactsRequest):
            return True

        return self.to_dict() != other.to_dict()
