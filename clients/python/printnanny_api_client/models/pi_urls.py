# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.133.2
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


class PiUrls(object):
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
        'moonraker_api': 'str',
        'mission_control': 'str',
        'octoprint': 'str',
        'swupdate': 'str',
        'syncthing': 'str'
    }

    attribute_map = {
        'moonraker_api': 'moonraker_api',
        'mission_control': 'mission_control',
        'octoprint': 'octoprint',
        'swupdate': 'swupdate',
        'syncthing': 'syncthing'
    }

    def __init__(self, moonraker_api=None, mission_control=None, octoprint=None, swupdate=None, syncthing=None, local_vars_configuration=None):  # noqa: E501
        """PiUrls - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._moonraker_api = None
        self._mission_control = None
        self._octoprint = None
        self._swupdate = None
        self._syncthing = None
        self.discriminator = None

        self.moonraker_api = moonraker_api
        self.mission_control = mission_control
        self.octoprint = octoprint
        self.swupdate = swupdate
        self.syncthing = syncthing

    @property
    def moonraker_api(self):
        """Gets the moonraker_api of this PiUrls.  # noqa: E501


        :return: The moonraker_api of this PiUrls.  # noqa: E501
        :rtype: str
        """
        return self._moonraker_api

    @moonraker_api.setter
    def moonraker_api(self, moonraker_api):
        """Sets the moonraker_api of this PiUrls.


        :param moonraker_api: The moonraker_api of this PiUrls.  # noqa: E501
        :type moonraker_api: str
        """
        if self.local_vars_configuration.client_side_validation and moonraker_api is None:  # noqa: E501
            raise ValueError("Invalid value for `moonraker_api`, must not be `None`")  # noqa: E501

        self._moonraker_api = moonraker_api

    @property
    def mission_control(self):
        """Gets the mission_control of this PiUrls.  # noqa: E501


        :return: The mission_control of this PiUrls.  # noqa: E501
        :rtype: str
        """
        return self._mission_control

    @mission_control.setter
    def mission_control(self, mission_control):
        """Sets the mission_control of this PiUrls.


        :param mission_control: The mission_control of this PiUrls.  # noqa: E501
        :type mission_control: str
        """
        if self.local_vars_configuration.client_side_validation and mission_control is None:  # noqa: E501
            raise ValueError("Invalid value for `mission_control`, must not be `None`")  # noqa: E501

        self._mission_control = mission_control

    @property
    def octoprint(self):
        """Gets the octoprint of this PiUrls.  # noqa: E501


        :return: The octoprint of this PiUrls.  # noqa: E501
        :rtype: str
        """
        return self._octoprint

    @octoprint.setter
    def octoprint(self, octoprint):
        """Sets the octoprint of this PiUrls.


        :param octoprint: The octoprint of this PiUrls.  # noqa: E501
        :type octoprint: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint`, must not be `None`")  # noqa: E501

        self._octoprint = octoprint

    @property
    def swupdate(self):
        """Gets the swupdate of this PiUrls.  # noqa: E501


        :return: The swupdate of this PiUrls.  # noqa: E501
        :rtype: str
        """
        return self._swupdate

    @swupdate.setter
    def swupdate(self, swupdate):
        """Sets the swupdate of this PiUrls.


        :param swupdate: The swupdate of this PiUrls.  # noqa: E501
        :type swupdate: str
        """
        if self.local_vars_configuration.client_side_validation and swupdate is None:  # noqa: E501
            raise ValueError("Invalid value for `swupdate`, must not be `None`")  # noqa: E501

        self._swupdate = swupdate

    @property
    def syncthing(self):
        """Gets the syncthing of this PiUrls.  # noqa: E501


        :return: The syncthing of this PiUrls.  # noqa: E501
        :rtype: str
        """
        return self._syncthing

    @syncthing.setter
    def syncthing(self, syncthing):
        """Sets the syncthing of this PiUrls.


        :param syncthing: The syncthing of this PiUrls.  # noqa: E501
        :type syncthing: str
        """
        if self.local_vars_configuration.client_side_validation and syncthing is None:  # noqa: E501
            raise ValueError("Invalid value for `syncthing`, must not be `None`")  # noqa: E501

        self._syncthing = syncthing

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
        if not isinstance(other, PiUrls):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PiUrls):
            return True

        return self.to_dict() != other.to_dict()
