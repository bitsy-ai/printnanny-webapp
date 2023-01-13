import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stripe_session_billing_address_collection import StripeSessionBillingAddressCollection
from ..models.stripe_session_mode import StripeSessionMode
from ..models.stripe_submit_type_status import StripeSubmitTypeStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dj_stripe_checkout_session_display_items import DjStripeCheckoutSessionDisplayItems
    from ..models.dj_stripe_checkout_session_metadata import DjStripeCheckoutSessionMetadata
    from ..models.dj_stripe_checkout_session_payment_method_types import DjStripeCheckoutSessionPaymentMethodTypes


T = TypeVar("T", bound="DjStripeCheckoutSession")


@attr.s(auto_attribs=True)
class DjStripeCheckoutSession:
    """
    Attributes:
        djstripe_id (int):
        billing_address_collection (StripeSessionBillingAddressCollection):
        mode (StripeSessionMode):
        submit_type (StripeSubmitTypeStatus):
        djstripe_created (datetime.datetime):
        djstripe_updated (datetime.datetime):
        id (str):
        payment_method_types (DjStripeCheckoutSessionPaymentMethodTypes): The list of payment method types (e.g. card)
            that this Checkout Session is allowed to accept.
        livemode (Union[Unset, None, bool]): Null here indicates that the livemode status is unknown or was previously
            unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode
            operation.
        created (Union[Unset, None, datetime.datetime]): The datetime this object was created in stripe.
        metadata (Union[Unset, None, DjStripeCheckoutSessionMetadata]): A set of key/value pairs that you can attach to
            an object. It can be useful for storing additional information about an object in a structured format.
        description (Union[Unset, None, str]): A description of this object.
        cancel_url (Union[Unset, str]): The URL the customer will be directed to if theydecide to cancel payment and
            return to your website.
        client_reference_id (Union[Unset, str]): A unique string to reference the Checkout Session.This can be a
            customer ID, a cart ID, or similar, andcan be used to reconcile the session with your internal systems.
        customer_email (Union[Unset, str]): If provided, this value will be used when the Customer object is created.
        display_items (Union[Unset, None, DjStripeCheckoutSessionDisplayItems]): The line items, plans, or SKUs
            purchased by the customer.
        locale (Union[Unset, str]): The IETF language tag of the locale Checkout is displayed in.If blank or auto, the
            browser's locale is used.
        success_url (Union[Unset, str]): The URL the customer will be directed to after the payment or
            subscriptioncreation is successful.
        djstripe_owner_account (Union[Unset, None, str]): The Stripe Account this object belongs to.
        customer (Union[Unset, None, str]): Customer this Checkout is for if one exists.
        payment_intent (Union[Unset, None, str]): PaymentIntent created if SKUs or line items were provided.
        subscription (Union[Unset, None, str]): Subscription created if one or more plans were provided.
    """

    djstripe_id: int
    billing_address_collection: StripeSessionBillingAddressCollection
    mode: StripeSessionMode
    submit_type: StripeSubmitTypeStatus
    djstripe_created: datetime.datetime
    djstripe_updated: datetime.datetime
    id: str
    payment_method_types: "DjStripeCheckoutSessionPaymentMethodTypes"
    livemode: Union[Unset, None, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "DjStripeCheckoutSessionMetadata"] = UNSET
    description: Union[Unset, None, str] = UNSET
    cancel_url: Union[Unset, str] = UNSET
    client_reference_id: Union[Unset, str] = UNSET
    customer_email: Union[Unset, str] = UNSET
    display_items: Union[Unset, None, "DjStripeCheckoutSessionDisplayItems"] = UNSET
    locale: Union[Unset, str] = UNSET
    success_url: Union[Unset, str] = UNSET
    djstripe_owner_account: Union[Unset, None, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    payment_intent: Union[Unset, None, str] = UNSET
    subscription: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        djstripe_id = self.djstripe_id
        billing_address_collection = self.billing_address_collection.value

        mode = self.mode.value

        submit_type = self.submit_type.value

        djstripe_created = self.djstripe_created.isoformat()

        djstripe_updated = self.djstripe_updated.isoformat()

        id = self.id
        payment_method_types = self.payment_method_types.to_dict()

        livemode = self.livemode
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        description = self.description
        cancel_url = self.cancel_url
        client_reference_id = self.client_reference_id
        customer_email = self.customer_email
        display_items: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.display_items, Unset):
            display_items = self.display_items.to_dict() if self.display_items else None

        locale = self.locale
        success_url = self.success_url
        djstripe_owner_account = self.djstripe_owner_account
        customer = self.customer
        payment_intent = self.payment_intent
        subscription = self.subscription

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "djstripe_id": djstripe_id,
                "billing_address_collection": billing_address_collection,
                "mode": mode,
                "submit_type": submit_type,
                "djstripe_created": djstripe_created,
                "djstripe_updated": djstripe_updated,
                "id": id,
                "payment_method_types": payment_method_types,
            }
        )
        if livemode is not UNSET:
            field_dict["livemode"] = livemode
        if created is not UNSET:
            field_dict["created"] = created
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if description is not UNSET:
            field_dict["description"] = description
        if cancel_url is not UNSET:
            field_dict["cancel_url"] = cancel_url
        if client_reference_id is not UNSET:
            field_dict["client_reference_id"] = client_reference_id
        if customer_email is not UNSET:
            field_dict["customer_email"] = customer_email
        if display_items is not UNSET:
            field_dict["display_items"] = display_items
        if locale is not UNSET:
            field_dict["locale"] = locale
        if success_url is not UNSET:
            field_dict["success_url"] = success_url
        if djstripe_owner_account is not UNSET:
            field_dict["djstripe_owner_account"] = djstripe_owner_account
        if customer is not UNSET:
            field_dict["customer"] = customer
        if payment_intent is not UNSET:
            field_dict["payment_intent"] = payment_intent
        if subscription is not UNSET:
            field_dict["subscription"] = subscription

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dj_stripe_checkout_session_display_items import DjStripeCheckoutSessionDisplayItems
        from ..models.dj_stripe_checkout_session_metadata import DjStripeCheckoutSessionMetadata
        from ..models.dj_stripe_checkout_session_payment_method_types import DjStripeCheckoutSessionPaymentMethodTypes

        d = src_dict.copy()
        djstripe_id = d.pop("djstripe_id")

        billing_address_collection = StripeSessionBillingAddressCollection(d.pop("billing_address_collection"))

        mode = StripeSessionMode(d.pop("mode"))

        submit_type = StripeSubmitTypeStatus(d.pop("submit_type"))

        djstripe_created = isoparse(d.pop("djstripe_created"))

        djstripe_updated = isoparse(d.pop("djstripe_updated"))

        id = d.pop("id")

        payment_method_types = DjStripeCheckoutSessionPaymentMethodTypes.from_dict(d.pop("payment_method_types"))

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
        metadata: Union[Unset, None, DjStripeCheckoutSessionMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DjStripeCheckoutSessionMetadata.from_dict(_metadata)

        description = d.pop("description", UNSET)

        cancel_url = d.pop("cancel_url", UNSET)

        client_reference_id = d.pop("client_reference_id", UNSET)

        customer_email = d.pop("customer_email", UNSET)

        _display_items = d.pop("display_items", UNSET)
        display_items: Union[Unset, None, DjStripeCheckoutSessionDisplayItems]
        if _display_items is None:
            display_items = None
        elif isinstance(_display_items, Unset):
            display_items = UNSET
        else:
            display_items = DjStripeCheckoutSessionDisplayItems.from_dict(_display_items)

        locale = d.pop("locale", UNSET)

        success_url = d.pop("success_url", UNSET)

        djstripe_owner_account = d.pop("djstripe_owner_account", UNSET)

        customer = d.pop("customer", UNSET)

        payment_intent = d.pop("payment_intent", UNSET)

        subscription = d.pop("subscription", UNSET)

        dj_stripe_checkout_session = cls(
            djstripe_id=djstripe_id,
            billing_address_collection=billing_address_collection,
            mode=mode,
            submit_type=submit_type,
            djstripe_created=djstripe_created,
            djstripe_updated=djstripe_updated,
            id=id,
            payment_method_types=payment_method_types,
            livemode=livemode,
            created=created,
            metadata=metadata,
            description=description,
            cancel_url=cancel_url,
            client_reference_id=client_reference_id,
            customer_email=customer_email,
            display_items=display_items,
            locale=locale,
            success_url=success_url,
            djstripe_owner_account=djstripe_owner_account,
            customer=customer,
            payment_intent=payment_intent,
            subscription=subscription,
        )

        dj_stripe_checkout_session.additional_properties = d
        return dj_stripe_checkout_session

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
