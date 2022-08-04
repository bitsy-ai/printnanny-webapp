# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.6
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


class PublicKeyRequest(object):
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
        'pem': 'str',
        'cipher': 'str',
        'length': 'int',
        'fingerprint': 'str',
        'pi': 'int'
    }

    attribute_map = {
        'pem': 'pem',
        'cipher': 'cipher',
        'length': 'length',
        'fingerprint': 'fingerprint',
        'pi': 'pi'
    }

    def __init__(self, pem=None, cipher=None, length=None, fingerprint=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """PublicKeyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._pem = None
        self._cipher = None
        self._length = None
        self._fingerprint = None
        self._pi = None
        self.discriminator = None

        self.pem = pem
        self.cipher = cipher
        self.length = length
        self.fingerprint = fingerprint
        self.pi = pi

    @property
    def pem(self):
        """Gets the pem of this PublicKeyRequest.  # noqa: E501


        :return: The pem of this PublicKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._pem

    @pem.setter
    def pem(self, pem):
        """Sets the pem of this PublicKeyRequest.


        :param pem: The pem of this PublicKeyRequest.  # noqa: E501
        :type pem: str
        """
        if self.local_vars_configuration.client_side_validation and pem is None:  # noqa: E501
            raise ValueError("Invalid value for `pem`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pem is not None and len(pem) < 1):
            raise ValueError("Invalid value for `pem`, length must be greater than or equal to `1`")  # noqa: E501

        self._pem = pem

    @property
    def cipher(self):
        """Gets the cipher of this PublicKeyRequest.  # noqa: E501


        :return: The cipher of this PublicKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this PublicKeyRequest.


        :param cipher: The cipher of this PublicKeyRequest.  # noqa: E501
        :type cipher: str
        """
        if self.local_vars_configuration.client_side_validation and cipher is None:  # noqa: E501
            raise ValueError("Invalid value for `cipher`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cipher is not None and len(cipher) > 32):
            raise ValueError("Invalid value for `cipher`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cipher is not None and len(cipher) < 1):
            raise ValueError("Invalid value for `cipher`, length must be greater than or equal to `1`")  # noqa: E501

        self._cipher = cipher

    @property
    def length(self):
        """Gets the length of this PublicKeyRequest.  # noqa: E501


        :return: The length of this PublicKeyRequest.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this PublicKeyRequest.


        :param length: The length of this PublicKeyRequest.  # noqa: E501
        :type length: int
        """
        if self.local_vars_configuration.client_side_validation and length is None:  # noqa: E501
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                length is not None and length > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                length is not None and length < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._length = length

    @property
    def fingerprint(self):
        """Gets the fingerprint of this PublicKeyRequest.  # noqa: E501


        :return: The fingerprint of this PublicKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this PublicKeyRequest.


        :param fingerprint: The fingerprint of this PublicKeyRequest.  # noqa: E501
        :type fingerprint: str
        """
        if self.local_vars_configuration.client_side_validation and fingerprint is None:  # noqa: E501
            raise ValueError("Invalid value for `fingerprint`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fingerprint is not None and len(fingerprint) > 255):
            raise ValueError("Invalid value for `fingerprint`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fingerprint is not None and len(fingerprint) < 1):
            raise ValueError("Invalid value for `fingerprint`, length must be greater than or equal to `1`")  # noqa: E501

        self._fingerprint = fingerprint

    @property
    def pi(self):
        """Gets the pi of this PublicKeyRequest.  # noqa: E501


        :return: The pi of this PublicKeyRequest.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PublicKeyRequest.


        :param pi: The pi of this PublicKeyRequest.  # noqa: E501
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
        if not isinstance(other, PublicKeyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicKeyRequest):
            return True

        return self.to_dict() != other.to_dict()
