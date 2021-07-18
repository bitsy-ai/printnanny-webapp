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


class PrinterProfile(object):
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
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'name': 'str',
        'local_webcam': 'str',
        'polymorphic_ctype': 'int',
        'user': 'int',
        'controller': 'int',
        'device': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'name': 'name',
        'local_webcam': 'local_webcam',
        'polymorphic_ctype': 'polymorphic_ctype',
        'user': 'user',
        'controller': 'controller',
        'device': 'device'
    }

    def __init__(self, id=None, created_dt=None, updated_dt=None, name=None, local_webcam=None, polymorphic_ctype=None, user=None, controller=None, device=None, local_vars_configuration=None):  # noqa: E501
        """PrinterProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._updated_dt = None
        self._name = None
        self._local_webcam = None
        self._polymorphic_ctype = None
        self._user = None
        self._controller = None
        self._device = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.name = name
        self.local_webcam = local_webcam
        self.polymorphic_ctype = polymorphic_ctype
        self.user = user
        self.controller = controller
        self.device = device

    @property
    def id(self):
        """Gets the id of this PrinterProfile.  # noqa: E501


        :return: The id of this PrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrinterProfile.


        :param id: The id of this PrinterProfile.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this PrinterProfile.  # noqa: E501


        :return: The created_dt of this PrinterProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PrinterProfile.


        :param created_dt: The created_dt of this PrinterProfile.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this PrinterProfile.  # noqa: E501


        :return: The updated_dt of this PrinterProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this PrinterProfile.


        :param updated_dt: The updated_dt of this PrinterProfile.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def name(self):
        """Gets the name of this PrinterProfile.  # noqa: E501


        :return: The name of this PrinterProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrinterProfile.


        :param name: The name of this PrinterProfile.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def local_webcam(self):
        """Gets the local_webcam of this PrinterProfile.  # noqa: E501


        :return: The local_webcam of this PrinterProfile.  # noqa: E501
        :rtype: str
        """
        return self._local_webcam

    @local_webcam.setter
    def local_webcam(self, local_webcam):
        """Sets the local_webcam of this PrinterProfile.


        :param local_webcam: The local_webcam of this PrinterProfile.  # noqa: E501
        :type local_webcam: str
        """
        if self.local_vars_configuration.client_side_validation and local_webcam is None:  # noqa: E501
            raise ValueError("Invalid value for `local_webcam`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                local_webcam is not None and len(local_webcam) > 255):
            raise ValueError("Invalid value for `local_webcam`, length must be less than or equal to `255`")  # noqa: E501

        self._local_webcam = local_webcam

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this PrinterProfile.  # noqa: E501


        :return: The polymorphic_ctype of this PrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this PrinterProfile.


        :param polymorphic_ctype: The polymorphic_ctype of this PrinterProfile.  # noqa: E501
        :type polymorphic_ctype: int
        """
        if self.local_vars_configuration.client_side_validation and polymorphic_ctype is None:  # noqa: E501
            raise ValueError("Invalid value for `polymorphic_ctype`, must not be `None`")  # noqa: E501

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def user(self):
        """Gets the user of this PrinterProfile.  # noqa: E501


        :return: The user of this PrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PrinterProfile.


        :param user: The user of this PrinterProfile.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def controller(self):
        """Gets the controller of this PrinterProfile.  # noqa: E501


        :return: The controller of this PrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this PrinterProfile.


        :param controller: The controller of this PrinterProfile.  # noqa: E501
        :type controller: int
        """
        if self.local_vars_configuration.client_side_validation and controller is None:  # noqa: E501
            raise ValueError("Invalid value for `controller`, must not be `None`")  # noqa: E501

        self._controller = controller

    @property
    def device(self):
        """Gets the device of this PrinterProfile.  # noqa: E501


        :return: The device of this PrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PrinterProfile.


        :param device: The device of this PrinterProfile.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

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
        if not isinstance(other, PrinterProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrinterProfile):
            return True

        return self.to_dict() != other.to_dict()
