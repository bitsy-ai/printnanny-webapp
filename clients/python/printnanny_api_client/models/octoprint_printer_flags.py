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


class OctoprintPrinterFlags(object):
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
        'operational': 'bool',
        'printing': 'bool',
        'cancelling': 'bool',
        'pausing': 'bool',
        'resuming': 'bool',
        'finishing': 'bool',
        'closed_or_error': 'bool',
        'error': 'bool',
        'paused': 'bool',
        'ready': 'bool',
        'sd_ready': 'bool'
    }

    attribute_map = {
        'operational': 'operational',
        'printing': 'printing',
        'cancelling': 'cancelling',
        'pausing': 'pausing',
        'resuming': 'resuming',
        'finishing': 'finishing',
        'closed_or_error': 'closedOrError',
        'error': 'error',
        'paused': 'paused',
        'ready': 'ready',
        'sd_ready': 'sdReady'
    }

    def __init__(self, operational=None, printing=None, cancelling=None, pausing=None, resuming=None, finishing=None, closed_or_error=None, error=None, paused=None, ready=None, sd_ready=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintPrinterFlags - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._operational = None
        self._printing = None
        self._cancelling = None
        self._pausing = None
        self._resuming = None
        self._finishing = None
        self._closed_or_error = None
        self._error = None
        self._paused = None
        self._ready = None
        self._sd_ready = None
        self.discriminator = None

        self.operational = operational
        self.printing = printing
        self.cancelling = cancelling
        self.pausing = pausing
        self.resuming = resuming
        self.finishing = finishing
        self.closed_or_error = closed_or_error
        self.error = error
        self.paused = paused
        self.ready = ready
        self.sd_ready = sd_ready

    @property
    def operational(self):
        """Gets the operational of this OctoprintPrinterFlags.  # noqa: E501


        :return: The operational of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._operational

    @operational.setter
    def operational(self, operational):
        """Sets the operational of this OctoprintPrinterFlags.


        :param operational: The operational of this OctoprintPrinterFlags.  # noqa: E501
        :type operational: bool
        """
        if self.local_vars_configuration.client_side_validation and operational is None:  # noqa: E501
            raise ValueError("Invalid value for `operational`, must not be `None`")  # noqa: E501

        self._operational = operational

    @property
    def printing(self):
        """Gets the printing of this OctoprintPrinterFlags.  # noqa: E501


        :return: The printing of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._printing

    @printing.setter
    def printing(self, printing):
        """Sets the printing of this OctoprintPrinterFlags.


        :param printing: The printing of this OctoprintPrinterFlags.  # noqa: E501
        :type printing: bool
        """
        if self.local_vars_configuration.client_side_validation and printing is None:  # noqa: E501
            raise ValueError("Invalid value for `printing`, must not be `None`")  # noqa: E501

        self._printing = printing

    @property
    def cancelling(self):
        """Gets the cancelling of this OctoprintPrinterFlags.  # noqa: E501


        :return: The cancelling of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._cancelling

    @cancelling.setter
    def cancelling(self, cancelling):
        """Sets the cancelling of this OctoprintPrinterFlags.


        :param cancelling: The cancelling of this OctoprintPrinterFlags.  # noqa: E501
        :type cancelling: bool
        """
        if self.local_vars_configuration.client_side_validation and cancelling is None:  # noqa: E501
            raise ValueError("Invalid value for `cancelling`, must not be `None`")  # noqa: E501

        self._cancelling = cancelling

    @property
    def pausing(self):
        """Gets the pausing of this OctoprintPrinterFlags.  # noqa: E501


        :return: The pausing of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._pausing

    @pausing.setter
    def pausing(self, pausing):
        """Sets the pausing of this OctoprintPrinterFlags.


        :param pausing: The pausing of this OctoprintPrinterFlags.  # noqa: E501
        :type pausing: bool
        """
        if self.local_vars_configuration.client_side_validation and pausing is None:  # noqa: E501
            raise ValueError("Invalid value for `pausing`, must not be `None`")  # noqa: E501

        self._pausing = pausing

    @property
    def resuming(self):
        """Gets the resuming of this OctoprintPrinterFlags.  # noqa: E501


        :return: The resuming of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._resuming

    @resuming.setter
    def resuming(self, resuming):
        """Sets the resuming of this OctoprintPrinterFlags.


        :param resuming: The resuming of this OctoprintPrinterFlags.  # noqa: E501
        :type resuming: bool
        """
        if self.local_vars_configuration.client_side_validation and resuming is None:  # noqa: E501
            raise ValueError("Invalid value for `resuming`, must not be `None`")  # noqa: E501

        self._resuming = resuming

    @property
    def finishing(self):
        """Gets the finishing of this OctoprintPrinterFlags.  # noqa: E501


        :return: The finishing of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._finishing

    @finishing.setter
    def finishing(self, finishing):
        """Sets the finishing of this OctoprintPrinterFlags.


        :param finishing: The finishing of this OctoprintPrinterFlags.  # noqa: E501
        :type finishing: bool
        """
        if self.local_vars_configuration.client_side_validation and finishing is None:  # noqa: E501
            raise ValueError("Invalid value for `finishing`, must not be `None`")  # noqa: E501

        self._finishing = finishing

    @property
    def closed_or_error(self):
        """Gets the closed_or_error of this OctoprintPrinterFlags.  # noqa: E501


        :return: The closed_or_error of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._closed_or_error

    @closed_or_error.setter
    def closed_or_error(self, closed_or_error):
        """Sets the closed_or_error of this OctoprintPrinterFlags.


        :param closed_or_error: The closed_or_error of this OctoprintPrinterFlags.  # noqa: E501
        :type closed_or_error: bool
        """
        if self.local_vars_configuration.client_side_validation and closed_or_error is None:  # noqa: E501
            raise ValueError("Invalid value for `closed_or_error`, must not be `None`")  # noqa: E501

        self._closed_or_error = closed_or_error

    @property
    def error(self):
        """Gets the error of this OctoprintPrinterFlags.  # noqa: E501


        :return: The error of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this OctoprintPrinterFlags.


        :param error: The error of this OctoprintPrinterFlags.  # noqa: E501
        :type error: bool
        """
        if self.local_vars_configuration.client_side_validation and error is None:  # noqa: E501
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def paused(self):
        """Gets the paused of this OctoprintPrinterFlags.  # noqa: E501


        :return: The paused of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this OctoprintPrinterFlags.


        :param paused: The paused of this OctoprintPrinterFlags.  # noqa: E501
        :type paused: bool
        """
        if self.local_vars_configuration.client_side_validation and paused is None:  # noqa: E501
            raise ValueError("Invalid value for `paused`, must not be `None`")  # noqa: E501

        self._paused = paused

    @property
    def ready(self):
        """Gets the ready of this OctoprintPrinterFlags.  # noqa: E501


        :return: The ready of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this OctoprintPrinterFlags.


        :param ready: The ready of this OctoprintPrinterFlags.  # noqa: E501
        :type ready: bool
        """
        if self.local_vars_configuration.client_side_validation and ready is None:  # noqa: E501
            raise ValueError("Invalid value for `ready`, must not be `None`")  # noqa: E501

        self._ready = ready

    @property
    def sd_ready(self):
        """Gets the sd_ready of this OctoprintPrinterFlags.  # noqa: E501


        :return: The sd_ready of this OctoprintPrinterFlags.  # noqa: E501
        :rtype: bool
        """
        return self._sd_ready

    @sd_ready.setter
    def sd_ready(self, sd_ready):
        """Sets the sd_ready of this OctoprintPrinterFlags.


        :param sd_ready: The sd_ready of this OctoprintPrinterFlags.  # noqa: E501
        :type sd_ready: bool
        """
        if self.local_vars_configuration.client_side_validation and sd_ready is None:  # noqa: E501
            raise ValueError("Invalid value for `sd_ready`, must not be `None`")  # noqa: E501

        self._sd_ready = sd_ready

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
        if not isinstance(other, OctoprintPrinterFlags):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintPrinterFlags):
            return True

        return self.to_dict() != other.to_dict()
