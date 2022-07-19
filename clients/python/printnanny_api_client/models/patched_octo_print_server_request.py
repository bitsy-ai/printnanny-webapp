# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.95.0
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


class PatchedOctoPrintServerRequest(object):
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
        'octoprint_version': 'str',
        'pip_version': 'str',
        'python_version': 'str',
        'printnanny_plugin_version': 'str',
        'device': 'int'
    }

    attribute_map = {
        'octoprint_version': 'octoprint_version',
        'pip_version': 'pip_version',
        'python_version': 'python_version',
        'printnanny_plugin_version': 'printnanny_plugin_version',
        'device': 'device'
    }

    def __init__(self, octoprint_version=None, pip_version=None, python_version=None, printnanny_plugin_version=None, device=None, local_vars_configuration=None):  # noqa: E501
        """PatchedOctoPrintServerRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._octoprint_version = None
        self._pip_version = None
        self._python_version = None
        self._printnanny_plugin_version = None
        self._device = None
        self.discriminator = None

        if octoprint_version is not None:
            self.octoprint_version = octoprint_version
        if pip_version is not None:
            self.pip_version = pip_version
        if python_version is not None:
            self.python_version = python_version
        if printnanny_plugin_version is not None:
            self.printnanny_plugin_version = printnanny_plugin_version
        if device is not None:
            self.device = device

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this PatchedOctoPrintServerRequest.  # noqa: E501


        :return: The octoprint_version of this PatchedOctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this PatchedOctoPrintServerRequest.


        :param octoprint_version: The octoprint_version of this PatchedOctoPrintServerRequest.  # noqa: E501
        :type octoprint_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 32):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) < 1):
            raise ValueError("Invalid value for `octoprint_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def pip_version(self):
        """Gets the pip_version of this PatchedOctoPrintServerRequest.  # noqa: E501


        :return: The pip_version of this PatchedOctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._pip_version

    @pip_version.setter
    def pip_version(self, pip_version):
        """Sets the pip_version of this PatchedOctoPrintServerRequest.


        :param pip_version: The pip_version of this PatchedOctoPrintServerRequest.  # noqa: E501
        :type pip_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pip_version is not None and len(pip_version) > 32):
            raise ValueError("Invalid value for `pip_version`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pip_version is not None and len(pip_version) < 1):
            raise ValueError("Invalid value for `pip_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._pip_version = pip_version

    @property
    def python_version(self):
        """Gets the python_version of this PatchedOctoPrintServerRequest.  # noqa: E501


        :return: The python_version of this PatchedOctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this PatchedOctoPrintServerRequest.


        :param python_version: The python_version of this PatchedOctoPrintServerRequest.  # noqa: E501
        :type python_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                python_version is not None and len(python_version) > 32):
            raise ValueError("Invalid value for `python_version`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                python_version is not None and len(python_version) < 1):
            raise ValueError("Invalid value for `python_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._python_version = python_version

    @property
    def printnanny_plugin_version(self):
        """Gets the printnanny_plugin_version of this PatchedOctoPrintServerRequest.  # noqa: E501


        :return: The printnanny_plugin_version of this PatchedOctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._printnanny_plugin_version

    @printnanny_plugin_version.setter
    def printnanny_plugin_version(self, printnanny_plugin_version):
        """Sets the printnanny_plugin_version of this PatchedOctoPrintServerRequest.


        :param printnanny_plugin_version: The printnanny_plugin_version of this PatchedOctoPrintServerRequest.  # noqa: E501
        :type printnanny_plugin_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                printnanny_plugin_version is not None and len(printnanny_plugin_version) > 64):
            raise ValueError("Invalid value for `printnanny_plugin_version`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                printnanny_plugin_version is not None and len(printnanny_plugin_version) < 1):
            raise ValueError("Invalid value for `printnanny_plugin_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._printnanny_plugin_version = printnanny_plugin_version

    @property
    def device(self):
        """Gets the device of this PatchedOctoPrintServerRequest.  # noqa: E501


        :return: The device of this PatchedOctoPrintServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PatchedOctoPrintServerRequest.


        :param device: The device of this PatchedOctoPrintServerRequest.  # noqa: E501
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
        if not isinstance(other, PatchedOctoPrintServerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedOctoPrintServerRequest):
            return True

        return self.to_dict() != other.to_dict()
