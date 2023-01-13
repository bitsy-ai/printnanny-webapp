import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dj_stripe_price import DjStripePrice
    from ..models.dj_stripe_product import DjStripeProduct


T = TypeVar("T", bound="Product")


@attr.s(auto_attribs=True)
class Product:
    """
    Attributes:
        djstripe_product (DjStripeProduct):
        prices (List['DjStripePrice']):
        deleted (datetime.datetime):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime):
        sku (str):
        slug (str):
        unit_label (str):
        name (str):
        description (str):
        statement_descriptor (str):
        is_shippable (bool):
        is_preorder (bool):
        is_subscription (bool):
        id (Union[Unset, str]):
        images (Union[Unset, List[str]]):
        is_active (Union[Unset, bool]):
        stripe_price_lookup_key (Union[Unset, None, str]):
        stripe_product_id (Union[Unset, None, str]):
    """

    djstripe_product: "DjStripeProduct"
    prices: List["DjStripePrice"]
    deleted: datetime.datetime
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    sku: str
    slug: str
    unit_label: str
    name: str
    description: str
    statement_descriptor: str
    is_shippable: bool
    is_preorder: bool
    is_subscription: bool
    id: Union[Unset, str] = UNSET
    images: Union[Unset, List[str]] = UNSET
    is_active: Union[Unset, bool] = UNSET
    stripe_price_lookup_key: Union[Unset, None, str] = UNSET
    stripe_product_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        djstripe_product = self.djstripe_product.to_dict()

        prices = []
        for prices_item_data in self.prices:
            prices_item = prices_item_data.to_dict()

            prices.append(prices_item)

        deleted = self.deleted.isoformat()

        created_dt = self.created_dt.isoformat()

        updated_dt = self.updated_dt.isoformat()

        sku = self.sku
        slug = self.slug
        unit_label = self.unit_label
        name = self.name
        description = self.description
        statement_descriptor = self.statement_descriptor
        is_shippable = self.is_shippable
        is_preorder = self.is_preorder
        is_subscription = self.is_subscription
        id = self.id
        images: Union[Unset, List[str]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images

        is_active = self.is_active
        stripe_price_lookup_key = self.stripe_price_lookup_key
        stripe_product_id = self.stripe_product_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "djstripe_product": djstripe_product,
                "prices": prices,
                "deleted": deleted,
                "created_dt": created_dt,
                "updated_dt": updated_dt,
                "sku": sku,
                "slug": slug,
                "unit_label": unit_label,
                "name": name,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "is_shippable": is_shippable,
                "is_preorder": is_preorder,
                "is_subscription": is_subscription,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if images is not UNSET:
            field_dict["images"] = images
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if stripe_price_lookup_key is not UNSET:
            field_dict["stripe_price_lookup_key"] = stripe_price_lookup_key
        if stripe_product_id is not UNSET:
            field_dict["stripe_product_id"] = stripe_product_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dj_stripe_price import DjStripePrice
        from ..models.dj_stripe_product import DjStripeProduct

        d = src_dict.copy()
        djstripe_product = DjStripeProduct.from_dict(d.pop("djstripe_product"))

        prices = []
        _prices = d.pop("prices")
        for prices_item_data in _prices:
            prices_item = DjStripePrice.from_dict(prices_item_data)

            prices.append(prices_item)

        deleted = isoparse(d.pop("deleted"))

        created_dt = isoparse(d.pop("created_dt"))

        updated_dt = isoparse(d.pop("updated_dt"))

        sku = d.pop("sku")

        slug = d.pop("slug")

        unit_label = d.pop("unit_label")

        name = d.pop("name")

        description = d.pop("description")

        statement_descriptor = d.pop("statement_descriptor")

        is_shippable = d.pop("is_shippable")

        is_preorder = d.pop("is_preorder")

        is_subscription = d.pop("is_subscription")

        id = d.pop("id", UNSET)

        images = cast(List[str], d.pop("images", UNSET))

        is_active = d.pop("is_active", UNSET)

        stripe_price_lookup_key = d.pop("stripe_price_lookup_key", UNSET)

        stripe_product_id = d.pop("stripe_product_id", UNSET)

        product = cls(
            djstripe_product=djstripe_product,
            prices=prices,
            deleted=deleted,
            created_dt=created_dt,
            updated_dt=updated_dt,
            sku=sku,
            slug=slug,
            unit_label=unit_label,
            name=name,
            description=description,
            statement_descriptor=statement_descriptor,
            is_shippable=is_shippable,
            is_preorder=is_preorder,
            is_subscription=is_subscription,
            id=id,
            images=images,
            is_active=is_active,
            stripe_price_lookup_key=stripe_price_lookup_key,
            stripe_product_id=stripe_product_id,
        )

        product.additional_properties = d
        return product

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
