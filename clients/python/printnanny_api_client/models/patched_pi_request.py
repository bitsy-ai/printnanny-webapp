# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.102.2
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


class PatchedPiRequest(object):
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
        'sbc': 'SbcEnum',
        'edition': 'OsEdition',
        'hostname': 'str',
        'fqdn': 'str',
        'favorite': 'bool',
        'setup_finished': 'bool'
    }

    attribute_map = {
        'sbc': 'sbc',
        'edition': 'edition',
        'hostname': 'hostname',
        'fqdn': 'fqdn',
        'favorite': 'favorite',
        'setup_finished': 'setup_finished'
    }

    def __init__(self, sbc=None, edition=None, hostname=None, fqdn=None, favorite=None, setup_finished=None, local_vars_configuration=None):  # noqa: E501
        """PatchedPiRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._sbc = None
        self._edition = None
        self._hostname = None
        self._fqdn = None
        self._favorite = None
        self._setup_finished = None
        self.discriminator = None

        if sbc is not None:
            self.sbc = sbc
        if edition is not None:
            self.edition = edition
        if hostname is not None:
            self.hostname = hostname
        if fqdn is not None:
            self.fqdn = fqdn
        if favorite is not None:
            self.favorite = favorite
        if setup_finished is not None:
            self.setup_finished = setup_finished

    @property
    def sbc(self):
        """Gets the sbc of this PatchedPiRequest.  # noqa: E501


        :return: The sbc of this PatchedPiRequest.  # noqa: E501
        :rtype: SbcEnum
        """
        return self._sbc

    @sbc.setter
    def sbc(self, sbc):
        """Sets the sbc of this PatchedPiRequest.


        :param sbc: The sbc of this PatchedPiRequest.  # noqa: E501
        :type sbc: SbcEnum
        """

        self._sbc = sbc

    @property
    def edition(self):
        """Gets the edition of this PatchedPiRequest.  # noqa: E501


        :return: The edition of this PatchedPiRequest.  # noqa: E501
        :rtype: OsEdition
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this PatchedPiRequest.


        :param edition: The edition of this PatchedPiRequest.  # noqa: E501
        :type edition: OsEdition
        """

        self._edition = edition

    @property
    def hostname(self):
        """Gets the hostname of this PatchedPiRequest.  # noqa: E501

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :return: The hostname of this PatchedPiRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PatchedPiRequest.

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :param hostname: The hostname of this PatchedPiRequest.  # noqa: E501
        :type hostname: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) < 1):
            raise ValueError("Invalid value for `hostname`, length must be greater than or equal to `1`")  # noqa: E501

        self._hostname = hostname

    @property
    def fqdn(self):
        """Gets the fqdn of this PatchedPiRequest.  # noqa: E501


        :return: The fqdn of this PatchedPiRequest.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this PatchedPiRequest.


        :param fqdn: The fqdn of this PatchedPiRequest.  # noqa: E501
        :type fqdn: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fqdn is not None and len(fqdn) > 255):
            raise ValueError("Invalid value for `fqdn`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fqdn is not None and len(fqdn) < 1):
            raise ValueError("Invalid value for `fqdn`, length must be greater than or equal to `1`")  # noqa: E501

        self._fqdn = fqdn

    @property
    def favorite(self):
        """Gets the favorite of this PatchedPiRequest.  # noqa: E501


        :return: The favorite of this PatchedPiRequest.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this PatchedPiRequest.


        :param favorite: The favorite of this PatchedPiRequest.  # noqa: E501
        :type favorite: bool
        """

        self._favorite = favorite

    @property
    def setup_finished(self):
        """Gets the setup_finished of this PatchedPiRequest.  # noqa: E501


        :return: The setup_finished of this PatchedPiRequest.  # noqa: E501
        :rtype: bool
        """
        return self._setup_finished

    @setup_finished.setter
    def setup_finished(self, setup_finished):
        """Sets the setup_finished of this PatchedPiRequest.


        :param setup_finished: The setup_finished of this PatchedPiRequest.  # noqa: E501
        :type setup_finished: bool
        """

        self._setup_finished = setup_finished

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
        if not isinstance(other, PatchedPiRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedPiRequest):
            return True

        return self.to_dict() != other.to_dict()
