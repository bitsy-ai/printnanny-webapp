# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.0
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


class DjStripeCheckoutSession(object):
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
        'djstripe_id': 'int',
        'billing_address_collection': 'StripeSessionBillingAddressCollection',
        'mode': 'StripeSessionMode',
        'submit_type': 'StripeSubmitTypeStatus',
        'djstripe_created': 'datetime',
        'djstripe_updated': 'datetime',
        'id': 'str',
        'livemode': 'bool',
        'created': 'datetime',
        'metadata': 'dict(str, object)',
        'description': 'str',
        'cancel_url': 'str',
        'client_reference_id': 'str',
        'customer_email': 'str',
        'display_items': 'dict(str, object)',
        'locale': 'str',
        'payment_method_types': 'dict(str, object)',
        'success_url': 'str',
        'djstripe_owner_account': 'str',
        'customer': 'str',
        'payment_intent': 'str',
        'subscription': 'str'
    }

    attribute_map = {
        'djstripe_id': 'djstripe_id',
        'billing_address_collection': 'billing_address_collection',
        'mode': 'mode',
        'submit_type': 'submit_type',
        'djstripe_created': 'djstripe_created',
        'djstripe_updated': 'djstripe_updated',
        'id': 'id',
        'livemode': 'livemode',
        'created': 'created',
        'metadata': 'metadata',
        'description': 'description',
        'cancel_url': 'cancel_url',
        'client_reference_id': 'client_reference_id',
        'customer_email': 'customer_email',
        'display_items': 'display_items',
        'locale': 'locale',
        'payment_method_types': 'payment_method_types',
        'success_url': 'success_url',
        'djstripe_owner_account': 'djstripe_owner_account',
        'customer': 'customer',
        'payment_intent': 'payment_intent',
        'subscription': 'subscription'
    }

    def __init__(self, djstripe_id=None, billing_address_collection=None, mode=None, submit_type=None, djstripe_created=None, djstripe_updated=None, id=None, livemode=None, created=None, metadata=None, description=None, cancel_url=None, client_reference_id=None, customer_email=None, display_items=None, locale=None, payment_method_types=None, success_url=None, djstripe_owner_account=None, customer=None, payment_intent=None, subscription=None, local_vars_configuration=None):  # noqa: E501
        """DjStripeCheckoutSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._djstripe_id = None
        self._billing_address_collection = None
        self._mode = None
        self._submit_type = None
        self._djstripe_created = None
        self._djstripe_updated = None
        self._id = None
        self._livemode = None
        self._created = None
        self._metadata = None
        self._description = None
        self._cancel_url = None
        self._client_reference_id = None
        self._customer_email = None
        self._display_items = None
        self._locale = None
        self._payment_method_types = None
        self._success_url = None
        self._djstripe_owner_account = None
        self._customer = None
        self._payment_intent = None
        self._subscription = None
        self.discriminator = None

        self.djstripe_id = djstripe_id
        self.billing_address_collection = billing_address_collection
        self.mode = mode
        self.submit_type = submit_type
        self.djstripe_created = djstripe_created
        self.djstripe_updated = djstripe_updated
        self.id = id
        self.livemode = livemode
        self.created = created
        self.metadata = metadata
        self.description = description
        if cancel_url is not None:
            self.cancel_url = cancel_url
        if client_reference_id is not None:
            self.client_reference_id = client_reference_id
        if customer_email is not None:
            self.customer_email = customer_email
        self.display_items = display_items
        if locale is not None:
            self.locale = locale
        self.payment_method_types = payment_method_types
        if success_url is not None:
            self.success_url = success_url
        self.djstripe_owner_account = djstripe_owner_account
        self.customer = customer
        self.payment_intent = payment_intent
        self.subscription = subscription

    @property
    def djstripe_id(self):
        """Gets the djstripe_id of this DjStripeCheckoutSession.  # noqa: E501


        :return: The djstripe_id of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: int
        """
        return self._djstripe_id

    @djstripe_id.setter
    def djstripe_id(self, djstripe_id):
        """Sets the djstripe_id of this DjStripeCheckoutSession.


        :param djstripe_id: The djstripe_id of this DjStripeCheckoutSession.  # noqa: E501
        :type djstripe_id: int
        """
        if self.local_vars_configuration.client_side_validation and djstripe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_id`, must not be `None`")  # noqa: E501

        self._djstripe_id = djstripe_id

    @property
    def billing_address_collection(self):
        """Gets the billing_address_collection of this DjStripeCheckoutSession.  # noqa: E501


        :return: The billing_address_collection of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: StripeSessionBillingAddressCollection
        """
        return self._billing_address_collection

    @billing_address_collection.setter
    def billing_address_collection(self, billing_address_collection):
        """Sets the billing_address_collection of this DjStripeCheckoutSession.


        :param billing_address_collection: The billing_address_collection of this DjStripeCheckoutSession.  # noqa: E501
        :type billing_address_collection: StripeSessionBillingAddressCollection
        """
        if self.local_vars_configuration.client_side_validation and billing_address_collection is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_address_collection`, must not be `None`")  # noqa: E501

        self._billing_address_collection = billing_address_collection

    @property
    def mode(self):
        """Gets the mode of this DjStripeCheckoutSession.  # noqa: E501


        :return: The mode of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: StripeSessionMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DjStripeCheckoutSession.


        :param mode: The mode of this DjStripeCheckoutSession.  # noqa: E501
        :type mode: StripeSessionMode
        """
        if self.local_vars_configuration.client_side_validation and mode is None:  # noqa: E501
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def submit_type(self):
        """Gets the submit_type of this DjStripeCheckoutSession.  # noqa: E501


        :return: The submit_type of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: StripeSubmitTypeStatus
        """
        return self._submit_type

    @submit_type.setter
    def submit_type(self, submit_type):
        """Sets the submit_type of this DjStripeCheckoutSession.


        :param submit_type: The submit_type of this DjStripeCheckoutSession.  # noqa: E501
        :type submit_type: StripeSubmitTypeStatus
        """
        if self.local_vars_configuration.client_side_validation and submit_type is None:  # noqa: E501
            raise ValueError("Invalid value for `submit_type`, must not be `None`")  # noqa: E501

        self._submit_type = submit_type

    @property
    def djstripe_created(self):
        """Gets the djstripe_created of this DjStripeCheckoutSession.  # noqa: E501


        :return: The djstripe_created of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_created

    @djstripe_created.setter
    def djstripe_created(self, djstripe_created):
        """Sets the djstripe_created of this DjStripeCheckoutSession.


        :param djstripe_created: The djstripe_created of this DjStripeCheckoutSession.  # noqa: E501
        :type djstripe_created: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_created is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_created`, must not be `None`")  # noqa: E501

        self._djstripe_created = djstripe_created

    @property
    def djstripe_updated(self):
        """Gets the djstripe_updated of this DjStripeCheckoutSession.  # noqa: E501


        :return: The djstripe_updated of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_updated

    @djstripe_updated.setter
    def djstripe_updated(self, djstripe_updated):
        """Sets the djstripe_updated of this DjStripeCheckoutSession.


        :param djstripe_updated: The djstripe_updated of this DjStripeCheckoutSession.  # noqa: E501
        :type djstripe_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_updated`, must not be `None`")  # noqa: E501

        self._djstripe_updated = djstripe_updated

    @property
    def id(self):
        """Gets the id of this DjStripeCheckoutSession.  # noqa: E501


        :return: The id of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DjStripeCheckoutSession.


        :param id: The id of this DjStripeCheckoutSession.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id

    @property
    def livemode(self):
        """Gets the livemode of this DjStripeCheckoutSession.  # noqa: E501

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :return: The livemode of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this DjStripeCheckoutSession.

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :param livemode: The livemode of this DjStripeCheckoutSession.  # noqa: E501
        :type livemode: bool
        """

        self._livemode = livemode

    @property
    def created(self):
        """Gets the created of this DjStripeCheckoutSession.  # noqa: E501

        The datetime this object was created in stripe.  # noqa: E501

        :return: The created of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DjStripeCheckoutSession.

        The datetime this object was created in stripe.  # noqa: E501

        :param created: The created of this DjStripeCheckoutSession.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def metadata(self):
        """Gets the metadata of this DjStripeCheckoutSession.  # noqa: E501

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :return: The metadata of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DjStripeCheckoutSession.

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :param metadata: The metadata of this DjStripeCheckoutSession.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this DjStripeCheckoutSession.  # noqa: E501

        A description of this object.  # noqa: E501

        :return: The description of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DjStripeCheckoutSession.

        A description of this object.  # noqa: E501

        :param description: The description of this DjStripeCheckoutSession.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def cancel_url(self):
        """Gets the cancel_url of this DjStripeCheckoutSession.  # noqa: E501

        The URL the customer will be directed to if theydecide to cancel payment and return to your website.  # noqa: E501

        :return: The cancel_url of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this DjStripeCheckoutSession.

        The URL the customer will be directed to if theydecide to cancel payment and return to your website.  # noqa: E501

        :param cancel_url: The cancel_url of this DjStripeCheckoutSession.  # noqa: E501
        :type cancel_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cancel_url is not None and len(cancel_url) > 5000):
            raise ValueError("Invalid value for `cancel_url`, length must be less than or equal to `5000`")  # noqa: E501

        self._cancel_url = cancel_url

    @property
    def client_reference_id(self):
        """Gets the client_reference_id of this DjStripeCheckoutSession.  # noqa: E501

        A unique string to reference the Checkout Session.This can be a customer ID, a cart ID, or similar, andcan be used to reconcile the session with your internal systems.  # noqa: E501

        :return: The client_reference_id of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._client_reference_id

    @client_reference_id.setter
    def client_reference_id(self, client_reference_id):
        """Sets the client_reference_id of this DjStripeCheckoutSession.

        A unique string to reference the Checkout Session.This can be a customer ID, a cart ID, or similar, andcan be used to reconcile the session with your internal systems.  # noqa: E501

        :param client_reference_id: The client_reference_id of this DjStripeCheckoutSession.  # noqa: E501
        :type client_reference_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                client_reference_id is not None and len(client_reference_id) > 5000):
            raise ValueError("Invalid value for `client_reference_id`, length must be less than or equal to `5000`")  # noqa: E501

        self._client_reference_id = client_reference_id

    @property
    def customer_email(self):
        """Gets the customer_email of this DjStripeCheckoutSession.  # noqa: E501

        If provided, this value will be used when the Customer object is created.  # noqa: E501

        :return: The customer_email of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email):
        """Sets the customer_email of this DjStripeCheckoutSession.

        If provided, this value will be used when the Customer object is created.  # noqa: E501

        :param customer_email: The customer_email of this DjStripeCheckoutSession.  # noqa: E501
        :type customer_email: str
        """
        if (self.local_vars_configuration.client_side_validation and
                customer_email is not None and len(customer_email) > 255):
            raise ValueError("Invalid value for `customer_email`, length must be less than or equal to `255`")  # noqa: E501

        self._customer_email = customer_email

    @property
    def display_items(self):
        """Gets the display_items of this DjStripeCheckoutSession.  # noqa: E501

        The line items, plans, or SKUs purchased by the customer.  # noqa: E501

        :return: The display_items of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._display_items

    @display_items.setter
    def display_items(self, display_items):
        """Sets the display_items of this DjStripeCheckoutSession.

        The line items, plans, or SKUs purchased by the customer.  # noqa: E501

        :param display_items: The display_items of this DjStripeCheckoutSession.  # noqa: E501
        :type display_items: dict(str, object)
        """

        self._display_items = display_items

    @property
    def locale(self):
        """Gets the locale of this DjStripeCheckoutSession.  # noqa: E501

        The IETF language tag of the locale Checkout is displayed in.If blank or auto, the browser's locale is used.  # noqa: E501

        :return: The locale of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this DjStripeCheckoutSession.

        The IETF language tag of the locale Checkout is displayed in.If blank or auto, the browser's locale is used.  # noqa: E501

        :param locale: The locale of this DjStripeCheckoutSession.  # noqa: E501
        :type locale: str
        """
        if (self.local_vars_configuration.client_side_validation and
                locale is not None and len(locale) > 255):
            raise ValueError("Invalid value for `locale`, length must be less than or equal to `255`")  # noqa: E501

        self._locale = locale

    @property
    def payment_method_types(self):
        """Gets the payment_method_types of this DjStripeCheckoutSession.  # noqa: E501

        The list of payment method types (e.g. card) that this Checkout Session is allowed to accept.  # noqa: E501

        :return: The payment_method_types of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._payment_method_types

    @payment_method_types.setter
    def payment_method_types(self, payment_method_types):
        """Sets the payment_method_types of this DjStripeCheckoutSession.

        The list of payment method types (e.g. card) that this Checkout Session is allowed to accept.  # noqa: E501

        :param payment_method_types: The payment_method_types of this DjStripeCheckoutSession.  # noqa: E501
        :type payment_method_types: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and payment_method_types is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_method_types`, must not be `None`")  # noqa: E501

        self._payment_method_types = payment_method_types

    @property
    def success_url(self):
        """Gets the success_url of this DjStripeCheckoutSession.  # noqa: E501

        The URL the customer will be directed to after the payment or subscriptioncreation is successful.  # noqa: E501

        :return: The success_url of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """Sets the success_url of this DjStripeCheckoutSession.

        The URL the customer will be directed to after the payment or subscriptioncreation is successful.  # noqa: E501

        :param success_url: The success_url of this DjStripeCheckoutSession.  # noqa: E501
        :type success_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                success_url is not None and len(success_url) > 5000):
            raise ValueError("Invalid value for `success_url`, length must be less than or equal to `5000`")  # noqa: E501

        self._success_url = success_url

    @property
    def djstripe_owner_account(self):
        """Gets the djstripe_owner_account of this DjStripeCheckoutSession.  # noqa: E501

        The Stripe Account this object belongs to.  # noqa: E501

        :return: The djstripe_owner_account of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._djstripe_owner_account

    @djstripe_owner_account.setter
    def djstripe_owner_account(self, djstripe_owner_account):
        """Sets the djstripe_owner_account of this DjStripeCheckoutSession.

        The Stripe Account this object belongs to.  # noqa: E501

        :param djstripe_owner_account: The djstripe_owner_account of this DjStripeCheckoutSession.  # noqa: E501
        :type djstripe_owner_account: str
        """

        self._djstripe_owner_account = djstripe_owner_account

    @property
    def customer(self):
        """Gets the customer of this DjStripeCheckoutSession.  # noqa: E501

        Customer this Checkout is for if one exists.  # noqa: E501

        :return: The customer of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this DjStripeCheckoutSession.

        Customer this Checkout is for if one exists.  # noqa: E501

        :param customer: The customer of this DjStripeCheckoutSession.  # noqa: E501
        :type customer: str
        """

        self._customer = customer

    @property
    def payment_intent(self):
        """Gets the payment_intent of this DjStripeCheckoutSession.  # noqa: E501

        PaymentIntent created if SKUs or line items were provided.  # noqa: E501

        :return: The payment_intent of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._payment_intent

    @payment_intent.setter
    def payment_intent(self, payment_intent):
        """Sets the payment_intent of this DjStripeCheckoutSession.

        PaymentIntent created if SKUs or line items were provided.  # noqa: E501

        :param payment_intent: The payment_intent of this DjStripeCheckoutSession.  # noqa: E501
        :type payment_intent: str
        """

        self._payment_intent = payment_intent

    @property
    def subscription(self):
        """Gets the subscription of this DjStripeCheckoutSession.  # noqa: E501

        Subscription created if one or more plans were provided.  # noqa: E501

        :return: The subscription of this DjStripeCheckoutSession.  # noqa: E501
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this DjStripeCheckoutSession.

        Subscription created if one or more plans were provided.  # noqa: E501

        :param subscription: The subscription of this DjStripeCheckoutSession.  # noqa: E501
        :type subscription: str
        """

        self._subscription = subscription

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
        if not isinstance(other, DjStripeCheckoutSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DjStripeCheckoutSession):
            return True

        return self.to_dict() != other.to_dict()
