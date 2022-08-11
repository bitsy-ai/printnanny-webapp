# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.8
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


class Pi(object):
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
        'last_boot': 'str',
        'settings': 'PiSettings',
        'cloudiot_device': 'CloudiotDevice',
        'user': 'User',
        'system_info': 'SystemInfo',
        'public_key': 'PublicKey',
        'webrtc_edge': 'WebrtcStream',
        'webrtc_cloud': 'WebrtcStream',
        'octoprint_server': 'OctoPrintServer',
        'urls': 'PiUrls',
        'sbc': 'SbcEnum',
        'edition': 'OsEdition',
        'created_dt': 'datetime',
        'hostname': 'str',
        'fqdn': 'str',
        'favorite': 'bool',
        'setup_finished': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'last_boot': 'last_boot',
        'settings': 'settings',
        'cloudiot_device': 'cloudiot_device',
        'user': 'user',
        'system_info': 'system_info',
        'public_key': 'public_key',
        'webrtc_edge': 'webrtc_edge',
        'webrtc_cloud': 'webrtc_cloud',
        'octoprint_server': 'octoprint_server',
        'urls': 'urls',
        'sbc': 'sbc',
        'edition': 'edition',
        'created_dt': 'created_dt',
        'hostname': 'hostname',
        'fqdn': 'fqdn',
        'favorite': 'favorite',
        'setup_finished': 'setup_finished'
    }

    def __init__(self, id=None, last_boot=None, settings=None, cloudiot_device=None, user=None, system_info=None, public_key=None, webrtc_edge=None, webrtc_cloud=None, octoprint_server=None, urls=None, sbc=None, edition=None, created_dt=None, hostname=None, fqdn=None, favorite=None, setup_finished=None, local_vars_configuration=None):  # noqa: E501
        """Pi - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._last_boot = None
        self._settings = None
        self._cloudiot_device = None
        self._user = None
        self._system_info = None
        self._public_key = None
        self._webrtc_edge = None
        self._webrtc_cloud = None
        self._octoprint_server = None
        self._urls = None
        self._sbc = None
        self._edition = None
        self._created_dt = None
        self._hostname = None
        self._fqdn = None
        self._favorite = None
        self._setup_finished = None
        self.discriminator = None

        self.id = id
        self.last_boot = last_boot
        self.settings = settings
        self.cloudiot_device = cloudiot_device
        self.user = user
        self.system_info = system_info
        self.public_key = public_key
        self.webrtc_edge = webrtc_edge
        self.webrtc_cloud = webrtc_cloud
        self.octoprint_server = octoprint_server
        self.urls = urls
        if sbc is not None:
            self.sbc = sbc
        if edition is not None:
            self.edition = edition
        self.created_dt = created_dt
        if hostname is not None:
            self.hostname = hostname
        if fqdn is not None:
            self.fqdn = fqdn
        if favorite is not None:
            self.favorite = favorite
        if setup_finished is not None:
            self.setup_finished = setup_finished

    @property
    def id(self):
        """Gets the id of this Pi.  # noqa: E501


        :return: The id of this Pi.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pi.


        :param id: The id of this Pi.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_boot(self):
        """Gets the last_boot of this Pi.  # noqa: E501


        :return: The last_boot of this Pi.  # noqa: E501
        :rtype: str
        """
        return self._last_boot

    @last_boot.setter
    def last_boot(self, last_boot):
        """Sets the last_boot of this Pi.


        :param last_boot: The last_boot of this Pi.  # noqa: E501
        :type last_boot: str
        """

        self._last_boot = last_boot

    @property
    def settings(self):
        """Gets the settings of this Pi.  # noqa: E501


        :return: The settings of this Pi.  # noqa: E501
        :rtype: PiSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Pi.


        :param settings: The settings of this Pi.  # noqa: E501
        :type settings: PiSettings
        """

        self._settings = settings

    @property
    def cloudiot_device(self):
        """Gets the cloudiot_device of this Pi.  # noqa: E501


        :return: The cloudiot_device of this Pi.  # noqa: E501
        :rtype: CloudiotDevice
        """
        return self._cloudiot_device

    @cloudiot_device.setter
    def cloudiot_device(self, cloudiot_device):
        """Sets the cloudiot_device of this Pi.


        :param cloudiot_device: The cloudiot_device of this Pi.  # noqa: E501
        :type cloudiot_device: CloudiotDevice
        """

        self._cloudiot_device = cloudiot_device

    @property
    def user(self):
        """Gets the user of this Pi.  # noqa: E501


        :return: The user of this Pi.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Pi.


        :param user: The user of this Pi.  # noqa: E501
        :type user: User
        """

        self._user = user

    @property
    def system_info(self):
        """Gets the system_info of this Pi.  # noqa: E501


        :return: The system_info of this Pi.  # noqa: E501
        :rtype: SystemInfo
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this Pi.


        :param system_info: The system_info of this Pi.  # noqa: E501
        :type system_info: SystemInfo
        """

        self._system_info = system_info

    @property
    def public_key(self):
        """Gets the public_key of this Pi.  # noqa: E501


        :return: The public_key of this Pi.  # noqa: E501
        :rtype: PublicKey
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Pi.


        :param public_key: The public_key of this Pi.  # noqa: E501
        :type public_key: PublicKey
        """

        self._public_key = public_key

    @property
    def webrtc_edge(self):
        """Gets the webrtc_edge of this Pi.  # noqa: E501


        :return: The webrtc_edge of this Pi.  # noqa: E501
        :rtype: WebrtcStream
        """
        return self._webrtc_edge

    @webrtc_edge.setter
    def webrtc_edge(self, webrtc_edge):
        """Sets the webrtc_edge of this Pi.


        :param webrtc_edge: The webrtc_edge of this Pi.  # noqa: E501
        :type webrtc_edge: WebrtcStream
        """

        self._webrtc_edge = webrtc_edge

    @property
    def webrtc_cloud(self):
        """Gets the webrtc_cloud of this Pi.  # noqa: E501


        :return: The webrtc_cloud of this Pi.  # noqa: E501
        :rtype: WebrtcStream
        """
        return self._webrtc_cloud

    @webrtc_cloud.setter
    def webrtc_cloud(self, webrtc_cloud):
        """Sets the webrtc_cloud of this Pi.


        :param webrtc_cloud: The webrtc_cloud of this Pi.  # noqa: E501
        :type webrtc_cloud: WebrtcStream
        """

        self._webrtc_cloud = webrtc_cloud

    @property
    def octoprint_server(self):
        """Gets the octoprint_server of this Pi.  # noqa: E501


        :return: The octoprint_server of this Pi.  # noqa: E501
        :rtype: OctoPrintServer
        """
        return self._octoprint_server

    @octoprint_server.setter
    def octoprint_server(self, octoprint_server):
        """Sets the octoprint_server of this Pi.


        :param octoprint_server: The octoprint_server of this Pi.  # noqa: E501
        :type octoprint_server: OctoPrintServer
        """

        self._octoprint_server = octoprint_server

    @property
    def urls(self):
        """Gets the urls of this Pi.  # noqa: E501


        :return: The urls of this Pi.  # noqa: E501
        :rtype: PiUrls
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this Pi.


        :param urls: The urls of this Pi.  # noqa: E501
        :type urls: PiUrls
        """
        if self.local_vars_configuration.client_side_validation and urls is None:  # noqa: E501
            raise ValueError("Invalid value for `urls`, must not be `None`")  # noqa: E501

        self._urls = urls

    @property
    def sbc(self):
        """Gets the sbc of this Pi.  # noqa: E501


        :return: The sbc of this Pi.  # noqa: E501
        :rtype: SbcEnum
        """
        return self._sbc

    @sbc.setter
    def sbc(self, sbc):
        """Sets the sbc of this Pi.


        :param sbc: The sbc of this Pi.  # noqa: E501
        :type sbc: SbcEnum
        """

        self._sbc = sbc

    @property
    def edition(self):
        """Gets the edition of this Pi.  # noqa: E501


        :return: The edition of this Pi.  # noqa: E501
        :rtype: OsEdition
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this Pi.


        :param edition: The edition of this Pi.  # noqa: E501
        :type edition: OsEdition
        """

        self._edition = edition

    @property
    def created_dt(self):
        """Gets the created_dt of this Pi.  # noqa: E501


        :return: The created_dt of this Pi.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Pi.


        :param created_dt: The created_dt of this Pi.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def hostname(self):
        """Gets the hostname of this Pi.  # noqa: E501

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :return: The hostname of this Pi.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Pi.

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :param hostname: The hostname of this Pi.  # noqa: E501
        :type hostname: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501

        self._hostname = hostname

    @property
    def fqdn(self):
        """Gets the fqdn of this Pi.  # noqa: E501


        :return: The fqdn of this Pi.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this Pi.


        :param fqdn: The fqdn of this Pi.  # noqa: E501
        :type fqdn: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fqdn is not None and len(fqdn) > 255):
            raise ValueError("Invalid value for `fqdn`, length must be less than or equal to `255`")  # noqa: E501

        self._fqdn = fqdn

    @property
    def favorite(self):
        """Gets the favorite of this Pi.  # noqa: E501


        :return: The favorite of this Pi.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this Pi.


        :param favorite: The favorite of this Pi.  # noqa: E501
        :type favorite: bool
        """

        self._favorite = favorite

    @property
    def setup_finished(self):
        """Gets the setup_finished of this Pi.  # noqa: E501


        :return: The setup_finished of this Pi.  # noqa: E501
        :rtype: bool
        """
        return self._setup_finished

    @setup_finished.setter
    def setup_finished(self, setup_finished):
        """Sets the setup_finished of this Pi.


        :param setup_finished: The setup_finished of this Pi.  # noqa: E501
        :type setup_finished: bool
        """

        self._setup_finished = setup_finished

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
        if not isinstance(other, Pi):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Pi):
            return True

        return self.to_dict() != other.to_dict()
