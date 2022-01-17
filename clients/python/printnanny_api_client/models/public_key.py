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


class PublicKey(object):
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
        'pem': 'str',
        'cipher': 'CipherEnum',
        'length': 'int',
        'fingerprint': 'str',
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'device': 'int'
    }

    attribute_map = {
        'id': 'id',
        'pem': 'pem',
        'cipher': 'cipher',
        'length': 'length',
        'fingerprint': 'fingerprint',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'device': 'device'
    }

    def __init__(self, id=None, pem=None, cipher=None, length=None, fingerprint=None, created_dt=None, updated_dt=None, device=None, local_vars_configuration=None):  # noqa: E501
        """PublicKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._pem = None
        self._cipher = None
        self._length = None
        self._fingerprint = None
        self._created_dt = None
        self._updated_dt = None
        self._device = None
        self.discriminator = None

        self.id = id
        self.pem = pem
        self.cipher = cipher
        self.length = length
        self.fingerprint = fingerprint
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.device = device

    @property
    def id(self):
        """Gets the id of this PublicKey.  # noqa: E501


        :return: The id of this PublicKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicKey.


        :param id: The id of this PublicKey.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def pem(self):
        """Gets the pem of this PublicKey.  # noqa: E501


        :return: The pem of this PublicKey.  # noqa: E501
        :rtype: str
        """
        return self._pem

    @pem.setter
    def pem(self, pem):
        """Sets the pem of this PublicKey.


        :param pem: The pem of this PublicKey.  # noqa: E501
        :type pem: str
        """
        if self.local_vars_configuration.client_side_validation and pem is None:  # noqa: E501
            raise ValueError("Invalid value for `pem`, must not be `None`")  # noqa: E501

        self._pem = pem

    @property
    def cipher(self):
        """Gets the cipher of this PublicKey.  # noqa: E501


        :return: The cipher of this PublicKey.  # noqa: E501
        :rtype: CipherEnum
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this PublicKey.


        :param cipher: The cipher of this PublicKey.  # noqa: E501
        :type cipher: CipherEnum
        """
        if self.local_vars_configuration.client_side_validation and cipher is None:  # noqa: E501
            raise ValueError("Invalid value for `cipher`, must not be `None`")  # noqa: E501

        self._cipher = cipher

    @property
    def length(self):
        """Gets the length of this PublicKey.  # noqa: E501


        :return: The length of this PublicKey.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this PublicKey.


        :param length: The length of this PublicKey.  # noqa: E501
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
        """Gets the fingerprint of this PublicKey.  # noqa: E501


        :return: The fingerprint of this PublicKey.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this PublicKey.


        :param fingerprint: The fingerprint of this PublicKey.  # noqa: E501
        :type fingerprint: str
        """
        if self.local_vars_configuration.client_side_validation and fingerprint is None:  # noqa: E501
            raise ValueError("Invalid value for `fingerprint`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fingerprint is not None and len(fingerprint) > 255):
            raise ValueError("Invalid value for `fingerprint`, length must be less than or equal to `255`")  # noqa: E501

        self._fingerprint = fingerprint

    @property
    def created_dt(self):
        """Gets the created_dt of this PublicKey.  # noqa: E501


        :return: The created_dt of this PublicKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PublicKey.


        :param created_dt: The created_dt of this PublicKey.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this PublicKey.  # noqa: E501


        :return: The updated_dt of this PublicKey.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this PublicKey.


        :param updated_dt: The updated_dt of this PublicKey.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def device(self):
        """Gets the device of this PublicKey.  # noqa: E501


        :return: The device of this PublicKey.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PublicKey.


        :param device: The device of this PublicKey.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, PublicKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicKey):
            return True

        return self.to_dict() != other.to_dict()
