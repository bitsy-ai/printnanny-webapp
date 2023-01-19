# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.124.5
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


class PatchedMoonrakerServerRequest(object):
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
        'base_path': 'str',
        'moonraker_version': 'str',
        'pip_version': 'str',
        'python_version': 'str',
        'api_key': 'str',
        'pi': 'int'
    }

    attribute_map = {
        'base_path': 'base_path',
        'moonraker_version': 'moonraker_version',
        'pip_version': 'pip_version',
        'python_version': 'python_version',
        'api_key': 'api_key',
        'pi': 'pi'
    }

    def __init__(self, base_path=None, moonraker_version=None, pip_version=None, python_version=None, api_key=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """PatchedMoonrakerServerRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_path = None
        self._moonraker_version = None
        self._pip_version = None
        self._python_version = None
        self._api_key = None
        self._pi = None
        self.discriminator = None

        if base_path is not None:
            self.base_path = base_path
        if moonraker_version is not None:
            self.moonraker_version = moonraker_version
        if pip_version is not None:
            self.pip_version = pip_version
        if python_version is not None:
            self.python_version = python_version
        self.api_key = api_key
        if pi is not None:
            self.pi = pi

    @property
    def base_path(self):
        """Gets the base_path of this PatchedMoonrakerServerRequest.  # noqa: E501


        :return: The base_path of this PatchedMoonrakerServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this PatchedMoonrakerServerRequest.


        :param base_path: The base_path of this PatchedMoonrakerServerRequest.  # noqa: E501
        :type base_path: str
        """
        if (self.local_vars_configuration.client_side_validation and
                base_path is not None and len(base_path) < 1):
            raise ValueError("Invalid value for `base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._base_path = base_path

    @property
    def moonraker_version(self):
        """Gets the moonraker_version of this PatchedMoonrakerServerRequest.  # noqa: E501


        :return: The moonraker_version of this PatchedMoonrakerServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._moonraker_version

    @moonraker_version.setter
    def moonraker_version(self, moonraker_version):
        """Sets the moonraker_version of this PatchedMoonrakerServerRequest.


        :param moonraker_version: The moonraker_version of this PatchedMoonrakerServerRequest.  # noqa: E501
        :type moonraker_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                moonraker_version is not None and len(moonraker_version) > 32):
            raise ValueError("Invalid value for `moonraker_version`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                moonraker_version is not None and len(moonraker_version) < 1):
            raise ValueError("Invalid value for `moonraker_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._moonraker_version = moonraker_version

    @property
    def pip_version(self):
        """Gets the pip_version of this PatchedMoonrakerServerRequest.  # noqa: E501


        :return: The pip_version of this PatchedMoonrakerServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._pip_version

    @pip_version.setter
    def pip_version(self, pip_version):
        """Sets the pip_version of this PatchedMoonrakerServerRequest.


        :param pip_version: The pip_version of this PatchedMoonrakerServerRequest.  # noqa: E501
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
        """Gets the python_version of this PatchedMoonrakerServerRequest.  # noqa: E501


        :return: The python_version of this PatchedMoonrakerServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this PatchedMoonrakerServerRequest.


        :param python_version: The python_version of this PatchedMoonrakerServerRequest.  # noqa: E501
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
    def api_key(self):
        """Gets the api_key of this PatchedMoonrakerServerRequest.  # noqa: E501


        :return: The api_key of this PatchedMoonrakerServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this PatchedMoonrakerServerRequest.


        :param api_key: The api_key of this PatchedMoonrakerServerRequest.  # noqa: E501
        :type api_key: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_key is not None and len(api_key) > 255):
            raise ValueError("Invalid value for `api_key`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                api_key is not None and len(api_key) < 1):
            raise ValueError("Invalid value for `api_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._api_key = api_key

    @property
    def pi(self):
        """Gets the pi of this PatchedMoonrakerServerRequest.  # noqa: E501


        :return: The pi of this PatchedMoonrakerServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PatchedMoonrakerServerRequest.


        :param pi: The pi of this PatchedMoonrakerServerRequest.  # noqa: E501
        :type pi: int
        """

        self._pi = pi

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
        if not isinstance(other, PatchedMoonrakerServerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedMoonrakerServerRequest):
            return True

        return self.to_dict() != other.to_dict()
