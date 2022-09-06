# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.107.2
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


class DjStripePrice(object):
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
        'billing_scheme': 'StripeBillingScheme',
        'human_readable_price': 'str',
        'tiers_mode': 'StripePriceTiersMode',
        'djstripe_created': 'datetime',
        'djstripe_updated': 'datetime',
        'id': 'str',
        'livemode': 'bool',
        'created': 'datetime',
        'metadata': 'dict(str, object)',
        'description': 'str',
        'active': 'bool',
        'currency': 'str',
        'nickname': 'str',
        'recurring': 'dict(str, object)',
        'type': 'StripePriceType',
        'unit_amount': 'int',
        'unit_amount_decimal': 'str',
        'lookup_key': 'str',
        'tiers': 'dict(str, object)',
        'transform_quantity': 'dict(str, object)',
        'djstripe_owner_account': 'str',
        'product': 'str'
    }

    attribute_map = {
        'djstripe_id': 'djstripe_id',
        'billing_scheme': 'billing_scheme',
        'human_readable_price': 'human_readable_price',
        'tiers_mode': 'tiers_mode',
        'djstripe_created': 'djstripe_created',
        'djstripe_updated': 'djstripe_updated',
        'id': 'id',
        'livemode': 'livemode',
        'created': 'created',
        'metadata': 'metadata',
        'description': 'description',
        'active': 'active',
        'currency': 'currency',
        'nickname': 'nickname',
        'recurring': 'recurring',
        'type': 'type',
        'unit_amount': 'unit_amount',
        'unit_amount_decimal': 'unit_amount_decimal',
        'lookup_key': 'lookup_key',
        'tiers': 'tiers',
        'transform_quantity': 'transform_quantity',
        'djstripe_owner_account': 'djstripe_owner_account',
        'product': 'product'
    }

    def __init__(self, djstripe_id=None, billing_scheme=None, human_readable_price=None, tiers_mode=None, djstripe_created=None, djstripe_updated=None, id=None, livemode=None, created=None, metadata=None, description=None, active=None, currency=None, nickname=None, recurring=None, type=None, unit_amount=None, unit_amount_decimal=None, lookup_key=None, tiers=None, transform_quantity=None, djstripe_owner_account=None, product=None, local_vars_configuration=None):  # noqa: E501
        """DjStripePrice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._djstripe_id = None
        self._billing_scheme = None
        self._human_readable_price = None
        self._tiers_mode = None
        self._djstripe_created = None
        self._djstripe_updated = None
        self._id = None
        self._livemode = None
        self._created = None
        self._metadata = None
        self._description = None
        self._active = None
        self._currency = None
        self._nickname = None
        self._recurring = None
        self._type = None
        self._unit_amount = None
        self._unit_amount_decimal = None
        self._lookup_key = None
        self._tiers = None
        self._transform_quantity = None
        self._djstripe_owner_account = None
        self._product = None
        self.discriminator = None

        self.djstripe_id = djstripe_id
        self.billing_scheme = billing_scheme
        self.human_readable_price = human_readable_price
        self.tiers_mode = tiers_mode
        self.djstripe_created = djstripe_created
        self.djstripe_updated = djstripe_updated
        self.id = id
        self.livemode = livemode
        self.created = created
        self.metadata = metadata
        self.description = description
        self.active = active
        self.currency = currency
        if nickname is not None:
            self.nickname = nickname
        self.recurring = recurring
        self.type = type
        self.unit_amount = unit_amount
        self.unit_amount_decimal = unit_amount_decimal
        self.lookup_key = lookup_key
        self.tiers = tiers
        self.transform_quantity = transform_quantity
        self.djstripe_owner_account = djstripe_owner_account
        self.product = product

    @property
    def djstripe_id(self):
        """Gets the djstripe_id of this DjStripePrice.  # noqa: E501


        :return: The djstripe_id of this DjStripePrice.  # noqa: E501
        :rtype: int
        """
        return self._djstripe_id

    @djstripe_id.setter
    def djstripe_id(self, djstripe_id):
        """Sets the djstripe_id of this DjStripePrice.


        :param djstripe_id: The djstripe_id of this DjStripePrice.  # noqa: E501
        :type djstripe_id: int
        """
        if self.local_vars_configuration.client_side_validation and djstripe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_id`, must not be `None`")  # noqa: E501

        self._djstripe_id = djstripe_id

    @property
    def billing_scheme(self):
        """Gets the billing_scheme of this DjStripePrice.  # noqa: E501


        :return: The billing_scheme of this DjStripePrice.  # noqa: E501
        :rtype: StripeBillingScheme
        """
        return self._billing_scheme

    @billing_scheme.setter
    def billing_scheme(self, billing_scheme):
        """Sets the billing_scheme of this DjStripePrice.


        :param billing_scheme: The billing_scheme of this DjStripePrice.  # noqa: E501
        :type billing_scheme: StripeBillingScheme
        """
        if self.local_vars_configuration.client_side_validation and billing_scheme is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_scheme`, must not be `None`")  # noqa: E501

        self._billing_scheme = billing_scheme

    @property
    def human_readable_price(self):
        """Gets the human_readable_price of this DjStripePrice.  # noqa: E501


        :return: The human_readable_price of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._human_readable_price

    @human_readable_price.setter
    def human_readable_price(self, human_readable_price):
        """Sets the human_readable_price of this DjStripePrice.


        :param human_readable_price: The human_readable_price of this DjStripePrice.  # noqa: E501
        :type human_readable_price: str
        """
        if self.local_vars_configuration.client_side_validation and human_readable_price is None:  # noqa: E501
            raise ValueError("Invalid value for `human_readable_price`, must not be `None`")  # noqa: E501

        self._human_readable_price = human_readable_price

    @property
    def tiers_mode(self):
        """Gets the tiers_mode of this DjStripePrice.  # noqa: E501


        :return: The tiers_mode of this DjStripePrice.  # noqa: E501
        :rtype: StripePriceTiersMode
        """
        return self._tiers_mode

    @tiers_mode.setter
    def tiers_mode(self, tiers_mode):
        """Sets the tiers_mode of this DjStripePrice.


        :param tiers_mode: The tiers_mode of this DjStripePrice.  # noqa: E501
        :type tiers_mode: StripePriceTiersMode
        """
        if self.local_vars_configuration.client_side_validation and tiers_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `tiers_mode`, must not be `None`")  # noqa: E501

        self._tiers_mode = tiers_mode

    @property
    def djstripe_created(self):
        """Gets the djstripe_created of this DjStripePrice.  # noqa: E501


        :return: The djstripe_created of this DjStripePrice.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_created

    @djstripe_created.setter
    def djstripe_created(self, djstripe_created):
        """Sets the djstripe_created of this DjStripePrice.


        :param djstripe_created: The djstripe_created of this DjStripePrice.  # noqa: E501
        :type djstripe_created: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_created is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_created`, must not be `None`")  # noqa: E501

        self._djstripe_created = djstripe_created

    @property
    def djstripe_updated(self):
        """Gets the djstripe_updated of this DjStripePrice.  # noqa: E501


        :return: The djstripe_updated of this DjStripePrice.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_updated

    @djstripe_updated.setter
    def djstripe_updated(self, djstripe_updated):
        """Sets the djstripe_updated of this DjStripePrice.


        :param djstripe_updated: The djstripe_updated of this DjStripePrice.  # noqa: E501
        :type djstripe_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_updated`, must not be `None`")  # noqa: E501

        self._djstripe_updated = djstripe_updated

    @property
    def id(self):
        """Gets the id of this DjStripePrice.  # noqa: E501


        :return: The id of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DjStripePrice.


        :param id: The id of this DjStripePrice.  # noqa: E501
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
        """Gets the livemode of this DjStripePrice.  # noqa: E501

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :return: The livemode of this DjStripePrice.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this DjStripePrice.

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :param livemode: The livemode of this DjStripePrice.  # noqa: E501
        :type livemode: bool
        """

        self._livemode = livemode

    @property
    def created(self):
        """Gets the created of this DjStripePrice.  # noqa: E501

        The datetime this object was created in stripe.  # noqa: E501

        :return: The created of this DjStripePrice.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DjStripePrice.

        The datetime this object was created in stripe.  # noqa: E501

        :param created: The created of this DjStripePrice.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def metadata(self):
        """Gets the metadata of this DjStripePrice.  # noqa: E501

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :return: The metadata of this DjStripePrice.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DjStripePrice.

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :param metadata: The metadata of this DjStripePrice.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this DjStripePrice.  # noqa: E501

        A description of this object.  # noqa: E501

        :return: The description of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DjStripePrice.

        A description of this object.  # noqa: E501

        :param description: The description of this DjStripePrice.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def active(self):
        """Gets the active of this DjStripePrice.  # noqa: E501

        Whether the price can be used for new purchases.  # noqa: E501

        :return: The active of this DjStripePrice.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DjStripePrice.

        Whether the price can be used for new purchases.  # noqa: E501

        :param active: The active of this DjStripePrice.  # noqa: E501
        :type active: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def currency(self):
        """Gets the currency of this DjStripePrice.  # noqa: E501

        Three-letter ISO currency code  # noqa: E501

        :return: The currency of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this DjStripePrice.

        Three-letter ISO currency code  # noqa: E501

        :param currency: The currency of this DjStripePrice.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) > 3):
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501

        self._currency = currency

    @property
    def nickname(self):
        """Gets the nickname of this DjStripePrice.  # noqa: E501

        A brief description of the plan, hidden from customers.  # noqa: E501

        :return: The nickname of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this DjStripePrice.

        A brief description of the plan, hidden from customers.  # noqa: E501

        :param nickname: The nickname of this DjStripePrice.  # noqa: E501
        :type nickname: str
        """
        if (self.local_vars_configuration.client_side_validation and
                nickname is not None and len(nickname) > 250):
            raise ValueError("Invalid value for `nickname`, length must be less than or equal to `250`")  # noqa: E501

        self._nickname = nickname

    @property
    def recurring(self):
        """Gets the recurring of this DjStripePrice.  # noqa: E501

        The recurring components of a price such as `interval` and `usage_type`.  # noqa: E501

        :return: The recurring of this DjStripePrice.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """Sets the recurring of this DjStripePrice.

        The recurring components of a price such as `interval` and `usage_type`.  # noqa: E501

        :param recurring: The recurring of this DjStripePrice.  # noqa: E501
        :type recurring: dict(str, object)
        """

        self._recurring = recurring

    @property
    def type(self):
        """Gets the type of this DjStripePrice.  # noqa: E501

        Whether the price is for a one-time purchase or a recurring (subscription) purchase.  # noqa: E501

        :return: The type of this DjStripePrice.  # noqa: E501
        :rtype: StripePriceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DjStripePrice.

        Whether the price is for a one-time purchase or a recurring (subscription) purchase.  # noqa: E501

        :param type: The type of this DjStripePrice.  # noqa: E501
        :type type: StripePriceType
        """

        self._type = type

    @property
    def unit_amount(self):
        """Gets the unit_amount of this DjStripePrice.  # noqa: E501

        The unit amount in cents to be charged, represented as a whole integer if possible. Null if a sub-cent precision is required.  # noqa: E501

        :return: The unit_amount of this DjStripePrice.  # noqa: E501
        :rtype: int
        """
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        """Sets the unit_amount of this DjStripePrice.

        The unit amount in cents to be charged, represented as a whole integer if possible. Null if a sub-cent precision is required.  # noqa: E501

        :param unit_amount: The unit_amount of this DjStripePrice.  # noqa: E501
        :type unit_amount: int
        """
        if (self.local_vars_configuration.client_side_validation and
                unit_amount is not None and unit_amount > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `unit_amount`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unit_amount is not None and unit_amount < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `unit_amount`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._unit_amount = unit_amount

    @property
    def unit_amount_decimal(self):
        """Gets the unit_amount_decimal of this DjStripePrice.  # noqa: E501

        The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places.  # noqa: E501

        :return: The unit_amount_decimal of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._unit_amount_decimal

    @unit_amount_decimal.setter
    def unit_amount_decimal(self, unit_amount_decimal):
        """Sets the unit_amount_decimal of this DjStripePrice.

        The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places.  # noqa: E501

        :param unit_amount_decimal: The unit_amount_decimal of this DjStripePrice.  # noqa: E501
        :type unit_amount_decimal: str
        """
        if (self.local_vars_configuration.client_side_validation and
                unit_amount_decimal is not None and not re.search(r'^-?\d{0,7}(?:\.\d{0,12})?$', unit_amount_decimal)):  # noqa: E501
            raise ValueError(r"Invalid value for `unit_amount_decimal`, must be a follow pattern or equal to `/^-?\d{0,7}(?:\.\d{0,12})?$/`")  # noqa: E501

        self._unit_amount_decimal = unit_amount_decimal

    @property
    def lookup_key(self):
        """Gets the lookup_key of this DjStripePrice.  # noqa: E501

        A lookup key used to retrieve prices dynamically from a static string.  # noqa: E501

        :return: The lookup_key of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._lookup_key

    @lookup_key.setter
    def lookup_key(self, lookup_key):
        """Sets the lookup_key of this DjStripePrice.

        A lookup key used to retrieve prices dynamically from a static string.  # noqa: E501

        :param lookup_key: The lookup_key of this DjStripePrice.  # noqa: E501
        :type lookup_key: str
        """
        if (self.local_vars_configuration.client_side_validation and
                lookup_key is not None and len(lookup_key) > 250):
            raise ValueError("Invalid value for `lookup_key`, length must be less than or equal to `250`")  # noqa: E501

        self._lookup_key = lookup_key

    @property
    def tiers(self):
        """Gets the tiers of this DjStripePrice.  # noqa: E501

        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.  # noqa: E501

        :return: The tiers of this DjStripePrice.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this DjStripePrice.

        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.  # noqa: E501

        :param tiers: The tiers of this DjStripePrice.  # noqa: E501
        :type tiers: dict(str, object)
        """

        self._tiers = tiers

    @property
    def transform_quantity(self):
        """Gets the transform_quantity of this DjStripePrice.  # noqa: E501

        Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.  # noqa: E501

        :return: The transform_quantity of this DjStripePrice.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._transform_quantity

    @transform_quantity.setter
    def transform_quantity(self, transform_quantity):
        """Sets the transform_quantity of this DjStripePrice.

        Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.  # noqa: E501

        :param transform_quantity: The transform_quantity of this DjStripePrice.  # noqa: E501
        :type transform_quantity: dict(str, object)
        """

        self._transform_quantity = transform_quantity

    @property
    def djstripe_owner_account(self):
        """Gets the djstripe_owner_account of this DjStripePrice.  # noqa: E501

        The Stripe Account this object belongs to.  # noqa: E501

        :return: The djstripe_owner_account of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._djstripe_owner_account

    @djstripe_owner_account.setter
    def djstripe_owner_account(self, djstripe_owner_account):
        """Sets the djstripe_owner_account of this DjStripePrice.

        The Stripe Account this object belongs to.  # noqa: E501

        :param djstripe_owner_account: The djstripe_owner_account of this DjStripePrice.  # noqa: E501
        :type djstripe_owner_account: str
        """

        self._djstripe_owner_account = djstripe_owner_account

    @property
    def product(self):
        """Gets the product of this DjStripePrice.  # noqa: E501

        The product this price is associated with.  # noqa: E501

        :return: The product of this DjStripePrice.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this DjStripePrice.

        The product this price is associated with.  # noqa: E501

        :param product: The product of this DjStripePrice.  # noqa: E501
        :type product: str
        """
        if self.local_vars_configuration.client_side_validation and product is None:  # noqa: E501
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

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
        if not isinstance(other, DjStripePrice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DjStripePrice):
            return True

        return self.to_dict() != other.to_dict()
