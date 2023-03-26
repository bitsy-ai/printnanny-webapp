# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.129.8
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
        'network_settings': 'NetworkSettings',
        'user': 'User',
        'system_info': 'SystemInfo',
        'webrtc_edge': 'WebrtcStream',
        'webrtc_cloud': 'WebrtcStream',
        'octoprint_server': 'OctoPrintServer',
        'hostname': 'str',
        'favorite': 'bool',
        'sbc': 'SbcEnum',
        'setup_finished': 'bool',
        'nats_app': 'PiNatsApp',
        'urls': 'PiUrls',
        'shortname_urls': 'PiUrls',
        'mdns_urls': 'PiUrls',
        'created_dt': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'last_boot': 'last_boot',
        'network_settings': 'network_settings',
        'user': 'user',
        'system_info': 'system_info',
        'webrtc_edge': 'webrtc_edge',
        'webrtc_cloud': 'webrtc_cloud',
        'octoprint_server': 'octoprint_server',
        'hostname': 'hostname',
        'favorite': 'favorite',
        'sbc': 'sbc',
        'setup_finished': 'setup_finished',
        'nats_app': 'nats_app',
        'urls': 'urls',
        'shortname_urls': 'shortname_urls',
        'mdns_urls': 'mdns_urls',
        'created_dt': 'created_dt'
    }

    def __init__(self, id=None, last_boot=None, network_settings=None, user=None, system_info=None, webrtc_edge=None, webrtc_cloud=None, octoprint_server=None, hostname=None, favorite=None, sbc=None, setup_finished=None, nats_app=None, urls=None, shortname_urls=None, mdns_urls=None, created_dt=None, local_vars_configuration=None):  # noqa: E501
        """Pi - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._last_boot = None
        self._network_settings = None
        self._user = None
        self._system_info = None
        self._webrtc_edge = None
        self._webrtc_cloud = None
        self._octoprint_server = None
        self._hostname = None
        self._favorite = None
        self._sbc = None
        self._setup_finished = None
        self._nats_app = None
        self._urls = None
        self._shortname_urls = None
        self._mdns_urls = None
        self._created_dt = None
        self.discriminator = None

        self.id = id
        self.last_boot = last_boot
        self.network_settings = network_settings
        self.user = user
        self.system_info = system_info
        self.webrtc_edge = webrtc_edge
        self.webrtc_cloud = webrtc_cloud
        self.octoprint_server = octoprint_server
        self.hostname = hostname
        self.favorite = favorite
        self.sbc = sbc
        self.setup_finished = setup_finished
        self.nats_app = nats_app
        self.urls = urls
        self.shortname_urls = shortname_urls
        self.mdns_urls = mdns_urls
        self.created_dt = created_dt

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
    def network_settings(self):
        """Gets the network_settings of this Pi.  # noqa: E501


        :return: The network_settings of this Pi.  # noqa: E501
        :rtype: NetworkSettings
        """
        return self._network_settings

    @network_settings.setter
    def network_settings(self, network_settings):
        """Sets the network_settings of this Pi.


        :param network_settings: The network_settings of this Pi.  # noqa: E501
        :type network_settings: NetworkSettings
        """

        self._network_settings = network_settings

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
    def hostname(self):
        """Gets the hostname of this Pi.  # noqa: E501


        :return: The hostname of this Pi.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Pi.


        :param hostname: The hostname of this Pi.  # noqa: E501
        :type hostname: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

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
        if self.local_vars_configuration.client_side_validation and favorite is None:  # noqa: E501
            raise ValueError("Invalid value for `favorite`, must not be `None`")  # noqa: E501

        self._favorite = favorite

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
        if self.local_vars_configuration.client_side_validation and sbc is None:  # noqa: E501
            raise ValueError("Invalid value for `sbc`, must not be `None`")  # noqa: E501

        self._sbc = sbc

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
        if self.local_vars_configuration.client_side_validation and setup_finished is None:  # noqa: E501
            raise ValueError("Invalid value for `setup_finished`, must not be `None`")  # noqa: E501

        self._setup_finished = setup_finished

    @property
    def nats_app(self):
        """Gets the nats_app of this Pi.  # noqa: E501


        :return: The nats_app of this Pi.  # noqa: E501
        :rtype: PiNatsApp
        """
        return self._nats_app

    @nats_app.setter
    def nats_app(self, nats_app):
        """Sets the nats_app of this Pi.


        :param nats_app: The nats_app of this Pi.  # noqa: E501
        :type nats_app: PiNatsApp
        """

        self._nats_app = nats_app

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
    def shortname_urls(self):
        """Gets the shortname_urls of this Pi.  # noqa: E501


        :return: The shortname_urls of this Pi.  # noqa: E501
        :rtype: PiUrls
        """
        return self._shortname_urls

    @shortname_urls.setter
    def shortname_urls(self, shortname_urls):
        """Sets the shortname_urls of this Pi.


        :param shortname_urls: The shortname_urls of this Pi.  # noqa: E501
        :type shortname_urls: PiUrls
        """
        if self.local_vars_configuration.client_side_validation and shortname_urls is None:  # noqa: E501
            raise ValueError("Invalid value for `shortname_urls`, must not be `None`")  # noqa: E501

        self._shortname_urls = shortname_urls

    @property
    def mdns_urls(self):
        """Gets the mdns_urls of this Pi.  # noqa: E501


        :return: The mdns_urls of this Pi.  # noqa: E501
        :rtype: PiUrls
        """
        return self._mdns_urls

    @mdns_urls.setter
    def mdns_urls(self, mdns_urls):
        """Sets the mdns_urls of this Pi.


        :param mdns_urls: The mdns_urls of this Pi.  # noqa: E501
        :type mdns_urls: PiUrls
        """
        if self.local_vars_configuration.client_side_validation and mdns_urls is None:  # noqa: E501
            raise ValueError("Invalid value for `mdns_urls`, must not be `None`")  # noqa: E501

        self._mdns_urls = mdns_urls

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
