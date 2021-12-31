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


class Release(object):
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
        'id': 'int',
        'deleted': 'datetime',
        'created_dt': 'datetime',
        'name': 'str',
        'variant': 'ReleaseVariant',
        'image_url': 'str',
        'manifest_url': 'str',
        'sig_url': 'str',
        'checksum': 'str',
        'checksum_url': 'str',
        'release_channel': 'ReleaseChannelEnum'
    }

    attribute_map = {
        'id': 'id',
        'deleted': 'deleted',
        'created_dt': 'created_dt',
        'name': 'name',
        'variant': 'variant',
        'image_url': 'image_url',
        'manifest_url': 'manifest_url',
        'sig_url': 'sig_url',
        'checksum': 'checksum',
        'checksum_url': 'checksum_url',
        'release_channel': 'release_channel'
    }

    def __init__(self, id=None, deleted=None, created_dt=None, name=None, variant=None, image_url=None, manifest_url=None, sig_url=None, checksum=None, checksum_url=None, release_channel=None, local_vars_configuration=None):  # noqa: E501
        """Release - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deleted = None
        self._created_dt = None
        self._name = None
        self._variant = None
        self._image_url = None
        self._manifest_url = None
        self._sig_url = None
        self._checksum = None
        self._checksum_url = None
        self._release_channel = None
        self.discriminator = None

        self.id = id
        self.deleted = deleted
        self.created_dt = created_dt
        self.name = name
        self.variant = variant
        self.image_url = image_url
        self.manifest_url = manifest_url
        self.sig_url = sig_url
        self.checksum = checksum
        self.checksum_url = checksum_url
        if release_channel is not None:
            self.release_channel = release_channel

    @property
    def id(self):
        """Gets the id of this Release.  # noqa: E501


        :return: The id of this Release.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Release.


        :param id: The id of this Release.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def deleted(self):
        """Gets the deleted of this Release.  # noqa: E501


        :return: The deleted of this Release.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Release.


        :param deleted: The deleted of this Release.  # noqa: E501
        :type deleted: datetime
        """
        if self.local_vars_configuration.client_side_validation and deleted is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

    @property
    def created_dt(self):
        """Gets the created_dt of this Release.  # noqa: E501


        :return: The created_dt of this Release.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Release.


        :param created_dt: The created_dt of this Release.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def name(self):
        """Gets the name of this Release.  # noqa: E501


        :return: The name of this Release.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Release.


        :param name: The name of this Release.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def variant(self):
        """Gets the variant of this Release.  # noqa: E501


        :return: The variant of this Release.  # noqa: E501
        :rtype: ReleaseVariant
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this Release.


        :param variant: The variant of this Release.  # noqa: E501
        :type variant: ReleaseVariant
        """
        if self.local_vars_configuration.client_side_validation and variant is None:  # noqa: E501
            raise ValueError("Invalid value for `variant`, must not be `None`")  # noqa: E501

        self._variant = variant

    @property
    def image_url(self):
        """Gets the image_url of this Release.  # noqa: E501


        :return: The image_url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Release.


        :param image_url: The image_url of this Release.  # noqa: E501
        :type image_url: str
        """
        if self.local_vars_configuration.client_side_validation and image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_url is not None and len(image_url) > 255):
            raise ValueError("Invalid value for `image_url`, length must be less than or equal to `255`")  # noqa: E501

        self._image_url = image_url

    @property
    def manifest_url(self):
        """Gets the manifest_url of this Release.  # noqa: E501


        :return: The manifest_url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._manifest_url

    @manifest_url.setter
    def manifest_url(self, manifest_url):
        """Sets the manifest_url of this Release.


        :param manifest_url: The manifest_url of this Release.  # noqa: E501
        :type manifest_url: str
        """
        if self.local_vars_configuration.client_side_validation and manifest_url is None:  # noqa: E501
            raise ValueError("Invalid value for `manifest_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                manifest_url is not None and len(manifest_url) > 255):
            raise ValueError("Invalid value for `manifest_url`, length must be less than or equal to `255`")  # noqa: E501

        self._manifest_url = manifest_url

    @property
    def sig_url(self):
        """Gets the sig_url of this Release.  # noqa: E501


        :return: The sig_url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._sig_url

    @sig_url.setter
    def sig_url(self, sig_url):
        """Sets the sig_url of this Release.


        :param sig_url: The sig_url of this Release.  # noqa: E501
        :type sig_url: str
        """
        if self.local_vars_configuration.client_side_validation and sig_url is None:  # noqa: E501
            raise ValueError("Invalid value for `sig_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sig_url is not None and len(sig_url) > 255):
            raise ValueError("Invalid value for `sig_url`, length must be less than or equal to `255`")  # noqa: E501

        self._sig_url = sig_url

    @property
    def checksum(self):
        """Gets the checksum of this Release.  # noqa: E501


        :return: The checksum of this Release.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this Release.


        :param checksum: The checksum of this Release.  # noqa: E501
        :type checksum: str
        """
        if self.local_vars_configuration.client_side_validation and checksum is None:  # noqa: E501
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                checksum is not None and len(checksum) > 255):
            raise ValueError("Invalid value for `checksum`, length must be less than or equal to `255`")  # noqa: E501

        self._checksum = checksum

    @property
    def checksum_url(self):
        """Gets the checksum_url of this Release.  # noqa: E501


        :return: The checksum_url of this Release.  # noqa: E501
        :rtype: str
        """
        return self._checksum_url

    @checksum_url.setter
    def checksum_url(self, checksum_url):
        """Sets the checksum_url of this Release.


        :param checksum_url: The checksum_url of this Release.  # noqa: E501
        :type checksum_url: str
        """
        if self.local_vars_configuration.client_side_validation and checksum_url is None:  # noqa: E501
            raise ValueError("Invalid value for `checksum_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                checksum_url is not None and len(checksum_url) > 255):
            raise ValueError("Invalid value for `checksum_url`, length must be less than or equal to `255`")  # noqa: E501

        self._checksum_url = checksum_url

    @property
    def release_channel(self):
        """Gets the release_channel of this Release.  # noqa: E501


        :return: The release_channel of this Release.  # noqa: E501
        :rtype: ReleaseChannelEnum
        """
        return self._release_channel

    @release_channel.setter
    def release_channel(self, release_channel):
        """Sets the release_channel of this Release.


        :param release_channel: The release_channel of this Release.  # noqa: E501
        :type release_channel: ReleaseChannelEnum
        """

        self._release_channel = release_channel

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
        if not isinstance(other, Release):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Release):
            return True

        return self.to_dict() != other.to_dict()
