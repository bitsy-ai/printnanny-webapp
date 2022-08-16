# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.101.2
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


class OctoPrinterProfile(object):
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
        'axes_e_inverted': 'bool',
        'axes_e_speed': 'int',
        'axes_x_speed': 'int',
        'axes_x_inverted': 'bool',
        'axes_y_inverted': 'bool',
        'axes_y_speed': 'int',
        'axes_z_inverted': 'bool',
        'axes_z_speed': 'int',
        'extruder_count': 'int',
        'extruder_nozzle_diameter': 'float',
        'extruder_shared_nozzle': 'bool',
        'heated_bed': 'bool',
        'heated_chamber': 'bool',
        'model': 'str',
        'name': 'str',
        'octoprint_key': 'str',
        'volume_custom_box': 'dict(str, object)',
        'volume_depth': 'float',
        'volume_formfactor': 'str',
        'volume_height': 'float',
        'volume_origin': 'str',
        'volume_width': 'float',
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'axes_e_inverted': 'axes_e_inverted',
        'axes_e_speed': 'axes_e_speed',
        'axes_x_speed': 'axes_x_speed',
        'axes_x_inverted': 'axes_x_inverted',
        'axes_y_inverted': 'axes_y_inverted',
        'axes_y_speed': 'axes_y_speed',
        'axes_z_inverted': 'axes_z_inverted',
        'axes_z_speed': 'axes_z_speed',
        'extruder_count': 'extruder_count',
        'extruder_nozzle_diameter': 'extruder_nozzle_diameter',
        'extruder_shared_nozzle': 'extruder_shared_nozzle',
        'heated_bed': 'heated_bed',
        'heated_chamber': 'heated_chamber',
        'model': 'model',
        'name': 'name',
        'octoprint_key': 'octoprint_key',
        'volume_custom_box': 'volume_custom_box',
        'volume_depth': 'volume_depth',
        'volume_formfactor': 'volume_formfactor',
        'volume_height': 'volume_height',
        'volume_origin': 'volume_origin',
        'volume_width': 'volume_width',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'user': 'user'
    }

    def __init__(self, id=None, axes_e_inverted=None, axes_e_speed=None, axes_x_speed=None, axes_x_inverted=None, axes_y_inverted=None, axes_y_speed=None, axes_z_inverted=None, axes_z_speed=None, extruder_count=None, extruder_nozzle_diameter=None, extruder_shared_nozzle=None, heated_bed=None, heated_chamber=None, model=None, name=None, octoprint_key=None, volume_custom_box=None, volume_depth=None, volume_formfactor=None, volume_height=None, volume_origin=None, volume_width=None, created_dt=None, updated_dt=None, user=None, local_vars_configuration=None):  # noqa: E501
        """OctoPrinterProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._axes_e_inverted = None
        self._axes_e_speed = None
        self._axes_x_speed = None
        self._axes_x_inverted = None
        self._axes_y_inverted = None
        self._axes_y_speed = None
        self._axes_z_inverted = None
        self._axes_z_speed = None
        self._extruder_count = None
        self._extruder_nozzle_diameter = None
        self._extruder_shared_nozzle = None
        self._heated_bed = None
        self._heated_chamber = None
        self._model = None
        self._name = None
        self._octoprint_key = None
        self._volume_custom_box = None
        self._volume_depth = None
        self._volume_formfactor = None
        self._volume_height = None
        self._volume_origin = None
        self._volume_width = None
        self._created_dt = None
        self._updated_dt = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.axes_e_inverted = axes_e_inverted
        self.axes_e_speed = axes_e_speed
        self.axes_x_speed = axes_x_speed
        self.axes_x_inverted = axes_x_inverted
        self.axes_y_inverted = axes_y_inverted
        self.axes_y_speed = axes_y_speed
        self.axes_z_inverted = axes_z_inverted
        self.axes_z_speed = axes_z_speed
        self.extruder_count = extruder_count
        self.extruder_nozzle_diameter = extruder_nozzle_diameter
        self.extruder_shared_nozzle = extruder_shared_nozzle
        self.heated_bed = heated_bed
        self.heated_chamber = heated_chamber
        self.model = model
        self.name = name
        self.octoprint_key = octoprint_key
        if volume_custom_box is not None:
            self.volume_custom_box = volume_custom_box
        self.volume_depth = volume_depth
        self.volume_formfactor = volume_formfactor
        self.volume_height = volume_height
        self.volume_origin = volume_origin
        self.volume_width = volume_width
        self.created_dt = created_dt
        self.updated_dt = updated_dt
        self.user = user

    @property
    def id(self):
        """Gets the id of this OctoPrinterProfile.  # noqa: E501


        :return: The id of this OctoPrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OctoPrinterProfile.


        :param id: The id of this OctoPrinterProfile.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def axes_e_inverted(self):
        """Gets the axes_e_inverted of this OctoPrinterProfile.  # noqa: E501


        :return: The axes_e_inverted of this OctoPrinterProfile.  # noqa: E501
        :rtype: bool
        """
        return self._axes_e_inverted

    @axes_e_inverted.setter
    def axes_e_inverted(self, axes_e_inverted):
        """Sets the axes_e_inverted of this OctoPrinterProfile.


        :param axes_e_inverted: The axes_e_inverted of this OctoPrinterProfile.  # noqa: E501
        :type axes_e_inverted: bool
        """

        self._axes_e_inverted = axes_e_inverted

    @property
    def axes_e_speed(self):
        """Gets the axes_e_speed of this OctoPrinterProfile.  # noqa: E501


        :return: The axes_e_speed of this OctoPrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._axes_e_speed

    @axes_e_speed.setter
    def axes_e_speed(self, axes_e_speed):
        """Sets the axes_e_speed of this OctoPrinterProfile.


        :param axes_e_speed: The axes_e_speed of this OctoPrinterProfile.  # noqa: E501
        :type axes_e_speed: int
        """
        if (self.local_vars_configuration.client_side_validation and
                axes_e_speed is not None and axes_e_speed > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `axes_e_speed`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                axes_e_speed is not None and axes_e_speed < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `axes_e_speed`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._axes_e_speed = axes_e_speed

    @property
    def axes_x_speed(self):
        """Gets the axes_x_speed of this OctoPrinterProfile.  # noqa: E501


        :return: The axes_x_speed of this OctoPrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._axes_x_speed

    @axes_x_speed.setter
    def axes_x_speed(self, axes_x_speed):
        """Sets the axes_x_speed of this OctoPrinterProfile.


        :param axes_x_speed: The axes_x_speed of this OctoPrinterProfile.  # noqa: E501
        :type axes_x_speed: int
        """
        if (self.local_vars_configuration.client_side_validation and
                axes_x_speed is not None and axes_x_speed > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `axes_x_speed`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                axes_x_speed is not None and axes_x_speed < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `axes_x_speed`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._axes_x_speed = axes_x_speed

    @property
    def axes_x_inverted(self):
        """Gets the axes_x_inverted of this OctoPrinterProfile.  # noqa: E501


        :return: The axes_x_inverted of this OctoPrinterProfile.  # noqa: E501
        :rtype: bool
        """
        return self._axes_x_inverted

    @axes_x_inverted.setter
    def axes_x_inverted(self, axes_x_inverted):
        """Sets the axes_x_inverted of this OctoPrinterProfile.


        :param axes_x_inverted: The axes_x_inverted of this OctoPrinterProfile.  # noqa: E501
        :type axes_x_inverted: bool
        """

        self._axes_x_inverted = axes_x_inverted

    @property
    def axes_y_inverted(self):
        """Gets the axes_y_inverted of this OctoPrinterProfile.  # noqa: E501


        :return: The axes_y_inverted of this OctoPrinterProfile.  # noqa: E501
        :rtype: bool
        """
        return self._axes_y_inverted

    @axes_y_inverted.setter
    def axes_y_inverted(self, axes_y_inverted):
        """Sets the axes_y_inverted of this OctoPrinterProfile.


        :param axes_y_inverted: The axes_y_inverted of this OctoPrinterProfile.  # noqa: E501
        :type axes_y_inverted: bool
        """

        self._axes_y_inverted = axes_y_inverted

    @property
    def axes_y_speed(self):
        """Gets the axes_y_speed of this OctoPrinterProfile.  # noqa: E501


        :return: The axes_y_speed of this OctoPrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._axes_y_speed

    @axes_y_speed.setter
    def axes_y_speed(self, axes_y_speed):
        """Sets the axes_y_speed of this OctoPrinterProfile.


        :param axes_y_speed: The axes_y_speed of this OctoPrinterProfile.  # noqa: E501
        :type axes_y_speed: int
        """
        if (self.local_vars_configuration.client_side_validation and
                axes_y_speed is not None and axes_y_speed > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `axes_y_speed`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                axes_y_speed is not None and axes_y_speed < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `axes_y_speed`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._axes_y_speed = axes_y_speed

    @property
    def axes_z_inverted(self):
        """Gets the axes_z_inverted of this OctoPrinterProfile.  # noqa: E501


        :return: The axes_z_inverted of this OctoPrinterProfile.  # noqa: E501
        :rtype: bool
        """
        return self._axes_z_inverted

    @axes_z_inverted.setter
    def axes_z_inverted(self, axes_z_inverted):
        """Sets the axes_z_inverted of this OctoPrinterProfile.


        :param axes_z_inverted: The axes_z_inverted of this OctoPrinterProfile.  # noqa: E501
        :type axes_z_inverted: bool
        """

        self._axes_z_inverted = axes_z_inverted

    @property
    def axes_z_speed(self):
        """Gets the axes_z_speed of this OctoPrinterProfile.  # noqa: E501


        :return: The axes_z_speed of this OctoPrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._axes_z_speed

    @axes_z_speed.setter
    def axes_z_speed(self, axes_z_speed):
        """Sets the axes_z_speed of this OctoPrinterProfile.


        :param axes_z_speed: The axes_z_speed of this OctoPrinterProfile.  # noqa: E501
        :type axes_z_speed: int
        """
        if (self.local_vars_configuration.client_side_validation and
                axes_z_speed is not None and axes_z_speed > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `axes_z_speed`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                axes_z_speed is not None and axes_z_speed < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `axes_z_speed`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._axes_z_speed = axes_z_speed

    @property
    def extruder_count(self):
        """Gets the extruder_count of this OctoPrinterProfile.  # noqa: E501


        :return: The extruder_count of this OctoPrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._extruder_count

    @extruder_count.setter
    def extruder_count(self, extruder_count):
        """Sets the extruder_count of this OctoPrinterProfile.


        :param extruder_count: The extruder_count of this OctoPrinterProfile.  # noqa: E501
        :type extruder_count: int
        """
        if (self.local_vars_configuration.client_side_validation and
                extruder_count is not None and extruder_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `extruder_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                extruder_count is not None and extruder_count < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `extruder_count`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._extruder_count = extruder_count

    @property
    def extruder_nozzle_diameter(self):
        """Gets the extruder_nozzle_diameter of this OctoPrinterProfile.  # noqa: E501


        :return: The extruder_nozzle_diameter of this OctoPrinterProfile.  # noqa: E501
        :rtype: float
        """
        return self._extruder_nozzle_diameter

    @extruder_nozzle_diameter.setter
    def extruder_nozzle_diameter(self, extruder_nozzle_diameter):
        """Sets the extruder_nozzle_diameter of this OctoPrinterProfile.


        :param extruder_nozzle_diameter: The extruder_nozzle_diameter of this OctoPrinterProfile.  # noqa: E501
        :type extruder_nozzle_diameter: float
        """

        self._extruder_nozzle_diameter = extruder_nozzle_diameter

    @property
    def extruder_shared_nozzle(self):
        """Gets the extruder_shared_nozzle of this OctoPrinterProfile.  # noqa: E501


        :return: The extruder_shared_nozzle of this OctoPrinterProfile.  # noqa: E501
        :rtype: bool
        """
        return self._extruder_shared_nozzle

    @extruder_shared_nozzle.setter
    def extruder_shared_nozzle(self, extruder_shared_nozzle):
        """Sets the extruder_shared_nozzle of this OctoPrinterProfile.


        :param extruder_shared_nozzle: The extruder_shared_nozzle of this OctoPrinterProfile.  # noqa: E501
        :type extruder_shared_nozzle: bool
        """

        self._extruder_shared_nozzle = extruder_shared_nozzle

    @property
    def heated_bed(self):
        """Gets the heated_bed of this OctoPrinterProfile.  # noqa: E501


        :return: The heated_bed of this OctoPrinterProfile.  # noqa: E501
        :rtype: bool
        """
        return self._heated_bed

    @heated_bed.setter
    def heated_bed(self, heated_bed):
        """Sets the heated_bed of this OctoPrinterProfile.


        :param heated_bed: The heated_bed of this OctoPrinterProfile.  # noqa: E501
        :type heated_bed: bool
        """

        self._heated_bed = heated_bed

    @property
    def heated_chamber(self):
        """Gets the heated_chamber of this OctoPrinterProfile.  # noqa: E501


        :return: The heated_chamber of this OctoPrinterProfile.  # noqa: E501
        :rtype: bool
        """
        return self._heated_chamber

    @heated_chamber.setter
    def heated_chamber(self, heated_chamber):
        """Sets the heated_chamber of this OctoPrinterProfile.


        :param heated_chamber: The heated_chamber of this OctoPrinterProfile.  # noqa: E501
        :type heated_chamber: bool
        """

        self._heated_chamber = heated_chamber

    @property
    def model(self):
        """Gets the model of this OctoPrinterProfile.  # noqa: E501


        :return: The model of this OctoPrinterProfile.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this OctoPrinterProfile.


        :param model: The model of this OctoPrinterProfile.  # noqa: E501
        :type model: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def name(self):
        """Gets the name of this OctoPrinterProfile.  # noqa: E501


        :return: The name of this OctoPrinterProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OctoPrinterProfile.


        :param name: The name of this OctoPrinterProfile.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def octoprint_key(self):
        """Gets the octoprint_key of this OctoPrinterProfile.  # noqa: E501


        :return: The octoprint_key of this OctoPrinterProfile.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_key

    @octoprint_key.setter
    def octoprint_key(self, octoprint_key):
        """Sets the octoprint_key of this OctoPrinterProfile.


        :param octoprint_key: The octoprint_key of this OctoPrinterProfile.  # noqa: E501
        :type octoprint_key: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_key is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_key is not None and len(octoprint_key) > 255):
            raise ValueError("Invalid value for `octoprint_key`, length must be less than or equal to `255`")  # noqa: E501

        self._octoprint_key = octoprint_key

    @property
    def volume_custom_box(self):
        """Gets the volume_custom_box of this OctoPrinterProfile.  # noqa: E501


        :return: The volume_custom_box of this OctoPrinterProfile.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._volume_custom_box

    @volume_custom_box.setter
    def volume_custom_box(self, volume_custom_box):
        """Sets the volume_custom_box of this OctoPrinterProfile.


        :param volume_custom_box: The volume_custom_box of this OctoPrinterProfile.  # noqa: E501
        :type volume_custom_box: dict(str, object)
        """

        self._volume_custom_box = volume_custom_box

    @property
    def volume_depth(self):
        """Gets the volume_depth of this OctoPrinterProfile.  # noqa: E501


        :return: The volume_depth of this OctoPrinterProfile.  # noqa: E501
        :rtype: float
        """
        return self._volume_depth

    @volume_depth.setter
    def volume_depth(self, volume_depth):
        """Sets the volume_depth of this OctoPrinterProfile.


        :param volume_depth: The volume_depth of this OctoPrinterProfile.  # noqa: E501
        :type volume_depth: float
        """

        self._volume_depth = volume_depth

    @property
    def volume_formfactor(self):
        """Gets the volume_formfactor of this OctoPrinterProfile.  # noqa: E501


        :return: The volume_formfactor of this OctoPrinterProfile.  # noqa: E501
        :rtype: str
        """
        return self._volume_formfactor

    @volume_formfactor.setter
    def volume_formfactor(self, volume_formfactor):
        """Sets the volume_formfactor of this OctoPrinterProfile.


        :param volume_formfactor: The volume_formfactor of this OctoPrinterProfile.  # noqa: E501
        :type volume_formfactor: str
        """
        if (self.local_vars_configuration.client_side_validation and
                volume_formfactor is not None and len(volume_formfactor) > 255):
            raise ValueError("Invalid value for `volume_formfactor`, length must be less than or equal to `255`")  # noqa: E501

        self._volume_formfactor = volume_formfactor

    @property
    def volume_height(self):
        """Gets the volume_height of this OctoPrinterProfile.  # noqa: E501


        :return: The volume_height of this OctoPrinterProfile.  # noqa: E501
        :rtype: float
        """
        return self._volume_height

    @volume_height.setter
    def volume_height(self, volume_height):
        """Sets the volume_height of this OctoPrinterProfile.


        :param volume_height: The volume_height of this OctoPrinterProfile.  # noqa: E501
        :type volume_height: float
        """

        self._volume_height = volume_height

    @property
    def volume_origin(self):
        """Gets the volume_origin of this OctoPrinterProfile.  # noqa: E501


        :return: The volume_origin of this OctoPrinterProfile.  # noqa: E501
        :rtype: str
        """
        return self._volume_origin

    @volume_origin.setter
    def volume_origin(self, volume_origin):
        """Sets the volume_origin of this OctoPrinterProfile.


        :param volume_origin: The volume_origin of this OctoPrinterProfile.  # noqa: E501
        :type volume_origin: str
        """
        if (self.local_vars_configuration.client_side_validation and
                volume_origin is not None and len(volume_origin) > 255):
            raise ValueError("Invalid value for `volume_origin`, length must be less than or equal to `255`")  # noqa: E501

        self._volume_origin = volume_origin

    @property
    def volume_width(self):
        """Gets the volume_width of this OctoPrinterProfile.  # noqa: E501


        :return: The volume_width of this OctoPrinterProfile.  # noqa: E501
        :rtype: float
        """
        return self._volume_width

    @volume_width.setter
    def volume_width(self, volume_width):
        """Sets the volume_width of this OctoPrinterProfile.


        :param volume_width: The volume_width of this OctoPrinterProfile.  # noqa: E501
        :type volume_width: float
        """

        self._volume_width = volume_width

    @property
    def created_dt(self):
        """Gets the created_dt of this OctoPrinterProfile.  # noqa: E501


        :return: The created_dt of this OctoPrinterProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OctoPrinterProfile.


        :param created_dt: The created_dt of this OctoPrinterProfile.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OctoPrinterProfile.  # noqa: E501


        :return: The updated_dt of this OctoPrinterProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OctoPrinterProfile.


        :param updated_dt: The updated_dt of this OctoPrinterProfile.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def user(self):
        """Gets the user of this OctoPrinterProfile.  # noqa: E501


        :return: The user of this OctoPrinterProfile.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OctoPrinterProfile.


        :param user: The user of this OctoPrinterProfile.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, OctoPrinterProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoPrinterProfile):
            return True

        return self.to_dict() != other.to_dict()
