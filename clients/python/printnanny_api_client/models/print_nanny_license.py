# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.110.1
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


class PrintNannyLicense(object):
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
        'api': 'PrintNannyApiConfig',
        'pi': 'Pi'
    }

    attribute_map = {
        'api': 'api',
        'pi': 'pi'
    }

    def __init__(self, api=None, pi=None, local_vars_configuration=None):  # noqa: E501
        """PrintNannyLicense - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._api = None
        self._pi = None
        self.discriminator = None

        self.api = api
        self.pi = pi

    @property
    def api(self):
        """Gets the api of this PrintNannyLicense.  # noqa: E501


        :return: The api of this PrintNannyLicense.  # noqa: E501
        :rtype: PrintNannyApiConfig
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this PrintNannyLicense.


        :param api: The api of this PrintNannyLicense.  # noqa: E501
        :type api: PrintNannyApiConfig
        """

        self._api = api

    @property
    def pi(self):
        """Gets the pi of this PrintNannyLicense.  # noqa: E501


        :return: The pi of this PrintNannyLicense.  # noqa: E501
        :rtype: Pi
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PrintNannyLicense.


        :param pi: The pi of this PrintNannyLicense.  # noqa: E501
        :type pi: Pi
        """

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
        if not isinstance(other, PrintNannyLicense):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintNannyLicense):
            return True

        return self.to_dict() != other.to_dict()
