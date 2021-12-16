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


class License(object):
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
        'device': 'Device',
        'user': 'User',
        'last_check_task': 'Task',
        'honeycomb_dataset': 'str',
        'honeycomb_api_key': 'str',
        'janus_admin_secret': 'str',
        'janus_token': 'str',
        'activated': 'bool',
        'public_key': 'str',
        'fingerprint': 'str',
        'created_dt': 'datetime',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'user': 'user',
        'last_check_task': 'last_check_task',
        'honeycomb_dataset': 'honeycomb_dataset',
        'honeycomb_api_key': 'honeycomb_api_key',
        'janus_admin_secret': 'janus_admin_secret',
        'janus_token': 'janus_token',
        'activated': 'activated',
        'public_key': 'public_key',
        'fingerprint': 'fingerprint',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, id=None, device=None, user=None, last_check_task=None, honeycomb_dataset=None, honeycomb_api_key=None, janus_admin_secret=None, janus_token=None, activated=None, public_key=None, fingerprint=None, created_dt=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """License - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._device = None
        self._user = None
        self._last_check_task = None
        self._honeycomb_dataset = None
        self._honeycomb_api_key = None
        self._janus_admin_secret = None
        self._janus_token = None
        self._activated = None
        self._public_key = None
        self._fingerprint = None
        self._created_dt = None
        self._updated_dt = None
        self.discriminator = None

        self.id = id
        self.device = device
        self.user = user
        self.last_check_task = last_check_task
        self.honeycomb_dataset = honeycomb_dataset
        self.honeycomb_api_key = honeycomb_api_key
        self.janus_admin_secret = janus_admin_secret
        self.janus_token = janus_token
        if activated is not None:
            self.activated = activated
        self.public_key = public_key
        self.fingerprint = fingerprint
        self.created_dt = created_dt
        self.updated_dt = updated_dt

    @property
    def id(self):
        """Gets the id of this License.  # noqa: E501


        :return: The id of this License.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this License.


        :param id: The id of this License.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def device(self):
        """Gets the device of this License.  # noqa: E501


        :return: The device of this License.  # noqa: E501
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this License.


        :param device: The device of this License.  # noqa: E501
        :type device: Device
        """

        self._device = device

    @property
    def user(self):
        """Gets the user of this License.  # noqa: E501


        :return: The user of this License.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this License.


        :param user: The user of this License.  # noqa: E501
        :type user: User
        """

        self._user = user

    @property
    def last_check_task(self):
        """Gets the last_check_task of this License.  # noqa: E501


        :return: The last_check_task of this License.  # noqa: E501
        :rtype: Task
        """
        return self._last_check_task

    @last_check_task.setter
    def last_check_task(self, last_check_task):
        """Sets the last_check_task of this License.


        :param last_check_task: The last_check_task of this License.  # noqa: E501
        :type last_check_task: Task
        """

        self._last_check_task = last_check_task

    @property
    def honeycomb_dataset(self):
        """Gets the honeycomb_dataset of this License.  # noqa: E501


        :return: The honeycomb_dataset of this License.  # noqa: E501
        :rtype: str
        """
        return self._honeycomb_dataset

    @honeycomb_dataset.setter
    def honeycomb_dataset(self, honeycomb_dataset):
        """Sets the honeycomb_dataset of this License.


        :param honeycomb_dataset: The honeycomb_dataset of this License.  # noqa: E501
        :type honeycomb_dataset: str
        """
        if self.local_vars_configuration.client_side_validation and honeycomb_dataset is None:  # noqa: E501
            raise ValueError("Invalid value for `honeycomb_dataset`, must not be `None`")  # noqa: E501

        self._honeycomb_dataset = honeycomb_dataset

    @property
    def honeycomb_api_key(self):
        """Gets the honeycomb_api_key of this License.  # noqa: E501


        :return: The honeycomb_api_key of this License.  # noqa: E501
        :rtype: str
        """
        return self._honeycomb_api_key

    @honeycomb_api_key.setter
    def honeycomb_api_key(self, honeycomb_api_key):
        """Sets the honeycomb_api_key of this License.


        :param honeycomb_api_key: The honeycomb_api_key of this License.  # noqa: E501
        :type honeycomb_api_key: str
        """
        if self.local_vars_configuration.client_side_validation and honeycomb_api_key is None:  # noqa: E501
            raise ValueError("Invalid value for `honeycomb_api_key`, must not be `None`")  # noqa: E501

        self._honeycomb_api_key = honeycomb_api_key

    @property
    def janus_admin_secret(self):
        """Gets the janus_admin_secret of this License.  # noqa: E501


        :return: The janus_admin_secret of this License.  # noqa: E501
        :rtype: str
        """
        return self._janus_admin_secret

    @janus_admin_secret.setter
    def janus_admin_secret(self, janus_admin_secret):
        """Sets the janus_admin_secret of this License.


        :param janus_admin_secret: The janus_admin_secret of this License.  # noqa: E501
        :type janus_admin_secret: str
        """
        if self.local_vars_configuration.client_side_validation and janus_admin_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `janus_admin_secret`, must not be `None`")  # noqa: E501

        self._janus_admin_secret = janus_admin_secret

    @property
    def janus_token(self):
        """Gets the janus_token of this License.  # noqa: E501


        :return: The janus_token of this License.  # noqa: E501
        :rtype: str
        """
        return self._janus_token

    @janus_token.setter
    def janus_token(self, janus_token):
        """Sets the janus_token of this License.


        :param janus_token: The janus_token of this License.  # noqa: E501
        :type janus_token: str
        """
        if self.local_vars_configuration.client_side_validation and janus_token is None:  # noqa: E501
            raise ValueError("Invalid value for `janus_token`, must not be `None`")  # noqa: E501

        self._janus_token = janus_token

    @property
    def activated(self):
        """Gets the activated of this License.  # noqa: E501


        :return: The activated of this License.  # noqa: E501
        :rtype: bool
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this License.


        :param activated: The activated of this License.  # noqa: E501
        :type activated: bool
        """

        self._activated = activated

    @property
    def public_key(self):
        """Gets the public_key of this License.  # noqa: E501


        :return: The public_key of this License.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this License.


        :param public_key: The public_key of this License.  # noqa: E501
        :type public_key: str
        """
        if self.local_vars_configuration.client_side_validation and public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def fingerprint(self):
        """Gets the fingerprint of this License.  # noqa: E501


        :return: The fingerprint of this License.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this License.


        :param fingerprint: The fingerprint of this License.  # noqa: E501
        :type fingerprint: str
        """
        if self.local_vars_configuration.client_side_validation and fingerprint is None:  # noqa: E501
            raise ValueError("Invalid value for `fingerprint`, must not be `None`")  # noqa: E501

        self._fingerprint = fingerprint

    @property
    def created_dt(self):
        """Gets the created_dt of this License.  # noqa: E501


        :return: The created_dt of this License.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this License.


        :param created_dt: The created_dt of this License.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this License.  # noqa: E501


        :return: The updated_dt of this License.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this License.


        :param updated_dt: The updated_dt of this License.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

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
        if not isinstance(other, License):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, License):
            return True

        return self.to_dict() != other.to_dict()
