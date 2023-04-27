# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.133.4
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


class WebrtcStream(object):
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
        'active': 'bool',
        'admin_port': 'int',
        'admin_secret': 'str',
        'admin_url': 'str',
        'api_domain': 'str',
        'api_port': 'int',
        'api_token': 'str',
        'api_url': 'str',
        'config_type': 'JanusConfigType',
        'created_dt': 'datetime',
        'id': 'int',
        'info': 'dict(str, object)',
        'is_admin': 'bool',
        'pi': 'int',
        'pt': 'int',
        'rtp_domain': 'str',
        'video_rtp_port': 'int',
        'data_rtp_port': 'int',
        'rtpmap': 'str',
        'stream_pin': 'str',
        'stream_secret': 'str',
        'updated_dt': 'datetime',
        'ws_port': 'int',
        'ws_url': 'str'
    }

    attribute_map = {
        'active': 'active',
        'admin_port': 'admin_port',
        'admin_secret': 'admin_secret',
        'admin_url': 'admin_url',
        'api_domain': 'api_domain',
        'api_port': 'api_port',
        'api_token': 'api_token',
        'api_url': 'api_url',
        'config_type': 'config_type',
        'created_dt': 'created_dt',
        'id': 'id',
        'info': 'info',
        'is_admin': 'is_admin',
        'pi': 'pi',
        'pt': 'pt',
        'rtp_domain': 'rtp_domain',
        'video_rtp_port': 'video_rtp_port',
        'data_rtp_port': 'data_rtp_port',
        'rtpmap': 'rtpmap',
        'stream_pin': 'stream_pin',
        'stream_secret': 'stream_secret',
        'updated_dt': 'updated_dt',
        'ws_port': 'ws_port',
        'ws_url': 'ws_url'
    }

    def __init__(self, active=None, admin_port=None, admin_secret=None, admin_url=None, api_domain=None, api_port=None, api_token=None, api_url=None, config_type=None, created_dt=None, id=None, info=None, is_admin=None, pi=None, pt=None, rtp_domain=None, video_rtp_port=None, data_rtp_port=None, rtpmap=None, stream_pin=None, stream_secret=None, updated_dt=None, ws_port=None, ws_url=None, local_vars_configuration=None):  # noqa: E501
        """WebrtcStream - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._admin_port = None
        self._admin_secret = None
        self._admin_url = None
        self._api_domain = None
        self._api_port = None
        self._api_token = None
        self._api_url = None
        self._config_type = None
        self._created_dt = None
        self._id = None
        self._info = None
        self._is_admin = None
        self._pi = None
        self._pt = None
        self._rtp_domain = None
        self._video_rtp_port = None
        self._data_rtp_port = None
        self._rtpmap = None
        self._stream_pin = None
        self._stream_secret = None
        self._updated_dt = None
        self._ws_port = None
        self._ws_url = None
        self.discriminator = None

        if active is not None:
            self.active = active
        self.admin_port = admin_port
        self.admin_secret = admin_secret
        self.admin_url = admin_url
        self.api_domain = api_domain
        self.api_port = api_port
        self.api_token = api_token
        self.api_url = api_url
        if config_type is not None:
            self.config_type = config_type
        self.created_dt = created_dt
        self.id = id
        self.info = info
        self.is_admin = is_admin
        self.pi = pi
        self.pt = pt
        self.rtp_domain = rtp_domain
        self.video_rtp_port = video_rtp_port
        self.data_rtp_port = data_rtp_port
        self.rtpmap = rtpmap
        self.stream_pin = stream_pin
        self.stream_secret = stream_secret
        self.updated_dt = updated_dt
        self.ws_port = ws_port
        self.ws_url = ws_url

    @property
    def active(self):
        """Gets the active of this WebrtcStream.  # noqa: E501


        :return: The active of this WebrtcStream.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this WebrtcStream.


        :param active: The active of this WebrtcStream.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def admin_port(self):
        """Gets the admin_port of this WebrtcStream.  # noqa: E501


        :return: The admin_port of this WebrtcStream.  # noqa: E501
        :rtype: int
        """
        return self._admin_port

    @admin_port.setter
    def admin_port(self, admin_port):
        """Sets the admin_port of this WebrtcStream.


        :param admin_port: The admin_port of this WebrtcStream.  # noqa: E501
        :type admin_port: int
        """
        if self.local_vars_configuration.client_side_validation and admin_port is None:  # noqa: E501
            raise ValueError("Invalid value for `admin_port`, must not be `None`")  # noqa: E501

        self._admin_port = admin_port

    @property
    def admin_secret(self):
        """Gets the admin_secret of this WebrtcStream.  # noqa: E501


        :return: The admin_secret of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._admin_secret

    @admin_secret.setter
    def admin_secret(self, admin_secret):
        """Sets the admin_secret of this WebrtcStream.


        :param admin_secret: The admin_secret of this WebrtcStream.  # noqa: E501
        :type admin_secret: str
        """
        if self.local_vars_configuration.client_side_validation and admin_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `admin_secret`, must not be `None`")  # noqa: E501

        self._admin_secret = admin_secret

    @property
    def admin_url(self):
        """Gets the admin_url of this WebrtcStream.  # noqa: E501


        :return: The admin_url of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._admin_url

    @admin_url.setter
    def admin_url(self, admin_url):
        """Sets the admin_url of this WebrtcStream.


        :param admin_url: The admin_url of this WebrtcStream.  # noqa: E501
        :type admin_url: str
        """
        if self.local_vars_configuration.client_side_validation and admin_url is None:  # noqa: E501
            raise ValueError("Invalid value for `admin_url`, must not be `None`")  # noqa: E501

        self._admin_url = admin_url

    @property
    def api_domain(self):
        """Gets the api_domain of this WebrtcStream.  # noqa: E501


        :return: The api_domain of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._api_domain

    @api_domain.setter
    def api_domain(self, api_domain):
        """Sets the api_domain of this WebrtcStream.


        :param api_domain: The api_domain of this WebrtcStream.  # noqa: E501
        :type api_domain: str
        """
        if self.local_vars_configuration.client_side_validation and api_domain is None:  # noqa: E501
            raise ValueError("Invalid value for `api_domain`, must not be `None`")  # noqa: E501

        self._api_domain = api_domain

    @property
    def api_port(self):
        """Gets the api_port of this WebrtcStream.  # noqa: E501


        :return: The api_port of this WebrtcStream.  # noqa: E501
        :rtype: int
        """
        return self._api_port

    @api_port.setter
    def api_port(self, api_port):
        """Sets the api_port of this WebrtcStream.


        :param api_port: The api_port of this WebrtcStream.  # noqa: E501
        :type api_port: int
        """
        if self.local_vars_configuration.client_side_validation and api_port is None:  # noqa: E501
            raise ValueError("Invalid value for `api_port`, must not be `None`")  # noqa: E501

        self._api_port = api_port

    @property
    def api_token(self):
        """Gets the api_token of this WebrtcStream.  # noqa: E501


        :return: The api_token of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this WebrtcStream.


        :param api_token: The api_token of this WebrtcStream.  # noqa: E501
        :type api_token: str
        """
        if self.local_vars_configuration.client_side_validation and api_token is None:  # noqa: E501
            raise ValueError("Invalid value for `api_token`, must not be `None`")  # noqa: E501

        self._api_token = api_token

    @property
    def api_url(self):
        """Gets the api_url of this WebrtcStream.  # noqa: E501


        :return: The api_url of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._api_url

    @api_url.setter
    def api_url(self, api_url):
        """Sets the api_url of this WebrtcStream.


        :param api_url: The api_url of this WebrtcStream.  # noqa: E501
        :type api_url: str
        """
        if self.local_vars_configuration.client_side_validation and api_url is None:  # noqa: E501
            raise ValueError("Invalid value for `api_url`, must not be `None`")  # noqa: E501

        self._api_url = api_url

    @property
    def config_type(self):
        """Gets the config_type of this WebrtcStream.  # noqa: E501


        :return: The config_type of this WebrtcStream.  # noqa: E501
        :rtype: JanusConfigType
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this WebrtcStream.


        :param config_type: The config_type of this WebrtcStream.  # noqa: E501
        :type config_type: JanusConfigType
        """

        self._config_type = config_type

    @property
    def created_dt(self):
        """Gets the created_dt of this WebrtcStream.  # noqa: E501


        :return: The created_dt of this WebrtcStream.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this WebrtcStream.


        :param created_dt: The created_dt of this WebrtcStream.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def id(self):
        """Gets the id of this WebrtcStream.  # noqa: E501


        :return: The id of this WebrtcStream.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebrtcStream.


        :param id: The id of this WebrtcStream.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def info(self):
        """Gets the info of this WebrtcStream.  # noqa: E501


        :return: The info of this WebrtcStream.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this WebrtcStream.


        :param info: The info of this WebrtcStream.  # noqa: E501
        :type info: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and info is None:  # noqa: E501
            raise ValueError("Invalid value for `info`, must not be `None`")  # noqa: E501

        self._info = info

    @property
    def is_admin(self):
        """Gets the is_admin of this WebrtcStream.  # noqa: E501


        :return: The is_admin of this WebrtcStream.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this WebrtcStream.


        :param is_admin: The is_admin of this WebrtcStream.  # noqa: E501
        :type is_admin: bool
        """
        if self.local_vars_configuration.client_side_validation and is_admin is None:  # noqa: E501
            raise ValueError("Invalid value for `is_admin`, must not be `None`")  # noqa: E501

        self._is_admin = is_admin

    @property
    def pi(self):
        """Gets the pi of this WebrtcStream.  # noqa: E501


        :return: The pi of this WebrtcStream.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this WebrtcStream.


        :param pi: The pi of this WebrtcStream.  # noqa: E501
        :type pi: int
        """
        if self.local_vars_configuration.client_side_validation and pi is None:  # noqa: E501
            raise ValueError("Invalid value for `pi`, must not be `None`")  # noqa: E501

        self._pi = pi

    @property
    def pt(self):
        """Gets the pt of this WebrtcStream.  # noqa: E501


        :return: The pt of this WebrtcStream.  # noqa: E501
        :rtype: int
        """
        return self._pt

    @pt.setter
    def pt(self, pt):
        """Sets the pt of this WebrtcStream.


        :param pt: The pt of this WebrtcStream.  # noqa: E501
        :type pt: int
        """
        if self.local_vars_configuration.client_side_validation and pt is None:  # noqa: E501
            raise ValueError("Invalid value for `pt`, must not be `None`")  # noqa: E501

        self._pt = pt

    @property
    def rtp_domain(self):
        """Gets the rtp_domain of this WebrtcStream.  # noqa: E501


        :return: The rtp_domain of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._rtp_domain

    @rtp_domain.setter
    def rtp_domain(self, rtp_domain):
        """Sets the rtp_domain of this WebrtcStream.


        :param rtp_domain: The rtp_domain of this WebrtcStream.  # noqa: E501
        :type rtp_domain: str
        """
        if self.local_vars_configuration.client_side_validation and rtp_domain is None:  # noqa: E501
            raise ValueError("Invalid value for `rtp_domain`, must not be `None`")  # noqa: E501

        self._rtp_domain = rtp_domain

    @property
    def video_rtp_port(self):
        """Gets the video_rtp_port of this WebrtcStream.  # noqa: E501


        :return: The video_rtp_port of this WebrtcStream.  # noqa: E501
        :rtype: int
        """
        return self._video_rtp_port

    @video_rtp_port.setter
    def video_rtp_port(self, video_rtp_port):
        """Sets the video_rtp_port of this WebrtcStream.


        :param video_rtp_port: The video_rtp_port of this WebrtcStream.  # noqa: E501
        :type video_rtp_port: int
        """

        self._video_rtp_port = video_rtp_port

    @property
    def data_rtp_port(self):
        """Gets the data_rtp_port of this WebrtcStream.  # noqa: E501


        :return: The data_rtp_port of this WebrtcStream.  # noqa: E501
        :rtype: int
        """
        return self._data_rtp_port

    @data_rtp_port.setter
    def data_rtp_port(self, data_rtp_port):
        """Sets the data_rtp_port of this WebrtcStream.


        :param data_rtp_port: The data_rtp_port of this WebrtcStream.  # noqa: E501
        :type data_rtp_port: int
        """

        self._data_rtp_port = data_rtp_port

    @property
    def rtpmap(self):
        """Gets the rtpmap of this WebrtcStream.  # noqa: E501


        :return: The rtpmap of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._rtpmap

    @rtpmap.setter
    def rtpmap(self, rtpmap):
        """Sets the rtpmap of this WebrtcStream.


        :param rtpmap: The rtpmap of this WebrtcStream.  # noqa: E501
        :type rtpmap: str
        """
        if self.local_vars_configuration.client_side_validation and rtpmap is None:  # noqa: E501
            raise ValueError("Invalid value for `rtpmap`, must not be `None`")  # noqa: E501

        self._rtpmap = rtpmap

    @property
    def stream_pin(self):
        """Gets the stream_pin of this WebrtcStream.  # noqa: E501


        :return: The stream_pin of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._stream_pin

    @stream_pin.setter
    def stream_pin(self, stream_pin):
        """Sets the stream_pin of this WebrtcStream.


        :param stream_pin: The stream_pin of this WebrtcStream.  # noqa: E501
        :type stream_pin: str
        """
        if self.local_vars_configuration.client_side_validation and stream_pin is None:  # noqa: E501
            raise ValueError("Invalid value for `stream_pin`, must not be `None`")  # noqa: E501

        self._stream_pin = stream_pin

    @property
    def stream_secret(self):
        """Gets the stream_secret of this WebrtcStream.  # noqa: E501


        :return: The stream_secret of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._stream_secret

    @stream_secret.setter
    def stream_secret(self, stream_secret):
        """Sets the stream_secret of this WebrtcStream.


        :param stream_secret: The stream_secret of this WebrtcStream.  # noqa: E501
        :type stream_secret: str
        """
        if self.local_vars_configuration.client_side_validation and stream_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `stream_secret`, must not be `None`")  # noqa: E501

        self._stream_secret = stream_secret

    @property
    def updated_dt(self):
        """Gets the updated_dt of this WebrtcStream.  # noqa: E501


        :return: The updated_dt of this WebrtcStream.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this WebrtcStream.


        :param updated_dt: The updated_dt of this WebrtcStream.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def ws_port(self):
        """Gets the ws_port of this WebrtcStream.  # noqa: E501


        :return: The ws_port of this WebrtcStream.  # noqa: E501
        :rtype: int
        """
        return self._ws_port

    @ws_port.setter
    def ws_port(self, ws_port):
        """Sets the ws_port of this WebrtcStream.


        :param ws_port: The ws_port of this WebrtcStream.  # noqa: E501
        :type ws_port: int
        """
        if self.local_vars_configuration.client_side_validation and ws_port is None:  # noqa: E501
            raise ValueError("Invalid value for `ws_port`, must not be `None`")  # noqa: E501

        self._ws_port = ws_port

    @property
    def ws_url(self):
        """Gets the ws_url of this WebrtcStream.  # noqa: E501


        :return: The ws_url of this WebrtcStream.  # noqa: E501
        :rtype: str
        """
        return self._ws_url

    @ws_url.setter
    def ws_url(self, ws_url):
        """Sets the ws_url of this WebrtcStream.


        :param ws_url: The ws_url of this WebrtcStream.  # noqa: E501
        :type ws_url: str
        """
        if self.local_vars_configuration.client_side_validation and ws_url is None:  # noqa: E501
            raise ValueError("Invalid value for `ws_url`, must not be `None`")  # noqa: E501

        self._ws_url = ws_url

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
        if not isinstance(other, WebrtcStream):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebrtcStream):
            return True

        return self.to_dict() != other.to_dict()
