# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class Appliance(object):
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
        'pki': 'AppliancePKI',
        'ansible_facts': 'AnsibleFacts',
        'deleted': 'datetime',
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'hostname': 'str',
        'user': 'Nested'
    }

    attribute_map = {
        'id': 'id',
        'pki': 'pki',
        'ansible_facts': 'ansible_facts',
        'deleted': 'deleted',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'hostname': 'hostname',
        'user': 'user'
    }

    def __init__(self, id=None, pki=None, ansible_facts=None, deleted=None, created_dt=None, updated_dt=None, hostname=None, user=None, local_vars_configuration=None):  # noqa: E501
        """Appliance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._pki = None
        self._ansible_facts = None
        self._deleted = None
        self._created_dt = None
        self._updated_dt = None
        self._hostname = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.pki = pki
        self.ansible_facts = ansible_facts
        self.deleted = deleted
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.hostname = hostname
        self.user = user

    @property
    def id(self):
        """Gets the id of this Appliance.  # noqa: E501


        :return: The id of this Appliance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Appliance.


        :param id: The id of this Appliance.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def pki(self):
        """Gets the pki of this Appliance.  # noqa: E501


        :return: The pki of this Appliance.  # noqa: E501
        :rtype: AppliancePKI
        """
        return self._pki

    @pki.setter
    def pki(self, pki):
        """Sets the pki of this Appliance.


        :param pki: The pki of this Appliance.  # noqa: E501
        :type pki: AppliancePKI
        """
        if self.local_vars_configuration.client_side_validation and pki is None:  # noqa: E501
            raise ValueError("Invalid value for `pki`, must not be `None`")  # noqa: E501

        self._pki = pki

    @property
    def ansible_facts(self):
        """Gets the ansible_facts of this Appliance.  # noqa: E501


        :return: The ansible_facts of this Appliance.  # noqa: E501
        :rtype: AnsibleFacts
        """
        return self._ansible_facts

    @ansible_facts.setter
    def ansible_facts(self, ansible_facts):
        """Sets the ansible_facts of this Appliance.


        :param ansible_facts: The ansible_facts of this Appliance.  # noqa: E501
        :type ansible_facts: AnsibleFacts
        """
        if self.local_vars_configuration.client_side_validation and ansible_facts is None:  # noqa: E501
            raise ValueError("Invalid value for `ansible_facts`, must not be `None`")  # noqa: E501

        self._ansible_facts = ansible_facts

    @property
    def deleted(self):
        """Gets the deleted of this Appliance.  # noqa: E501


        :return: The deleted of this Appliance.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Appliance.


        :param deleted: The deleted of this Appliance.  # noqa: E501
        :type deleted: datetime
        """
        if self.local_vars_configuration.client_side_validation and deleted is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

    @property
    def created_dt(self):
        """Gets the created_dt of this Appliance.  # noqa: E501


        :return: The created_dt of this Appliance.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Appliance.


        :param created_dt: The created_dt of this Appliance.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this Appliance.  # noqa: E501


        :return: The updated_dt of this Appliance.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this Appliance.


        :param updated_dt: The updated_dt of this Appliance.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def hostname(self):
        """Gets the hostname of this Appliance.  # noqa: E501


        :return: The hostname of this Appliance.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Appliance.


        :param hostname: The hostname of this Appliance.  # noqa: E501
        :type hostname: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501

        self._hostname = hostname

    @property
    def user(self):
        """Gets the user of this Appliance.  # noqa: E501


        :return: The user of this Appliance.  # noqa: E501
        :rtype: Nested
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Appliance.


        :param user: The user of this Appliance.  # noqa: E501
        :type user: Nested
        """

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
        if not isinstance(other, Appliance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Appliance):
            return True

        return self.to_dict() != other.to_dict()
