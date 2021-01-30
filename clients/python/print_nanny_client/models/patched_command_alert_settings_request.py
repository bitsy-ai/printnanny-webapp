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


class PatchedCommandAlertSettingsRequest(object):
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
        'alert_type': 'AlertTypeEnum',
        'alert_methods': 'list[str]',
        'enabled': 'bool',
        'snapshot': 'list[str]',
        'stop_monitoring': 'list[str]',
        'start_monitoring': 'list[str]',
        'stop_print': 'list[str]',
        'start_print': 'list[str]',
        'move_nozzle': 'list[str]',
        'pause_print': 'list[str]',
        'resume_print': 'list[str]'
    }

    attribute_map = {
        'alert_type': 'alert_type',
        'alert_methods': 'alert_methods',
        'enabled': 'enabled',
        'snapshot': 'snapshot',
        'stop_monitoring': 'stop_monitoring',
        'start_monitoring': 'start_monitoring',
        'stop_print': 'stop_print',
        'start_print': 'start_print',
        'move_nozzle': 'move_nozzle',
        'pause_print': 'pause_print',
        'resume_print': 'resume_print'
    }

    def __init__(self, alert_type=None, alert_methods=None, enabled=None, snapshot=None, stop_monitoring=None, start_monitoring=None, stop_print=None, start_print=None, move_nozzle=None, pause_print=None, resume_print=None, local_vars_configuration=None):  # noqa: E501
        """PatchedCommandAlertSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alert_type = None
        self._alert_methods = None
        self._enabled = None
        self._snapshot = None
        self._stop_monitoring = None
        self._start_monitoring = None
        self._stop_print = None
        self._start_print = None
        self._move_nozzle = None
        self._pause_print = None
        self._resume_print = None
        self.discriminator = None

        if alert_type is not None:
            self.alert_type = alert_type
        if alert_methods is not None:
            self.alert_methods = alert_methods
        if enabled is not None:
            self.enabled = enabled
        if snapshot is not None:
            self.snapshot = snapshot
        if stop_monitoring is not None:
            self.stop_monitoring = stop_monitoring
        if start_monitoring is not None:
            self.start_monitoring = start_monitoring
        if stop_print is not None:
            self.stop_print = stop_print
        if start_print is not None:
            self.start_print = start_print
        if move_nozzle is not None:
            self.move_nozzle = move_nozzle
        if pause_print is not None:
            self.pause_print = pause_print
        if resume_print is not None:
            self.resume_print = resume_print

    @property
    def alert_type(self):
        """Gets the alert_type of this PatchedCommandAlertSettingsRequest.  # noqa: E501


        :return: The alert_type of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: AlertTypeEnum
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this PatchedCommandAlertSettingsRequest.


        :param alert_type: The alert_type of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type alert_type: AlertTypeEnum
        """

        self._alert_type = alert_type

    @property
    def alert_methods(self):
        """Gets the alert_methods of this PatchedCommandAlertSettingsRequest.  # noqa: E501


        :return: The alert_methods of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_methods

    @alert_methods.setter
    def alert_methods(self, alert_methods):
        """Sets the alert_methods of this PatchedCommandAlertSettingsRequest.


        :param alert_methods: The alert_methods of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type alert_methods: list[str]
        """
        allowed_values = ["UI", "EMAIL"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(alert_methods).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `alert_methods` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(alert_methods) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._alert_methods = alert_methods

    @property
    def enabled(self):
        """Gets the enabled of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Enable or disable this alert channel  # noqa: E501

        :return: The enabled of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PatchedCommandAlertSettingsRequest.

        Enable or disable this alert channel  # noqa: E501

        :param enabled: The enabled of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def snapshot(self):
        """Gets the snapshot of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Fires on web camera <strong>Snapshot</strong> command  # noqa: E501

        :return: The snapshot of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this PatchedCommandAlertSettingsRequest.

        Fires on web camera <strong>Snapshot</strong> command  # noqa: E501

        :param snapshot: The snapshot of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type snapshot: list[str]
        """
        allowed_values = ["RECEIVED", "FAILED", "SUCCESS"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(snapshot).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `snapshot` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(snapshot) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._snapshot = snapshot

    @property
    def stop_monitoring(self):
        """Gets the stop_monitoring of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>MonitoringStop<strong> updates.   Helps debug unexpected Print Nanny crashes.  # noqa: E501

        :return: The stop_monitoring of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._stop_monitoring

    @stop_monitoring.setter
    def stop_monitoring(self, stop_monitoring):
        """Sets the stop_monitoring of this PatchedCommandAlertSettingsRequest.

        Fires on <strong>MonitoringStop<strong> updates.   Helps debug unexpected Print Nanny crashes.  # noqa: E501

        :param stop_monitoring: The stop_monitoring of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type stop_monitoring: list[str]
        """
        allowed_values = ["RECEIVED", "FAILED", "SUCCESS"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(stop_monitoring).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `stop_monitoring` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(stop_monitoring) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._stop_monitoring = stop_monitoring

    @property
    def start_monitoring(self):
        """Gets the start_monitoring of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem.  # noqa: E501

        :return: The start_monitoring of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._start_monitoring

    @start_monitoring.setter
    def start_monitoring(self, start_monitoring):
        """Sets the start_monitoring of this PatchedCommandAlertSettingsRequest.

        Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem.  # noqa: E501

        :param start_monitoring: The start_monitoring of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type start_monitoring: list[str]
        """
        allowed_values = ["RECEIVED", "FAILED", "SUCCESS"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(start_monitoring).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `start_monitoring` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(start_monitoring) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._start_monitoring = start_monitoring

    @property
    def stop_print(self):
        """Gets the stop_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>StopPrint</strong> updates. Get notifed as soon as a print job finishes.   # noqa: E501

        :return: The stop_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._stop_print

    @stop_print.setter
    def stop_print(self, stop_print):
        """Sets the stop_print of this PatchedCommandAlertSettingsRequest.

        Fires on <strong>StopPrint</strong> updates. Get notifed as soon as a print job finishes.   # noqa: E501

        :param stop_print: The stop_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type stop_print: list[str]
        """
        allowed_values = ["RECEIVED", "FAILED", "SUCCESS"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(stop_print).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `stop_print` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(stop_print) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._stop_print = stop_print

    @property
    def start_print(self):
        """Gets the start_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem.  # noqa: E501

        :return: The start_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._start_print

    @start_print.setter
    def start_print(self, start_print):
        """Sets the start_print of this PatchedCommandAlertSettingsRequest.

        Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem.  # noqa: E501

        :param start_print: The start_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type start_print: list[str]
        """
        allowed_values = ["RECEIVED", "FAILED", "SUCCESS"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(start_print).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `start_print` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(start_print) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._start_print = start_print

    @property
    def move_nozzle(self):
        """Gets the move_nozzle of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint  # noqa: E501

        :return: The move_nozzle of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._move_nozzle

    @move_nozzle.setter
    def move_nozzle(self, move_nozzle):
        """Sets the move_nozzle of this PatchedCommandAlertSettingsRequest.

        Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint  # noqa: E501

        :param move_nozzle: The move_nozzle of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type move_nozzle: list[str]
        """
        allowed_values = ["RECEIVED", "FAILED", "SUCCESS"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(move_nozzle).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `move_nozzle` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(move_nozzle) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._move_nozzle = move_nozzle

    @property
    def pause_print(self):
        """Gets the pause_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.  # noqa: E501

        :return: The pause_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._pause_print

    @pause_print.setter
    def pause_print(self, pause_print):
        """Sets the pause_print of this PatchedCommandAlertSettingsRequest.

        Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.  # noqa: E501

        :param pause_print: The pause_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type pause_print: list[str]
        """
        allowed_values = ["RECEIVED", "FAILED", "SUCCESS"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(pause_print).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `pause_print` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(pause_print) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._pause_print = pause_print

    @property
    def resume_print(self):
        """Gets the resume_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.  # noqa: E501

        :return: The resume_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resume_print

    @resume_print.setter
    def resume_print(self, resume_print):
        """Sets the resume_print of this PatchedCommandAlertSettingsRequest.

        Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.  # noqa: E501

        :param resume_print: The resume_print of this PatchedCommandAlertSettingsRequest.  # noqa: E501
        :type resume_print: list[str]
        """
        allowed_values = ["RECEIVED", "FAILED", "SUCCESS"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(resume_print).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `resume_print` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(resume_print) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._resume_print = resume_print

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
        if not isinstance(other, PatchedCommandAlertSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedCommandAlertSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
