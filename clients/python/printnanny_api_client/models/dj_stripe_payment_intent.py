import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stripe_confirmation_method import StripeConfirmationMethod
from ..models.stripe_intent_usage import StripeIntentUsage
from ..models.stripe_payment_intent_cancellation_reason import StripePaymentIntentCancellationReason
from ..models.stripe_payment_intent_status import StripePaymentIntentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dj_stripe_charge import DjStripeCharge
    from ..models.dj_stripe_payment_intent_last_payment_error import DjStripePaymentIntentLastPaymentError
    from ..models.dj_stripe_payment_intent_metadata import DjStripePaymentIntentMetadata
    from ..models.dj_stripe_payment_intent_next_action import DjStripePaymentIntentNextAction
    from ..models.dj_stripe_payment_intent_payment_method_types import DjStripePaymentIntentPaymentMethodTypes
    from ..models.dj_stripe_payment_intent_shipping import DjStripePaymentIntentShipping
    from ..models.dj_stripe_payment_intent_transfer_data import DjStripePaymentIntentTransferData


T = TypeVar("T", bound="DjStripePaymentIntent")


@attr.s(auto_attribs=True)
class DjStripePaymentIntent:
    """
    Attributes:
        djstripe_id (int):
        cancellation_reason (StripePaymentIntentCancellationReason):
        charges (List['DjStripeCharge']):
        setup_future_usage (StripeIntentUsage):
        djstripe_created (datetime.datetime):
        djstripe_updated (datetime.datetime):
        id (str):
        amount (int): Amount (in cents) intended to be collected by this PaymentIntent.
        amount_capturable (int): Amount (in cents) that can be captured from this PaymentIntent.
        amount_received (int): Amount (in cents) that was collected by this PaymentIntent.
        capture_method (StripeConfirmationMethod):
        client_secret (str): The client secret of this PaymentIntent. Used for client-side retrieval using a publishable
            key.
        confirmation_method (StripeConfirmationMethod):
        currency (str): Three-letter ISO currency code
        payment_method_types (DjStripePaymentIntentPaymentMethodTypes): The list of payment method types (e.g. card)
            that this PaymentIntent is allowed to use.
        status (StripePaymentIntentStatus):
        livemode (Union[Unset, None, bool]): Null here indicates that the livemode status is unknown or was previously
            unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode
            operation.
        created (Union[Unset, None, datetime.datetime]): The datetime this object was created in stripe.
        metadata (Union[Unset, None, DjStripePaymentIntentMetadata]): A set of key/value pairs that you can attach to an
            object. It can be useful for storing additional information about an object in a structured format.
        canceled_at (Union[Unset, None, datetime.datetime]): Populated when status is canceled, this is the time at
            which the PaymentIntent was canceled. Measured in seconds since the Unix epoch.
        description (Union[Unset, str]): An arbitrary string attached to the object. Often useful for displaying to
            users.
        last_payment_error (Union[Unset, None, DjStripePaymentIntentLastPaymentError]): The payment error encountered in
            the previous PaymentIntent confirmation.
        next_action (Union[Unset, None, DjStripePaymentIntentNextAction]): If present, this property tells you what
            actions you need to take in order for your customer to fulfill a payment using the provided source.
        receipt_email (Union[Unset, str]): Email address that the receipt for the resulting payment will be sent to.
        shipping (Union[Unset, None, DjStripePaymentIntentShipping]): Shipping information for this PaymentIntent.
        statement_descriptor (Union[Unset, str]): For non-card charges, you can use this value as the complete
            description that appears on your customers' statements. Must contain at least one letter, maximum 22 characters.
        transfer_data (Union[Unset, None, DjStripePaymentIntentTransferData]): The data with which to automatically
            create a Transfer when the payment is finalized. See the PaymentIntents Connect usage guide for details.
        transfer_group (Union[Unset, str]): A string that identifies the resulting payment as part of a group. See the
            PaymentIntents Connect usage guide for details.
        djstripe_owner_account (Union[Unset, None, str]): The Stripe Account this object belongs to.
        customer (Union[Unset, None, str]): Customer this PaymentIntent is for if one exists.
        on_behalf_of (Union[Unset, None, str]): The account (if any) for which the funds of the PaymentIntent are
            intended.
        payment_method (Union[Unset, None, str]): Payment method used in this PaymentIntent.
    """

    djstripe_id: int
    cancellation_reason: StripePaymentIntentCancellationReason
    charges: List["DjStripeCharge"]
    setup_future_usage: StripeIntentUsage
    djstripe_created: datetime.datetime
    djstripe_updated: datetime.datetime
    id: str
    amount: int
    amount_capturable: int
    amount_received: int
    capture_method: StripeConfirmationMethod
    client_secret: str
    confirmation_method: StripeConfirmationMethod
    currency: str
    payment_method_types: "DjStripePaymentIntentPaymentMethodTypes"
    status: StripePaymentIntentStatus
    livemode: Union[Unset, None, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "DjStripePaymentIntentMetadata"] = UNSET
    canceled_at: Union[Unset, None, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    last_payment_error: Union[Unset, None, "DjStripePaymentIntentLastPaymentError"] = UNSET
    next_action: Union[Unset, None, "DjStripePaymentIntentNextAction"] = UNSET
    receipt_email: Union[Unset, str] = UNSET
    shipping: Union[Unset, None, "DjStripePaymentIntentShipping"] = UNSET
    statement_descriptor: Union[Unset, str] = UNSET
    transfer_data: Union[Unset, None, "DjStripePaymentIntentTransferData"] = UNSET
    transfer_group: Union[Unset, str] = UNSET
    djstripe_owner_account: Union[Unset, None, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    on_behalf_of: Union[Unset, None, str] = UNSET
    payment_method: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        djstripe_id = self.djstripe_id
        cancellation_reason = self.cancellation_reason.value

        charges = []
        for charges_item_data in self.charges:
            charges_item = charges_item_data.to_dict()

            charges.append(charges_item)

        setup_future_usage = self.setup_future_usage.value

        djstripe_created = self.djstripe_created.isoformat()

        djstripe_updated = self.djstripe_updated.isoformat()

        id = self.id
        amount = self.amount
        amount_capturable = self.amount_capturable
        amount_received = self.amount_received
        capture_method = self.capture_method.value

        client_secret = self.client_secret
        confirmation_method = self.confirmation_method.value

        currency = self.currency
        payment_method_types = self.payment_method_types.to_dict()

        status = self.status.value

        livemode = self.livemode
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        canceled_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.canceled_at, Unset):
            canceled_at = self.canceled_at.isoformat() if self.canceled_at else None

        description = self.description
        last_payment_error: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_payment_error, Unset):
            last_payment_error = self.last_payment_error.to_dict() if self.last_payment_error else None

        next_action: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.next_action, Unset):
            next_action = self.next_action.to_dict() if self.next_action else None

        receipt_email = self.receipt_email
        shipping: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict() if self.shipping else None

        statement_descriptor = self.statement_descriptor
        transfer_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transfer_data, Unset):
            transfer_data = self.transfer_data.to_dict() if self.transfer_data else None

        transfer_group = self.transfer_group
        djstripe_owner_account = self.djstripe_owner_account
        customer = self.customer
        on_behalf_of = self.on_behalf_of
        payment_method = self.payment_method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "djstripe_id": djstripe_id,
                "cancellation_reason": cancellation_reason,
                "charges": charges,
                "setup_future_usage": setup_future_usage,
                "djstripe_created": djstripe_created,
                "djstripe_updated": djstripe_updated,
                "id": id,
                "amount": amount,
                "amount_capturable": amount_capturable,
                "amount_received": amount_received,
                "capture_method": capture_method,
                "client_secret": client_secret,
                "confirmation_method": confirmation_method,
                "currency": currency,
                "payment_method_types": payment_method_types,
                "status": status,
            }
        )
        if livemode is not UNSET:
            field_dict["livemode"] = livemode
        if created is not UNSET:
            field_dict["created"] = created
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if canceled_at is not UNSET:
            field_dict["canceled_at"] = canceled_at
        if description is not UNSET:
            field_dict["description"] = description
        if last_payment_error is not UNSET:
            field_dict["last_payment_error"] = last_payment_error
        if next_action is not UNSET:
            field_dict["next_action"] = next_action
        if receipt_email is not UNSET:
            field_dict["receipt_email"] = receipt_email
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if statement_descriptor is not UNSET:
            field_dict["statement_descriptor"] = statement_descriptor
        if transfer_data is not UNSET:
            field_dict["transfer_data"] = transfer_data
        if transfer_group is not UNSET:
            field_dict["transfer_group"] = transfer_group
        if djstripe_owner_account is not UNSET:
            field_dict["djstripe_owner_account"] = djstripe_owner_account
        if customer is not UNSET:
            field_dict["customer"] = customer
        if on_behalf_of is not UNSET:
            field_dict["on_behalf_of"] = on_behalf_of
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dj_stripe_charge import DjStripeCharge
        from ..models.dj_stripe_payment_intent_last_payment_error import DjStripePaymentIntentLastPaymentError
        from ..models.dj_stripe_payment_intent_metadata import DjStripePaymentIntentMetadata
        from ..models.dj_stripe_payment_intent_next_action import DjStripePaymentIntentNextAction
        from ..models.dj_stripe_payment_intent_payment_method_types import DjStripePaymentIntentPaymentMethodTypes
        from ..models.dj_stripe_payment_intent_shipping import DjStripePaymentIntentShipping
        from ..models.dj_stripe_payment_intent_transfer_data import DjStripePaymentIntentTransferData

        d = src_dict.copy()
        djstripe_id = d.pop("djstripe_id")

        cancellation_reason = StripePaymentIntentCancellationReason(d.pop("cancellation_reason"))

        charges = []
        _charges = d.pop("charges")
        for charges_item_data in _charges:
            charges_item = DjStripeCharge.from_dict(charges_item_data)

            charges.append(charges_item)

        setup_future_usage = StripeIntentUsage(d.pop("setup_future_usage"))

        djstripe_created = isoparse(d.pop("djstripe_created"))

        djstripe_updated = isoparse(d.pop("djstripe_updated"))

        id = d.pop("id")

        amount = d.pop("amount")

        amount_capturable = d.pop("amount_capturable")

        amount_received = d.pop("amount_received")

        capture_method = StripeConfirmationMethod(d.pop("capture_method"))

        client_secret = d.pop("client_secret")

        confirmation_method = StripeConfirmationMethod(d.pop("confirmation_method"))

        currency = d.pop("currency")

        payment_method_types = DjStripePaymentIntentPaymentMethodTypes.from_dict(d.pop("payment_method_types"))

        status = StripePaymentIntentStatus(d.pop("status"))

        livemode = d.pop("livemode", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, DjStripePaymentIntentMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DjStripePaymentIntentMetadata.from_dict(_metadata)

        _canceled_at = d.pop("canceled_at", UNSET)
        canceled_at: Union[Unset, None, datetime.datetime]
        if _canceled_at is None:
            canceled_at = None
        elif isinstance(_canceled_at, Unset):
            canceled_at = UNSET
        else:
            canceled_at = isoparse(_canceled_at)

        description = d.pop("description", UNSET)

        _last_payment_error = d.pop("last_payment_error", UNSET)
        last_payment_error: Union[Unset, None, DjStripePaymentIntentLastPaymentError]
        if _last_payment_error is None:
            last_payment_error = None
        elif isinstance(_last_payment_error, Unset):
            last_payment_error = UNSET
        else:
            last_payment_error = DjStripePaymentIntentLastPaymentError.from_dict(_last_payment_error)

        _next_action = d.pop("next_action", UNSET)
        next_action: Union[Unset, None, DjStripePaymentIntentNextAction]
        if _next_action is None:
            next_action = None
        elif isinstance(_next_action, Unset):
            next_action = UNSET
        else:
            next_action = DjStripePaymentIntentNextAction.from_dict(_next_action)

        receipt_email = d.pop("receipt_email", UNSET)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, None, DjStripePaymentIntentShipping]
        if _shipping is None:
            shipping = None
        elif isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = DjStripePaymentIntentShipping.from_dict(_shipping)

        statement_descriptor = d.pop("statement_descriptor", UNSET)

        _transfer_data = d.pop("transfer_data", UNSET)
        transfer_data: Union[Unset, None, DjStripePaymentIntentTransferData]
        if _transfer_data is None:
            transfer_data = None
        elif isinstance(_transfer_data, Unset):
            transfer_data = UNSET
        else:
            transfer_data = DjStripePaymentIntentTransferData.from_dict(_transfer_data)

        transfer_group = d.pop("transfer_group", UNSET)

        djstripe_owner_account = d.pop("djstripe_owner_account", UNSET)

        customer = d.pop("customer", UNSET)

        on_behalf_of = d.pop("on_behalf_of", UNSET)

        payment_method = d.pop("payment_method", UNSET)

        dj_stripe_payment_intent = cls(
            djstripe_id=djstripe_id,
            cancellation_reason=cancellation_reason,
            charges=charges,
            setup_future_usage=setup_future_usage,
            djstripe_created=djstripe_created,
            djstripe_updated=djstripe_updated,
            id=id,
            amount=amount,
            amount_capturable=amount_capturable,
            amount_received=amount_received,
            capture_method=capture_method,
            client_secret=client_secret,
            confirmation_method=confirmation_method,
            currency=currency,
            payment_method_types=payment_method_types,
            status=status,
            livemode=livemode,
            created=created,
            metadata=metadata,
            canceled_at=canceled_at,
            description=description,
            last_payment_error=last_payment_error,
            next_action=next_action,
            receipt_email=receipt_email,
            shipping=shipping,
            statement_descriptor=statement_descriptor,
            transfer_data=transfer_data,
            transfer_group=transfer_group,
            djstripe_owner_account=djstripe_owner_account,
            customer=customer,
            on_behalf_of=on_behalf_of,
            payment_method=payment_method,
        )

        dj_stripe_payment_intent.additional_properties = d
        return dj_stripe_payment_intent

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
