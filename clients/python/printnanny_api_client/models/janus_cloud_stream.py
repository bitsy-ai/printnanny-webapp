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


class JanusCloudStream(object):
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
        'auth': 'JanusAuth',
        'api_domain': 'str',
        'api_port': 'int',
        'api_url': 'str',
        'admin_url': 'str',
        'admin_port': 'int',
        'rtp_domain': 'str',
        'websocket_url': 'str',
        'websocket_port': 'int',
        'config_type': 'str',
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'active': 'bool',
        'secret': 'str',
        'pin': 'str',
        'info': 'dict(str, object)',
        'ws_port': 'int',
        'rtp_port': 'int',
        'device': 'int'
    }

    attribute_map = {
        'id': 'id',
        'auth': 'auth',
        'api_domain': 'api_domain',
        'api_port': 'api_port',
        'api_url': 'api_url',
        'admin_url': 'admin_url',
        'admin_port': 'admin_port',
        'rtp_domain': 'rtp_domain',
        'websocket_url': 'websocket_url',
        'websocket_port': 'websocket_port',
        'config_type': 'config_type',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'active': 'active',
        'secret': 'secret',
        'pin': 'pin',
        'info': 'info',
        'ws_port': 'ws_port',
        'rtp_port': 'rtp_port',
        'device': 'device'
    }

    def __init__(self, id=None, auth=None, api_domain=None, api_port=None, api_url=None, admin_url=None, admin_port=None, rtp_domain=None, websocket_url=None, websocket_port=None, config_type=None, created_dt=None, updated_dt=None, active=None, secret=None, pin=None, info=None, ws_port=None, rtp_port=None, device=None, local_vars_configuration=None):  # noqa: E501
        """JanusCloudStream - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._auth = None
        self._api_domain = None
        self._api_port = None
        self._api_url = None
        self._admin_url = None
        self._admin_port = None
        self._rtp_domain = None
        self._websocket_url = None
        self._websocket_port = None
        self._config_type = None
        self._created_dt = None
        self._updated_dt = None
        self._active = None
        self._secret = None
        self._pin = None
        self._info = None
        self._ws_port = None
        self._rtp_port = None
        self._device = None
        self.discriminator = None

        self.id = id
        self.auth = auth
        self.api_domain = api_domain
        self.api_port = api_port
        self.api_url = api_url
        self.admin_url = admin_url
        self.admin_port = admin_port
        self.rtp_domain = rtp_domain
        self.websocket_url = websocket_url
        self.websocket_port = websocket_port
        self.config_type = config_type
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        if active is not None:
            self.active = active
        if secret is not None:
            self.secret = secret
        if pin is not None:
            self.pin = pin
        if info is not None:
            self.info = info
        if ws_port is not None:
            self.ws_port = ws_port
        if rtp_port is not None:
            self.rtp_port = rtp_port
        self.device = device

    @property
    def id(self):
        """Gets the id of this JanusCloudStream.  # noqa: E501


        :return: The id of this JanusCloudStream.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JanusCloudStream.


        :param id: The id of this JanusCloudStream.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def auth(self):
        """Gets the auth of this JanusCloudStream.  # noqa: E501


        :return: The auth of this JanusCloudStream.  # noqa: E501
        :rtype: JanusAuth
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this JanusCloudStream.


        :param auth: The auth of this JanusCloudStream.  # noqa: E501
        :type auth: JanusAuth
        """

        self._auth = auth

    @property
    def api_domain(self):
        """Gets the api_domain of this JanusCloudStream.  # noqa: E501


        :return: The api_domain of this JanusCloudStream.  # noqa: E501
        :rtype: str
        """
        return self._api_domain

    @api_domain.setter
    def api_domain(self, api_domain):
        """Sets the api_domain of this JanusCloudStream.


        :param api_domain: The api_domain of this JanusCloudStream.  # noqa: E501
        :type api_domain: str
        """
        if self.local_vars_configuration.client_side_validation and api_domain is None:  # noqa: E501
            raise ValueError("Invalid value for `api_domain`, must not be `None`")  # noqa: E501

        self._api_domain = api_domain

    @property
    def api_port(self):
        """Gets the api_port of this JanusCloudStream.  # noqa: E501


        :return: The api_port of this JanusCloudStream.  # noqa: E501
        :rtype: int
        """
        return self._api_port

    @api_port.setter
    def api_port(self, api_port):
        """Sets the api_port of this JanusCloudStream.


        :param api_port: The api_port of this JanusCloudStream.  # noqa: E501
        :type api_port: int
        """
        if self.local_vars_configuration.client_side_validation and api_port is None:  # noqa: E501
            raise ValueError("Invalid value for `api_port`, must not be `None`")  # noqa: E501

        self._api_port = api_port

    @property
    def api_url(self):
        """Gets the api_url of this JanusCloudStream.  # noqa: E501


        :return: The api_url of this JanusCloudStream.  # noqa: E501
        :rtype: str
        """
        return self._api_url

    @api_url.setter
    def api_url(self, api_url):
        """Sets the api_url of this JanusCloudStream.


        :param api_url: The api_url of this JanusCloudStream.  # noqa: E501
        :type api_url: str
        """
        if self.local_vars_configuration.client_side_validation and api_url is None:  # noqa: E501
            raise ValueError("Invalid value for `api_url`, must not be `None`")  # noqa: E501

        self._api_url = api_url

    @property
    def admin_url(self):
        """Gets the admin_url of this JanusCloudStream.  # noqa: E501


        :return: The admin_url of this JanusCloudStream.  # noqa: E501
        :rtype: str
        """
        return self._admin_url

    @admin_url.setter
    def admin_url(self, admin_url):
        """Sets the admin_url of this JanusCloudStream.


        :param admin_url: The admin_url of this JanusCloudStream.  # noqa: E501
        :type admin_url: str
        """
        if self.local_vars_configuration.client_side_validation and admin_url is None:  # noqa: E501
            raise ValueError("Invalid value for `admin_url`, must not be `None`")  # noqa: E501

        self._admin_url = admin_url

    @property
    def admin_port(self):
        """Gets the admin_port of this JanusCloudStream.  # noqa: E501


        :return: The admin_port of this JanusCloudStream.  # noqa: E501
        :rtype: int
        """
        return self._admin_port

    @admin_port.setter
    def admin_port(self, admin_port):
        """Sets the admin_port of this JanusCloudStream.


        :param admin_port: The admin_port of this JanusCloudStream.  # noqa: E501
        :type admin_port: int
        """
        if self.local_vars_configuration.client_side_validation and admin_port is None:  # noqa: E501
            raise ValueError("Invalid value for `admin_port`, must not be `None`")  # noqa: E501

        self._admin_port = admin_port

    @property
    def rtp_domain(self):
        """Gets the rtp_domain of this JanusCloudStream.  # noqa: E501


        :return: The rtp_domain of this JanusCloudStream.  # noqa: E501
        :rtype: str
        """
        return self._rtp_domain

    @rtp_domain.setter
    def rtp_domain(self, rtp_domain):
        """Sets the rtp_domain of this JanusCloudStream.


        :param rtp_domain: The rtp_domain of this JanusCloudStream.  # noqa: E501
        :type rtp_domain: str
        """
        if self.local_vars_configuration.client_side_validation and rtp_domain is None:  # noqa: E501
            raise ValueError("Invalid value for `rtp_domain`, must not be `None`")  # noqa: E501

        self._rtp_domain = rtp_domain

    @property
    def websocket_url(self):
        """Gets the websocket_url of this JanusCloudStream.  # noqa: E501


        :return: The websocket_url of this JanusCloudStream.  # noqa: E501
        :rtype: str
        """
        return self._websocket_url

    @websocket_url.setter
    def websocket_url(self, websocket_url):
        """Sets the websocket_url of this JanusCloudStream.


        :param websocket_url: The websocket_url of this JanusCloudStream.  # noqa: E501
        :type websocket_url: str
        """
        if self.local_vars_configuration.client_side_validation and websocket_url is None:  # noqa: E501
            raise ValueError("Invalid value for `websocket_url`, must not be `None`")  # noqa: E501

        self._websocket_url = websocket_url

    @property
    def websocket_port(self):
        """Gets the websocket_port of this JanusCloudStream.  # noqa: E501


        :return: The websocket_port of this JanusCloudStream.  # noqa: E501
        :rtype: int
        """
        return self._websocket_port

    @websocket_port.setter
    def websocket_port(self, websocket_port):
        """Sets the websocket_port of this JanusCloudStream.


        :param websocket_port: The websocket_port of this JanusCloudStream.  # noqa: E501
        :type websocket_port: int
        """
        if self.local_vars_configuration.client_side_validation and websocket_port is None:  # noqa: E501
            raise ValueError("Invalid value for `websocket_port`, must not be `None`")  # noqa: E501

        self._websocket_port = websocket_port

    @property
    def config_type(self):
        """Gets the config_type of this JanusCloudStream.  # noqa: E501


        :return: The config_type of this JanusCloudStream.  # noqa: E501
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this JanusCloudStream.


        :param config_type: The config_type of this JanusCloudStream.  # noqa: E501
        :type config_type: str
        """
        if self.local_vars_configuration.client_side_validation and config_type is None:  # noqa: E501
            raise ValueError("Invalid value for `config_type`, must not be `None`")  # noqa: E501

        self._config_type = config_type

    @property
    def created_dt(self):
        """Gets the created_dt of this JanusCloudStream.  # noqa: E501


        :return: The created_dt of this JanusCloudStream.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this JanusCloudStream.


        :param created_dt: The created_dt of this JanusCloudStream.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this JanusCloudStream.  # noqa: E501


        :return: The updated_dt of this JanusCloudStream.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this JanusCloudStream.


        :param updated_dt: The updated_dt of this JanusCloudStream.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def active(self):
        """Gets the active of this JanusCloudStream.  # noqa: E501


        :return: The active of this JanusCloudStream.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this JanusCloudStream.


        :param active: The active of this JanusCloudStream.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def secret(self):
        """Gets the secret of this JanusCloudStream.  # noqa: E501


        :return: The secret of this JanusCloudStream.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this JanusCloudStream.


        :param secret: The secret of this JanusCloudStream.  # noqa: E501
        :type secret: str
        """
        if (self.local_vars_configuration.client_side_validation and
                secret is not None and len(secret) > 255):
            raise ValueError("Invalid value for `secret`, length must be less than or equal to `255`")  # noqa: E501

        self._secret = secret

    @property
    def pin(self):
        """Gets the pin of this JanusCloudStream.  # noqa: E501


        :return: The pin of this JanusCloudStream.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this JanusCloudStream.


        :param pin: The pin of this JanusCloudStream.  # noqa: E501
        :type pin: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pin is not None and len(pin) > 255):
            raise ValueError("Invalid value for `pin`, length must be less than or equal to `255`")  # noqa: E501

        self._pin = pin

    @property
    def info(self):
        """Gets the info of this JanusCloudStream.  # noqa: E501


        :return: The info of this JanusCloudStream.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this JanusCloudStream.


        :param info: The info of this JanusCloudStream.  # noqa: E501
        :type info: dict(str, object)
        """

        self._info = info

    @property
    def ws_port(self):
        """Gets the ws_port of this JanusCloudStream.  # noqa: E501


        :return: The ws_port of this JanusCloudStream.  # noqa: E501
        :rtype: int
        """
        return self._ws_port

    @ws_port.setter
    def ws_port(self, ws_port):
        """Sets the ws_port of this JanusCloudStream.


        :param ws_port: The ws_port of this JanusCloudStream.  # noqa: E501
        :type ws_port: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ws_port is not None and ws_port > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `ws_port`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ws_port is not None and ws_port < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `ws_port`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._ws_port = ws_port

    @property
    def rtp_port(self):
        """Gets the rtp_port of this JanusCloudStream.  # noqa: E501


        :return: The rtp_port of this JanusCloudStream.  # noqa: E501
        :rtype: int
        """
        return self._rtp_port

    @rtp_port.setter
    def rtp_port(self, rtp_port):
        """Sets the rtp_port of this JanusCloudStream.


        :param rtp_port: The rtp_port of this JanusCloudStream.  # noqa: E501
        :type rtp_port: int
        """
        if (self.local_vars_configuration.client_side_validation and
                rtp_port is not None and rtp_port > 32767):  # noqa: E501
            raise ValueError("Invalid value for `rtp_port`, must be a value less than or equal to `32767`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rtp_port is not None and rtp_port < 0):  # noqa: E501
            raise ValueError("Invalid value for `rtp_port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._rtp_port = rtp_port

    @property
    def device(self):
        """Gets the device of this JanusCloudStream.  # noqa: E501


        :return: The device of this JanusCloudStream.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this JanusCloudStream.


        :param device: The device of this JanusCloudStream.  # noqa: E501
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
        if not isinstance(other, JanusCloudStream):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JanusCloudStream):
            return True

        return self.to_dict() != other.to_dict()
