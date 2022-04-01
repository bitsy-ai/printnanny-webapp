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


class PatchedJanusEdgeStreamRequest(object):
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
        'auth': 'JanusAuthRequest',
        'api_domain': 'str',
        'api_port': 'int',
        'admin_port': 'int',
        'rtp_domain': 'str',
        'websocket_port': 'int',
        'active': 'bool',
        'secret': 'str',
        'pin': 'str',
        'info': 'dict(str, object)',
        'ws_port': 'int',
        'rtp_port': 'int',
        'device': 'int'
    }

    attribute_map = {
        'auth': 'auth',
        'api_domain': 'api_domain',
        'api_port': 'api_port',
        'admin_port': 'admin_port',
        'rtp_domain': 'rtp_domain',
        'websocket_port': 'websocket_port',
        'active': 'active',
        'secret': 'secret',
        'pin': 'pin',
        'info': 'info',
        'ws_port': 'ws_port',
        'rtp_port': 'rtp_port',
        'device': 'device'
    }

    def __init__(self, auth=None, api_domain=None, api_port=None, admin_port=None, rtp_domain=None, websocket_port=None, active=None, secret=None, pin=None, info=None, ws_port=None, rtp_port=None, device=None, local_vars_configuration=None):  # noqa: E501
        """PatchedJanusEdgeStreamRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._auth = None
        self._api_domain = None
        self._api_port = None
        self._admin_port = None
        self._rtp_domain = None
        self._websocket_port = None
        self._active = None
        self._secret = None
        self._pin = None
        self._info = None
        self._ws_port = None
        self._rtp_port = None
        self._device = None
        self.discriminator = None

        if auth is not None:
            self.auth = auth
        if api_domain is not None:
            self.api_domain = api_domain
        if api_port is not None:
            self.api_port = api_port
        if admin_port is not None:
            self.admin_port = admin_port
        if rtp_domain is not None:
            self.rtp_domain = rtp_domain
        if websocket_port is not None:
            self.websocket_port = websocket_port
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
        if device is not None:
            self.device = device

    @property
    def auth(self):
        """Gets the auth of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The auth of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: JanusAuthRequest
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this PatchedJanusEdgeStreamRequest.


        :param auth: The auth of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type auth: JanusAuthRequest
        """

        self._auth = auth

    @property
    def api_domain(self):
        """Gets the api_domain of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The api_domain of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_domain

    @api_domain.setter
    def api_domain(self, api_domain):
        """Sets the api_domain of this PatchedJanusEdgeStreamRequest.


        :param api_domain: The api_domain of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type api_domain: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_domain is not None and len(api_domain) < 1):
            raise ValueError("Invalid value for `api_domain`, length must be greater than or equal to `1`")  # noqa: E501

        self._api_domain = api_domain

    @property
    def api_port(self):
        """Gets the api_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The api_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: int
        """
        return self._api_port

    @api_port.setter
    def api_port(self, api_port):
        """Sets the api_port of this PatchedJanusEdgeStreamRequest.


        :param api_port: The api_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type api_port: int
        """

        self._api_port = api_port

    @property
    def admin_port(self):
        """Gets the admin_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The admin_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: int
        """
        return self._admin_port

    @admin_port.setter
    def admin_port(self, admin_port):
        """Sets the admin_port of this PatchedJanusEdgeStreamRequest.


        :param admin_port: The admin_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type admin_port: int
        """

        self._admin_port = admin_port

    @property
    def rtp_domain(self):
        """Gets the rtp_domain of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The rtp_domain of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._rtp_domain

    @rtp_domain.setter
    def rtp_domain(self, rtp_domain):
        """Sets the rtp_domain of this PatchedJanusEdgeStreamRequest.


        :param rtp_domain: The rtp_domain of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type rtp_domain: str
        """
        if (self.local_vars_configuration.client_side_validation and
                rtp_domain is not None and len(rtp_domain) < 1):
            raise ValueError("Invalid value for `rtp_domain`, length must be greater than or equal to `1`")  # noqa: E501

        self._rtp_domain = rtp_domain

    @property
    def websocket_port(self):
        """Gets the websocket_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The websocket_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: int
        """
        return self._websocket_port

    @websocket_port.setter
    def websocket_port(self, websocket_port):
        """Sets the websocket_port of this PatchedJanusEdgeStreamRequest.


        :param websocket_port: The websocket_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type websocket_port: int
        """

        self._websocket_port = websocket_port

    @property
    def active(self):
        """Gets the active of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The active of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PatchedJanusEdgeStreamRequest.


        :param active: The active of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def secret(self):
        """Gets the secret of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The secret of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this PatchedJanusEdgeStreamRequest.


        :param secret: The secret of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type secret: str
        """
        if (self.local_vars_configuration.client_side_validation and
                secret is not None and len(secret) > 255):
            raise ValueError("Invalid value for `secret`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                secret is not None and len(secret) < 1):
            raise ValueError("Invalid value for `secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._secret = secret

    @property
    def pin(self):
        """Gets the pin of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The pin of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this PatchedJanusEdgeStreamRequest.


        :param pin: The pin of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type pin: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pin is not None and len(pin) > 255):
            raise ValueError("Invalid value for `pin`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pin is not None and len(pin) < 1):
            raise ValueError("Invalid value for `pin`, length must be greater than or equal to `1`")  # noqa: E501

        self._pin = pin

    @property
    def info(self):
        """Gets the info of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The info of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this PatchedJanusEdgeStreamRequest.


        :param info: The info of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type info: dict(str, object)
        """

        self._info = info

    @property
    def ws_port(self):
        """Gets the ws_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The ws_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: int
        """
        return self._ws_port

    @ws_port.setter
    def ws_port(self, ws_port):
        """Sets the ws_port of this PatchedJanusEdgeStreamRequest.


        :param ws_port: The ws_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
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
        """Gets the rtp_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The rtp_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: int
        """
        return self._rtp_port

    @rtp_port.setter
    def rtp_port(self, rtp_port):
        """Sets the rtp_port of this PatchedJanusEdgeStreamRequest.


        :param rtp_port: The rtp_port of this PatchedJanusEdgeStreamRequest.  # noqa: E501
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
        """Gets the device of this PatchedJanusEdgeStreamRequest.  # noqa: E501


        :return: The device of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PatchedJanusEdgeStreamRequest.


        :param device: The device of this PatchedJanusEdgeStreamRequest.  # noqa: E501
        :type device: int
        """

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
        if not isinstance(other, PatchedJanusEdgeStreamRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedJanusEdgeStreamRequest):
            return True

        return self.to_dict() != other.to_dict()
