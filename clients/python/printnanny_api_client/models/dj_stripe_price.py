import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stripe_billing_scheme import StripeBillingScheme
from ..models.stripe_price_tiers_mode import StripePriceTiersMode
from ..models.stripe_price_type import StripePriceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dj_stripe_price_metadata import DjStripePriceMetadata
    from ..models.dj_stripe_price_recurring import DjStripePriceRecurring
    from ..models.dj_stripe_price_tiers import DjStripePriceTiers
    from ..models.dj_stripe_price_transform_quantity import DjStripePriceTransformQuantity


T = TypeVar("T", bound="DjStripePrice")


@attr.s(auto_attribs=True)
class DjStripePrice:
    """
    Attributes:
        djstripe_id (int):
        billing_scheme (StripeBillingScheme):
        human_readable_price (str):
        tiers_mode (StripePriceTiersMode):
        djstripe_created (datetime.datetime):
        djstripe_updated (datetime.datetime):
        id (str):
        active (bool): Whether the price can be used for new purchases.
        currency (str): Three-letter ISO currency code
        type (StripePriceType):
        product (str): The product this price is associated with.
        livemode (Union[Unset, None, bool]): Null here indicates that the livemode status is unknown or was previously
            unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode
            operation.
        created (Union[Unset, None, datetime.datetime]): The datetime this object was created in stripe.
        metadata (Union[Unset, None, DjStripePriceMetadata]): A set of key/value pairs that you can attach to an object.
            It can be useful for storing additional information about an object in a structured format.
        description (Union[Unset, None, str]): A description of this object.
        nickname (Union[Unset, str]): A brief description of the plan, hidden from customers.
        recurring (Union[Unset, None, DjStripePriceRecurring]): The recurring components of a price such as `interval`
            and `usage_type`.
        unit_amount (Union[Unset, None, int]): The unit amount in cents to be charged, represented as a whole integer if
            possible. Null if a sub-cent precision is required.
        unit_amount_decimal (Union[Unset, None, str]): The unit amount in cents to be charged, represented as a decimal
            string with at most 12 decimal places.
        lookup_key (Union[Unset, None, str]): A lookup key used to retrieve prices dynamically from a static string.
        tiers (Union[Unset, None, DjStripePriceTiers]): Each element represents a pricing tier. This parameter requires
            `billing_scheme` to be set to `tiered`.
        transform_quantity (Union[Unset, None, DjStripePriceTransformQuantity]): Apply a transformation to the reported
            usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.
        djstripe_owner_account (Union[Unset, None, str]): The Stripe Account this object belongs to.
    """

    djstripe_id: int
    billing_scheme: StripeBillingScheme
    human_readable_price: str
    tiers_mode: StripePriceTiersMode
    djstripe_created: datetime.datetime
    djstripe_updated: datetime.datetime
    id: str
    active: bool
    currency: str
    type: StripePriceType
    product: str
    livemode: Union[Unset, None, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "DjStripePriceMetadata"] = UNSET
    description: Union[Unset, None, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    recurring: Union[Unset, None, "DjStripePriceRecurring"] = UNSET
    unit_amount: Union[Unset, None, int] = UNSET
    unit_amount_decimal: Union[Unset, None, str] = UNSET
    lookup_key: Union[Unset, None, str] = UNSET
    tiers: Union[Unset, None, "DjStripePriceTiers"] = UNSET
    transform_quantity: Union[Unset, None, "DjStripePriceTransformQuantity"] = UNSET
    djstripe_owner_account: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        djstripe_id = self.djstripe_id
        billing_scheme = self.billing_scheme.value

        human_readable_price = self.human_readable_price
        tiers_mode = self.tiers_mode.value

        djstripe_created = self.djstripe_created.isoformat()

        djstripe_updated = self.djstripe_updated.isoformat()

        id = self.id
        active = self.active
        currency = self.currency
        type = self.type.value

        product = self.product
        livemode = self.livemode
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        description = self.description
        nickname = self.nickname
        recurring: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.recurring, Unset):
            recurring = self.recurring.to_dict() if self.recurring else None

        unit_amount = self.unit_amount
        unit_amount_decimal = self.unit_amount_decimal
        lookup_key = self.lookup_key
        tiers: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = self.tiers.to_dict() if self.tiers else None

        transform_quantity: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transform_quantity, Unset):
            transform_quantity = self.transform_quantity.to_dict() if self.transform_quantity else None

        djstripe_owner_account = self.djstripe_owner_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "djstripe_id": djstripe_id,
                "billing_scheme": billing_scheme,
                "human_readable_price": human_readable_price,
                "tiers_mode": tiers_mode,
                "djstripe_created": djstripe_created,
                "djstripe_updated": djstripe_updated,
                "id": id,
                "active": active,
                "currency": currency,
                "type": type,
                "product": product,
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
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if recurring is not UNSET:
            field_dict["recurring"] = recurring
        if unit_amount is not UNSET:
            field_dict["unit_amount"] = unit_amount
        if unit_amount_decimal is not UNSET:
            field_dict["unit_amount_decimal"] = unit_amount_decimal
        if lookup_key is not UNSET:
            field_dict["lookup_key"] = lookup_key
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if transform_quantity is not UNSET:
            field_dict["transform_quantity"] = transform_quantity
        if djstripe_owner_account is not UNSET:
            field_dict["djstripe_owner_account"] = djstripe_owner_account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dj_stripe_price_metadata import DjStripePriceMetadata
        from ..models.dj_stripe_price_recurring import DjStripePriceRecurring
        from ..models.dj_stripe_price_tiers import DjStripePriceTiers
        from ..models.dj_stripe_price_transform_quantity import DjStripePriceTransformQuantity

        d = src_dict.copy()
        djstripe_id = d.pop("djstripe_id")

        billing_scheme = StripeBillingScheme(d.pop("billing_scheme"))

        human_readable_price = d.pop("human_readable_price")

        tiers_mode = StripePriceTiersMode(d.pop("tiers_mode"))

        djstripe_created = isoparse(d.pop("djstripe_created"))

        djstripe_updated = isoparse(d.pop("djstripe_updated"))

        id = d.pop("id")

        active = d.pop("active")

        currency = d.pop("currency")

        type = StripePriceType(d.pop("type"))

        product = d.pop("product")

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
        metadata: Union[Unset, None, DjStripePriceMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DjStripePriceMetadata.from_dict(_metadata)

        description = d.pop("description", UNSET)

        nickname = d.pop("nickname", UNSET)

        _recurring = d.pop("recurring", UNSET)
        recurring: Union[Unset, None, DjStripePriceRecurring]
        if _recurring is None:
            recurring = None
        elif isinstance(_recurring, Unset):
            recurring = UNSET
        else:
            recurring = DjStripePriceRecurring.from_dict(_recurring)

        unit_amount = d.pop("unit_amount", UNSET)

        unit_amount_decimal = d.pop("unit_amount_decimal", UNSET)

        lookup_key = d.pop("lookup_key", UNSET)

        _tiers = d.pop("tiers", UNSET)
        tiers: Union[Unset, None, DjStripePriceTiers]
        if _tiers is None:
            tiers = None
        elif isinstance(_tiers, Unset):
            tiers = UNSET
        else:
            tiers = DjStripePriceTiers.from_dict(_tiers)

        _transform_quantity = d.pop("transform_quantity", UNSET)
        transform_quantity: Union[Unset, None, DjStripePriceTransformQuantity]
        if _transform_quantity is None:
            transform_quantity = None
        elif isinstance(_transform_quantity, Unset):
            transform_quantity = UNSET
        else:
            transform_quantity = DjStripePriceTransformQuantity.from_dict(_transform_quantity)

        djstripe_owner_account = d.pop("djstripe_owner_account", UNSET)

        dj_stripe_price = cls(
            djstripe_id=djstripe_id,
            billing_scheme=billing_scheme,
            human_readable_price=human_readable_price,
            tiers_mode=tiers_mode,
            djstripe_created=djstripe_created,
            djstripe_updated=djstripe_updated,
            id=id,
            active=active,
            currency=currency,
            type=type,
            product=product,
            livemode=livemode,
            created=created,
            metadata=metadata,
            description=description,
            nickname=nickname,
            recurring=recurring,
            unit_amount=unit_amount,
            unit_amount_decimal=unit_amount_decimal,
            lookup_key=lookup_key,
            tiers=tiers,
            transform_quantity=transform_quantity,
            djstripe_owner_account=djstripe_owner_account,
        )

        dj_stripe_price.additional_properties = d
        return dj_stripe_price

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
