# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
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


class Device(object):
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
        'alert_settings': 'AlertSettings',
        'cloudiot_device': 'CloudiotDevice',
        'user': 'User',
        'system_info': 'SystemInfo',
        'public_key': 'PublicKey',
        'urls': 'DeviceUrls',
        'created_dt': 'datetime',
        'hostname': 'str',
        'fqdn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'alert_settings': 'alert_settings',
        'cloudiot_device': 'cloudiot_device',
        'user': 'user',
        'system_info': 'system_info',
        'public_key': 'public_key',
        'urls': 'urls',
        'created_dt': 'created_dt',
        'hostname': 'hostname',
        'fqdn': 'fqdn'
    }

    def __init__(self, id=None, alert_settings=None, cloudiot_device=None, user=None, system_info=None, public_key=None, urls=None, created_dt=None, hostname=None, fqdn=None, local_vars_configuration=None):  # noqa: E501
        """Device - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._alert_settings = None
        self._cloudiot_device = None
        self._user = None
        self._system_info = None
        self._public_key = None
        self._urls = None
        self._created_dt = None
        self._hostname = None
        self._fqdn = None
        self.discriminator = None

        self.id = id
        self.alert_settings = alert_settings
        self.cloudiot_device = cloudiot_device
        self.user = user
        self.system_info = system_info
        self.public_key = public_key
        self.urls = urls
        self.created_dt = created_dt
        if hostname is not None:
            self.hostname = hostname
        if fqdn is not None:
            self.fqdn = fqdn

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def alert_settings(self):
        """Gets the alert_settings of this Device.  # noqa: E501


        :return: The alert_settings of this Device.  # noqa: E501
        :rtype: AlertSettings
        """
        return self._alert_settings

    @alert_settings.setter
    def alert_settings(self, alert_settings):
        """Sets the alert_settings of this Device.


        :param alert_settings: The alert_settings of this Device.  # noqa: E501
        :type alert_settings: AlertSettings
        """

        self._alert_settings = alert_settings

    @property
    def cloudiot_device(self):
        """Gets the cloudiot_device of this Device.  # noqa: E501


        :return: The cloudiot_device of this Device.  # noqa: E501
        :rtype: CloudiotDevice
        """
        return self._cloudiot_device

    @cloudiot_device.setter
    def cloudiot_device(self, cloudiot_device):
        """Sets the cloudiot_device of this Device.


        :param cloudiot_device: The cloudiot_device of this Device.  # noqa: E501
        :type cloudiot_device: CloudiotDevice
        """

        self._cloudiot_device = cloudiot_device

    @property
    def user(self):
        """Gets the user of this Device.  # noqa: E501


        :return: The user of this Device.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Device.


        :param user: The user of this Device.  # noqa: E501
        :type user: User
        """

        self._user = user

    @property
    def system_info(self):
        """Gets the system_info of this Device.  # noqa: E501


        :return: The system_info of this Device.  # noqa: E501
        :rtype: SystemInfo
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this Device.


        :param system_info: The system_info of this Device.  # noqa: E501
        :type system_info: SystemInfo
        """

        self._system_info = system_info

    @property
    def public_key(self):
        """Gets the public_key of this Device.  # noqa: E501


        :return: The public_key of this Device.  # noqa: E501
        :rtype: PublicKey
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Device.


        :param public_key: The public_key of this Device.  # noqa: E501
        :type public_key: PublicKey
        """

        self._public_key = public_key

    @property
    def urls(self):
        """Gets the urls of this Device.  # noqa: E501


        :return: The urls of this Device.  # noqa: E501
        :rtype: DeviceUrls
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this Device.


        :param urls: The urls of this Device.  # noqa: E501
        :type urls: DeviceUrls
        """
        if self.local_vars_configuration.client_side_validation and urls is None:  # noqa: E501
            raise ValueError("Invalid value for `urls`, must not be `None`")  # noqa: E501

        self._urls = urls

    @property
    def created_dt(self):
        """Gets the created_dt of this Device.  # noqa: E501


        :return: The created_dt of this Device.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Device.


        :param created_dt: The created_dt of this Device.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def hostname(self):
        """Gets the hostname of this Device.  # noqa: E501

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :return: The hostname of this Device.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Device.

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :param hostname: The hostname of this Device.  # noqa: E501
        :type hostname: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501

        self._hostname = hostname

    @property
    def fqdn(self):
        """Gets the fqdn of this Device.  # noqa: E501


        :return: The fqdn of this Device.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this Device.


        :param fqdn: The fqdn of this Device.  # noqa: E501
        :type fqdn: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fqdn is not None and len(fqdn) > 255):
            raise ValueError("Invalid value for `fqdn`, length must be less than or equal to `255`")  # noqa: E501

        self._fqdn = fqdn

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
        if not isinstance(other, Device):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Device):
            return True

        return self.to_dict() != other.to_dict()
