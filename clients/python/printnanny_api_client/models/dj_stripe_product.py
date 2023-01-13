import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stripe_product_type import StripeProductType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dj_stripe_product_attributes import DjStripeProductAttributes
    from ..models.dj_stripe_product_deactivate_on import DjStripeProductDeactivateOn
    from ..models.dj_stripe_product_images import DjStripeProductImages
    from ..models.dj_stripe_product_metadata import DjStripeProductMetadata
    from ..models.dj_stripe_product_package_dimensions import DjStripeProductPackageDimensions


T = TypeVar("T", bound="DjStripeProduct")


@attr.s(auto_attribs=True)
class DjStripeProduct:
    """
    Attributes:
        djstripe_id (int):
        djstripe_created (datetime.datetime):
        djstripe_updated (datetime.datetime):
        id (str):
        name (str): The product's name, meant to be displayable to the customer. Applicable to both `service` and `good`
            types.
        type (StripeProductType):
        livemode (Union[Unset, None, bool]): Null here indicates that the livemode status is unknown or was previously
            unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode
            operation.
        created (Union[Unset, None, datetime.datetime]): The datetime this object was created in stripe.
        metadata (Union[Unset, None, DjStripeProductMetadata]): A set of key/value pairs that you can attach to an
            object. It can be useful for storing additional information about an object in a structured format.
        description (Union[Unset, None, str]): A description of this object.
        active (Union[Unset, None, bool]): Whether the product is currently available for purchase. Only applicable to
            products of `type=good`.
        attributes (Union[Unset, None, DjStripeProductAttributes]): A list of up to 5 attributes that each SKU can
            provide values for (e.g., `["color", "size"]`). Only applicable to products of `type=good`.
        caption (Union[Unset, str]): A short one-line description of the product, meant to be displayableto the
            customer. Only applicable to products of `type=good`.
        deactivate_on (Union[Unset, None, DjStripeProductDeactivateOn]): An array of connect application identifiers
            that cannot purchase this product. Only applicable to products of `type=good`.
        images (Union[Unset, None, DjStripeProductImages]): A list of up to 8 URLs of images for this product, meant to
            be displayable to the customer. Only applicable to products of `type=good`.
        package_dimensions (Union[Unset, None, DjStripeProductPackageDimensions]): The dimensions of this product for
            shipping purposes. A SKU associated with this product can override this value by having its own
            `package_dimensions`. Only applicable to products of `type=good`.
        shippable (Union[Unset, None, bool]): Whether this product is a shipped good. Only applicable to products of
            `type=good`.
        url (Union[Unset, None, str]): A URL of a publicly-accessible webpage for this product. Only applicable to
            products of `type=good`.
        statement_descriptor (Union[Unset, str]): Extra information about a product which will appear on your customer's
            credit card statement. In the case that multiple products are billed at once, the first statement descriptor
            will be used. Only available on products of type=`service`.
        unit_label (Union[Unset, str]):
        djstripe_owner_account (Union[Unset, None, str]): The Stripe Account this object belongs to.
    """

    djstripe_id: int
    djstripe_created: datetime.datetime
    djstripe_updated: datetime.datetime
    id: str
    name: str
    type: StripeProductType
    livemode: Union[Unset, None, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "DjStripeProductMetadata"] = UNSET
    description: Union[Unset, None, str] = UNSET
    active: Union[Unset, None, bool] = UNSET
    attributes: Union[Unset, None, "DjStripeProductAttributes"] = UNSET
    caption: Union[Unset, str] = UNSET
    deactivate_on: Union[Unset, None, "DjStripeProductDeactivateOn"] = UNSET
    images: Union[Unset, None, "DjStripeProductImages"] = UNSET
    package_dimensions: Union[Unset, None, "DjStripeProductPackageDimensions"] = UNSET
    shippable: Union[Unset, None, bool] = UNSET
    url: Union[Unset, None, str] = UNSET
    statement_descriptor: Union[Unset, str] = UNSET
    unit_label: Union[Unset, str] = UNSET
    djstripe_owner_account: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        djstripe_id = self.djstripe_id
        djstripe_created = self.djstripe_created.isoformat()

        djstripe_updated = self.djstripe_updated.isoformat()

        id = self.id
        name = self.name
        type = self.type.value

        livemode = self.livemode
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        description = self.description
        active = self.active
        attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict() if self.attributes else None

        caption = self.caption
        deactivate_on: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.deactivate_on, Unset):
            deactivate_on = self.deactivate_on.to_dict() if self.deactivate_on else None

        images: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict() if self.images else None

        package_dimensions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.package_dimensions, Unset):
            package_dimensions = self.package_dimensions.to_dict() if self.package_dimensions else None

        shippable = self.shippable
        url = self.url
        statement_descriptor = self.statement_descriptor
        unit_label = self.unit_label
        djstripe_owner_account = self.djstripe_owner_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "djstripe_id": djstripe_id,
                "djstripe_created": djstripe_created,
                "djstripe_updated": djstripe_updated,
                "id": id,
                "name": name,
                "type": type,
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
        if active is not UNSET:
            field_dict["active"] = active
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if caption is not UNSET:
            field_dict["caption"] = caption
        if deactivate_on is not UNSET:
            field_dict["deactivate_on"] = deactivate_on
        if images is not UNSET:
            field_dict["images"] = images
        if package_dimensions is not UNSET:
            field_dict["package_dimensions"] = package_dimensions
        if shippable is not UNSET:
            field_dict["shippable"] = shippable
        if url is not UNSET:
            field_dict["url"] = url
        if statement_descriptor is not UNSET:
            field_dict["statement_descriptor"] = statement_descriptor
        if unit_label is not UNSET:
            field_dict["unit_label"] = unit_label
        if djstripe_owner_account is not UNSET:
            field_dict["djstripe_owner_account"] = djstripe_owner_account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dj_stripe_product_attributes import DjStripeProductAttributes
        from ..models.dj_stripe_product_deactivate_on import DjStripeProductDeactivateOn
        from ..models.dj_stripe_product_images import DjStripeProductImages
        from ..models.dj_stripe_product_metadata import DjStripeProductMetadata
        from ..models.dj_stripe_product_package_dimensions import DjStripeProductPackageDimensions

        d = src_dict.copy()
        djstripe_id = d.pop("djstripe_id")

        djstripe_created = isoparse(d.pop("djstripe_created"))

        djstripe_updated = isoparse(d.pop("djstripe_updated"))

        id = d.pop("id")

        name = d.pop("name")

        type = StripeProductType(d.pop("type"))

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
        metadata: Union[Unset, None, DjStripeProductMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DjStripeProductMetadata.from_dict(_metadata)

        description = d.pop("description", UNSET)

        active = d.pop("active", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, None, DjStripeProductAttributes]
        if _attributes is None:
            attributes = None
        elif isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = DjStripeProductAttributes.from_dict(_attributes)

        caption = d.pop("caption", UNSET)

        _deactivate_on = d.pop("deactivate_on", UNSET)
        deactivate_on: Union[Unset, None, DjStripeProductDeactivateOn]
        if _deactivate_on is None:
            deactivate_on = None
        elif isinstance(_deactivate_on, Unset):
            deactivate_on = UNSET
        else:
            deactivate_on = DjStripeProductDeactivateOn.from_dict(_deactivate_on)

        _images = d.pop("images", UNSET)
        images: Union[Unset, None, DjStripeProductImages]
        if _images is None:
            images = None
        elif isinstance(_images, Unset):
            images = UNSET
        else:
            images = DjStripeProductImages.from_dict(_images)

        _package_dimensions = d.pop("package_dimensions", UNSET)
        package_dimensions: Union[Unset, None, DjStripeProductPackageDimensions]
        if _package_dimensions is None:
            package_dimensions = None
        elif isinstance(_package_dimensions, Unset):
            package_dimensions = UNSET
        else:
            package_dimensions = DjStripeProductPackageDimensions.from_dict(_package_dimensions)

        shippable = d.pop("shippable", UNSET)

        url = d.pop("url", UNSET)

        statement_descriptor = d.pop("statement_descriptor", UNSET)

        unit_label = d.pop("unit_label", UNSET)

        djstripe_owner_account = d.pop("djstripe_owner_account", UNSET)

        dj_stripe_product = cls(
            djstripe_id=djstripe_id,
            djstripe_created=djstripe_created,
            djstripe_updated=djstripe_updated,
            id=id,
            name=name,
            type=type,
            livemode=livemode,
            created=created,
            metadata=metadata,
            description=description,
            active=active,
            attributes=attributes,
            caption=caption,
            deactivate_on=deactivate_on,
            images=images,
            package_dimensions=package_dimensions,
            shippable=shippable,
            url=url,
            statement_descriptor=statement_descriptor,
            unit_label=unit_label,
            djstripe_owner_account=djstripe_owner_account,
        )

        dj_stripe_product.additional_properties = d
        return dj_stripe_product

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
