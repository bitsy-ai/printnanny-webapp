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


class CameraRequest(object):
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
        'name': 'str',
        'camera_type': 'CameraTypeEnum',
        'camera_source': 'str'
    }

    attribute_map = {
        'name': 'name',
        'camera_type': 'camera_type',
        'camera_source': 'camera_source'
    }

    def __init__(self, name=None, camera_type=None, camera_source=None, local_vars_configuration=None):  # noqa: E501
        """CameraRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._camera_type = None
        self._camera_source = None
        self.discriminator = None

        self.name = name
        self.camera_type = camera_type
        self.camera_source = camera_source

    @property
    def name(self):
        """Gets the name of this CameraRequest.  # noqa: E501


        :return: The name of this CameraRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CameraRequest.


        :param name: The name of this CameraRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def camera_type(self):
        """Gets the camera_type of this CameraRequest.  # noqa: E501


        :return: The camera_type of this CameraRequest.  # noqa: E501
        :rtype: CameraTypeEnum
        """
        return self._camera_type

    @camera_type.setter
    def camera_type(self, camera_type):
        """Sets the camera_type of this CameraRequest.


        :param camera_type: The camera_type of this CameraRequest.  # noqa: E501
        :type camera_type: CameraTypeEnum
        """

        self._camera_type = camera_type

    @property
    def camera_source(self):
        """Gets the camera_source of this CameraRequest.  # noqa: E501


        :return: The camera_source of this CameraRequest.  # noqa: E501
        :rtype: str
        """
        return self._camera_source

    @camera_source.setter
    def camera_source(self, camera_source):
        """Sets the camera_source of this CameraRequest.


        :param camera_source: The camera_source of this CameraRequest.  # noqa: E501
        :type camera_source: str
        """
        if self.local_vars_configuration.client_side_validation and camera_source is None:  # noqa: E501
            raise ValueError("Invalid value for `camera_source`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                camera_source is not None and len(camera_source) > 255):
            raise ValueError("Invalid value for `camera_source`, length must be less than or equal to `255`")  # noqa: E501

        self._camera_source = camera_source

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
        if not isinstance(other, CameraRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CameraRequest):
            return True

        return self.to_dict() != other.to_dict()
