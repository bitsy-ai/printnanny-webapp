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


class JanusStreamRequest(object):
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
        'config_type': 'JanusConfigType',
        'active': 'bool',
        'secret': 'str',
        'pin': 'str',
        'info': 'dict(str, object)'
    }

    attribute_map = {
        'config_type': 'config_type',
        'active': 'active',
        'secret': 'secret',
        'pin': 'pin',
        'info': 'info'
    }

    def __init__(self, config_type=None, active=None, secret=None, pin=None, info=None, local_vars_configuration=None):  # noqa: E501
        """JanusStreamRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._config_type = None
        self._active = None
        self._secret = None
        self._pin = None
        self._info = None
        self.discriminator = None

        if config_type is not None:
            self.config_type = config_type
        if active is not None:
            self.active = active
        if secret is not None:
            self.secret = secret
        if pin is not None:
            self.pin = pin
        if info is not None:
            self.info = info

    @property
    def config_type(self):
        """Gets the config_type of this JanusStreamRequest.  # noqa: E501


        :return: The config_type of this JanusStreamRequest.  # noqa: E501
        :rtype: JanusConfigType
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this JanusStreamRequest.


        :param config_type: The config_type of this JanusStreamRequest.  # noqa: E501
        :type config_type: JanusConfigType
        """

        self._config_type = config_type

    @property
    def active(self):
        """Gets the active of this JanusStreamRequest.  # noqa: E501


        :return: The active of this JanusStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this JanusStreamRequest.


        :param active: The active of this JanusStreamRequest.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def secret(self):
        """Gets the secret of this JanusStreamRequest.  # noqa: E501


        :return: The secret of this JanusStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this JanusStreamRequest.


        :param secret: The secret of this JanusStreamRequest.  # noqa: E501
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
        """Gets the pin of this JanusStreamRequest.  # noqa: E501


        :return: The pin of this JanusStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this JanusStreamRequest.


        :param pin: The pin of this JanusStreamRequest.  # noqa: E501
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
        """Gets the info of this JanusStreamRequest.  # noqa: E501


        :return: The info of this JanusStreamRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this JanusStreamRequest.


        :param info: The info of this JanusStreamRequest.  # noqa: E501
        :type info: dict(str, object)
        """

        self._info = info

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
        if not isinstance(other, JanusStreamRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JanusStreamRequest):
            return True

        return self.to_dict() != other.to_dict()
