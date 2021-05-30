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


class TelemetryEventPolymorphic(object):
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
        'print_session': 'str',
        'environment': 'OctoprintEnvironment',
        'printer_data': 'OctoprintPrinterData',
        'temperature': 'dict(str, object)',
        'event_type': 'PrintNannyPluginEventEventTypeEnum',
        'ts': 'datetime',
        'event_source': 'EventSourceEnum',
        'event_data': 'dict(str, object)',
        'print_nanny_plugin_version': 'str',
        'print_nanny_client_version': 'str',
        'octoprint_version': 'str',
        'octoprint_job': 'dict(str, object)',
        'polymorphic_ctype': 'int',
        'octoprint_device': 'int',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'print_session': 'print_session',
        'environment': 'environment',
        'printer_data': 'printer_data',
        'temperature': 'temperature',
        'event_type': 'event_type',
        'ts': 'ts',
        'event_source': 'event_source',
        'event_data': 'event_data',
        'print_nanny_plugin_version': 'print_nanny_plugin_version',
        'print_nanny_client_version': 'print_nanny_client_version',
        'octoprint_version': 'octoprint_version',
        'octoprint_job': 'octoprint_job',
        'polymorphic_ctype': 'polymorphic_ctype',
        'octoprint_device': 'octoprint_device',
        'user': 'user'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, id=None, print_session=None, environment=None, printer_data=None, temperature=None, event_type=None, ts=None, event_source=None, event_data=None, print_nanny_plugin_version=None, print_nanny_client_version=None, octoprint_version=None, octoprint_job=None, polymorphic_ctype=None, octoprint_device=None, user=None, local_vars_configuration=None):  # noqa: E501
        """TelemetryEventPolymorphic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._print_session = None
        self._environment = None
        self._printer_data = None
        self._temperature = None
        self._event_type = None
        self._ts = None
        self._event_source = None
        self._event_data = None
        self._print_nanny_plugin_version = None
        self._print_nanny_client_version = None
        self._octoprint_version = None
        self._octoprint_job = None
        self._polymorphic_ctype = None
        self._octoprint_device = None
        self._user = None
        self.discriminator = 'polymorphic_ctype'

        if id is not None:
            self.id = id
        if print_session is not None:
            self.print_session = print_session
        self.environment = environment
        self.printer_data = printer_data
        self.temperature = temperature
        self.event_type = event_type
        if ts is not None:
            self.ts = ts
        if event_source is not None:
            self.event_source = event_source
        self.event_data = event_data
        self.print_nanny_plugin_version = print_nanny_plugin_version
        self.print_nanny_client_version = print_nanny_client_version
        self.octoprint_version = octoprint_version
        self.octoprint_job = octoprint_job
        if polymorphic_ctype is not None:
            self.polymorphic_ctype = polymorphic_ctype
        self.octoprint_device = octoprint_device
        if user is not None:
            self.user = user

    @property
    def id(self):
        """Gets the id of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The id of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TelemetryEventPolymorphic.


        :param id: The id of this TelemetryEventPolymorphic.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def print_session(self):
        """Gets the print_session of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The print_session of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._print_session

    @print_session.setter
    def print_session(self, print_session):
        """Sets the print_session of this TelemetryEventPolymorphic.


        :param print_session: The print_session of this TelemetryEventPolymorphic.  # noqa: E501
        :type print_session: str
        """

        self._print_session = print_session

    @property
    def environment(self):
        """Gets the environment of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The environment of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: OctoprintEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this TelemetryEventPolymorphic.


        :param environment: The environment of this TelemetryEventPolymorphic.  # noqa: E501
        :type environment: OctoprintEnvironment
        """
        if self.local_vars_configuration.client_side_validation and environment is None:  # noqa: E501
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def printer_data(self):
        """Gets the printer_data of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The printer_data of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: OctoprintPrinterData
        """
        return self._printer_data

    @printer_data.setter
    def printer_data(self, printer_data):
        """Sets the printer_data of this TelemetryEventPolymorphic.


        :param printer_data: The printer_data of this TelemetryEventPolymorphic.  # noqa: E501
        :type printer_data: OctoprintPrinterData
        """
        if self.local_vars_configuration.client_side_validation and printer_data is None:  # noqa: E501
            raise ValueError("Invalid value for `printer_data`, must not be `None`")  # noqa: E501

        self._printer_data = printer_data

    @property
    def temperature(self):
        """Gets the temperature of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The temperature of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this TelemetryEventPolymorphic.


        :param temperature: The temperature of this TelemetryEventPolymorphic.  # noqa: E501
        :type temperature: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and temperature is None:  # noqa: E501
            raise ValueError("Invalid value for `temperature`, must not be `None`")  # noqa: E501

        self._temperature = temperature

    @property
    def event_type(self):
        """Gets the event_type of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The event_type of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: PrintNannyPluginEventEventTypeEnum
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this TelemetryEventPolymorphic.


        :param event_type: The event_type of this TelemetryEventPolymorphic.  # noqa: E501
        :type event_type: PrintNannyPluginEventEventTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def ts(self):
        """Gets the ts of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The ts of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: datetime
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this TelemetryEventPolymorphic.


        :param ts: The ts of this TelemetryEventPolymorphic.  # noqa: E501
        :type ts: datetime
        """

        self._ts = ts

    @property
    def event_source(self):
        """Gets the event_source of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The event_source of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: EventSourceEnum
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this TelemetryEventPolymorphic.


        :param event_source: The event_source of this TelemetryEventPolymorphic.  # noqa: E501
        :type event_source: EventSourceEnum
        """

        self._event_source = event_source

    @property
    def event_data(self):
        """Gets the event_data of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The event_data of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        """Sets the event_data of this TelemetryEventPolymorphic.


        :param event_data: The event_data of this TelemetryEventPolymorphic.  # noqa: E501
        :type event_data: dict(str, object)
        """

        self._event_data = event_data

    @property
    def print_nanny_plugin_version(self):
        """Gets the print_nanny_plugin_version of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The print_nanny_plugin_version of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_plugin_version

    @print_nanny_plugin_version.setter
    def print_nanny_plugin_version(self, print_nanny_plugin_version):
        """Sets the print_nanny_plugin_version of this TelemetryEventPolymorphic.


        :param print_nanny_plugin_version: The print_nanny_plugin_version of this TelemetryEventPolymorphic.  # noqa: E501
        :type print_nanny_plugin_version: str
        """
        if self.local_vars_configuration.client_side_validation and print_nanny_plugin_version is None:  # noqa: E501
            raise ValueError("Invalid value for `print_nanny_plugin_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_plugin_version is not None and len(print_nanny_plugin_version) > 60):
            raise ValueError("Invalid value for `print_nanny_plugin_version`, length must be less than or equal to `60`")  # noqa: E501

        self._print_nanny_plugin_version = print_nanny_plugin_version

    @property
    def print_nanny_client_version(self):
        """Gets the print_nanny_client_version of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The print_nanny_client_version of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_client_version

    @print_nanny_client_version.setter
    def print_nanny_client_version(self, print_nanny_client_version):
        """Sets the print_nanny_client_version of this TelemetryEventPolymorphic.


        :param print_nanny_client_version: The print_nanny_client_version of this TelemetryEventPolymorphic.  # noqa: E501
        :type print_nanny_client_version: str
        """
        if self.local_vars_configuration.client_side_validation and print_nanny_client_version is None:  # noqa: E501
            raise ValueError("Invalid value for `print_nanny_client_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_client_version is not None and len(print_nanny_client_version) > 60):
            raise ValueError("Invalid value for `print_nanny_client_version`, length must be less than or equal to `60`")  # noqa: E501

        self._print_nanny_client_version = print_nanny_client_version

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The octoprint_version of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this TelemetryEventPolymorphic.


        :param octoprint_version: The octoprint_version of this TelemetryEventPolymorphic.  # noqa: E501
        :type octoprint_version: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_version is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 36):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `36`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def octoprint_job(self):
        """Gets the octoprint_job of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The octoprint_job of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._octoprint_job

    @octoprint_job.setter
    def octoprint_job(self, octoprint_job):
        """Sets the octoprint_job of this TelemetryEventPolymorphic.


        :param octoprint_job: The octoprint_job of this TelemetryEventPolymorphic.  # noqa: E501
        :type octoprint_job: dict(str, object)
        """

        self._octoprint_job = octoprint_job

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The polymorphic_ctype of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this TelemetryEventPolymorphic.


        :param polymorphic_ctype: The polymorphic_ctype of this TelemetryEventPolymorphic.  # noqa: E501
        :type polymorphic_ctype: int
        """

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The octoprint_device of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this TelemetryEventPolymorphic.


        :param octoprint_device: The octoprint_device of this TelemetryEventPolymorphic.  # noqa: E501
        :type octoprint_device: int
        """
        if self.local_vars_configuration.client_side_validation and octoprint_device is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_device`, must not be `None`")  # noqa: E501

        self._octoprint_device = octoprint_device

    @property
    def user(self):
        """Gets the user of this TelemetryEventPolymorphic.  # noqa: E501


        :return: The user of this TelemetryEventPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TelemetryEventPolymorphic.


        :param user: The user of this TelemetryEventPolymorphic.  # noqa: E501
        :type user: int
        """

        self._user = user

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, TelemetryEventPolymorphic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TelemetryEventPolymorphic):
            return True

        return self.to_dict() != other.to_dict()
