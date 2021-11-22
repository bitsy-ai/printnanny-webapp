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


class OctoprintPythonRequest(object):
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
        'version': 'str',
        'pip': 'str',
        'virtualenv': 'str'
    }

    attribute_map = {
        'version': 'version',
        'pip': 'pip',
        'virtualenv': 'virtualenv'
    }

    def __init__(self, version=None, pip=None, virtualenv=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintPythonRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._pip = None
        self._virtualenv = None
        self.discriminator = None

        self.version = version
        self.pip = pip
        self.virtualenv = virtualenv

    @property
    def version(self):
        """Gets the version of this OctoprintPythonRequest.  # noqa: E501


        :return: The version of this OctoprintPythonRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OctoprintPythonRequest.


        :param version: The version of this OctoprintPythonRequest.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def pip(self):
        """Gets the pip of this OctoprintPythonRequest.  # noqa: E501


        :return: The pip of this OctoprintPythonRequest.  # noqa: E501
        :rtype: str
        """
        return self._pip

    @pip.setter
    def pip(self, pip):
        """Sets the pip of this OctoprintPythonRequest.


        :param pip: The pip of this OctoprintPythonRequest.  # noqa: E501
        :type pip: str
        """
        if self.local_vars_configuration.client_side_validation and pip is None:  # noqa: E501
            raise ValueError("Invalid value for `pip`, must not be `None`")  # noqa: E501

        self._pip = pip

    @property
    def virtualenv(self):
        """Gets the virtualenv of this OctoprintPythonRequest.  # noqa: E501


        :return: The virtualenv of this OctoprintPythonRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtualenv

    @virtualenv.setter
    def virtualenv(self, virtualenv):
        """Sets the virtualenv of this OctoprintPythonRequest.


        :param virtualenv: The virtualenv of this OctoprintPythonRequest.  # noqa: E501
        :type virtualenv: str
        """
        if self.local_vars_configuration.client_side_validation and virtualenv is None:  # noqa: E501
            raise ValueError("Invalid value for `virtualenv`, must not be `None`")  # noqa: E501

        self._virtualenv = virtualenv

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
        if not isinstance(other, OctoprintPythonRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintPythonRequest):
            return True

        return self.to_dict() != other.to_dict()
