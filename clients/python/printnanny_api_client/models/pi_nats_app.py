# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.113.0
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


class PiNatsApp(object):
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
        'app_name': 'str',
        'json': 'dict(str, object)',
        'pi': 'int',
        'organization': 'NatsOrganization',
        'organization_user': 'int',
        'nats_server_uri': 'str',
        'nats_ws_uri': 'str',
        'nats_subject_pattern': 'str',
        'nats_subject_pattern_template': 'str'
    }

    attribute_map = {
        'id': 'id',
        'app_name': 'app_name',
        'json': 'json',
        'pi': 'pi',
        'organization': 'organization',
        'organization_user': 'organization_user',
        'nats_server_uri': 'nats_server_uri',
        'nats_ws_uri': 'nats_ws_uri',
        'nats_subject_pattern': 'nats_subject_pattern',
        'nats_subject_pattern_template': 'nats_subject_pattern_template'
    }

    def __init__(self, id=None, app_name=None, json=None, pi=None, organization=None, organization_user=None, nats_server_uri=None, nats_ws_uri=None, nats_subject_pattern=None, nats_subject_pattern_template=None, local_vars_configuration=None):  # noqa: E501
        """PiNatsApp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._app_name = None
        self._json = None
        self._pi = None
        self._organization = None
        self._organization_user = None
        self._nats_server_uri = None
        self._nats_ws_uri = None
        self._nats_subject_pattern = None
        self._nats_subject_pattern_template = None
        self.discriminator = None

        self.id = id
        if app_name is not None:
            self.app_name = app_name
        if json is not None:
            self.json = json
        self.pi = pi
        self.organization = organization
        self.organization_user = organization_user
        self.nats_server_uri = nats_server_uri
        self.nats_ws_uri = nats_ws_uri
        self.nats_subject_pattern = nats_subject_pattern
        self.nats_subject_pattern_template = nats_subject_pattern_template

    @property
    def id(self):
        """Gets the id of this PiNatsApp.  # noqa: E501


        :return: The id of this PiNatsApp.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PiNatsApp.


        :param id: The id of this PiNatsApp.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def app_name(self):
        """Gets the app_name of this PiNatsApp.  # noqa: E501


        :return: The app_name of this PiNatsApp.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this PiNatsApp.


        :param app_name: The app_name of this PiNatsApp.  # noqa: E501
        :type app_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                app_name is not None and len(app_name) > 255):
            raise ValueError("Invalid value for `app_name`, length must be less than or equal to `255`")  # noqa: E501

        self._app_name = app_name

    @property
    def json(self):
        """Gets the json of this PiNatsApp.  # noqa: E501

        Output of `nsc describe account`  # noqa: E501

        :return: The json of this PiNatsApp.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this PiNatsApp.

        Output of `nsc describe account`  # noqa: E501

        :param json: The json of this PiNatsApp.  # noqa: E501
        :type json: dict(str, object)
        """

        self._json = json

    @property
    def pi(self):
        """Gets the pi of this PiNatsApp.  # noqa: E501


        :return: The pi of this PiNatsApp.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PiNatsApp.


        :param pi: The pi of this PiNatsApp.  # noqa: E501
        :type pi: int
        """
        if self.local_vars_configuration.client_side_validation and pi is None:  # noqa: E501
            raise ValueError("Invalid value for `pi`, must not be `None`")  # noqa: E501

        self._pi = pi

    @property
    def organization(self):
        """Gets the organization of this PiNatsApp.  # noqa: E501


        :return: The organization of this PiNatsApp.  # noqa: E501
        :rtype: NatsOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this PiNatsApp.


        :param organization: The organization of this PiNatsApp.  # noqa: E501
        :type organization: NatsOrganization
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def organization_user(self):
        """Gets the organization_user of this PiNatsApp.  # noqa: E501


        :return: The organization_user of this PiNatsApp.  # noqa: E501
        :rtype: int
        """
        return self._organization_user

    @organization_user.setter
    def organization_user(self, organization_user):
        """Sets the organization_user of this PiNatsApp.


        :param organization_user: The organization_user of this PiNatsApp.  # noqa: E501
        :type organization_user: int
        """
        if self.local_vars_configuration.client_side_validation and organization_user is None:  # noqa: E501
            raise ValueError("Invalid value for `organization_user`, must not be `None`")  # noqa: E501

        self._organization_user = organization_user

    @property
    def nats_server_uri(self):
        """Gets the nats_server_uri of this PiNatsApp.  # noqa: E501


        :return: The nats_server_uri of this PiNatsApp.  # noqa: E501
        :rtype: str
        """
        return self._nats_server_uri

    @nats_server_uri.setter
    def nats_server_uri(self, nats_server_uri):
        """Sets the nats_server_uri of this PiNatsApp.


        :param nats_server_uri: The nats_server_uri of this PiNatsApp.  # noqa: E501
        :type nats_server_uri: str
        """
        if self.local_vars_configuration.client_side_validation and nats_server_uri is None:  # noqa: E501
            raise ValueError("Invalid value for `nats_server_uri`, must not be `None`")  # noqa: E501

        self._nats_server_uri = nats_server_uri

    @property
    def nats_ws_uri(self):
        """Gets the nats_ws_uri of this PiNatsApp.  # noqa: E501


        :return: The nats_ws_uri of this PiNatsApp.  # noqa: E501
        :rtype: str
        """
        return self._nats_ws_uri

    @nats_ws_uri.setter
    def nats_ws_uri(self, nats_ws_uri):
        """Sets the nats_ws_uri of this PiNatsApp.


        :param nats_ws_uri: The nats_ws_uri of this PiNatsApp.  # noqa: E501
        :type nats_ws_uri: str
        """
        if self.local_vars_configuration.client_side_validation and nats_ws_uri is None:  # noqa: E501
            raise ValueError("Invalid value for `nats_ws_uri`, must not be `None`")  # noqa: E501

        self._nats_ws_uri = nats_ws_uri

    @property
    def nats_subject_pattern(self):
        """Gets the nats_subject_pattern of this PiNatsApp.  # noqa: E501


        :return: The nats_subject_pattern of this PiNatsApp.  # noqa: E501
        :rtype: str
        """
        return self._nats_subject_pattern

    @nats_subject_pattern.setter
    def nats_subject_pattern(self, nats_subject_pattern):
        """Sets the nats_subject_pattern of this PiNatsApp.


        :param nats_subject_pattern: The nats_subject_pattern of this PiNatsApp.  # noqa: E501
        :type nats_subject_pattern: str
        """
        if self.local_vars_configuration.client_side_validation and nats_subject_pattern is None:  # noqa: E501
            raise ValueError("Invalid value for `nats_subject_pattern`, must not be `None`")  # noqa: E501

        self._nats_subject_pattern = nats_subject_pattern

    @property
    def nats_subject_pattern_template(self):
        """Gets the nats_subject_pattern_template of this PiNatsApp.  # noqa: E501


        :return: The nats_subject_pattern_template of this PiNatsApp.  # noqa: E501
        :rtype: str
        """
        return self._nats_subject_pattern_template

    @nats_subject_pattern_template.setter
    def nats_subject_pattern_template(self, nats_subject_pattern_template):
        """Sets the nats_subject_pattern_template of this PiNatsApp.


        :param nats_subject_pattern_template: The nats_subject_pattern_template of this PiNatsApp.  # noqa: E501
        :type nats_subject_pattern_template: str
        """
        if self.local_vars_configuration.client_side_validation and nats_subject_pattern_template is None:  # noqa: E501
            raise ValueError("Invalid value for `nats_subject_pattern_template`, must not be `None`")  # noqa: E501

        self._nats_subject_pattern_template = nats_subject_pattern_template

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
        if not isinstance(other, PiNatsApp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PiNatsApp):
            return True

        return self.to_dict() != other.to_dict()
