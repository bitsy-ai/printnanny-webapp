# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.99.7
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


class BillingSummary(object):
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
        'subscription': 'StripeSubscription',
        'customer': 'StripeCustomer',
        'user': 'User',
        'billing_portal_url': 'str'
    }

    attribute_map = {
        'subscription': 'subscription',
        'customer': 'customer',
        'user': 'user',
        'billing_portal_url': 'billing_portal_url'
    }

    def __init__(self, subscription=None, customer=None, user=None, billing_portal_url=None, local_vars_configuration=None):  # noqa: E501
        """BillingSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._subscription = None
        self._customer = None
        self._user = None
        self._billing_portal_url = None
        self.discriminator = None

        self.subscription = subscription
        self.customer = customer
        self.user = user
        self.billing_portal_url = billing_portal_url

    @property
    def subscription(self):
        """Gets the subscription of this BillingSummary.  # noqa: E501


        :return: The subscription of this BillingSummary.  # noqa: E501
        :rtype: StripeSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this BillingSummary.


        :param subscription: The subscription of this BillingSummary.  # noqa: E501
        :type subscription: StripeSubscription
        """
        if self.local_vars_configuration.client_side_validation and subscription is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription`, must not be `None`")  # noqa: E501

        self._subscription = subscription

    @property
    def customer(self):
        """Gets the customer of this BillingSummary.  # noqa: E501


        :return: The customer of this BillingSummary.  # noqa: E501
        :rtype: StripeCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this BillingSummary.


        :param customer: The customer of this BillingSummary.  # noqa: E501
        :type customer: StripeCustomer
        """
        if self.local_vars_configuration.client_side_validation and customer is None:  # noqa: E501
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def user(self):
        """Gets the user of this BillingSummary.  # noqa: E501


        :return: The user of this BillingSummary.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BillingSummary.


        :param user: The user of this BillingSummary.  # noqa: E501
        :type user: User
        """

        self._user = user

    @property
    def billing_portal_url(self):
        """Gets the billing_portal_url of this BillingSummary.  # noqa: E501


        :return: The billing_portal_url of this BillingSummary.  # noqa: E501
        :rtype: str
        """
        return self._billing_portal_url

    @billing_portal_url.setter
    def billing_portal_url(self, billing_portal_url):
        """Sets the billing_portal_url of this BillingSummary.


        :param billing_portal_url: The billing_portal_url of this BillingSummary.  # noqa: E501
        :type billing_portal_url: str
        """
        if self.local_vars_configuration.client_side_validation and billing_portal_url is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_portal_url`, must not be `None`")  # noqa: E501

        self._billing_portal_url = billing_portal_url

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
        if not isinstance(other, BillingSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingSummary):
            return True

        return self.to_dict() != other.to_dict()
