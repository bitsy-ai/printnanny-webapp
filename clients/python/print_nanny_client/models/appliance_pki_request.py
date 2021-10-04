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


class AppliancePKIRequest(object):
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
        'public_key': 'str',
        'public_key_checksum': 'str',
        'private_key_checksum': 'str',
        'fingerprint': 'str',
        'appliance': 'int'
    }

    attribute_map = {
        'public_key': 'public_key',
        'public_key_checksum': 'public_key_checksum',
        'private_key_checksum': 'private_key_checksum',
        'fingerprint': 'fingerprint',
        'appliance': 'appliance'
    }

    def __init__(self, public_key=None, public_key_checksum=None, private_key_checksum=None, fingerprint=None, appliance=None, local_vars_configuration=None):  # noqa: E501
        """AppliancePKIRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._public_key = None
        self._public_key_checksum = None
        self._private_key_checksum = None
        self._fingerprint = None
        self._appliance = None
        self.discriminator = None

        self.public_key = public_key
        self.public_key_checksum = public_key_checksum
        self.private_key_checksum = private_key_checksum
        self.fingerprint = fingerprint
        self.appliance = appliance

    @property
    def public_key(self):
        """Gets the public_key of this AppliancePKIRequest.  # noqa: E501


        :return: The public_key of this AppliancePKIRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this AppliancePKIRequest.


        :param public_key: The public_key of this AppliancePKIRequest.  # noqa: E501
        :type public_key: str
        """
        if self.local_vars_configuration.client_side_validation and public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def public_key_checksum(self):
        """Gets the public_key_checksum of this AppliancePKIRequest.  # noqa: E501


        :return: The public_key_checksum of this AppliancePKIRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_key_checksum

    @public_key_checksum.setter
    def public_key_checksum(self, public_key_checksum):
        """Sets the public_key_checksum of this AppliancePKIRequest.


        :param public_key_checksum: The public_key_checksum of this AppliancePKIRequest.  # noqa: E501
        :type public_key_checksum: str
        """
        if self.local_vars_configuration.client_side_validation and public_key_checksum is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key_checksum`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                public_key_checksum is not None and len(public_key_checksum) > 255):
            raise ValueError("Invalid value for `public_key_checksum`, length must be less than or equal to `255`")  # noqa: E501

        self._public_key_checksum = public_key_checksum

    @property
    def private_key_checksum(self):
        """Gets the private_key_checksum of this AppliancePKIRequest.  # noqa: E501


        :return: The private_key_checksum of this AppliancePKIRequest.  # noqa: E501
        :rtype: str
        """
        return self._private_key_checksum

    @private_key_checksum.setter
    def private_key_checksum(self, private_key_checksum):
        """Sets the private_key_checksum of this AppliancePKIRequest.


        :param private_key_checksum: The private_key_checksum of this AppliancePKIRequest.  # noqa: E501
        :type private_key_checksum: str
        """
        if self.local_vars_configuration.client_side_validation and private_key_checksum is None:  # noqa: E501
            raise ValueError("Invalid value for `private_key_checksum`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                private_key_checksum is not None and len(private_key_checksum) > 255):
            raise ValueError("Invalid value for `private_key_checksum`, length must be less than or equal to `255`")  # noqa: E501

        self._private_key_checksum = private_key_checksum

    @property
    def fingerprint(self):
        """Gets the fingerprint of this AppliancePKIRequest.  # noqa: E501


        :return: The fingerprint of this AppliancePKIRequest.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this AppliancePKIRequest.


        :param fingerprint: The fingerprint of this AppliancePKIRequest.  # noqa: E501
        :type fingerprint: str
        """
        if self.local_vars_configuration.client_side_validation and fingerprint is None:  # noqa: E501
            raise ValueError("Invalid value for `fingerprint`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fingerprint is not None and len(fingerprint) > 255):
            raise ValueError("Invalid value for `fingerprint`, length must be less than or equal to `255`")  # noqa: E501

        self._fingerprint = fingerprint

    @property
    def appliance(self):
        """Gets the appliance of this AppliancePKIRequest.  # noqa: E501


        :return: The appliance of this AppliancePKIRequest.  # noqa: E501
        :rtype: int
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this AppliancePKIRequest.


        :param appliance: The appliance of this AppliancePKIRequest.  # noqa: E501
        :type appliance: int
        """
        if self.local_vars_configuration.client_side_validation and appliance is None:  # noqa: E501
            raise ValueError("Invalid value for `appliance`, must not be `None`")  # noqa: E501

        self._appliance = appliance

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
        if not isinstance(other, AppliancePKIRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppliancePKIRequest):
            return True

        return self.to_dict() != other.to_dict()
