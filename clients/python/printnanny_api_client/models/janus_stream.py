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


class JanusStream(object):
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
        'admin_secret': 'str',
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'config_type': 'JanusConfigType',
        'active': 'bool',
        'stream_secret': 'str',
        'stream_pin': 'str',
        'api_token': 'str',
        'rtp_port': 'int',
        'device': 'int'
    }

    attribute_map = {
        'id': 'id',
        'admin_secret': 'admin_secret',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'config_type': 'config_type',
        'active': 'active',
        'stream_secret': 'stream_secret',
        'stream_pin': 'stream_pin',
        'api_token': 'api_token',
        'rtp_port': 'rtp_port',
        'device': 'device'
    }

    def __init__(self, id=None, admin_secret=None, created_dt=None, updated_dt=None, config_type=None, active=None, stream_secret=None, stream_pin=None, api_token=None, rtp_port=None, device=None, local_vars_configuration=None):  # noqa: E501
        """JanusStream - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._admin_secret = None
        self._created_dt = None
        self._updated_dt = None
        self._config_type = None
        self._active = None
        self._stream_secret = None
        self._stream_pin = None
        self._api_token = None
        self._rtp_port = None
        self._device = None
        self.discriminator = None

        self.id = id
        self.admin_secret = admin_secret
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.config_type = config_type
        if active is not None:
            self.active = active
        if stream_secret is not None:
            self.stream_secret = stream_secret
        if stream_pin is not None:
            self.stream_pin = stream_pin
        if api_token is not None:
            self.api_token = api_token
        if rtp_port is not None:
            self.rtp_port = rtp_port
        self.device = device

    @property
    def id(self):
        """Gets the id of this JanusStream.  # noqa: E501


        :return: The id of this JanusStream.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JanusStream.


        :param id: The id of this JanusStream.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def admin_secret(self):
        """Gets the admin_secret of this JanusStream.  # noqa: E501


        :return: The admin_secret of this JanusStream.  # noqa: E501
        :rtype: str
        """
        return self._admin_secret

    @admin_secret.setter
    def admin_secret(self, admin_secret):
        """Sets the admin_secret of this JanusStream.


        :param admin_secret: The admin_secret of this JanusStream.  # noqa: E501
        :type admin_secret: str
        """
        if self.local_vars_configuration.client_side_validation and admin_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `admin_secret`, must not be `None`")  # noqa: E501

        self._admin_secret = admin_secret

    @property
    def created_dt(self):
        """Gets the created_dt of this JanusStream.  # noqa: E501


        :return: The created_dt of this JanusStream.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this JanusStream.


        :param created_dt: The created_dt of this JanusStream.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this JanusStream.  # noqa: E501


        :return: The updated_dt of this JanusStream.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this JanusStream.


        :param updated_dt: The updated_dt of this JanusStream.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def config_type(self):
        """Gets the config_type of this JanusStream.  # noqa: E501


        :return: The config_type of this JanusStream.  # noqa: E501
        :rtype: JanusConfigType
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this JanusStream.


        :param config_type: The config_type of this JanusStream.  # noqa: E501
        :type config_type: JanusConfigType
        """

        self._config_type = config_type

    @property
    def active(self):
        """Gets the active of this JanusStream.  # noqa: E501


        :return: The active of this JanusStream.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this JanusStream.


        :param active: The active of this JanusStream.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def stream_secret(self):
        """Gets the stream_secret of this JanusStream.  # noqa: E501


        :return: The stream_secret of this JanusStream.  # noqa: E501
        :rtype: str
        """
        return self._stream_secret

    @stream_secret.setter
    def stream_secret(self, stream_secret):
        """Sets the stream_secret of this JanusStream.


        :param stream_secret: The stream_secret of this JanusStream.  # noqa: E501
        :type stream_secret: str
        """
        if (self.local_vars_configuration.client_side_validation and
                stream_secret is not None and len(stream_secret) > 255):
            raise ValueError("Invalid value for `stream_secret`, length must be less than or equal to `255`")  # noqa: E501

        self._stream_secret = stream_secret

    @property
    def stream_pin(self):
        """Gets the stream_pin of this JanusStream.  # noqa: E501


        :return: The stream_pin of this JanusStream.  # noqa: E501
        :rtype: str
        """
        return self._stream_pin

    @stream_pin.setter
    def stream_pin(self, stream_pin):
        """Sets the stream_pin of this JanusStream.


        :param stream_pin: The stream_pin of this JanusStream.  # noqa: E501
        :type stream_pin: str
        """
        if (self.local_vars_configuration.client_side_validation and
                stream_pin is not None and len(stream_pin) > 255):
            raise ValueError("Invalid value for `stream_pin`, length must be less than or equal to `255`")  # noqa: E501

        self._stream_pin = stream_pin

    @property
    def api_token(self):
        """Gets the api_token of this JanusStream.  # noqa: E501


        :return: The api_token of this JanusStream.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this JanusStream.


        :param api_token: The api_token of this JanusStream.  # noqa: E501
        :type api_token: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_token is not None and len(api_token) > 255):
            raise ValueError("Invalid value for `api_token`, length must be less than or equal to `255`")  # noqa: E501

        self._api_token = api_token

    @property
    def rtp_port(self):
        """Gets the rtp_port of this JanusStream.  # noqa: E501


        :return: The rtp_port of this JanusStream.  # noqa: E501
        :rtype: int
        """
        return self._rtp_port

    @rtp_port.setter
    def rtp_port(self, rtp_port):
        """Sets the rtp_port of this JanusStream.


        :param rtp_port: The rtp_port of this JanusStream.  # noqa: E501
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
        """Gets the device of this JanusStream.  # noqa: E501


        :return: The device of this JanusStream.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this JanusStream.


        :param device: The device of this JanusStream.  # noqa: E501
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
        if not isinstance(other, JanusStream):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JanusStream):
            return True

        return self.to_dict() != other.to_dict()
