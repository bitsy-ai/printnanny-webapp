# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.107.2
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


class OctoPrintPrintJobPayloadRequest(object):
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
        'path': 'str',
        'origin': 'str',
        'size': 'int',
        'time': 'float',
        'position': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'origin': 'origin',
        'size': 'size',
        'time': 'time',
        'position': 'position'
    }

    def __init__(self, name=None, path=None, origin=None, size=None, time=None, position=None, local_vars_configuration=None):  # noqa: E501
        """OctoPrintPrintJobPayloadRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._path = None
        self._origin = None
        self._size = None
        self._time = None
        self._position = None
        self.discriminator = None

        self.name = name
        self.path = path
        self.origin = origin
        if size is not None:
            self.size = size
        if time is not None:
            self.time = time
        self.position = position

    @property
    def name(self):
        """Gets the name of this OctoPrintPrintJobPayloadRequest.  # noqa: E501


        :return: The name of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OctoPrintPrintJobPayloadRequest.


        :param name: The name of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this OctoPrintPrintJobPayloadRequest.  # noqa: E501


        :return: The path of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this OctoPrintPrintJobPayloadRequest.


        :param path: The path of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) < 1):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

    @property
    def origin(self):
        """Gets the origin of this OctoPrintPrintJobPayloadRequest.  # noqa: E501


        :return: The origin of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this OctoPrintPrintJobPayloadRequest.


        :param origin: The origin of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :type origin: str
        """
        if self.local_vars_configuration.client_side_validation and origin is None:  # noqa: E501
            raise ValueError("Invalid value for `origin`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                origin is not None and len(origin) < 1):
            raise ValueError("Invalid value for `origin`, length must be greater than or equal to `1`")  # noqa: E501

        self._origin = origin

    @property
    def size(self):
        """Gets the size of this OctoPrintPrintJobPayloadRequest.  # noqa: E501


        :return: The size of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OctoPrintPrintJobPayloadRequest.


        :param size: The size of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def time(self):
        """Gets the time of this OctoPrintPrintJobPayloadRequest.  # noqa: E501


        :return: The time of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OctoPrintPrintJobPayloadRequest.


        :param time: The time of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :type time: float
        """

        self._time = time

    @property
    def position(self):
        """Gets the position of this OctoPrintPrintJobPayloadRequest.  # noqa: E501


        :return: The position of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this OctoPrintPrintJobPayloadRequest.


        :param position: The position of this OctoPrintPrintJobPayloadRequest.  # noqa: E501
        :type position: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and position is None:  # noqa: E501
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

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
        if not isinstance(other, OctoPrintPrintJobPayloadRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoPrintPrintJobPayloadRequest):
            return True

        return self.to_dict() != other.to_dict()
