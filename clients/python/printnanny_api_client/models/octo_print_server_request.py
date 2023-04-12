# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.132.2
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


class OctoPrintServerRequest(object):
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
        'base_url': 'str',
        'base_path': 'str',
        'venv_path': 'str',
        'pip_path': 'str',
        'python_path': 'str',
        'octoprint_version': 'str',
        'pip_version': 'str',
        'python_version': 'str',
        'printnanny_plugin_version': 'str',
        'api_key': 'str',
        'pi': 'int'
    }

    attribute_map = {
        'base_url': 'base_url',
        'base_path': 'base_path',
        'venv_path': 'venv_path',
        'pip_path': 'pip_path',
        'python_path': 'python_path',
        'octoprint_version': 'octoprint_version',
        'pip_version': 'pip_version',
        'python_version': 'python_version',
        'printnanny_plugin_version': 'printnanny_plugin_version',
        'api_key': 'api_key',
        'pi': 'pi'
    }

    def __init__(self, base_url=None, base_path=None, venv_path=None, pip_path=None, python_path=None, octoprint_version=None, pip_version=None, python_version=None, printnanny_plugin_version=None, api_key=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """OctoPrintServerRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_url = None
        self._base_path = None
        self._venv_path = None
        self._pip_path = None
        self._python_path = None
        self._octoprint_version = None
        self._pip_version = None
        self._python_version = None
        self._printnanny_plugin_version = None
        self._api_key = None
        self._pi = None
        self.discriminator = None

        self.base_url = base_url
        self.base_path = base_path
        self.venv_path = venv_path
        self.pip_path = pip_path
        self.python_path = python_path
        if octoprint_version is not None:
            self.octoprint_version = octoprint_version
        if pip_version is not None:
            self.pip_version = pip_version
        if python_version is not None:
            self.python_version = python_version
        if printnanny_plugin_version is not None:
            self.printnanny_plugin_version = printnanny_plugin_version
        self.api_key = api_key
        self.pi = pi

    @property
    def base_url(self):
        """Gets the base_url of this OctoPrintServerRequest.  # noqa: E501


        :return: The base_url of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this OctoPrintServerRequest.


        :param base_url: The base_url of this OctoPrintServerRequest.  # noqa: E501
        :type base_url: str
        """
        if self.local_vars_configuration.client_side_validation and base_url is None:  # noqa: E501
            raise ValueError("Invalid value for `base_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                base_url is not None and len(base_url) < 1):
            raise ValueError("Invalid value for `base_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._base_url = base_url

    @property
    def base_path(self):
        """Gets the base_path of this OctoPrintServerRequest.  # noqa: E501


        :return: The base_path of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this OctoPrintServerRequest.


        :param base_path: The base_path of this OctoPrintServerRequest.  # noqa: E501
        :type base_path: str
        """
        if self.local_vars_configuration.client_side_validation and base_path is None:  # noqa: E501
            raise ValueError("Invalid value for `base_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                base_path is not None and len(base_path) < 1):
            raise ValueError("Invalid value for `base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._base_path = base_path

    @property
    def venv_path(self):
        """Gets the venv_path of this OctoPrintServerRequest.  # noqa: E501


        :return: The venv_path of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._venv_path

    @venv_path.setter
    def venv_path(self, venv_path):
        """Sets the venv_path of this OctoPrintServerRequest.


        :param venv_path: The venv_path of this OctoPrintServerRequest.  # noqa: E501
        :type venv_path: str
        """
        if self.local_vars_configuration.client_side_validation and venv_path is None:  # noqa: E501
            raise ValueError("Invalid value for `venv_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                venv_path is not None and len(venv_path) < 1):
            raise ValueError("Invalid value for `venv_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._venv_path = venv_path

    @property
    def pip_path(self):
        """Gets the pip_path of this OctoPrintServerRequest.  # noqa: E501


        :return: The pip_path of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._pip_path

    @pip_path.setter
    def pip_path(self, pip_path):
        """Sets the pip_path of this OctoPrintServerRequest.


        :param pip_path: The pip_path of this OctoPrintServerRequest.  # noqa: E501
        :type pip_path: str
        """
        if self.local_vars_configuration.client_side_validation and pip_path is None:  # noqa: E501
            raise ValueError("Invalid value for `pip_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pip_path is not None and len(pip_path) < 1):
            raise ValueError("Invalid value for `pip_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._pip_path = pip_path

    @property
    def python_path(self):
        """Gets the python_path of this OctoPrintServerRequest.  # noqa: E501


        :return: The python_path of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._python_path

    @python_path.setter
    def python_path(self, python_path):
        """Sets the python_path of this OctoPrintServerRequest.


        :param python_path: The python_path of this OctoPrintServerRequest.  # noqa: E501
        :type python_path: str
        """
        if self.local_vars_configuration.client_side_validation and python_path is None:  # noqa: E501
            raise ValueError("Invalid value for `python_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                python_path is not None and len(python_path) < 1):
            raise ValueError("Invalid value for `python_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._python_path = python_path

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this OctoPrintServerRequest.  # noqa: E501


        :return: The octoprint_version of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this OctoPrintServerRequest.


        :param octoprint_version: The octoprint_version of this OctoPrintServerRequest.  # noqa: E501
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
        """Gets the pip_version of this OctoPrintServerRequest.  # noqa: E501


        :return: The pip_version of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._pip_version

    @pip_version.setter
    def pip_version(self, pip_version):
        """Sets the pip_version of this OctoPrintServerRequest.


        :param pip_version: The pip_version of this OctoPrintServerRequest.  # noqa: E501
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
        """Gets the python_version of this OctoPrintServerRequest.  # noqa: E501


        :return: The python_version of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this OctoPrintServerRequest.


        :param python_version: The python_version of this OctoPrintServerRequest.  # noqa: E501
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
        """Gets the printnanny_plugin_version of this OctoPrintServerRequest.  # noqa: E501


        :return: The printnanny_plugin_version of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._printnanny_plugin_version

    @printnanny_plugin_version.setter
    def printnanny_plugin_version(self, printnanny_plugin_version):
        """Sets the printnanny_plugin_version of this OctoPrintServerRequest.


        :param printnanny_plugin_version: The printnanny_plugin_version of this OctoPrintServerRequest.  # noqa: E501
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
    def api_key(self):
        """Gets the api_key of this OctoPrintServerRequest.  # noqa: E501


        :return: The api_key of this OctoPrintServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this OctoPrintServerRequest.


        :param api_key: The api_key of this OctoPrintServerRequest.  # noqa: E501
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
        """Gets the pi of this OctoPrintServerRequest.  # noqa: E501


        :return: The pi of this OctoPrintServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this OctoPrintServerRequest.


        :param pi: The pi of this OctoPrintServerRequest.  # noqa: E501
        :type pi: int
        """
        if self.local_vars_configuration.client_side_validation and pi is None:  # noqa: E501
            raise ValueError("Invalid value for `pi`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, OctoPrintServerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoPrintServerRequest):
            return True

        return self.to_dict() != other.to_dict()
