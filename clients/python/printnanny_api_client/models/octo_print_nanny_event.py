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


class OctoPrintNannyEvent(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BACKUP_START = "plugin_octoprint_nanny_backup_start"
    BACKUP_SUCCESS = "plugin_octoprint_nanny_backup_success"
    BACKUP_FAILURE = "plugin_octoprint_nanny_backup_failure"
    MONITORING_START = "plugin_octoprint_nanny_monitoring_start"
    MONITORING_STOP = "plugin_octoprint_nanny_monitoring_stop"
    MONITORING_RESET = "plugin_octoprint_nanny_monitoring_reset"
    DEVICE_REGISTER_START = "plugin_octoprint_nanny_device_register_start"
    DEVICE_REGISTER_DONE = "plugin_octoprint_nanny_device_register_done"
    DEVICE_REGISTER_FAILED = "plugin_octoprint_nanny_device_register_failed"
    DEVICE_RESET = "plugin_octoprint_nanny_device_reset"
    PRINTER_PROFILE_SYNC_START = "plugin_octoprint_nanny_printer_profile_sync_start"
    PRINTER_PROFILE_SYNC_DONE = "plugin_octoprint_nanny_printer_profile_sync_done"
    PRINTER_PROFILE_SYNC_FAILED = "plugin_octoprint_nanny_printer_profile_sync_failed"
    CONNECT_TEST_REST_API = "plugin_octoprint_nanny_connect_test_rest_api"
    CONNECT_TEST_REST_API_FAILED = "plugin_octoprint_nanny_connect_test_rest_api_failed"
    CONNECT_TEST_REST_API_SUCCESS = "plugin_octoprint_nanny_connect_test_rest_api_success"
    CONNECT_TEST_MQTT_PING = "plugin_octoprint_nanny_connect_test_mqtt_ping"
    CONNECT_TEST_MQTT_PING_FAILED = "plugin_octoprint_nanny_connect_test_mqtt_ping_failed"
    CONNECT_TEST_MQTT_PING_SUCCESS = "plugin_octoprint_nanny_connect_test_mqtt_ping_success"
    CONNECT_TEST_MQTT_PONG = "plugin_octoprint_nanny_connect_test_mqtt_pong"
    CONNECT_TEST_MQTT_PONG_FAILED = "plugin_octoprint_nanny_connect_test_mqtt_pong_failed"
    CONNECT_TEST_MQTT_PONG_SUCCESS = "plugin_octoprint_nanny_connect_test_mqtt_pong_success"

    allowable_values = [BACKUP_START, BACKUP_SUCCESS, BACKUP_FAILURE, MONITORING_START, MONITORING_STOP, MONITORING_RESET, DEVICE_REGISTER_START, DEVICE_REGISTER_DONE, DEVICE_REGISTER_FAILED, DEVICE_RESET, PRINTER_PROFILE_SYNC_START, PRINTER_PROFILE_SYNC_DONE, PRINTER_PROFILE_SYNC_FAILED, CONNECT_TEST_REST_API, CONNECT_TEST_REST_API_FAILED, CONNECT_TEST_REST_API_SUCCESS, CONNECT_TEST_MQTT_PING, CONNECT_TEST_MQTT_PING_FAILED, CONNECT_TEST_MQTT_PING_SUCCESS, CONNECT_TEST_MQTT_PONG, CONNECT_TEST_MQTT_PONG_FAILED, CONNECT_TEST_MQTT_PONG_SUCCESS]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """OctoPrintNannyEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, OctoPrintNannyEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoPrintNannyEvent):
            return True

        return self.to_dict() != other.to_dict()
