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


class OctoprintPrinterData(object):
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
        'job': 'OctoprintJob',
        'state': 'OctoprintPrinterState',
        'user': 'str',
        'current_z': 'float',
        'progress': 'OctoprintProgress',
        'resends': 'dict(str, object)',
        'offsets': 'dict(str, object)'
    }

    attribute_map = {
        'job': 'job',
        'state': 'state',
        'user': 'user',
        'current_z': 'currentZ',
        'progress': 'progress',
        'resends': 'resends',
        'offsets': 'offsets'
    }

    def __init__(self, job=None, state=None, user=None, current_z=None, progress=None, resends=None, offsets=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintPrinterData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._job = None
        self._state = None
        self._user = None
        self._current_z = None
        self._progress = None
        self._resends = None
        self._offsets = None
        self.discriminator = None

        self.job = job
        self.state = state
        self.user = user
        self.current_z = current_z
        self.progress = progress
        self.resends = resends
        self.offsets = offsets

    @property
    def job(self):
        """Gets the job of this OctoprintPrinterData.  # noqa: E501


        :return: The job of this OctoprintPrinterData.  # noqa: E501
        :rtype: OctoprintJob
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this OctoprintPrinterData.


        :param job: The job of this OctoprintPrinterData.  # noqa: E501
        :type job: OctoprintJob
        """
        if self.local_vars_configuration.client_side_validation and job is None:  # noqa: E501
            raise ValueError("Invalid value for `job`, must not be `None`")  # noqa: E501

        self._job = job

    @property
    def state(self):
        """Gets the state of this OctoprintPrinterData.  # noqa: E501


        :return: The state of this OctoprintPrinterData.  # noqa: E501
        :rtype: OctoprintPrinterState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this OctoprintPrinterData.


        :param state: The state of this OctoprintPrinterData.  # noqa: E501
        :type state: OctoprintPrinterState
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def user(self):
        """Gets the user of this OctoprintPrinterData.  # noqa: E501


        :return: The user of this OctoprintPrinterData.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OctoprintPrinterData.


        :param user: The user of this OctoprintPrinterData.  # noqa: E501
        :type user: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def current_z(self):
        """Gets the current_z of this OctoprintPrinterData.  # noqa: E501


        :return: The current_z of this OctoprintPrinterData.  # noqa: E501
        :rtype: float
        """
        return self._current_z

    @current_z.setter
    def current_z(self, current_z):
        """Sets the current_z of this OctoprintPrinterData.


        :param current_z: The current_z of this OctoprintPrinterData.  # noqa: E501
        :type current_z: float
        """
        if self.local_vars_configuration.client_side_validation and current_z is None:  # noqa: E501
            raise ValueError("Invalid value for `current_z`, must not be `None`")  # noqa: E501

        self._current_z = current_z

    @property
    def progress(self):
        """Gets the progress of this OctoprintPrinterData.  # noqa: E501


        :return: The progress of this OctoprintPrinterData.  # noqa: E501
        :rtype: OctoprintProgress
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this OctoprintPrinterData.


        :param progress: The progress of this OctoprintPrinterData.  # noqa: E501
        :type progress: OctoprintProgress
        """
        if self.local_vars_configuration.client_side_validation and progress is None:  # noqa: E501
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501

        self._progress = progress

    @property
    def resends(self):
        """Gets the resends of this OctoprintPrinterData.  # noqa: E501


        :return: The resends of this OctoprintPrinterData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._resends

    @resends.setter
    def resends(self, resends):
        """Sets the resends of this OctoprintPrinterData.


        :param resends: The resends of this OctoprintPrinterData.  # noqa: E501
        :type resends: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and resends is None:  # noqa: E501
            raise ValueError("Invalid value for `resends`, must not be `None`")  # noqa: E501

        self._resends = resends

    @property
    def offsets(self):
        """Gets the offsets of this OctoprintPrinterData.  # noqa: E501


        :return: The offsets of this OctoprintPrinterData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._offsets

    @offsets.setter
    def offsets(self, offsets):
        """Sets the offsets of this OctoprintPrinterData.


        :param offsets: The offsets of this OctoprintPrinterData.  # noqa: E501
        :type offsets: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and offsets is None:  # noqa: E501
            raise ValueError("Invalid value for `offsets`, must not be `None`")  # noqa: E501

        self._offsets = offsets

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
        if not isinstance(other, OctoprintPrinterData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintPrinterData):
            return True

        return self.to_dict() != other.to_dict()
