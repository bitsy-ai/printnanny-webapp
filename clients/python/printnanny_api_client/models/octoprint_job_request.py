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


class OctoprintJobRequest(object):
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
        'file': 'OctoprintFileRequest',
        'estimated_print_time': 'float',
        'average_print_time': 'float',
        'last_print_time': 'float',
        'filament': 'dict(str, object)'
    }

    attribute_map = {
        'file': 'file',
        'estimated_print_time': 'estimatedPrintTime',
        'average_print_time': 'averagePrintTime',
        'last_print_time': 'lastPrintTime',
        'filament': 'filament'
    }

    def __init__(self, file=None, estimated_print_time=None, average_print_time=None, last_print_time=None, filament=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintJobRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._file = None
        self._estimated_print_time = None
        self._average_print_time = None
        self._last_print_time = None
        self._filament = None
        self.discriminator = None

        self.file = file
        self.estimated_print_time = estimated_print_time
        self.average_print_time = average_print_time
        self.last_print_time = last_print_time
        self.filament = filament

    @property
    def file(self):
        """Gets the file of this OctoprintJobRequest.  # noqa: E501


        :return: The file of this OctoprintJobRequest.  # noqa: E501
        :rtype: OctoprintFileRequest
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this OctoprintJobRequest.


        :param file: The file of this OctoprintJobRequest.  # noqa: E501
        :type file: OctoprintFileRequest
        """

        self._file = file

    @property
    def estimated_print_time(self):
        """Gets the estimated_print_time of this OctoprintJobRequest.  # noqa: E501


        :return: The estimated_print_time of this OctoprintJobRequest.  # noqa: E501
        :rtype: float
        """
        return self._estimated_print_time

    @estimated_print_time.setter
    def estimated_print_time(self, estimated_print_time):
        """Sets the estimated_print_time of this OctoprintJobRequest.


        :param estimated_print_time: The estimated_print_time of this OctoprintJobRequest.  # noqa: E501
        :type estimated_print_time: float
        """

        self._estimated_print_time = estimated_print_time

    @property
    def average_print_time(self):
        """Gets the average_print_time of this OctoprintJobRequest.  # noqa: E501


        :return: The average_print_time of this OctoprintJobRequest.  # noqa: E501
        :rtype: float
        """
        return self._average_print_time

    @average_print_time.setter
    def average_print_time(self, average_print_time):
        """Sets the average_print_time of this OctoprintJobRequest.


        :param average_print_time: The average_print_time of this OctoprintJobRequest.  # noqa: E501
        :type average_print_time: float
        """

        self._average_print_time = average_print_time

    @property
    def last_print_time(self):
        """Gets the last_print_time of this OctoprintJobRequest.  # noqa: E501


        :return: The last_print_time of this OctoprintJobRequest.  # noqa: E501
        :rtype: float
        """
        return self._last_print_time

    @last_print_time.setter
    def last_print_time(self, last_print_time):
        """Sets the last_print_time of this OctoprintJobRequest.


        :param last_print_time: The last_print_time of this OctoprintJobRequest.  # noqa: E501
        :type last_print_time: float
        """

        self._last_print_time = last_print_time

    @property
    def filament(self):
        """Gets the filament of this OctoprintJobRequest.  # noqa: E501


        :return: The filament of this OctoprintJobRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._filament

    @filament.setter
    def filament(self, filament):
        """Sets the filament of this OctoprintJobRequest.


        :param filament: The filament of this OctoprintJobRequest.  # noqa: E501
        :type filament: dict(str, object)
        """

        self._filament = filament

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
        if not isinstance(other, OctoprintJobRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintJobRequest):
            return True

        return self.to_dict() != other.to_dict()
