# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.109.1
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


class StripeSubscriptionSchedule(object):
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
        'billing_thresholds': 'dict(str, object)',
        'canceled_at': 'datetime',
        'completed_at': 'datetime',
        'current_phase': 'dict(str, object)',
        'default_settings': 'dict(str, object)',
        'end_behavior': 'StripeSubscriptionScheduleEndBehavior',
        'phases': 'dict(str, object)',
        'released_at': 'datetime',
        'status': 'StripeSubscriptionScheduleStatus',
        'djstripe_owner_account': 'str',
        'customer': 'int',
        'released_subscription': 'int'
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
        'billing_thresholds': 'billing_thresholds',
        'canceled_at': 'canceled_at',
        'completed_at': 'completed_at',
        'current_phase': 'current_phase',
        'default_settings': 'default_settings',
        'end_behavior': 'end_behavior',
        'phases': 'phases',
        'released_at': 'released_at',
        'status': 'status',
        'djstripe_owner_account': 'djstripe_owner_account',
        'customer': 'customer',
        'released_subscription': 'released_subscription'
    }

    def __init__(self, djstripe_id=None, djstripe_created=None, djstripe_updated=None, id=None, livemode=None, created=None, metadata=None, description=None, billing_thresholds=None, canceled_at=None, completed_at=None, current_phase=None, default_settings=None, end_behavior=None, phases=None, released_at=None, status=None, djstripe_owner_account=None, customer=None, released_subscription=None, local_vars_configuration=None):  # noqa: E501
        """StripeSubscriptionSchedule - a model defined in OpenAPI"""  # noqa: E501
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
        self._billing_thresholds = None
        self._canceled_at = None
        self._completed_at = None
        self._current_phase = None
        self._default_settings = None
        self._end_behavior = None
        self._phases = None
        self._released_at = None
        self._status = None
        self._djstripe_owner_account = None
        self._customer = None
        self._released_subscription = None
        self.discriminator = None

        self.djstripe_id = djstripe_id
        self.djstripe_created = djstripe_created
        self.djstripe_updated = djstripe_updated
        self.id = id
        self.livemode = livemode
        self.created = created
        self.metadata = metadata
        self.description = description
        self.billing_thresholds = billing_thresholds
        self.canceled_at = canceled_at
        self.completed_at = completed_at
        self.current_phase = current_phase
        self.default_settings = default_settings
        self.end_behavior = end_behavior
        self.phases = phases
        self.released_at = released_at
        self.status = status
        self.djstripe_owner_account = djstripe_owner_account
        self.customer = customer
        self.released_subscription = released_subscription

    @property
    def djstripe_id(self):
        """Gets the djstripe_id of this StripeSubscriptionSchedule.  # noqa: E501


        :return: The djstripe_id of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: int
        """
        return self._djstripe_id

    @djstripe_id.setter
    def djstripe_id(self, djstripe_id):
        """Sets the djstripe_id of this StripeSubscriptionSchedule.


        :param djstripe_id: The djstripe_id of this StripeSubscriptionSchedule.  # noqa: E501
        :type djstripe_id: int
        """
        if self.local_vars_configuration.client_side_validation and djstripe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_id`, must not be `None`")  # noqa: E501

        self._djstripe_id = djstripe_id

    @property
    def djstripe_created(self):
        """Gets the djstripe_created of this StripeSubscriptionSchedule.  # noqa: E501


        :return: The djstripe_created of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_created

    @djstripe_created.setter
    def djstripe_created(self, djstripe_created):
        """Sets the djstripe_created of this StripeSubscriptionSchedule.


        :param djstripe_created: The djstripe_created of this StripeSubscriptionSchedule.  # noqa: E501
        :type djstripe_created: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_created is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_created`, must not be `None`")  # noqa: E501

        self._djstripe_created = djstripe_created

    @property
    def djstripe_updated(self):
        """Gets the djstripe_updated of this StripeSubscriptionSchedule.  # noqa: E501


        :return: The djstripe_updated of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_updated

    @djstripe_updated.setter
    def djstripe_updated(self, djstripe_updated):
        """Sets the djstripe_updated of this StripeSubscriptionSchedule.


        :param djstripe_updated: The djstripe_updated of this StripeSubscriptionSchedule.  # noqa: E501
        :type djstripe_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_updated`, must not be `None`")  # noqa: E501

        self._djstripe_updated = djstripe_updated

    @property
    def id(self):
        """Gets the id of this StripeSubscriptionSchedule.  # noqa: E501


        :return: The id of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StripeSubscriptionSchedule.


        :param id: The id of this StripeSubscriptionSchedule.  # noqa: E501
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
        """Gets the livemode of this StripeSubscriptionSchedule.  # noqa: E501

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :return: The livemode of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this StripeSubscriptionSchedule.

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :param livemode: The livemode of this StripeSubscriptionSchedule.  # noqa: E501
        :type livemode: bool
        """

        self._livemode = livemode

    @property
    def created(self):
        """Gets the created of this StripeSubscriptionSchedule.  # noqa: E501

        The datetime this object was created in stripe.  # noqa: E501

        :return: The created of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this StripeSubscriptionSchedule.

        The datetime this object was created in stripe.  # noqa: E501

        :param created: The created of this StripeSubscriptionSchedule.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def metadata(self):
        """Gets the metadata of this StripeSubscriptionSchedule.  # noqa: E501

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :return: The metadata of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this StripeSubscriptionSchedule.

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :param metadata: The metadata of this StripeSubscriptionSchedule.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this StripeSubscriptionSchedule.  # noqa: E501

        A description of this object.  # noqa: E501

        :return: The description of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StripeSubscriptionSchedule.

        A description of this object.  # noqa: E501

        :param description: The description of this StripeSubscriptionSchedule.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def billing_thresholds(self):
        """Gets the billing_thresholds of this StripeSubscriptionSchedule.  # noqa: E501

        Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period.  # noqa: E501

        :return: The billing_thresholds of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._billing_thresholds

    @billing_thresholds.setter
    def billing_thresholds(self, billing_thresholds):
        """Sets the billing_thresholds of this StripeSubscriptionSchedule.

        Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period.  # noqa: E501

        :param billing_thresholds: The billing_thresholds of this StripeSubscriptionSchedule.  # noqa: E501
        :type billing_thresholds: dict(str, object)
        """

        self._billing_thresholds = billing_thresholds

    @property
    def canceled_at(self):
        """Gets the canceled_at of this StripeSubscriptionSchedule.  # noqa: E501

        Time at which the subscription schedule was canceled.  # noqa: E501

        :return: The canceled_at of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._canceled_at

    @canceled_at.setter
    def canceled_at(self, canceled_at):
        """Sets the canceled_at of this StripeSubscriptionSchedule.

        Time at which the subscription schedule was canceled.  # noqa: E501

        :param canceled_at: The canceled_at of this StripeSubscriptionSchedule.  # noqa: E501
        :type canceled_at: datetime
        """

        self._canceled_at = canceled_at

    @property
    def completed_at(self):
        """Gets the completed_at of this StripeSubscriptionSchedule.  # noqa: E501

        Time at which the subscription schedule was completed.  # noqa: E501

        :return: The completed_at of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this StripeSubscriptionSchedule.

        Time at which the subscription schedule was completed.  # noqa: E501

        :param completed_at: The completed_at of this StripeSubscriptionSchedule.  # noqa: E501
        :type completed_at: datetime
        """

        self._completed_at = completed_at

    @property
    def current_phase(self):
        """Gets the current_phase of this StripeSubscriptionSchedule.  # noqa: E501

        Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`.  # noqa: E501

        :return: The current_phase of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._current_phase

    @current_phase.setter
    def current_phase(self, current_phase):
        """Sets the current_phase of this StripeSubscriptionSchedule.

        Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`.  # noqa: E501

        :param current_phase: The current_phase of this StripeSubscriptionSchedule.  # noqa: E501
        :type current_phase: dict(str, object)
        """

        self._current_phase = current_phase

    @property
    def default_settings(self):
        """Gets the default_settings of this StripeSubscriptionSchedule.  # noqa: E501

        Object representing the subscription schedule's default settings.  # noqa: E501

        :return: The default_settings of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._default_settings

    @default_settings.setter
    def default_settings(self, default_settings):
        """Sets the default_settings of this StripeSubscriptionSchedule.

        Object representing the subscription schedule's default settings.  # noqa: E501

        :param default_settings: The default_settings of this StripeSubscriptionSchedule.  # noqa: E501
        :type default_settings: dict(str, object)
        """

        self._default_settings = default_settings

    @property
    def end_behavior(self):
        """Gets the end_behavior of this StripeSubscriptionSchedule.  # noqa: E501

        Behavior of the subscription schedule and underlying subscription when it ends.  # noqa: E501

        :return: The end_behavior of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: StripeSubscriptionScheduleEndBehavior
        """
        return self._end_behavior

    @end_behavior.setter
    def end_behavior(self, end_behavior):
        """Sets the end_behavior of this StripeSubscriptionSchedule.

        Behavior of the subscription schedule and underlying subscription when it ends.  # noqa: E501

        :param end_behavior: The end_behavior of this StripeSubscriptionSchedule.  # noqa: E501
        :type end_behavior: StripeSubscriptionScheduleEndBehavior
        """

        self._end_behavior = end_behavior

    @property
    def phases(self):
        """Gets the phases of this StripeSubscriptionSchedule.  # noqa: E501

        Configuration for the subscription schedule's phases.  # noqa: E501

        :return: The phases of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._phases

    @phases.setter
    def phases(self, phases):
        """Sets the phases of this StripeSubscriptionSchedule.

        Configuration for the subscription schedule's phases.  # noqa: E501

        :param phases: The phases of this StripeSubscriptionSchedule.  # noqa: E501
        :type phases: dict(str, object)
        """

        self._phases = phases

    @property
    def released_at(self):
        """Gets the released_at of this StripeSubscriptionSchedule.  # noqa: E501

        Time at which the subscription schedule was released.  # noqa: E501

        :return: The released_at of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._released_at

    @released_at.setter
    def released_at(self, released_at):
        """Sets the released_at of this StripeSubscriptionSchedule.

        Time at which the subscription schedule was released.  # noqa: E501

        :param released_at: The released_at of this StripeSubscriptionSchedule.  # noqa: E501
        :type released_at: datetime
        """

        self._released_at = released_at

    @property
    def status(self):
        """Gets the status of this StripeSubscriptionSchedule.  # noqa: E501

        The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`.  # noqa: E501

        :return: The status of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: StripeSubscriptionScheduleStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StripeSubscriptionSchedule.

        The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`.  # noqa: E501

        :param status: The status of this StripeSubscriptionSchedule.  # noqa: E501
        :type status: StripeSubscriptionScheduleStatus
        """

        self._status = status

    @property
    def djstripe_owner_account(self):
        """Gets the djstripe_owner_account of this StripeSubscriptionSchedule.  # noqa: E501

        The Stripe Account this object belongs to.  # noqa: E501

        :return: The djstripe_owner_account of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._djstripe_owner_account

    @djstripe_owner_account.setter
    def djstripe_owner_account(self, djstripe_owner_account):
        """Sets the djstripe_owner_account of this StripeSubscriptionSchedule.

        The Stripe Account this object belongs to.  # noqa: E501

        :param djstripe_owner_account: The djstripe_owner_account of this StripeSubscriptionSchedule.  # noqa: E501
        :type djstripe_owner_account: str
        """

        self._djstripe_owner_account = djstripe_owner_account

    @property
    def customer(self):
        """Gets the customer of this StripeSubscriptionSchedule.  # noqa: E501

        The customer who owns the subscription schedule.  # noqa: E501

        :return: The customer of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: int
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this StripeSubscriptionSchedule.

        The customer who owns the subscription schedule.  # noqa: E501

        :param customer: The customer of this StripeSubscriptionSchedule.  # noqa: E501
        :type customer: int
        """
        if self.local_vars_configuration.client_side_validation and customer is None:  # noqa: E501
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def released_subscription(self):
        """Gets the released_subscription of this StripeSubscriptionSchedule.  # noqa: E501

        The subscription once managed by this subscription schedule (if it is released).  # noqa: E501

        :return: The released_subscription of this StripeSubscriptionSchedule.  # noqa: E501
        :rtype: int
        """
        return self._released_subscription

    @released_subscription.setter
    def released_subscription(self, released_subscription):
        """Sets the released_subscription of this StripeSubscriptionSchedule.

        The subscription once managed by this subscription schedule (if it is released).  # noqa: E501

        :param released_subscription: The released_subscription of this StripeSubscriptionSchedule.  # noqa: E501
        :type released_subscription: int
        """

        self._released_subscription = released_subscription

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
        if not isinstance(other, StripeSubscriptionSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StripeSubscriptionSchedule):
            return True

        return self.to_dict() != other.to_dict()
