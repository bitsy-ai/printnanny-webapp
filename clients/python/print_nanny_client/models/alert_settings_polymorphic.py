# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class AlertSettingsPolymorphic(object):
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
        'alert_type': 'AlertTypeEnum',
        'alert_methods': 'list[AlertMethodsEnum]',
        'enabled': 'bool',
        'polymorphic_ctype': 'int',
        'monitoring_stop': 'list[MoveNozzleEnum]',
        'monitoring_start': 'list[MoveNozzleEnum]',
        'print_start': 'list[MoveNozzleEnum]',
        'print_stop': 'list[MoveNozzleEnum]',
        'print_pause': 'list[MoveNozzleEnum]',
        'print_resume': 'list[MoveNozzleEnum]',
        'move_nozzle': 'list[MoveNozzleEnum]',
        'user': 'int',
        'on_progress_percent': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'alert_type': 'alert_type',
        'alert_methods': 'alert_methods',
        'enabled': 'enabled',
        'polymorphic_ctype': 'polymorphic_ctype',
        'monitoring_stop': 'monitoring_stop',
        'monitoring_start': 'monitoring_start',
        'print_start': 'print_start',
        'print_stop': 'print_stop',
        'print_pause': 'print_pause',
        'print_resume': 'print_resume',
        'move_nozzle': 'move_nozzle',
        'user': 'user',
        'on_progress_percent': 'on_progress_percent'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, id=None, created_dt=None, updated_dt=None, alert_type=None, alert_methods=None, enabled=None, polymorphic_ctype=None, monitoring_stop=None, monitoring_start=None, print_start=None, print_stop=None, print_pause=None, print_resume=None, move_nozzle=None, user=None, on_progress_percent=None, local_vars_configuration=None):  # noqa: E501
        """AlertSettingsPolymorphic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._updated_dt = None
        self._alert_type = None
        self._alert_methods = None
        self._enabled = None
        self._polymorphic_ctype = None
        self._monitoring_stop = None
        self._monitoring_start = None
        self._print_start = None
        self._print_stop = None
        self._print_pause = None
        self._print_resume = None
        self._move_nozzle = None
        self._user = None
        self._on_progress_percent = None
        self.discriminator = 'type'

        if id is not None:
            self.id = id
        if created_dt is not None:
            self.created_dt = created_dt
        if updated_dt is not None:
            self.updated_dt = updated_dt
        self.alert_type = alert_type
        if alert_methods is not None:
            self.alert_methods = alert_methods
        if enabled is not None:
            self.enabled = enabled
        if polymorphic_ctype is not None:
            self.polymorphic_ctype = polymorphic_ctype
        if monitoring_stop is not None:
            self.monitoring_stop = monitoring_stop
        if monitoring_start is not None:
            self.monitoring_start = monitoring_start
        if print_start is not None:
            self.print_start = print_start
        if print_stop is not None:
            self.print_stop = print_stop
        if print_pause is not None:
            self.print_pause = print_pause
        if print_resume is not None:
            self.print_resume = print_resume
        if move_nozzle is not None:
            self.move_nozzle = move_nozzle
        if user is not None:
            self.user = user
        if on_progress_percent is not None:
            self.on_progress_percent = on_progress_percent

    @property
    def id(self):
        """Gets the id of this AlertSettingsPolymorphic.  # noqa: E501


        :return: The id of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertSettingsPolymorphic.


        :param id: The id of this AlertSettingsPolymorphic.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this AlertSettingsPolymorphic.  # noqa: E501


        :return: The created_dt of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this AlertSettingsPolymorphic.


        :param created_dt: The created_dt of this AlertSettingsPolymorphic.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this AlertSettingsPolymorphic.  # noqa: E501


        :return: The updated_dt of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this AlertSettingsPolymorphic.


        :param updated_dt: The updated_dt of this AlertSettingsPolymorphic.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def alert_type(self):
        """Gets the alert_type of this AlertSettingsPolymorphic.  # noqa: E501


        :return: The alert_type of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: AlertTypeEnum
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this AlertSettingsPolymorphic.


        :param alert_type: The alert_type of this AlertSettingsPolymorphic.  # noqa: E501
        :type alert_type: AlertTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and alert_type is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_type`, must not be `None`")  # noqa: E501

        self._alert_type = alert_type

    @property
    def alert_methods(self):
        """Gets the alert_methods of this AlertSettingsPolymorphic.  # noqa: E501


        :return: The alert_methods of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: list[AlertMethodsEnum]
        """
        return self._alert_methods

    @alert_methods.setter
    def alert_methods(self, alert_methods):
        """Sets the alert_methods of this AlertSettingsPolymorphic.


        :param alert_methods: The alert_methods of this AlertSettingsPolymorphic.  # noqa: E501
        :type alert_methods: list[AlertMethodsEnum]
        """

        self._alert_methods = alert_methods

    @property
    def enabled(self):
        """Gets the enabled of this AlertSettingsPolymorphic.  # noqa: E501

        Enable or disable this alert channel  # noqa: E501

        :return: The enabled of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AlertSettingsPolymorphic.

        Enable or disable this alert channel  # noqa: E501

        :param enabled: The enabled of this AlertSettingsPolymorphic.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this AlertSettingsPolymorphic.  # noqa: E501


        :return: The polymorphic_ctype of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this AlertSettingsPolymorphic.


        :param polymorphic_ctype: The polymorphic_ctype of this AlertSettingsPolymorphic.  # noqa: E501
        :type polymorphic_ctype: int
        """

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def monitoring_stop(self):
        """Gets the monitoring_stop of this AlertSettingsPolymorphic.  # noqa: E501

        Fires on <strong>MonitoringStop<strong> updates.   Helps debug unexpected Print Nanny crashes.  # noqa: E501

        :return: The monitoring_stop of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._monitoring_stop

    @monitoring_stop.setter
    def monitoring_stop(self, monitoring_stop):
        """Sets the monitoring_stop of this AlertSettingsPolymorphic.

        Fires on <strong>MonitoringStop<strong> updates.   Helps debug unexpected Print Nanny crashes.  # noqa: E501

        :param monitoring_stop: The monitoring_stop of this AlertSettingsPolymorphic.  # noqa: E501
        :type monitoring_stop: list[MoveNozzleEnum]
        """

        self._monitoring_stop = monitoring_stop

    @property
    def monitoring_start(self):
        """Gets the monitoring_start of this AlertSettingsPolymorphic.  # noqa: E501

        Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem.  # noqa: E501

        :return: The monitoring_start of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._monitoring_start

    @monitoring_start.setter
    def monitoring_start(self, monitoring_start):
        """Sets the monitoring_start of this AlertSettingsPolymorphic.

        Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem.  # noqa: E501

        :param monitoring_start: The monitoring_start of this AlertSettingsPolymorphic.  # noqa: E501
        :type monitoring_start: list[MoveNozzleEnum]
        """

        self._monitoring_start = monitoring_start

    @property
    def print_start(self):
        """Gets the print_start of this AlertSettingsPolymorphic.  # noqa: E501

        Fires on <strong>StopPrint</strong> updates. Get notified as soon as a print job finishes.   # noqa: E501

        :return: The print_start of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._print_start

    @print_start.setter
    def print_start(self, print_start):
        """Sets the print_start of this AlertSettingsPolymorphic.

        Fires on <strong>StopPrint</strong> updates. Get notified as soon as a print job finishes.   # noqa: E501

        :param print_start: The print_start of this AlertSettingsPolymorphic.  # noqa: E501
        :type print_start: list[MoveNozzleEnum]
        """

        self._print_start = print_start

    @property
    def print_stop(self):
        """Gets the print_stop of this AlertSettingsPolymorphic.  # noqa: E501

        Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem.  # noqa: E501

        :return: The print_stop of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._print_stop

    @print_stop.setter
    def print_stop(self, print_stop):
        """Sets the print_stop of this AlertSettingsPolymorphic.

        Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem.  # noqa: E501

        :param print_stop: The print_stop of this AlertSettingsPolymorphic.  # noqa: E501
        :type print_stop: list[MoveNozzleEnum]
        """

        self._print_stop = print_stop

    @property
    def print_pause(self):
        """Gets the print_pause of this AlertSettingsPolymorphic.  # noqa: E501

        Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.  # noqa: E501

        :return: The print_pause of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._print_pause

    @print_pause.setter
    def print_pause(self, print_pause):
        """Sets the print_pause of this AlertSettingsPolymorphic.

        Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.  # noqa: E501

        :param print_pause: The print_pause of this AlertSettingsPolymorphic.  # noqa: E501
        :type print_pause: list[MoveNozzleEnum]
        """

        self._print_pause = print_pause

    @property
    def print_resume(self):
        """Gets the print_resume of this AlertSettingsPolymorphic.  # noqa: E501

        Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.  # noqa: E501

        :return: The print_resume of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._print_resume

    @print_resume.setter
    def print_resume(self, print_resume):
        """Sets the print_resume of this AlertSettingsPolymorphic.

        Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.  # noqa: E501

        :param print_resume: The print_resume of this AlertSettingsPolymorphic.  # noqa: E501
        :type print_resume: list[MoveNozzleEnum]
        """

        self._print_resume = print_resume

    @property
    def move_nozzle(self):
        """Gets the move_nozzle of this AlertSettingsPolymorphic.  # noqa: E501

        Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint  # noqa: E501

        :return: The move_nozzle of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._move_nozzle

    @move_nozzle.setter
    def move_nozzle(self, move_nozzle):
        """Sets the move_nozzle of this AlertSettingsPolymorphic.

        Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint  # noqa: E501

        :param move_nozzle: The move_nozzle of this AlertSettingsPolymorphic.  # noqa: E501
        :type move_nozzle: list[MoveNozzleEnum]
        """

        self._move_nozzle = move_nozzle

    @property
    def user(self):
        """Gets the user of this AlertSettingsPolymorphic.  # noqa: E501


        :return: The user of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AlertSettingsPolymorphic.


        :param user: The user of this AlertSettingsPolymorphic.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def on_progress_percent(self):
        """Gets the on_progress_percent of this AlertSettingsPolymorphic.  # noqa: E501

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :return: The on_progress_percent of this AlertSettingsPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._on_progress_percent

    @on_progress_percent.setter
    def on_progress_percent(self, on_progress_percent):
        """Sets the on_progress_percent of this AlertSettingsPolymorphic.

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :param on_progress_percent: The on_progress_percent of this AlertSettingsPolymorphic.  # noqa: E501
        :type on_progress_percent: int
        """
        if (self.local_vars_configuration.client_side_validation and
                on_progress_percent is not None and on_progress_percent > 100):  # noqa: E501
            raise ValueError("Invalid value for `on_progress_percent`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                on_progress_percent is not None and on_progress_percent < 1):  # noqa: E501
            raise ValueError("Invalid value for `on_progress_percent`, must be a value greater than or equal to `1`")  # noqa: E501

        self._on_progress_percent = on_progress_percent

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
        if not isinstance(other, AlertSettingsPolymorphic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertSettingsPolymorphic):
            return True

        return self.to_dict() != other.to_dict()
