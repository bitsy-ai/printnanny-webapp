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


class Camera(object):
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
        'updated_dt': 'datetime',
        'user': 'int',
        'appliance': 'int',
        'name': 'str',
        'camera_type': 'CameraTypeEnum',
        'camera_source': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'deleted': 'deleted',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'user': 'user',
        'appliance': 'appliance',
        'name': 'name',
        'camera_type': 'camera_type',
        'camera_source': 'camera_source',
        'url': 'url'
    }

    def __init__(self, id=None, deleted=None, created_dt=None, updated_dt=None, user=None, appliance=None, name=None, camera_type=None, camera_source=None, url=None, local_vars_configuration=None):  # noqa: E501
        """Camera - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deleted = None
        self._created_dt = None
        self._updated_dt = None
        self._user = None
        self._appliance = None
        self._name = None
        self._camera_type = None
        self._camera_source = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if deleted is not None:
            self.deleted = deleted
        if created_dt is not None:
            self.created_dt = created_dt
        if updated_dt is not None:
            self.updated_dt = updated_dt
        if user is not None:
            self.user = user
        if appliance is not None:
            self.appliance = appliance
        self.name = name
        self.camera_type = camera_type
        self.camera_source = camera_source
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this Camera.  # noqa: E501


        :return: The id of this Camera.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Camera.


        :param id: The id of this Camera.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def deleted(self):
        """Gets the deleted of this Camera.  # noqa: E501


        :return: The deleted of this Camera.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Camera.


        :param deleted: The deleted of this Camera.  # noqa: E501
        :type deleted: datetime
        """

        self._deleted = deleted

    @property
    def created_dt(self):
        """Gets the created_dt of this Camera.  # noqa: E501


        :return: The created_dt of this Camera.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Camera.


        :param created_dt: The created_dt of this Camera.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this Camera.  # noqa: E501


        :return: The updated_dt of this Camera.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this Camera.


        :param updated_dt: The updated_dt of this Camera.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def user(self):
        """Gets the user of this Camera.  # noqa: E501


        :return: The user of this Camera.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Camera.


        :param user: The user of this Camera.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def appliance(self):
        """Gets the appliance of this Camera.  # noqa: E501


        :return: The appliance of this Camera.  # noqa: E501
        :rtype: int
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this Camera.


        :param appliance: The appliance of this Camera.  # noqa: E501
        :type appliance: int
        """

        self._appliance = appliance

    @property
    def name(self):
        """Gets the name of this Camera.  # noqa: E501


        :return: The name of this Camera.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Camera.


        :param name: The name of this Camera.  # noqa: E501
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
        """Gets the camera_type of this Camera.  # noqa: E501


        :return: The camera_type of this Camera.  # noqa: E501
        :rtype: CameraTypeEnum
        """
        return self._camera_type

    @camera_type.setter
    def camera_type(self, camera_type):
        """Sets the camera_type of this Camera.


        :param camera_type: The camera_type of this Camera.  # noqa: E501
        :type camera_type: CameraTypeEnum
        """

        self._camera_type = camera_type

    @property
    def camera_source(self):
        """Gets the camera_source of this Camera.  # noqa: E501


        :return: The camera_source of this Camera.  # noqa: E501
        :rtype: str
        """
        return self._camera_source

    @camera_source.setter
    def camera_source(self, camera_source):
        """Sets the camera_source of this Camera.


        :param camera_source: The camera_source of this Camera.  # noqa: E501
        :type camera_source: str
        """
        if self.local_vars_configuration.client_side_validation and camera_source is None:  # noqa: E501
            raise ValueError("Invalid value for `camera_source`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                camera_source is not None and len(camera_source) > 255):
            raise ValueError("Invalid value for `camera_source`, length must be less than or equal to `255`")  # noqa: E501

        self._camera_source = camera_source

    @property
    def url(self):
        """Gets the url of this Camera.  # noqa: E501


        :return: The url of this Camera.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Camera.


        :param url: The url of this Camera.  # noqa: E501
        :type url: str
        """

        self._url = url

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
        if not isinstance(other, Camera):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Camera):
            return True

        return self.to_dict() != other.to_dict()
