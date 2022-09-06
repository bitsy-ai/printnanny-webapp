# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.107.0
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


class Order(object):
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
        'id': 'str',
        'created_dt': 'datetime',
        'products': 'list[Product]',
        'djstripe_customer': 'DjStripeCustomer',
        'djstripe_checkout_session': 'DjStripeCheckoutSession',
        'djstripe_payment_intent': 'DjStripePaymentIntent',
        'last_status': 'OrderStatus',
        'status_history': 'list[OrderStatus]',
        'email': 'str',
        'stripe_checkout_redirect_url': 'str',
        'stripe_checkout_session_data': 'dict(str, object)',
        'user': 'User'
    }

    attribute_map = {
        'id': 'id',
        'created_dt': 'created_dt',
        'products': 'products',
        'djstripe_customer': 'djstripe_customer',
        'djstripe_checkout_session': 'djstripe_checkout_session',
        'djstripe_payment_intent': 'djstripe_payment_intent',
        'last_status': 'last_status',
        'status_history': 'status_history',
        'email': 'email',
        'stripe_checkout_redirect_url': 'stripe_checkout_redirect_url',
        'stripe_checkout_session_data': 'stripe_checkout_session_data',
        'user': 'user'
    }

    def __init__(self, id=None, created_dt=None, products=None, djstripe_customer=None, djstripe_checkout_session=None, djstripe_payment_intent=None, last_status=None, status_history=None, email=None, stripe_checkout_redirect_url=None, stripe_checkout_session_data=None, user=None, local_vars_configuration=None):  # noqa: E501
        """Order - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_dt = None
        self._products = None
        self._djstripe_customer = None
        self._djstripe_checkout_session = None
        self._djstripe_payment_intent = None
        self._last_status = None
        self._status_history = None
        self._email = None
        self._stripe_checkout_redirect_url = None
        self._stripe_checkout_session_data = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.created_dt = created_dt
        self.products = products
        self.djstripe_customer = djstripe_customer
        self.djstripe_checkout_session = djstripe_checkout_session
        self.djstripe_payment_intent = djstripe_payment_intent
        self.last_status = last_status
        self.status_history = status_history
        self.email = email
        self.stripe_checkout_redirect_url = stripe_checkout_redirect_url
        self.stripe_checkout_session_data = stripe_checkout_session_data
        if user is not None:
            self.user = user

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501


        :return: The id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        :param id: The id of this Order.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this Order.  # noqa: E501


        :return: The created_dt of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this Order.


        :param created_dt: The created_dt of this Order.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def products(self):
        """Gets the products of this Order.  # noqa: E501


        :return: The products of this Order.  # noqa: E501
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Order.


        :param products: The products of this Order.  # noqa: E501
        :type products: list[Product]
        """
        if self.local_vars_configuration.client_side_validation and products is None:  # noqa: E501
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def djstripe_customer(self):
        """Gets the djstripe_customer of this Order.  # noqa: E501


        :return: The djstripe_customer of this Order.  # noqa: E501
        :rtype: DjStripeCustomer
        """
        return self._djstripe_customer

    @djstripe_customer.setter
    def djstripe_customer(self, djstripe_customer):
        """Sets the djstripe_customer of this Order.


        :param djstripe_customer: The djstripe_customer of this Order.  # noqa: E501
        :type djstripe_customer: DjStripeCustomer
        """

        self._djstripe_customer = djstripe_customer

    @property
    def djstripe_checkout_session(self):
        """Gets the djstripe_checkout_session of this Order.  # noqa: E501


        :return: The djstripe_checkout_session of this Order.  # noqa: E501
        :rtype: DjStripeCheckoutSession
        """
        return self._djstripe_checkout_session

    @djstripe_checkout_session.setter
    def djstripe_checkout_session(self, djstripe_checkout_session):
        """Sets the djstripe_checkout_session of this Order.


        :param djstripe_checkout_session: The djstripe_checkout_session of this Order.  # noqa: E501
        :type djstripe_checkout_session: DjStripeCheckoutSession
        """

        self._djstripe_checkout_session = djstripe_checkout_session

    @property
    def djstripe_payment_intent(self):
        """Gets the djstripe_payment_intent of this Order.  # noqa: E501


        :return: The djstripe_payment_intent of this Order.  # noqa: E501
        :rtype: DjStripePaymentIntent
        """
        return self._djstripe_payment_intent

    @djstripe_payment_intent.setter
    def djstripe_payment_intent(self, djstripe_payment_intent):
        """Sets the djstripe_payment_intent of this Order.


        :param djstripe_payment_intent: The djstripe_payment_intent of this Order.  # noqa: E501
        :type djstripe_payment_intent: DjStripePaymentIntent
        """

        self._djstripe_payment_intent = djstripe_payment_intent

    @property
    def last_status(self):
        """Gets the last_status of this Order.  # noqa: E501


        :return: The last_status of this Order.  # noqa: E501
        :rtype: OrderStatus
        """
        return self._last_status

    @last_status.setter
    def last_status(self, last_status):
        """Sets the last_status of this Order.


        :param last_status: The last_status of this Order.  # noqa: E501
        :type last_status: OrderStatus
        """
        if self.local_vars_configuration.client_side_validation and last_status is None:  # noqa: E501
            raise ValueError("Invalid value for `last_status`, must not be `None`")  # noqa: E501

        self._last_status = last_status

    @property
    def status_history(self):
        """Gets the status_history of this Order.  # noqa: E501


        :return: The status_history of this Order.  # noqa: E501
        :rtype: list[OrderStatus]
        """
        return self._status_history

    @status_history.setter
    def status_history(self, status_history):
        """Sets the status_history of this Order.


        :param status_history: The status_history of this Order.  # noqa: E501
        :type status_history: list[OrderStatus]
        """
        if self.local_vars_configuration.client_side_validation and status_history is None:  # noqa: E501
            raise ValueError("Invalid value for `status_history`, must not be `None`")  # noqa: E501

        self._status_history = status_history

    @property
    def email(self):
        """Gets the email of this Order.  # noqa: E501


        :return: The email of this Order.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Order.


        :param email: The email of this Order.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501

        self._email = email

    @property
    def stripe_checkout_redirect_url(self):
        """Gets the stripe_checkout_redirect_url of this Order.  # noqa: E501


        :return: The stripe_checkout_redirect_url of this Order.  # noqa: E501
        :rtype: str
        """
        return self._stripe_checkout_redirect_url

    @stripe_checkout_redirect_url.setter
    def stripe_checkout_redirect_url(self, stripe_checkout_redirect_url):
        """Sets the stripe_checkout_redirect_url of this Order.


        :param stripe_checkout_redirect_url: The stripe_checkout_redirect_url of this Order.  # noqa: E501
        :type stripe_checkout_redirect_url: str
        """
        if self.local_vars_configuration.client_side_validation and stripe_checkout_redirect_url is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_checkout_redirect_url`, must not be `None`")  # noqa: E501

        self._stripe_checkout_redirect_url = stripe_checkout_redirect_url

    @property
    def stripe_checkout_session_data(self):
        """Gets the stripe_checkout_session_data of this Order.  # noqa: E501


        :return: The stripe_checkout_session_data of this Order.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._stripe_checkout_session_data

    @stripe_checkout_session_data.setter
    def stripe_checkout_session_data(self, stripe_checkout_session_data):
        """Sets the stripe_checkout_session_data of this Order.


        :param stripe_checkout_session_data: The stripe_checkout_session_data of this Order.  # noqa: E501
        :type stripe_checkout_session_data: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and stripe_checkout_session_data is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_checkout_session_data`, must not be `None`")  # noqa: E501

        self._stripe_checkout_session_data = stripe_checkout_session_data

    @property
    def user(self):
        """Gets the user of this Order.  # noqa: E501


        :return: The user of this Order.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Order.


        :param user: The user of this Order.  # noqa: E501
        :type user: User
        """

        self._user = user

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
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()
