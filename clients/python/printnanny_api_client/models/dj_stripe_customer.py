import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stripe_customer_tax_exempt import StripeCustomerTaxExempt
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dj_stripe_customer_address import DjStripeCustomerAddress
    from ..models.dj_stripe_customer_invoice_settings import DjStripeCustomerInvoiceSettings
    from ..models.dj_stripe_customer_metadata import DjStripeCustomerMetadata
    from ..models.dj_stripe_customer_preferred_locales import DjStripeCustomerPreferredLocales
    from ..models.dj_stripe_customer_shipping import DjStripeCustomerShipping


T = TypeVar("T", bound="DjStripeCustomer")


@attr.s(auto_attribs=True)
class DjStripeCustomer:
    """
    Attributes:
        djstripe_id (int):
        djstripe_created (datetime.datetime):
        djstripe_updated (datetime.datetime):
        id (str):
        coupon_start (datetime.datetime): If a coupon is present, the date at which it was applied.
        coupon_end (datetime.datetime): If a coupon is present and has a limited duration, the date that the discount
            will end.
        date_purged (datetime.datetime):
        livemode (Union[Unset, None, bool]): Null here indicates that the livemode status is unknown or was previously
            unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode
            operation.
        created (Union[Unset, None, datetime.datetime]): The datetime this object was created in stripe.
        metadata (Union[Unset, None, DjStripeCustomerMetadata]): A set of key/value pairs that you can attach to an
            object. It can be useful for storing additional information about an object in a structured format.
        description (Union[Unset, None, str]): A description of this object.
        address (Union[Unset, None, DjStripeCustomerAddress]): The customer's address.
        balance (Union[Unset, None, int]): Current balance (in cents), if any, being stored on the customer's account.
            If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed
            that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into
            account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account
            for recurring billing purposes (i.e., subscriptions, invoices, invoice items).
        currency (Union[Unset, str]): The currency the customer can be charged in for recurring billing purposes
        delinquent (Union[Unset, None, bool]): Whether or not the latest charge for the customer's latest invoice has
            failed.
        deleted (Union[Unset, None, bool]): Whether the Customer instance has been deleted upstream in Stripe or not.
        email (Union[Unset, str]):
        invoice_prefix (Union[Unset, str]): The prefix for the customer used to generate unique invoice numbers.
        invoice_settings (Union[Unset, None, DjStripeCustomerInvoiceSettings]): The customer's default invoice settings.
        name (Union[Unset, str]): The customer's full name or business name.
        phone (Union[Unset, str]): The customer's phone number.
        preferred_locales (Union[Unset, None, DjStripeCustomerPreferredLocales]): The customer's preferred locales
            (languages), ordered by preference.
        shipping (Union[Unset, None, DjStripeCustomerShipping]): Shipping information associated with the customer.
        tax_exempt (Union[Unset, StripeCustomerTaxExempt]):
        djstripe_owner_account (Optional[str]): The Stripe Account this object belongs to.
        default_source (Union[Unset, None, str]):
        coupon (Union[Unset, None, int]):
        default_payment_method (Union[Unset, None, str]): default payment method used for subscriptions and invoices for
            the customer.
        subscriber (Optional[int]):
    """

    djstripe_id: int
    djstripe_created: datetime.datetime
    djstripe_updated: datetime.datetime
    id: str
    coupon_start: datetime.datetime
    coupon_end: datetime.datetime
    date_purged: datetime.datetime
    djstripe_owner_account: Optional[str]
    subscriber: Optional[int]
    livemode: Union[Unset, None, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "DjStripeCustomerMetadata"] = UNSET
    description: Union[Unset, None, str] = UNSET
    address: Union[Unset, None, "DjStripeCustomerAddress"] = UNSET
    balance: Union[Unset, None, int] = UNSET
    currency: Union[Unset, str] = UNSET
    delinquent: Union[Unset, None, bool] = UNSET
    deleted: Union[Unset, None, bool] = UNSET
    email: Union[Unset, str] = UNSET
    invoice_prefix: Union[Unset, str] = UNSET
    invoice_settings: Union[Unset, None, "DjStripeCustomerInvoiceSettings"] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    preferred_locales: Union[Unset, None, "DjStripeCustomerPreferredLocales"] = UNSET
    shipping: Union[Unset, None, "DjStripeCustomerShipping"] = UNSET
    tax_exempt: Union[Unset, StripeCustomerTaxExempt] = UNSET
    default_source: Union[Unset, None, str] = UNSET
    coupon: Union[Unset, None, int] = UNSET
    default_payment_method: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        djstripe_id = self.djstripe_id
        djstripe_created = self.djstripe_created.isoformat()

        djstripe_updated = self.djstripe_updated.isoformat()

        id = self.id
        coupon_start = self.coupon_start.isoformat()

        coupon_end = self.coupon_end.isoformat()

        date_purged = self.date_purged.isoformat()

        livemode = self.livemode
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        description = self.description
        address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict() if self.address else None

        balance = self.balance
        currency = self.currency
        delinquent = self.delinquent
        deleted = self.deleted
        email = self.email
        invoice_prefix = self.invoice_prefix
        invoice_settings: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_settings, Unset):
            invoice_settings = self.invoice_settings.to_dict() if self.invoice_settings else None

        name = self.name
        phone = self.phone
        preferred_locales: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.preferred_locales, Unset):
            preferred_locales = self.preferred_locales.to_dict() if self.preferred_locales else None

        shipping: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict() if self.shipping else None

        tax_exempt: Union[Unset, str] = UNSET
        if not isinstance(self.tax_exempt, Unset):
            tax_exempt = self.tax_exempt.value

        djstripe_owner_account = self.djstripe_owner_account
        default_source = self.default_source
        coupon = self.coupon
        default_payment_method = self.default_payment_method
        subscriber = self.subscriber

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "djstripe_id": djstripe_id,
                "djstripe_created": djstripe_created,
                "djstripe_updated": djstripe_updated,
                "id": id,
                "coupon_start": coupon_start,
                "coupon_end": coupon_end,
                "date_purged": date_purged,
                "djstripe_owner_account": djstripe_owner_account,
                "subscriber": subscriber,
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
        if address is not UNSET:
            field_dict["address"] = address
        if balance is not UNSET:
            field_dict["balance"] = balance
        if currency is not UNSET:
            field_dict["currency"] = currency
        if delinquent is not UNSET:
            field_dict["delinquent"] = delinquent
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if email is not UNSET:
            field_dict["email"] = email
        if invoice_prefix is not UNSET:
            field_dict["invoice_prefix"] = invoice_prefix
        if invoice_settings is not UNSET:
            field_dict["invoice_settings"] = invoice_settings
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if preferred_locales is not UNSET:
            field_dict["preferred_locales"] = preferred_locales
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if tax_exempt is not UNSET:
            field_dict["tax_exempt"] = tax_exempt
        if default_source is not UNSET:
            field_dict["default_source"] = default_source
        if coupon is not UNSET:
            field_dict["coupon"] = coupon
        if default_payment_method is not UNSET:
            field_dict["default_payment_method"] = default_payment_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dj_stripe_customer_address import DjStripeCustomerAddress
        from ..models.dj_stripe_customer_invoice_settings import DjStripeCustomerInvoiceSettings
        from ..models.dj_stripe_customer_metadata import DjStripeCustomerMetadata
        from ..models.dj_stripe_customer_preferred_locales import DjStripeCustomerPreferredLocales
        from ..models.dj_stripe_customer_shipping import DjStripeCustomerShipping

        d = src_dict.copy()
        djstripe_id = d.pop("djstripe_id")

        djstripe_created = isoparse(d.pop("djstripe_created"))

        djstripe_updated = isoparse(d.pop("djstripe_updated"))

        id = d.pop("id")

        coupon_start = isoparse(d.pop("coupon_start"))

        coupon_end = isoparse(d.pop("coupon_end"))

        date_purged = isoparse(d.pop("date_purged"))

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
        metadata: Union[Unset, None, DjStripeCustomerMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DjStripeCustomerMetadata.from_dict(_metadata)

        description = d.pop("description", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, None, DjStripeCustomerAddress]
        if _address is None:
            address = None
        elif isinstance(_address, Unset):
            address = UNSET
        else:
            address = DjStripeCustomerAddress.from_dict(_address)

        balance = d.pop("balance", UNSET)

        currency = d.pop("currency", UNSET)

        delinquent = d.pop("delinquent", UNSET)

        deleted = d.pop("deleted", UNSET)

        email = d.pop("email", UNSET)

        invoice_prefix = d.pop("invoice_prefix", UNSET)

        _invoice_settings = d.pop("invoice_settings", UNSET)
        invoice_settings: Union[Unset, None, DjStripeCustomerInvoiceSettings]
        if _invoice_settings is None:
            invoice_settings = None
        elif isinstance(_invoice_settings, Unset):
            invoice_settings = UNSET
        else:
            invoice_settings = DjStripeCustomerInvoiceSettings.from_dict(_invoice_settings)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        _preferred_locales = d.pop("preferred_locales", UNSET)
        preferred_locales: Union[Unset, None, DjStripeCustomerPreferredLocales]
        if _preferred_locales is None:
            preferred_locales = None
        elif isinstance(_preferred_locales, Unset):
            preferred_locales = UNSET
        else:
            preferred_locales = DjStripeCustomerPreferredLocales.from_dict(_preferred_locales)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, None, DjStripeCustomerShipping]
        if _shipping is None:
            shipping = None
        elif isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = DjStripeCustomerShipping.from_dict(_shipping)

        _tax_exempt = d.pop("tax_exempt", UNSET)
        tax_exempt: Union[Unset, StripeCustomerTaxExempt]
        if isinstance(_tax_exempt, Unset):
            tax_exempt = UNSET
        else:
            tax_exempt = StripeCustomerTaxExempt(_tax_exempt)

        djstripe_owner_account = d.pop("djstripe_owner_account")

        default_source = d.pop("default_source", UNSET)

        coupon = d.pop("coupon", UNSET)

        default_payment_method = d.pop("default_payment_method", UNSET)

        subscriber = d.pop("subscriber")

        dj_stripe_customer = cls(
            djstripe_id=djstripe_id,
            djstripe_created=djstripe_created,
            djstripe_updated=djstripe_updated,
            id=id,
            coupon_start=coupon_start,
            coupon_end=coupon_end,
            date_purged=date_purged,
            livemode=livemode,
            created=created,
            metadata=metadata,
            description=description,
            address=address,
            balance=balance,
            currency=currency,
            delinquent=delinquent,
            deleted=deleted,
            email=email,
            invoice_prefix=invoice_prefix,
            invoice_settings=invoice_settings,
            name=name,
            phone=phone,
            preferred_locales=preferred_locales,
            shipping=shipping,
            tax_exempt=tax_exempt,
            djstripe_owner_account=djstripe_owner_account,
            default_source=default_source,
            coupon=coupon,
            default_payment_method=default_payment_method,
            subscriber=subscriber,
        )

        dj_stripe_customer.additional_properties = d
        return dj_stripe_customer

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
