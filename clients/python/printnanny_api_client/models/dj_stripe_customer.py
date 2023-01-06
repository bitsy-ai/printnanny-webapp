# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.119.5
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


class DjStripeCustomer(object):
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
        'djstripe_created': 'datetime',
        'djstripe_updated': 'datetime',
        'id': 'str',
        'livemode': 'bool',
        'created': 'datetime',
        'metadata': 'dict(str, object)',
        'description': 'str',
        'address': 'dict(str, object)',
        'balance': 'int',
        'currency': 'str',
        'delinquent': 'bool',
        'deleted': 'bool',
        'coupon_start': 'datetime',
        'coupon_end': 'datetime',
        'email': 'str',
        'invoice_prefix': 'str',
        'invoice_settings': 'dict(str, object)',
        'name': 'str',
        'phone': 'str',
        'preferred_locales': 'dict(str, object)',
        'shipping': 'dict(str, object)',
        'tax_exempt': 'StripeCustomerTaxExempt',
        'date_purged': 'datetime',
        'djstripe_owner_account': 'str',
        'default_source': 'str',
        'coupon': 'int',
        'default_payment_method': 'str',
        'subscriber': 'int'
    }

    attribute_map = {
        'djstripe_id': 'djstripe_id',
        'djstripe_created': 'djstripe_created',
        'djstripe_updated': 'djstripe_updated',
        'id': 'id',
        'livemode': 'livemode',
        'created': 'created',
        'metadata': 'metadata',
        'description': 'description',
        'address': 'address',
        'balance': 'balance',
        'currency': 'currency',
        'delinquent': 'delinquent',
        'deleted': 'deleted',
        'coupon_start': 'coupon_start',
        'coupon_end': 'coupon_end',
        'email': 'email',
        'invoice_prefix': 'invoice_prefix',
        'invoice_settings': 'invoice_settings',
        'name': 'name',
        'phone': 'phone',
        'preferred_locales': 'preferred_locales',
        'shipping': 'shipping',
        'tax_exempt': 'tax_exempt',
        'date_purged': 'date_purged',
        'djstripe_owner_account': 'djstripe_owner_account',
        'default_source': 'default_source',
        'coupon': 'coupon',
        'default_payment_method': 'default_payment_method',
        'subscriber': 'subscriber'
    }

    def __init__(self, djstripe_id=None, djstripe_created=None, djstripe_updated=None, id=None, livemode=None, created=None, metadata=None, description=None, address=None, balance=None, currency=None, delinquent=None, deleted=None, coupon_start=None, coupon_end=None, email=None, invoice_prefix=None, invoice_settings=None, name=None, phone=None, preferred_locales=None, shipping=None, tax_exempt=None, date_purged=None, djstripe_owner_account=None, default_source=None, coupon=None, default_payment_method=None, subscriber=None, local_vars_configuration=None):  # noqa: E501
        """DjStripeCustomer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._djstripe_id = None
        self._djstripe_created = None
        self._djstripe_updated = None
        self._id = None
        self._livemode = None
        self._created = None
        self._metadata = None
        self._description = None
        self._address = None
        self._balance = None
        self._currency = None
        self._delinquent = None
        self._deleted = None
        self._coupon_start = None
        self._coupon_end = None
        self._email = None
        self._invoice_prefix = None
        self._invoice_settings = None
        self._name = None
        self._phone = None
        self._preferred_locales = None
        self._shipping = None
        self._tax_exempt = None
        self._date_purged = None
        self._djstripe_owner_account = None
        self._default_source = None
        self._coupon = None
        self._default_payment_method = None
        self._subscriber = None
        self.discriminator = None

        self.djstripe_id = djstripe_id
        self.djstripe_created = djstripe_created
        self.djstripe_updated = djstripe_updated
        self.id = id
        self.livemode = livemode
        self.created = created
        self.metadata = metadata
        self.description = description
        self.address = address
        self.balance = balance
        if currency is not None:
            self.currency = currency
        self.delinquent = delinquent
        self.deleted = deleted
        self.coupon_start = coupon_start
        self.coupon_end = coupon_end
        if email is not None:
            self.email = email
        if invoice_prefix is not None:
            self.invoice_prefix = invoice_prefix
        self.invoice_settings = invoice_settings
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        self.preferred_locales = preferred_locales
        self.shipping = shipping
        self.tax_exempt = tax_exempt
        self.date_purged = date_purged
        self.djstripe_owner_account = djstripe_owner_account
        self.default_source = default_source
        self.coupon = coupon
        self.default_payment_method = default_payment_method
        self.subscriber = subscriber

    @property
    def djstripe_id(self):
        """Gets the djstripe_id of this DjStripeCustomer.  # noqa: E501


        :return: The djstripe_id of this DjStripeCustomer.  # noqa: E501
        :rtype: int
        """
        return self._djstripe_id

    @djstripe_id.setter
    def djstripe_id(self, djstripe_id):
        """Sets the djstripe_id of this DjStripeCustomer.


        :param djstripe_id: The djstripe_id of this DjStripeCustomer.  # noqa: E501
        :type djstripe_id: int
        """
        if self.local_vars_configuration.client_side_validation and djstripe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_id`, must not be `None`")  # noqa: E501

        self._djstripe_id = djstripe_id

    @property
    def djstripe_created(self):
        """Gets the djstripe_created of this DjStripeCustomer.  # noqa: E501


        :return: The djstripe_created of this DjStripeCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_created

    @djstripe_created.setter
    def djstripe_created(self, djstripe_created):
        """Sets the djstripe_created of this DjStripeCustomer.


        :param djstripe_created: The djstripe_created of this DjStripeCustomer.  # noqa: E501
        :type djstripe_created: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_created is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_created`, must not be `None`")  # noqa: E501

        self._djstripe_created = djstripe_created

    @property
    def djstripe_updated(self):
        """Gets the djstripe_updated of this DjStripeCustomer.  # noqa: E501


        :return: The djstripe_updated of this DjStripeCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_updated

    @djstripe_updated.setter
    def djstripe_updated(self, djstripe_updated):
        """Sets the djstripe_updated of this DjStripeCustomer.


        :param djstripe_updated: The djstripe_updated of this DjStripeCustomer.  # noqa: E501
        :type djstripe_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_updated`, must not be `None`")  # noqa: E501

        self._djstripe_updated = djstripe_updated

    @property
    def id(self):
        """Gets the id of this DjStripeCustomer.  # noqa: E501


        :return: The id of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DjStripeCustomer.


        :param id: The id of this DjStripeCustomer.  # noqa: E501
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
        """Gets the livemode of this DjStripeCustomer.  # noqa: E501

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :return: The livemode of this DjStripeCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this DjStripeCustomer.

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :param livemode: The livemode of this DjStripeCustomer.  # noqa: E501
        :type livemode: bool
        """

        self._livemode = livemode

    @property
    def created(self):
        """Gets the created of this DjStripeCustomer.  # noqa: E501

        The datetime this object was created in stripe.  # noqa: E501

        :return: The created of this DjStripeCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DjStripeCustomer.

        The datetime this object was created in stripe.  # noqa: E501

        :param created: The created of this DjStripeCustomer.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def metadata(self):
        """Gets the metadata of this DjStripeCustomer.  # noqa: E501

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :return: The metadata of this DjStripeCustomer.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DjStripeCustomer.

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :param metadata: The metadata of this DjStripeCustomer.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this DjStripeCustomer.  # noqa: E501

        A description of this object.  # noqa: E501

        :return: The description of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DjStripeCustomer.

        A description of this object.  # noqa: E501

        :param description: The description of this DjStripeCustomer.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def address(self):
        """Gets the address of this DjStripeCustomer.  # noqa: E501

        The customer's address.  # noqa: E501

        :return: The address of this DjStripeCustomer.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DjStripeCustomer.

        The customer's address.  # noqa: E501

        :param address: The address of this DjStripeCustomer.  # noqa: E501
        :type address: dict(str, object)
        """

        self._address = address

    @property
    def balance(self):
        """Gets the balance of this DjStripeCustomer.  # noqa: E501

        Current balance (in cents), if any, being stored on the customer's account. If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account for recurring billing purposes (i.e., subscriptions, invoices, invoice items).  # noqa: E501

        :return: The balance of this DjStripeCustomer.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this DjStripeCustomer.

        Current balance (in cents), if any, being stored on the customer's account. If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account for recurring billing purposes (i.e., subscriptions, invoices, invoice items).  # noqa: E501

        :param balance: The balance of this DjStripeCustomer.  # noqa: E501
        :type balance: int
        """
        if (self.local_vars_configuration.client_side_validation and
                balance is not None and balance > 9223372036854775807):  # noqa: E501
            raise ValueError("Invalid value for `balance`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                balance is not None and balance < -9223372036854775808):  # noqa: E501
            raise ValueError("Invalid value for `balance`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._balance = balance

    @property
    def currency(self):
        """Gets the currency of this DjStripeCustomer.  # noqa: E501

        The currency the customer can be charged in for recurring billing purposes  # noqa: E501

        :return: The currency of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this DjStripeCustomer.

        The currency the customer can be charged in for recurring billing purposes  # noqa: E501

        :param currency: The currency of this DjStripeCustomer.  # noqa: E501
        :type currency: str
        """
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) > 3):
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501

        self._currency = currency

    @property
    def delinquent(self):
        """Gets the delinquent of this DjStripeCustomer.  # noqa: E501

        Whether or not the latest charge for the customer's latest invoice has failed.  # noqa: E501

        :return: The delinquent of this DjStripeCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._delinquent

    @delinquent.setter
    def delinquent(self, delinquent):
        """Sets the delinquent of this DjStripeCustomer.

        Whether or not the latest charge for the customer's latest invoice has failed.  # noqa: E501

        :param delinquent: The delinquent of this DjStripeCustomer.  # noqa: E501
        :type delinquent: bool
        """

        self._delinquent = delinquent

    @property
    def deleted(self):
        """Gets the deleted of this DjStripeCustomer.  # noqa: E501

        Whether the Customer instance has been deleted upstream in Stripe or not.  # noqa: E501

        :return: The deleted of this DjStripeCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DjStripeCustomer.

        Whether the Customer instance has been deleted upstream in Stripe or not.  # noqa: E501

        :param deleted: The deleted of this DjStripeCustomer.  # noqa: E501
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def coupon_start(self):
        """Gets the coupon_start of this DjStripeCustomer.  # noqa: E501

        If a coupon is present, the date at which it was applied.  # noqa: E501

        :return: The coupon_start of this DjStripeCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._coupon_start

    @coupon_start.setter
    def coupon_start(self, coupon_start):
        """Sets the coupon_start of this DjStripeCustomer.

        If a coupon is present, the date at which it was applied.  # noqa: E501

        :param coupon_start: The coupon_start of this DjStripeCustomer.  # noqa: E501
        :type coupon_start: datetime
        """
        if self.local_vars_configuration.client_side_validation and coupon_start is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_start`, must not be `None`")  # noqa: E501

        self._coupon_start = coupon_start

    @property
    def coupon_end(self):
        """Gets the coupon_end of this DjStripeCustomer.  # noqa: E501

        If a coupon is present and has a limited duration, the date that the discount will end.  # noqa: E501

        :return: The coupon_end of this DjStripeCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._coupon_end

    @coupon_end.setter
    def coupon_end(self, coupon_end):
        """Sets the coupon_end of this DjStripeCustomer.

        If a coupon is present and has a limited duration, the date that the discount will end.  # noqa: E501

        :param coupon_end: The coupon_end of this DjStripeCustomer.  # noqa: E501
        :type coupon_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and coupon_end is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_end`, must not be `None`")  # noqa: E501

        self._coupon_end = coupon_end

    @property
    def email(self):
        """Gets the email of this DjStripeCustomer.  # noqa: E501


        :return: The email of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DjStripeCustomer.


        :param email: The email of this DjStripeCustomer.  # noqa: E501
        :type email: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 5000):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `5000`")  # noqa: E501

        self._email = email

    @property
    def invoice_prefix(self):
        """Gets the invoice_prefix of this DjStripeCustomer.  # noqa: E501

        The prefix for the customer used to generate unique invoice numbers.  # noqa: E501

        :return: The invoice_prefix of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._invoice_prefix

    @invoice_prefix.setter
    def invoice_prefix(self, invoice_prefix):
        """Sets the invoice_prefix of this DjStripeCustomer.

        The prefix for the customer used to generate unique invoice numbers.  # noqa: E501

        :param invoice_prefix: The invoice_prefix of this DjStripeCustomer.  # noqa: E501
        :type invoice_prefix: str
        """
        if (self.local_vars_configuration.client_side_validation and
                invoice_prefix is not None and len(invoice_prefix) > 255):
            raise ValueError("Invalid value for `invoice_prefix`, length must be less than or equal to `255`")  # noqa: E501

        self._invoice_prefix = invoice_prefix

    @property
    def invoice_settings(self):
        """Gets the invoice_settings of this DjStripeCustomer.  # noqa: E501

        The customer's default invoice settings.  # noqa: E501

        :return: The invoice_settings of this DjStripeCustomer.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._invoice_settings

    @invoice_settings.setter
    def invoice_settings(self, invoice_settings):
        """Sets the invoice_settings of this DjStripeCustomer.

        The customer's default invoice settings.  # noqa: E501

        :param invoice_settings: The invoice_settings of this DjStripeCustomer.  # noqa: E501
        :type invoice_settings: dict(str, object)
        """

        self._invoice_settings = invoice_settings

    @property
    def name(self):
        """Gets the name of this DjStripeCustomer.  # noqa: E501

        The customer's full name or business name.  # noqa: E501

        :return: The name of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DjStripeCustomer.

        The customer's full name or business name.  # noqa: E501

        :param name: The name of this DjStripeCustomer.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 5000):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `5000`")  # noqa: E501

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this DjStripeCustomer.  # noqa: E501

        The customer's phone number.  # noqa: E501

        :return: The phone of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this DjStripeCustomer.

        The customer's phone number.  # noqa: E501

        :param phone: The phone of this DjStripeCustomer.  # noqa: E501
        :type phone: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone is not None and len(phone) > 5000):
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `5000`")  # noqa: E501

        self._phone = phone

    @property
    def preferred_locales(self):
        """Gets the preferred_locales of this DjStripeCustomer.  # noqa: E501

        The customer's preferred locales (languages), ordered by preference.  # noqa: E501

        :return: The preferred_locales of this DjStripeCustomer.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._preferred_locales

    @preferred_locales.setter
    def preferred_locales(self, preferred_locales):
        """Sets the preferred_locales of this DjStripeCustomer.

        The customer's preferred locales (languages), ordered by preference.  # noqa: E501

        :param preferred_locales: The preferred_locales of this DjStripeCustomer.  # noqa: E501
        :type preferred_locales: dict(str, object)
        """

        self._preferred_locales = preferred_locales

    @property
    def shipping(self):
        """Gets the shipping of this DjStripeCustomer.  # noqa: E501

        Shipping information associated with the customer.  # noqa: E501

        :return: The shipping of this DjStripeCustomer.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this DjStripeCustomer.

        Shipping information associated with the customer.  # noqa: E501

        :param shipping: The shipping of this DjStripeCustomer.  # noqa: E501
        :type shipping: dict(str, object)
        """

        self._shipping = shipping

    @property
    def tax_exempt(self):
        """Gets the tax_exempt of this DjStripeCustomer.  # noqa: E501

        Describes the customer's tax exemption status. When set to reverse, invoice and receipt PDFs include the text \"Reverse charge\".  # noqa: E501

        :return: The tax_exempt of this DjStripeCustomer.  # noqa: E501
        :rtype: StripeCustomerTaxExempt
        """
        return self._tax_exempt

    @tax_exempt.setter
    def tax_exempt(self, tax_exempt):
        """Sets the tax_exempt of this DjStripeCustomer.

        Describes the customer's tax exemption status. When set to reverse, invoice and receipt PDFs include the text \"Reverse charge\".  # noqa: E501

        :param tax_exempt: The tax_exempt of this DjStripeCustomer.  # noqa: E501
        :type tax_exempt: StripeCustomerTaxExempt
        """

        self._tax_exempt = tax_exempt

    @property
    def date_purged(self):
        """Gets the date_purged of this DjStripeCustomer.  # noqa: E501


        :return: The date_purged of this DjStripeCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._date_purged

    @date_purged.setter
    def date_purged(self, date_purged):
        """Sets the date_purged of this DjStripeCustomer.


        :param date_purged: The date_purged of this DjStripeCustomer.  # noqa: E501
        :type date_purged: datetime
        """
        if self.local_vars_configuration.client_side_validation and date_purged is None:  # noqa: E501
            raise ValueError("Invalid value for `date_purged`, must not be `None`")  # noqa: E501

        self._date_purged = date_purged

    @property
    def djstripe_owner_account(self):
        """Gets the djstripe_owner_account of this DjStripeCustomer.  # noqa: E501

        The Stripe Account this object belongs to.  # noqa: E501

        :return: The djstripe_owner_account of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._djstripe_owner_account

    @djstripe_owner_account.setter
    def djstripe_owner_account(self, djstripe_owner_account):
        """Sets the djstripe_owner_account of this DjStripeCustomer.

        The Stripe Account this object belongs to.  # noqa: E501

        :param djstripe_owner_account: The djstripe_owner_account of this DjStripeCustomer.  # noqa: E501
        :type djstripe_owner_account: str
        """

        self._djstripe_owner_account = djstripe_owner_account

    @property
    def default_source(self):
        """Gets the default_source of this DjStripeCustomer.  # noqa: E501


        :return: The default_source of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._default_source

    @default_source.setter
    def default_source(self, default_source):
        """Sets the default_source of this DjStripeCustomer.


        :param default_source: The default_source of this DjStripeCustomer.  # noqa: E501
        :type default_source: str
        """

        self._default_source = default_source

    @property
    def coupon(self):
        """Gets the coupon of this DjStripeCustomer.  # noqa: E501


        :return: The coupon of this DjStripeCustomer.  # noqa: E501
        :rtype: int
        """
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        """Sets the coupon of this DjStripeCustomer.


        :param coupon: The coupon of this DjStripeCustomer.  # noqa: E501
        :type coupon: int
        """

        self._coupon = coupon

    @property
    def default_payment_method(self):
        """Gets the default_payment_method of this DjStripeCustomer.  # noqa: E501

        default payment method used for subscriptions and invoices for the customer.  # noqa: E501

        :return: The default_payment_method of this DjStripeCustomer.  # noqa: E501
        :rtype: str
        """
        return self._default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, default_payment_method):
        """Sets the default_payment_method of this DjStripeCustomer.

        default payment method used for subscriptions and invoices for the customer.  # noqa: E501

        :param default_payment_method: The default_payment_method of this DjStripeCustomer.  # noqa: E501
        :type default_payment_method: str
        """

        self._default_payment_method = default_payment_method

    @property
    def subscriber(self):
        """Gets the subscriber of this DjStripeCustomer.  # noqa: E501


        :return: The subscriber of this DjStripeCustomer.  # noqa: E501
        :rtype: int
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """Sets the subscriber of this DjStripeCustomer.


        :param subscriber: The subscriber of this DjStripeCustomer.  # noqa: E501
        :type subscriber: int
        """

        self._subscriber = subscriber

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
        if not isinstance(other, DjStripeCustomer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DjStripeCustomer):
            return True

        return self.to_dict() != other.to_dict()
