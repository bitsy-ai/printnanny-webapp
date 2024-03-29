# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
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


class PiNatsAppRequest(object):
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
        'app_name': 'str',
        'json': 'dict(str, object)',
        'pi': 'int',
        'organization': 'NatsOrganizationRequest',
        'organization_user': 'int'
    }

    attribute_map = {
        'app_name': 'app_name',
        'json': 'json',
        'pi': 'pi',
        'organization': 'organization',
        'organization_user': 'organization_user'
    }

    def __init__(self, app_name=None, json=None, pi=None, organization=None, organization_user=None, local_vars_configuration=None):  # noqa: E501
        """PiNatsAppRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._app_name = None
        self._json = None
        self._pi = None
        self._organization = None
        self._organization_user = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if json is not None:
            self.json = json
        self.pi = pi
        self.organization = organization
        self.organization_user = organization_user

    @property
    def app_name(self):
        """Gets the app_name of this PiNatsAppRequest.  # noqa: E501


        :return: The app_name of this PiNatsAppRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this PiNatsAppRequest.


        :param app_name: The app_name of this PiNatsAppRequest.  # noqa: E501
        :type app_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                app_name is not None and len(app_name) > 255):
            raise ValueError("Invalid value for `app_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                app_name is not None and len(app_name) < 1):
            raise ValueError("Invalid value for `app_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._app_name = app_name

    @property
    def json(self):
        """Gets the json of this PiNatsAppRequest.  # noqa: E501

        Output of `nsc describe account`  # noqa: E501

        :return: The json of this PiNatsAppRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this PiNatsAppRequest.

        Output of `nsc describe account`  # noqa: E501

        :param json: The json of this PiNatsAppRequest.  # noqa: E501
        :type json: dict(str, object)
        """

        self._json = json

    @property
    def pi(self):
        """Gets the pi of this PiNatsAppRequest.  # noqa: E501


        :return: The pi of this PiNatsAppRequest.  # noqa: E501
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        """Sets the pi of this PiNatsAppRequest.


        :param pi: The pi of this PiNatsAppRequest.  # noqa: E501
        :type pi: int
        """
        if self.local_vars_configuration.client_side_validation and pi is None:  # noqa: E501
            raise ValueError("Invalid value for `pi`, must not be `None`")  # noqa: E501

        self._pi = pi

    @property
    def organization(self):
        """Gets the organization of this PiNatsAppRequest.  # noqa: E501


        :return: The organization of this PiNatsAppRequest.  # noqa: E501
        :rtype: NatsOrganizationRequest
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this PiNatsAppRequest.


        :param organization: The organization of this PiNatsAppRequest.  # noqa: E501
        :type organization: NatsOrganizationRequest
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def organization_user(self):
        """Gets the organization_user of this PiNatsAppRequest.  # noqa: E501


        :return: The organization_user of this PiNatsAppRequest.  # noqa: E501
        :rtype: int
        """
        return self._organization_user

    @organization_user.setter
    def organization_user(self, organization_user):
        """Sets the organization_user of this PiNatsAppRequest.


        :param organization_user: The organization_user of this PiNatsAppRequest.  # noqa: E501
        :type organization_user: int
        """
        if self.local_vars_configuration.client_side_validation and organization_user is None:  # noqa: E501
            raise ValueError("Invalid value for `organization_user`, must not be `None`")  # noqa: E501

        self._organization_user = organization_user

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
        if not isinstance(other, PiNatsAppRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PiNatsAppRequest):
            return True

        return self.to_dict() != other.to_dict()
