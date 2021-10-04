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


class ApplianceRequest(object):
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
        'pki': 'AppliancePKIRequest',
        'ansible_facts': 'AnsibleFactsRequest',
        'hostname': 'str'
    }

    attribute_map = {
        'pki': 'pki',
        'ansible_facts': 'ansible_facts',
        'hostname': 'hostname'
    }

    def __init__(self, pki=None, ansible_facts=None, hostname=None, local_vars_configuration=None):  # noqa: E501
        """ApplianceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._pki = None
        self._ansible_facts = None
        self._hostname = None
        self.discriminator = None

        self.pki = pki
        self.ansible_facts = ansible_facts
        self.hostname = hostname

    @property
    def pki(self):
        """Gets the pki of this ApplianceRequest.  # noqa: E501


        :return: The pki of this ApplianceRequest.  # noqa: E501
        :rtype: AppliancePKIRequest
        """
        return self._pki

    @pki.setter
    def pki(self, pki):
        """Sets the pki of this ApplianceRequest.


        :param pki: The pki of this ApplianceRequest.  # noqa: E501
        :type pki: AppliancePKIRequest
        """
        if self.local_vars_configuration.client_side_validation and pki is None:  # noqa: E501
            raise ValueError("Invalid value for `pki`, must not be `None`")  # noqa: E501

        self._pki = pki

    @property
    def ansible_facts(self):
        """Gets the ansible_facts of this ApplianceRequest.  # noqa: E501


        :return: The ansible_facts of this ApplianceRequest.  # noqa: E501
        :rtype: AnsibleFactsRequest
        """
        return self._ansible_facts

    @ansible_facts.setter
    def ansible_facts(self, ansible_facts):
        """Sets the ansible_facts of this ApplianceRequest.


        :param ansible_facts: The ansible_facts of this ApplianceRequest.  # noqa: E501
        :type ansible_facts: AnsibleFactsRequest
        """
        if self.local_vars_configuration.client_side_validation and ansible_facts is None:  # noqa: E501
            raise ValueError("Invalid value for `ansible_facts`, must not be `None`")  # noqa: E501

        self._ansible_facts = ansible_facts

    @property
    def hostname(self):
        """Gets the hostname of this ApplianceRequest.  # noqa: E501


        :return: The hostname of this ApplianceRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ApplianceRequest.


        :param hostname: The hostname of this ApplianceRequest.  # noqa: E501
        :type hostname: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501

        self._hostname = hostname

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
        if not isinstance(other, ApplianceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplianceRequest):
            return True

        return self.to_dict() != other.to_dict()
