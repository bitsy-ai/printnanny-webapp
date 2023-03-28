# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.131.2
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


class OrderCheckout(object):
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
        'items': 'list[OrderItem]',
        'email': 'str',
        'stripe_checkout_redirect_url': 'str',
        'stripe_checkout_session_id': 'str'
    }

    attribute_map = {
        'items': 'items',
        'email': 'email',
        'stripe_checkout_redirect_url': 'stripe_checkout_redirect_url',
        'stripe_checkout_session_id': 'stripe_checkout_session_id'
    }

    def __init__(self, items=None, email=None, stripe_checkout_redirect_url=None, stripe_checkout_session_id=None, local_vars_configuration=None):  # noqa: E501
        """OrderCheckout - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._items = None
        self._email = None
        self._stripe_checkout_redirect_url = None
        self._stripe_checkout_session_id = None
        self.discriminator = None

        self.items = items
        self.email = email
        self.stripe_checkout_redirect_url = stripe_checkout_redirect_url
        self.stripe_checkout_session_id = stripe_checkout_session_id

    @property
    def items(self):
        """Gets the items of this OrderCheckout.  # noqa: E501


        :return: The items of this OrderCheckout.  # noqa: E501
        :rtype: list[OrderItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this OrderCheckout.


        :param items: The items of this OrderCheckout.  # noqa: E501
        :type items: list[OrderItem]
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def email(self):
        """Gets the email of this OrderCheckout.  # noqa: E501


        :return: The email of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OrderCheckout.


        :param email: The email of this OrderCheckout.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def stripe_checkout_redirect_url(self):
        """Gets the stripe_checkout_redirect_url of this OrderCheckout.  # noqa: E501


        :return: The stripe_checkout_redirect_url of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._stripe_checkout_redirect_url

    @stripe_checkout_redirect_url.setter
    def stripe_checkout_redirect_url(self, stripe_checkout_redirect_url):
        """Sets the stripe_checkout_redirect_url of this OrderCheckout.


        :param stripe_checkout_redirect_url: The stripe_checkout_redirect_url of this OrderCheckout.  # noqa: E501
        :type stripe_checkout_redirect_url: str
        """
        if self.local_vars_configuration.client_side_validation and stripe_checkout_redirect_url is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_checkout_redirect_url`, must not be `None`")  # noqa: E501

        self._stripe_checkout_redirect_url = stripe_checkout_redirect_url

    @property
    def stripe_checkout_session_id(self):
        """Gets the stripe_checkout_session_id of this OrderCheckout.  # noqa: E501


        :return: The stripe_checkout_session_id of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._stripe_checkout_session_id

    @stripe_checkout_session_id.setter
    def stripe_checkout_session_id(self, stripe_checkout_session_id):
        """Sets the stripe_checkout_session_id of this OrderCheckout.


        :param stripe_checkout_session_id: The stripe_checkout_session_id of this OrderCheckout.  # noqa: E501
        :type stripe_checkout_session_id: str
        """
        if self.local_vars_configuration.client_side_validation and stripe_checkout_session_id is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_checkout_session_id`, must not be `None`")  # noqa: E501

        self._stripe_checkout_session_id = stripe_checkout_session_id

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
        if not isinstance(other, OrderCheckout):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderCheckout):
            return True

        return self.to_dict() != other.to_dict()
