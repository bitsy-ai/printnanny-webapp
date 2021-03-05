# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class ManualVideoUploadAlertRequest(object):
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
        'dismissed': 'bool',
        'alert_type': 'AlertTypeEnum'
    }

    attribute_map = {
        'dismissed': 'dismissed',
        'alert_type': 'alert_type'
    }

    def __init__(self, dismissed=None, alert_type=None, local_vars_configuration=None):  # noqa: E501
        """ManualVideoUploadAlertRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dismissed = None
        self._alert_type = None
        self.discriminator = None

        if dismissed is not None:
            self.dismissed = dismissed
        self.alert_type = alert_type

    @property
    def dismissed(self):
        """Gets the dismissed of this ManualVideoUploadAlertRequest.  # noqa: E501


        :return: The dismissed of this ManualVideoUploadAlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dismissed

    @dismissed.setter
    def dismissed(self, dismissed):
        """Sets the dismissed of this ManualVideoUploadAlertRequest.


        :param dismissed: The dismissed of this ManualVideoUploadAlertRequest.  # noqa: E501
        :type dismissed: bool
        """

        self._dismissed = dismissed

    @property
    def alert_type(self):
        """Gets the alert_type of this ManualVideoUploadAlertRequest.  # noqa: E501


        :return: The alert_type of this ManualVideoUploadAlertRequest.  # noqa: E501
        :rtype: AlertTypeEnum
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this ManualVideoUploadAlertRequest.


        :param alert_type: The alert_type of this ManualVideoUploadAlertRequest.  # noqa: E501
        :type alert_type: AlertTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and alert_type is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_type`, must not be `None`")  # noqa: E501

        self._alert_type = alert_type

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, ManualVideoUploadAlertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManualVideoUploadAlertRequest):
            return True

        return self.to_dict() != other.to_dict()
