# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.102.0
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


class StripePlan(object):
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
        'active': 'bool',
        'amount': 'str',
        'amount_decimal': 'str',
        'currency': 'str',
        'interval': 'IntervalEnum',
        'interval_count': 'int',
        'nickname': 'str',
        'tiers': 'dict(str, object)',
        'transform_usage': 'dict(str, object)',
        'trial_period_days': 'int',
        'usage_type': 'UsageTypeEnum',
        'djstripe_owner_account': 'str',
        'product': 'str'
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
        'active': 'active',
        'amount': 'amount',
        'amount_decimal': 'amount_decimal',
        'currency': 'currency',
        'interval': 'interval',
        'interval_count': 'interval_count',
        'nickname': 'nickname',
        'tiers': 'tiers',
        'transform_usage': 'transform_usage',
        'trial_period_days': 'trial_period_days',
        'usage_type': 'usage_type',
        'djstripe_owner_account': 'djstripe_owner_account',
        'product': 'product'
    }

    def __init__(self, djstripe_id=None, djstripe_created=None, djstripe_updated=None, id=None, livemode=None, created=None, metadata=None, description=None, active=None, amount=None, amount_decimal=None, currency=None, interval=None, interval_count=None, nickname=None, tiers=None, transform_usage=None, trial_period_days=None, usage_type=None, djstripe_owner_account=None, product=None, local_vars_configuration=None):  # noqa: E501
        """StripePlan - a model defined in OpenAPI"""  # noqa: E501
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
        self._active = None
        self._amount = None
        self._amount_decimal = None
        self._currency = None
        self._interval = None
        self._interval_count = None
        self._nickname = None
        self._tiers = None
        self._transform_usage = None
        self._trial_period_days = None
        self._usage_type = None
        self._djstripe_owner_account = None
        self._product = None
        self.discriminator = None

        self.djstripe_id = djstripe_id
        self.djstripe_created = djstripe_created
        self.djstripe_updated = djstripe_updated
        self.id = id
        self.livemode = livemode
        self.created = created
        self.metadata = metadata
        self.description = description
        self.active = active
        self.amount = amount
        self.amount_decimal = amount_decimal
        self.currency = currency
        self.interval = interval
        self.interval_count = interval_count
        if nickname is not None:
            self.nickname = nickname
        self.tiers = tiers
        self.transform_usage = transform_usage
        self.trial_period_days = trial_period_days
        self.usage_type = usage_type
        self.djstripe_owner_account = djstripe_owner_account
        self.product = product

    @property
    def djstripe_id(self):
        """Gets the djstripe_id of this StripePlan.  # noqa: E501


        :return: The djstripe_id of this StripePlan.  # noqa: E501
        :rtype: int
        """
        return self._djstripe_id

    @djstripe_id.setter
    def djstripe_id(self, djstripe_id):
        """Sets the djstripe_id of this StripePlan.


        :param djstripe_id: The djstripe_id of this StripePlan.  # noqa: E501
        :type djstripe_id: int
        """
        if self.local_vars_configuration.client_side_validation and djstripe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_id`, must not be `None`")  # noqa: E501

        self._djstripe_id = djstripe_id

    @property
    def djstripe_created(self):
        """Gets the djstripe_created of this StripePlan.  # noqa: E501


        :return: The djstripe_created of this StripePlan.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_created

    @djstripe_created.setter
    def djstripe_created(self, djstripe_created):
        """Sets the djstripe_created of this StripePlan.


        :param djstripe_created: The djstripe_created of this StripePlan.  # noqa: E501
        :type djstripe_created: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_created is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_created`, must not be `None`")  # noqa: E501

        self._djstripe_created = djstripe_created

    @property
    def djstripe_updated(self):
        """Gets the djstripe_updated of this StripePlan.  # noqa: E501


        :return: The djstripe_updated of this StripePlan.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_updated

    @djstripe_updated.setter
    def djstripe_updated(self, djstripe_updated):
        """Sets the djstripe_updated of this StripePlan.


        :param djstripe_updated: The djstripe_updated of this StripePlan.  # noqa: E501
        :type djstripe_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_updated`, must not be `None`")  # noqa: E501

        self._djstripe_updated = djstripe_updated

    @property
    def id(self):
        """Gets the id of this StripePlan.  # noqa: E501


        :return: The id of this StripePlan.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StripePlan.


        :param id: The id of this StripePlan.  # noqa: E501
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
        """Gets the livemode of this StripePlan.  # noqa: E501

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :return: The livemode of this StripePlan.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this StripePlan.

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :param livemode: The livemode of this StripePlan.  # noqa: E501
        :type livemode: bool
        """

        self._livemode = livemode

    @property
    def created(self):
        """Gets the created of this StripePlan.  # noqa: E501

        The datetime this object was created in stripe.  # noqa: E501

        :return: The created of this StripePlan.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this StripePlan.

        The datetime this object was created in stripe.  # noqa: E501

        :param created: The created of this StripePlan.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def metadata(self):
        """Gets the metadata of this StripePlan.  # noqa: E501

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :return: The metadata of this StripePlan.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this StripePlan.

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :param metadata: The metadata of this StripePlan.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this StripePlan.  # noqa: E501

        A description of this object.  # noqa: E501

        :return: The description of this StripePlan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StripePlan.

        A description of this object.  # noqa: E501

        :param description: The description of this StripePlan.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def active(self):
        """Gets the active of this StripePlan.  # noqa: E501

        Whether the plan can be used for new purchases.  # noqa: E501

        :return: The active of this StripePlan.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this StripePlan.

        Whether the plan can be used for new purchases.  # noqa: E501

        :param active: The active of this StripePlan.  # noqa: E501
        :type active: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def amount(self):
        """Gets the amount of this StripePlan.  # noqa: E501

        Amount (as decimal) to be charged on the interval specified.  # noqa: E501

        :return: The amount of this StripePlan.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this StripePlan.

        Amount (as decimal) to be charged on the interval specified.  # noqa: E501

        :param amount: The amount of this StripePlan.  # noqa: E501
        :type amount: str
        """
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and not re.search(r'^-?\d{0,9}(?:\.\d{0,2})?$', amount)):  # noqa: E501
            raise ValueError(r"Invalid value for `amount`, must be a follow pattern or equal to `/^-?\d{0,9}(?:\.\d{0,2})?$/`")  # noqa: E501

        self._amount = amount

    @property
    def amount_decimal(self):
        """Gets the amount_decimal of this StripePlan.  # noqa: E501

        The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places.  # noqa: E501

        :return: The amount_decimal of this StripePlan.  # noqa: E501
        :rtype: str
        """
        return self._amount_decimal

    @amount_decimal.setter
    def amount_decimal(self, amount_decimal):
        """Sets the amount_decimal of this StripePlan.

        The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places.  # noqa: E501

        :param amount_decimal: The amount_decimal of this StripePlan.  # noqa: E501
        :type amount_decimal: str
        """
        if (self.local_vars_configuration.client_side_validation and
                amount_decimal is not None and not re.search(r'^-?\d{0,7}(?:\.\d{0,12})?$', amount_decimal)):  # noqa: E501
            raise ValueError(r"Invalid value for `amount_decimal`, must be a follow pattern or equal to `/^-?\d{0,7}(?:\.\d{0,12})?$/`")  # noqa: E501

        self._amount_decimal = amount_decimal

    @property
    def currency(self):
        """Gets the currency of this StripePlan.  # noqa: E501

        Three-letter ISO currency code  # noqa: E501

        :return: The currency of this StripePlan.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this StripePlan.

        Three-letter ISO currency code  # noqa: E501

        :param currency: The currency of this StripePlan.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) > 3):
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501

        self._currency = currency

    @property
    def interval(self):
        """Gets the interval of this StripePlan.  # noqa: E501

        The frequency with which a subscription should be billed.  # noqa: E501

        :return: The interval of this StripePlan.  # noqa: E501
        :rtype: IntervalEnum
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this StripePlan.

        The frequency with which a subscription should be billed.  # noqa: E501

        :param interval: The interval of this StripePlan.  # noqa: E501
        :type interval: IntervalEnum
        """

        self._interval = interval

    @property
    def interval_count(self):
        """Gets the interval_count of this StripePlan.  # noqa: E501

        The number of intervals (specified in the interval property) between each subscription billing.  # noqa: E501

        :return: The interval_count of this StripePlan.  # noqa: E501
        :rtype: int
        """
        return self._interval_count

    @interval_count.setter
    def interval_count(self, interval_count):
        """Sets the interval_count of this StripePlan.

        The number of intervals (specified in the interval property) between each subscription billing.  # noqa: E501

        :param interval_count: The interval_count of this StripePlan.  # noqa: E501
        :type interval_count: int
        """
        if (self.local_vars_configuration.client_side_validation and
                interval_count is not None and interval_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `interval_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                interval_count is not None and interval_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `interval_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._interval_count = interval_count

    @property
    def nickname(self):
        """Gets the nickname of this StripePlan.  # noqa: E501

        A brief description of the plan, hidden from customers.  # noqa: E501

        :return: The nickname of this StripePlan.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this StripePlan.

        A brief description of the plan, hidden from customers.  # noqa: E501

        :param nickname: The nickname of this StripePlan.  # noqa: E501
        :type nickname: str
        """
        if (self.local_vars_configuration.client_side_validation and
                nickname is not None and len(nickname) > 5000):
            raise ValueError("Invalid value for `nickname`, length must be less than or equal to `5000`")  # noqa: E501

        self._nickname = nickname

    @property
    def tiers(self):
        """Gets the tiers of this StripePlan.  # noqa: E501

        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.  # noqa: E501

        :return: The tiers of this StripePlan.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this StripePlan.

        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.  # noqa: E501

        :param tiers: The tiers of this StripePlan.  # noqa: E501
        :type tiers: dict(str, object)
        """

        self._tiers = tiers

    @property
    def transform_usage(self):
        """Gets the transform_usage of this StripePlan.  # noqa: E501

        Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.  # noqa: E501

        :return: The transform_usage of this StripePlan.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._transform_usage

    @transform_usage.setter
    def transform_usage(self, transform_usage):
        """Sets the transform_usage of this StripePlan.

        Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.  # noqa: E501

        :param transform_usage: The transform_usage of this StripePlan.  # noqa: E501
        :type transform_usage: dict(str, object)
        """

        self._transform_usage = transform_usage

    @property
    def trial_period_days(self):
        """Gets the trial_period_days of this StripePlan.  # noqa: E501

        Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period.  # noqa: E501

        :return: The trial_period_days of this StripePlan.  # noqa: E501
        :rtype: int
        """
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, trial_period_days):
        """Sets the trial_period_days of this StripePlan.

        Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period.  # noqa: E501

        :param trial_period_days: The trial_period_days of this StripePlan.  # noqa: E501
        :type trial_period_days: int
        """
        if (self.local_vars_configuration.client_side_validation and
                trial_period_days is not None and trial_period_days > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `trial_period_days`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trial_period_days is not None and trial_period_days < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `trial_period_days`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._trial_period_days = trial_period_days

    @property
    def usage_type(self):
        """Gets the usage_type of this StripePlan.  # noqa: E501

        Configures how the quantity per period should be determined, can be either `metered` or `licensed`. `licensed` will automatically bill the `quantity` set for a plan when adding it to a subscription, `metered` will aggregate the total usage based on usage records. Defaults to `licensed`.  # noqa: E501

        :return: The usage_type of this StripePlan.  # noqa: E501
        :rtype: UsageTypeEnum
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this StripePlan.

        Configures how the quantity per period should be determined, can be either `metered` or `licensed`. `licensed` will automatically bill the `quantity` set for a plan when adding it to a subscription, `metered` will aggregate the total usage based on usage records. Defaults to `licensed`.  # noqa: E501

        :param usage_type: The usage_type of this StripePlan.  # noqa: E501
        :type usage_type: UsageTypeEnum
        """

        self._usage_type = usage_type

    @property
    def djstripe_owner_account(self):
        """Gets the djstripe_owner_account of this StripePlan.  # noqa: E501

        The Stripe Account this object belongs to.  # noqa: E501

        :return: The djstripe_owner_account of this StripePlan.  # noqa: E501
        :rtype: str
        """
        return self._djstripe_owner_account

    @djstripe_owner_account.setter
    def djstripe_owner_account(self, djstripe_owner_account):
        """Sets the djstripe_owner_account of this StripePlan.

        The Stripe Account this object belongs to.  # noqa: E501

        :param djstripe_owner_account: The djstripe_owner_account of this StripePlan.  # noqa: E501
        :type djstripe_owner_account: str
        """

        self._djstripe_owner_account = djstripe_owner_account

    @property
    def product(self):
        """Gets the product of this StripePlan.  # noqa: E501

        The product whose pricing this plan determines.  # noqa: E501

        :return: The product of this StripePlan.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this StripePlan.

        The product whose pricing this plan determines.  # noqa: E501

        :param product: The product of this StripePlan.  # noqa: E501
        :type product: str
        """

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
        if not isinstance(other, StripePlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StripePlan):
            return True

        return self.to_dict() != other.to_dict()
