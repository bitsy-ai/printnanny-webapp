# coding: utf-8

"""
    print-nanny-client

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

from print_nanny_client.configuration import Configuration


class DeviceCalibrationRequest(object):
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
        'octoprint_device': 'int',
        'fps': 'float',
        'xy': 'dict(str, object)',
        'height': 'int',
        'width': 'int'
    }

    attribute_map = {
        'octoprint_device': 'octoprint_device',
        'fps': 'fps',
        'xy': 'xy',
        'height': 'height',
        'width': 'width'
    }

    def __init__(self, octoprint_device=None, fps=None, xy=None, height=None, width=None, local_vars_configuration=None):  # noqa: E501
        """DeviceCalibrationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._octoprint_device = None
        self._fps = None
        self._xy = None
        self._height = None
        self._width = None
        self.discriminator = None

        self.octoprint_device = octoprint_device
        if fps is not None:
            self.fps = fps
        self.xy = xy
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this DeviceCalibrationRequest.  # noqa: E501


        :return: The octoprint_device of this DeviceCalibrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this DeviceCalibrationRequest.


        :param octoprint_device: The octoprint_device of this DeviceCalibrationRequest.  # noqa: E501
        :type octoprint_device: int
        """
        if self.local_vars_configuration.client_side_validation and octoprint_device is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_device`, must not be `None`")  # noqa: E501

        self._octoprint_device = octoprint_device

    @property
    def fps(self):
        """Gets the fps of this DeviceCalibrationRequest.  # noqa: E501


        :return: The fps of this DeviceCalibrationRequest.  # noqa: E501
        :rtype: float
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this DeviceCalibrationRequest.


        :param fps: The fps of this DeviceCalibrationRequest.  # noqa: E501
        :type fps: float
        """

        self._fps = fps

    @property
    def xy(self):
        """Gets the xy of this DeviceCalibrationRequest.  # noqa: E501


        :return: The xy of this DeviceCalibrationRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._xy

    @xy.setter
    def xy(self, xy):
        """Sets the xy of this DeviceCalibrationRequest.


        :param xy: The xy of this DeviceCalibrationRequest.  # noqa: E501
        :type xy: dict(str, object)
        """

        self._xy = xy

    @property
    def height(self):
        """Gets the height of this DeviceCalibrationRequest.  # noqa: E501


        :return: The height of this DeviceCalibrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DeviceCalibrationRequest.


        :param height: The height of this DeviceCalibrationRequest.  # noqa: E501
        :type height: int
        """
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                height is not None and height < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._height = height

    @property
    def width(self):
        """Gets the width of this DeviceCalibrationRequest.  # noqa: E501


        :return: The width of this DeviceCalibrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DeviceCalibrationRequest.


        :param width: The width of this DeviceCalibrationRequest.  # noqa: E501
        :type width: int
        """
        if (self.local_vars_configuration.client_side_validation and
                width is not None and width > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                width is not None and width < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._width = width

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
        if not isinstance(other, DeviceCalibrationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceCalibrationRequest):
            return True

        return self.to_dict() != other.to_dict()
