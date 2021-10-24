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


class CloudiotDevice(object):
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
        'num_id': 'int',
        'gcp_project_id': 'str',
        'gcp_region': 'str',
        'gcp_cloudiot_device_registry': 'str',
        'mqtt_bridge_hostname': 'str',
        'mqtt_bridge_port': 'int',
        'mqtt_client_id': 'str',
        'user': 'str',
        'device': 'int',
        'deleted': 'datetime',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'num_id': 'num_id',
        'gcp_project_id': 'gcp_project_id',
        'gcp_region': 'gcp_region',
        'gcp_cloudiot_device_registry': 'gcp_cloudiot_device_registry',
        'mqtt_bridge_hostname': 'mqtt_bridge_hostname',
        'mqtt_bridge_port': 'mqtt_bridge_port',
        'mqtt_client_id': 'mqtt_client_id',
        'user': 'user',
        'device': 'device',
        'deleted': 'deleted',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, num_id=None, gcp_project_id=None, gcp_region=None, gcp_cloudiot_device_registry=None, mqtt_bridge_hostname=None, mqtt_bridge_port=None, mqtt_client_id=None, user=None, device=None, deleted=None, name=None, id=None, local_vars_configuration=None):  # noqa: E501
        """CloudiotDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._num_id = None
        self._gcp_project_id = None
        self._gcp_region = None
        self._gcp_cloudiot_device_registry = None
        self._mqtt_bridge_hostname = None
        self._mqtt_bridge_port = None
        self._mqtt_client_id = None
        self._user = None
        self._device = None
        self._deleted = None
        self._name = None
        self._id = None
        self.discriminator = None

        self.num_id = num_id
        if gcp_project_id is not None:
            self.gcp_project_id = gcp_project_id
        if gcp_region is not None:
            self.gcp_region = gcp_region
        if gcp_cloudiot_device_registry is not None:
            self.gcp_cloudiot_device_registry = gcp_cloudiot_device_registry
        if mqtt_bridge_hostname is not None:
            self.mqtt_bridge_hostname = mqtt_bridge_hostname
        if mqtt_bridge_port is not None:
            self.mqtt_bridge_port = mqtt_bridge_port
        if mqtt_client_id is not None:
            self.mqtt_client_id = mqtt_client_id
        if user is not None:
            self.user = user
        if device is not None:
            self.device = device
        if deleted is not None:
            self.deleted = deleted
        self.name = name
        self.id = id

    @property
    def num_id(self):
        """Gets the num_id of this CloudiotDevice.  # noqa: E501


        :return: The num_id of this CloudiotDevice.  # noqa: E501
        :rtype: int
        """
        return self._num_id

    @num_id.setter
    def num_id(self, num_id):
        """Sets the num_id of this CloudiotDevice.


        :param num_id: The num_id of this CloudiotDevice.  # noqa: E501
        :type num_id: int
        """
        if self.local_vars_configuration.client_side_validation and num_id is None:  # noqa: E501
            raise ValueError("Invalid value for `num_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_id is not None and num_id > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `num_id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_id is not None and num_id < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `num_id`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._num_id = num_id

    @property
    def gcp_project_id(self):
        """Gets the gcp_project_id of this CloudiotDevice.  # noqa: E501


        :return: The gcp_project_id of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._gcp_project_id

    @gcp_project_id.setter
    def gcp_project_id(self, gcp_project_id):
        """Sets the gcp_project_id of this CloudiotDevice.


        :param gcp_project_id: The gcp_project_id of this CloudiotDevice.  # noqa: E501
        :type gcp_project_id: str
        """

        self._gcp_project_id = gcp_project_id

    @property
    def gcp_region(self):
        """Gets the gcp_region of this CloudiotDevice.  # noqa: E501


        :return: The gcp_region of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._gcp_region

    @gcp_region.setter
    def gcp_region(self, gcp_region):
        """Sets the gcp_region of this CloudiotDevice.


        :param gcp_region: The gcp_region of this CloudiotDevice.  # noqa: E501
        :type gcp_region: str
        """

        self._gcp_region = gcp_region

    @property
    def gcp_cloudiot_device_registry(self):
        """Gets the gcp_cloudiot_device_registry of this CloudiotDevice.  # noqa: E501


        :return: The gcp_cloudiot_device_registry of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._gcp_cloudiot_device_registry

    @gcp_cloudiot_device_registry.setter
    def gcp_cloudiot_device_registry(self, gcp_cloudiot_device_registry):
        """Sets the gcp_cloudiot_device_registry of this CloudiotDevice.


        :param gcp_cloudiot_device_registry: The gcp_cloudiot_device_registry of this CloudiotDevice.  # noqa: E501
        :type gcp_cloudiot_device_registry: str
        """

        self._gcp_cloudiot_device_registry = gcp_cloudiot_device_registry

    @property
    def mqtt_bridge_hostname(self):
        """Gets the mqtt_bridge_hostname of this CloudiotDevice.  # noqa: E501


        :return: The mqtt_bridge_hostname of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._mqtt_bridge_hostname

    @mqtt_bridge_hostname.setter
    def mqtt_bridge_hostname(self, mqtt_bridge_hostname):
        """Sets the mqtt_bridge_hostname of this CloudiotDevice.


        :param mqtt_bridge_hostname: The mqtt_bridge_hostname of this CloudiotDevice.  # noqa: E501
        :type mqtt_bridge_hostname: str
        """

        self._mqtt_bridge_hostname = mqtt_bridge_hostname

    @property
    def mqtt_bridge_port(self):
        """Gets the mqtt_bridge_port of this CloudiotDevice.  # noqa: E501


        :return: The mqtt_bridge_port of this CloudiotDevice.  # noqa: E501
        :rtype: int
        """
        return self._mqtt_bridge_port

    @mqtt_bridge_port.setter
    def mqtt_bridge_port(self, mqtt_bridge_port):
        """Sets the mqtt_bridge_port of this CloudiotDevice.


        :param mqtt_bridge_port: The mqtt_bridge_port of this CloudiotDevice.  # noqa: E501
        :type mqtt_bridge_port: int
        """

        self._mqtt_bridge_port = mqtt_bridge_port

    @property
    def mqtt_client_id(self):
        """Gets the mqtt_client_id of this CloudiotDevice.  # noqa: E501


        :return: The mqtt_client_id of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._mqtt_client_id

    @mqtt_client_id.setter
    def mqtt_client_id(self, mqtt_client_id):
        """Sets the mqtt_client_id of this CloudiotDevice.


        :param mqtt_client_id: The mqtt_client_id of this CloudiotDevice.  # noqa: E501
        :type mqtt_client_id: str
        """

        self._mqtt_client_id = mqtt_client_id

    @property
    def user(self):
        """Gets the user of this CloudiotDevice.  # noqa: E501


        :return: The user of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CloudiotDevice.


        :param user: The user of this CloudiotDevice.  # noqa: E501
        :type user: str
        """

        self._user = user

    @property
    def device(self):
        """Gets the device of this CloudiotDevice.  # noqa: E501


        :return: The device of this CloudiotDevice.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this CloudiotDevice.


        :param device: The device of this CloudiotDevice.  # noqa: E501
        :type device: int
        """

        self._device = device

    @property
    def deleted(self):
        """Gets the deleted of this CloudiotDevice.  # noqa: E501


        :return: The deleted of this CloudiotDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CloudiotDevice.


        :param deleted: The deleted of this CloudiotDevice.  # noqa: E501
        :type deleted: datetime
        """

        self._deleted = deleted

    @property
    def name(self):
        """Gets the name of this CloudiotDevice.  # noqa: E501


        :return: The name of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudiotDevice.


        :param name: The name of this CloudiotDevice.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this CloudiotDevice.  # noqa: E501


        :return: The id of this CloudiotDevice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudiotDevice.


        :param id: The id of this CloudiotDevice.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, CloudiotDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudiotDevice):
            return True

        return self.to_dict() != other.to_dict()
