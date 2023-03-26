# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.129.9
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


class WebrtcStreamRequest(object):
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
        'active': 'bool',
        'config_type': 'JanusConfigType'
    }

    attribute_map = {
        'active': 'active',
        'config_type': 'config_type'
    }

    def __init__(self, active=None, config_type=None, local_vars_configuration=None):  # noqa: E501
        """WebrtcStreamRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._config_type = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if config_type is not None:
            self.config_type = config_type

    @property
    def active(self):
        """Gets the active of this WebrtcStreamRequest.  # noqa: E501


        :return: The active of this WebrtcStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this WebrtcStreamRequest.


        :param active: The active of this WebrtcStreamRequest.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def config_type(self):
        """Gets the config_type of this WebrtcStreamRequest.  # noqa: E501


        :return: The config_type of this WebrtcStreamRequest.  # noqa: E501
        :rtype: JanusConfigType
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this WebrtcStreamRequest.


        :param config_type: The config_type of this WebrtcStreamRequest.  # noqa: E501
        :type config_type: JanusConfigType
        """

        self._config_type = config_type

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
        if not isinstance(other, WebrtcStreamRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebrtcStreamRequest):
            return True

        return self.to_dict() != other.to_dict()
