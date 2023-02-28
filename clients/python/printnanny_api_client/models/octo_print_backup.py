# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.127.1
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


class OctoPrintBackup(object):
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
        'deleted': 'datetime',
        'created_dt': 'datetime',
        'hostname': 'str',
        'name': 'str',
        'octoprint_version': 'str',
        'file': 'str',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'deleted': 'deleted',
        'created_dt': 'created_dt',
        'hostname': 'hostname',
        'name': 'name',
        'octoprint_version': 'octoprint_version',
        'file': 'file',
        'user': 'user'
    }

    def __init__(self, id=None, deleted=None, created_dt=None, hostname=None, name=None, octoprint_version=None, file=None, user=None, local_vars_configuration=None):  # noqa: E501
        """OctoPrintBackup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deleted = None
        self._created_dt = None
        self._hostname = None
        self._name = None
        self._octoprint_version = None
        self._file = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.deleted = deleted
        self.created_dt = created_dt
        self.hostname = hostname
        self.name = name
        self.octoprint_version = octoprint_version
        self.file = file
        self.user = user

    @property
    def id(self):
        """Gets the id of this OctoPrintBackup.  # noqa: E501


        :return: The id of this OctoPrintBackup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OctoPrintBackup.


        :param id: The id of this OctoPrintBackup.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def deleted(self):
        """Gets the deleted of this OctoPrintBackup.  # noqa: E501


        :return: The deleted of this OctoPrintBackup.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this OctoPrintBackup.


        :param deleted: The deleted of this OctoPrintBackup.  # noqa: E501
        :type deleted: datetime
        """
        if self.local_vars_configuration.client_side_validation and deleted is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

    @property
    def created_dt(self):
        """Gets the created_dt of this OctoPrintBackup.  # noqa: E501


        :return: The created_dt of this OctoPrintBackup.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OctoPrintBackup.


        :param created_dt: The created_dt of this OctoPrintBackup.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def hostname(self):
        """Gets the hostname of this OctoPrintBackup.  # noqa: E501


        :return: The hostname of this OctoPrintBackup.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this OctoPrintBackup.


        :param hostname: The hostname of this OctoPrintBackup.  # noqa: E501
        :type hostname: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 64):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `64`")  # noqa: E501

        self._hostname = hostname

    @property
    def name(self):
        """Gets the name of this OctoPrintBackup.  # noqa: E501


        :return: The name of this OctoPrintBackup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OctoPrintBackup.


        :param name: The name of this OctoPrintBackup.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this OctoPrintBackup.  # noqa: E501


        :return: The octoprint_version of this OctoPrintBackup.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this OctoPrintBackup.


        :param octoprint_version: The octoprint_version of this OctoPrintBackup.  # noqa: E501
        :type octoprint_version: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_version is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 64):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `64`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def file(self):
        """Gets the file of this OctoPrintBackup.  # noqa: E501


        :return: The file of this OctoPrintBackup.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this OctoPrintBackup.


        :param file: The file of this OctoPrintBackup.  # noqa: E501
        :type file: str
        """
        if self.local_vars_configuration.client_side_validation and file is None:  # noqa: E501
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def user(self):
        """Gets the user of this OctoPrintBackup.  # noqa: E501


        :return: The user of this OctoPrintBackup.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OctoPrintBackup.


        :param user: The user of this OctoPrintBackup.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, OctoPrintBackup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoPrintBackup):
            return True

        return self.to_dict() != other.to_dict()
