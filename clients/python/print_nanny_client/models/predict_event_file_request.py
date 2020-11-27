# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class PredictEventFileRequest(object):
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
        'annotated_image': 'file',
        'hash': 'str',
        'original_image': 'file'
    }

    attribute_map = {
        'annotated_image': 'annotated_image',
        'hash': 'hash',
        'original_image': 'original_image'
    }

    def __init__(self, annotated_image=None, hash=None, original_image=None, local_vars_configuration=None):  # noqa: E501
        """PredictEventFileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotated_image = None
        self._hash = None
        self._original_image = None
        self.discriminator = None

        self.annotated_image = annotated_image
        self.hash = hash
        self.original_image = original_image

    @property
    def annotated_image(self):
        """Gets the annotated_image of this PredictEventFileRequest.  # noqa: E501


        :return: The annotated_image of this PredictEventFileRequest.  # noqa: E501
        :rtype: file
        """
        return self._annotated_image

    @annotated_image.setter
    def annotated_image(self, annotated_image):
        """Sets the annotated_image of this PredictEventFileRequest.


        :param annotated_image: The annotated_image of this PredictEventFileRequest.  # noqa: E501
        :type annotated_image: file
        """
        if self.local_vars_configuration.client_side_validation and annotated_image is None:  # noqa: E501
            raise ValueError("Invalid value for `annotated_image`, must not be `None`")  # noqa: E501

        self._annotated_image = annotated_image

    @property
    def hash(self):
        """Gets the hash of this PredictEventFileRequest.  # noqa: E501


        :return: The hash of this PredictEventFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this PredictEventFileRequest.


        :param hash: The hash of this PredictEventFileRequest.  # noqa: E501
        :type hash: str
        """
        if self.local_vars_configuration.client_side_validation and hash is None:  # noqa: E501
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hash is not None and len(hash) > 255):
            raise ValueError("Invalid value for `hash`, length must be less than or equal to `255`")  # noqa: E501

        self._hash = hash

    @property
    def original_image(self):
        """Gets the original_image of this PredictEventFileRequest.  # noqa: E501


        :return: The original_image of this PredictEventFileRequest.  # noqa: E501
        :rtype: file
        """
        return self._original_image

    @original_image.setter
    def original_image(self, original_image):
        """Sets the original_image of this PredictEventFileRequest.


        :param original_image: The original_image of this PredictEventFileRequest.  # noqa: E501
        :type original_image: file
        """
        if self.local_vars_configuration.client_side_validation and original_image is None:  # noqa: E501
            raise ValueError("Invalid value for `original_image`, must not be `None`")  # noqa: E501

        self._original_image = original_image

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
        if not isinstance(other, PredictEventFileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PredictEventFileRequest):
            return True

        return self.to_dict() != other.to_dict()
