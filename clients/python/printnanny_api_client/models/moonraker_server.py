# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
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


class MoonrakerServer(object):
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
        'base_url': 'str',
        'base_path': 'str',
        'venv_path': 'str',
        'pip_path': 'str',
        'python_path': 'str',
        'moonraker_version': 'str',
        'pip_version': 'str',
        'python_version': 'str',
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'api_key': 'str',
        'user': 'int',
        'pi': 'int'
    }

    attribute_map = {
        'id': 'id',
        'base_url': 'base_url',
        'base_path': 'base_path',
        'venv_path': 'venv_path',
        'pip_path': 'pip_path',
        'python_path': 'python_path',
        'moonraker_version': 'moonraker_version',
        'pip_version': 'pip_version',
        'python_version': 'python_version',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'api_key': 'api_key',
        'user': 'user',
        'pi': 'pi'
    }

    def __init__(self, id=None, base_url=None, base_path=None, venv_path=None, pip_path=None, python_path=None, moonraker_version=None, pip_version=None, python_version=None, created_dt=None, updated_dt=None, api_key=None, user=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """MoonrakerServer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._base_url = None
        self._base_path = None
        self._venv_path = None
        self._pip_path = None
        self._python_path = None
        self._moonraker_version = None
        self._pip_version = None
        self._python_version = None
        self._created_dt = None
        self._updated_dt = None
        self._api_key = None
        self._user = None
        self._pi = None
        self.discriminator = None

        self.id = id
        self.base_url = base_url
        self.base_path = base_path
        self.venv_path = venv_path
        self.pip_path = pip_path
        self.python_path = python_path
        if moonraker_version is not None:
            self.moonraker_version = moonraker_version
        if pip_version is not None:
            self.pip_version = pip_version
        if python_version is not None:
            self.python_version = python_version
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.api_key = api_key
        self.user = user
        self.pi = pi

    @property
    def id(self):
        """Gets the id of this MoonrakerServer.  # noqa: E501


        :return: The id of this MoonrakerServer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MoonrakerServer.


        :param id: The id of this MoonrakerServer.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def base_url(self):
        """Gets the base_url of this MoonrakerServer.  # noqa: E501


        :return: The base_url of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this MoonrakerServer.


        :param base_url: The base_url of this MoonrakerServer.  # noqa: E501
        :type base_url: str
        """
        if self.local_vars_configuration.client_side_validation and base_url is None:  # noqa: E501
            raise ValueError("Invalid value for `base_url`, must not be `None`")  # noqa: E501

        self._base_url = base_url

    @property
    def base_path(self):
        """Gets the base_path of this MoonrakerServer.  # noqa: E501


        :return: The base_path of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this MoonrakerServer.


        :param base_path: The base_path of this MoonrakerServer.  # noqa: E501
        :type base_path: str
        """
        if self.local_vars_configuration.client_side_validation and base_path is None:  # noqa: E501
            raise ValueError("Invalid value for `base_path`, must not be `None`")  # noqa: E501

        self._base_path = base_path

    @property
    def venv_path(self):
        """Gets the venv_path of this MoonrakerServer.  # noqa: E501


        :return: The venv_path of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._venv_path

    @venv_path.setter
    def venv_path(self, venv_path):
        """Sets the venv_path of this MoonrakerServer.


        :param venv_path: The venv_path of this MoonrakerServer.  # noqa: E501
        :type venv_path: str
        """
        if self.local_vars_configuration.client_side_validation and venv_path is None:  # noqa: E501
            raise ValueError("Invalid value for `venv_path`, must not be `None`")  # noqa: E501

        self._venv_path = venv_path

    @property
    def pip_path(self):
        """Gets the pip_path of this MoonrakerServer.  # noqa: E501


        :return: The pip_path of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._pip_path

    @pip_path.setter
    def pip_path(self, pip_path):
        """Sets the pip_path of this MoonrakerServer.


        :param pip_path: The pip_path of this MoonrakerServer.  # noqa: E501
        :type pip_path: str
        """
        if self.local_vars_configuration.client_side_validation and pip_path is None:  # noqa: E501
            raise ValueError("Invalid value for `pip_path`, must not be `None`")  # noqa: E501

        self._pip_path = pip_path

    @property
    def python_path(self):
        """Gets the python_path of this MoonrakerServer.  # noqa: E501


        :return: The python_path of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._python_path

    @python_path.setter
    def python_path(self, python_path):
        """Sets the python_path of this MoonrakerServer.


        :param python_path: The python_path of this MoonrakerServer.  # noqa: E501
        :type python_path: str
        """
        if self.local_vars_configuration.client_side_validation and python_path is None:  # noqa: E501
            raise ValueError("Invalid value for `python_path`, must not be `None`")  # noqa: E501

        self._python_path = python_path

    @property
    def moonraker_version(self):
        """Gets the moonraker_version of this MoonrakerServer.  # noqa: E501


        :return: The moonraker_version of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._moonraker_version

    @moonraker_version.setter
    def moonraker_version(self, moonraker_version):
        """Sets the moonraker_version of this MoonrakerServer.


        :param moonraker_version: The moonraker_version of this MoonrakerServer.  # noqa: E501
        :type moonraker_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                moonraker_version is not None and len(moonraker_version) > 32):
            raise ValueError("Invalid value for `moonraker_version`, length must be less than or equal to `32`")  # noqa: E501

        self._moonraker_version = moonraker_version

    @property
    def pip_version(self):
        """Gets the pip_version of this MoonrakerServer.  # noqa: E501


        :return: The pip_version of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._pip_version

    @pip_version.setter
    def pip_version(self, pip_version):
        """Sets the pip_version of this MoonrakerServer.


        :param pip_version: The pip_version of this MoonrakerServer.  # noqa: E501
        :type pip_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pip_version is not None and len(pip_version) > 32):
            raise ValueError("Invalid value for `pip_version`, length must be less than or equal to `32`")  # noqa: E501

        self._pip_version = pip_version

    @property
    def python_version(self):
        """Gets the python_version of this MoonrakerServer.  # noqa: E501


        :return: The python_version of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this MoonrakerServer.


        :param python_version: The python_version of this MoonrakerServer.  # noqa: E501
        :type python_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                python_version is not None and len(python_version) > 32):
            raise ValueError("Invalid value for `python_version`, length must be less than or equal to `32`")  # noqa: E501

        self._python_version = python_version

    @property
    def created_dt(self):
        """Gets the created_dt of this MoonrakerServer.  # noqa: E501


        :return: The created_dt of this MoonrakerServer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this MoonrakerServer.


        :param created_dt: The created_dt of this MoonrakerServer.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this MoonrakerServer.  # noqa: E501


        :return: The updated_dt of this MoonrakerServer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this MoonrakerServer.


        :param updated_dt: The updated_dt of this MoonrakerServer.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def api_key(self):
        """Gets the api_key of this MoonrakerServer.  # noqa: E501


        :return: The api_key of this MoonrakerServer.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this MoonrakerServer.


        :param api_key: The api_key of this MoonrakerServer.  # noqa: E501
        :type api_key: str
        """
        if (self.local_vars_configuration.client_side_validation and
                api_key is not None and len(api_key) > 255):
            raise ValueError("Invalid value for `api_key`, length must be less than or equal to `255`")  # noqa: E501

        self._api_key = api_key

    @property
    def user(self):
        """Gets the user of this MoonrakerServer.  # noqa: E501


        :return: The user of this MoonrakerServer.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this MoonrakerServer.


        :param user: The user of this MoonrakerServer.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def pi(self):
        """Gets the pi of this MoonrakerServer.  # noqa: E501


        :return: The pi of this MoonrakerServer.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this MoonrakerServer.


        :param pi: The pi of this MoonrakerServer.  # noqa: E501
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
        if not isinstance(other, MoonrakerServer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MoonrakerServer):
            return True

        return self.to_dict() != other.to_dict()
