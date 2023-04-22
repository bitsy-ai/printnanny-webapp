# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.133.0
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


class NatsOrganizationUser(object):
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
        'organization': 'int',
        'creds': 'str',
        'json': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'app_name': 'app_name',
        'organization': 'organization',
        'creds': 'creds',
        'json': 'json'
    }

    def __init__(self, id=None, app_name=None, organization=None, creds=None, json=None, local_vars_configuration=None):  # noqa: E501
        """NatsOrganizationUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._app_name = None
        self._organization = None
        self._creds = None
        self._json = None
        self.discriminator = None

        self.id = id
        if app_name is not None:
            self.app_name = app_name
        self.organization = organization
        self.creds = creds
        if json is not None:
            self.json = json

    @property
    def id(self):
        """Gets the id of this NatsOrganizationUser.  # noqa: E501


        :return: The id of this NatsOrganizationUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NatsOrganizationUser.


        :param id: The id of this NatsOrganizationUser.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def app_name(self):
        """Gets the app_name of this NatsOrganizationUser.  # noqa: E501


        :return: The app_name of this NatsOrganizationUser.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this NatsOrganizationUser.


        :param app_name: The app_name of this NatsOrganizationUser.  # noqa: E501
        :type app_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                app_name is not None and len(app_name) > 255):
            raise ValueError("Invalid value for `app_name`, length must be less than or equal to `255`")  # noqa: E501

        self._app_name = app_name

    @property
    def organization(self):
        """Gets the organization of this NatsOrganizationUser.  # noqa: E501


        :return: The organization of this NatsOrganizationUser.  # noqa: E501
        :rtype: int
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this NatsOrganizationUser.


        :param organization: The organization of this NatsOrganizationUser.  # noqa: E501
        :type organization: int
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def creds(self):
        """Gets the creds of this NatsOrganizationUser.  # noqa: E501


        :return: The creds of this NatsOrganizationUser.  # noqa: E501
        :rtype: str
        """
        return self._creds

    @creds.setter
    def creds(self, creds):
        """Sets the creds of this NatsOrganizationUser.


        :param creds: The creds of this NatsOrganizationUser.  # noqa: E501
        :type creds: str
        """
        if self.local_vars_configuration.client_side_validation and creds is None:  # noqa: E501
            raise ValueError("Invalid value for `creds`, must not be `None`")  # noqa: E501

        self._creds = creds

    @property
    def json(self):
        """Gets the json of this NatsOrganizationUser.  # noqa: E501

        Output of `nsc describe account`  # noqa: E501

        :return: The json of this NatsOrganizationUser.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this NatsOrganizationUser.

        Output of `nsc describe account`  # noqa: E501

        :param json: The json of this NatsOrganizationUser.  # noqa: E501
        :type json: dict(str, object)
        """

        self._json = json

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
        if not isinstance(other, NatsOrganizationUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NatsOrganizationUser):
            return True

        return self.to_dict() != other.to_dict()
