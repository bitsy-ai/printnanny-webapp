# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.133.3
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


class VideoRecordingFinalizeRequest(object):
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
        'recording_end': 'datetime'
    }

    attribute_map = {
        'recording_end': 'recording_end'
    }

    def __init__(self, recording_end=None, local_vars_configuration=None):  # noqa: E501
        """VideoRecordingFinalizeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._recording_end = None
        self.discriminator = None

        self.recording_end = recording_end

    @property
    def recording_end(self):
        """Gets the recording_end of this VideoRecordingFinalizeRequest.  # noqa: E501


        :return: The recording_end of this VideoRecordingFinalizeRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._recording_end

    @recording_end.setter
    def recording_end(self, recording_end):
        """Sets the recording_end of this VideoRecordingFinalizeRequest.


        :param recording_end: The recording_end of this VideoRecordingFinalizeRequest.  # noqa: E501
        :type recording_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and recording_end is None:  # noqa: E501
            raise ValueError("Invalid value for `recording_end`, must not be `None`")  # noqa: E501

        self._recording_end = recording_end

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
        if not isinstance(other, VideoRecordingFinalizeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VideoRecordingFinalizeRequest):
            return True

        return self.to_dict() != other.to_dict()
