# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
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


class DeviceUrls(object):
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
        'cloud_dash': 'str',
        'edge_dash': 'str',
        'swupdate': 'str',
        'octoprint': 'str'
    }

    attribute_map = {
        'cloud_dash': 'cloud_dash',
        'edge_dash': 'edge_dash',
        'swupdate': 'swupdate',
        'octoprint': 'octoprint'
    }

    def __init__(self, cloud_dash=None, edge_dash=None, swupdate=None, octoprint=None, local_vars_configuration=None):  # noqa: E501
        """DeviceUrls - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_dash = None
        self._edge_dash = None
        self._swupdate = None
        self._octoprint = None
        self.discriminator = None

        self.cloud_dash = cloud_dash
        self.edge_dash = edge_dash
        self.swupdate = swupdate
        self.octoprint = octoprint

    @property
    def cloud_dash(self):
        """Gets the cloud_dash of this DeviceUrls.  # noqa: E501


        :return: The cloud_dash of this DeviceUrls.  # noqa: E501
        :rtype: str
        """
        return self._cloud_dash

    @cloud_dash.setter
    def cloud_dash(self, cloud_dash):
        """Sets the cloud_dash of this DeviceUrls.


        :param cloud_dash: The cloud_dash of this DeviceUrls.  # noqa: E501
        :type cloud_dash: str
        """
        if self.local_vars_configuration.client_side_validation and cloud_dash is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud_dash`, must not be `None`")  # noqa: E501

        self._cloud_dash = cloud_dash

    @property
    def edge_dash(self):
        """Gets the edge_dash of this DeviceUrls.  # noqa: E501


        :return: The edge_dash of this DeviceUrls.  # noqa: E501
        :rtype: str
        """
        return self._edge_dash

    @edge_dash.setter
    def edge_dash(self, edge_dash):
        """Sets the edge_dash of this DeviceUrls.


        :param edge_dash: The edge_dash of this DeviceUrls.  # noqa: E501
        :type edge_dash: str
        """
        if self.local_vars_configuration.client_side_validation and edge_dash is None:  # noqa: E501
            raise ValueError("Invalid value for `edge_dash`, must not be `None`")  # noqa: E501

        self._edge_dash = edge_dash

    @property
    def swupdate(self):
        """Gets the swupdate of this DeviceUrls.  # noqa: E501


        :return: The swupdate of this DeviceUrls.  # noqa: E501
        :rtype: str
        """
        return self._swupdate

    @swupdate.setter
    def swupdate(self, swupdate):
        """Sets the swupdate of this DeviceUrls.


        :param swupdate: The swupdate of this DeviceUrls.  # noqa: E501
        :type swupdate: str
        """
        if self.local_vars_configuration.client_side_validation and swupdate is None:  # noqa: E501
            raise ValueError("Invalid value for `swupdate`, must not be `None`")  # noqa: E501

        self._swupdate = swupdate

    @property
    def octoprint(self):
        """Gets the octoprint of this DeviceUrls.  # noqa: E501


        :return: The octoprint of this DeviceUrls.  # noqa: E501
        :rtype: str
        """
        return self._octoprint

    @octoprint.setter
    def octoprint(self, octoprint):
        """Sets the octoprint of this DeviceUrls.


        :param octoprint: The octoprint of this DeviceUrls.  # noqa: E501
        :type octoprint: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint`, must not be `None`")  # noqa: E501

        self._octoprint = octoprint

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
        if not isinstance(other, DeviceUrls):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceUrls):
            return True

        return self.to_dict() != other.to_dict()