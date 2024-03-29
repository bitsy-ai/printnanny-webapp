/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct DjStripeProduct {
    #[serde(rename = "djstripe_id")]
    pub djstripe_id: i32,
    #[serde(rename = "djstripe_created")]
    pub djstripe_created: String,
    #[serde(rename = "djstripe_updated")]
    pub djstripe_updated: String,
    #[serde(rename = "id")]
    pub id: String,
    /// Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.
    #[serde(rename = "livemode", skip_serializing_if = "Option::is_none")]
    pub livemode: Option<bool>,
    /// The datetime this object was created in stripe.
    #[serde(rename = "created", skip_serializing_if = "Option::is_none")]
    pub created: Option<String>,
    /// A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.
    #[serde(rename = "metadata", skip_serializing_if = "Option::is_none")]
    pub metadata: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// A description of this object.
    #[serde(rename = "description", skip_serializing_if = "Option::is_none")]
    pub description: Option<String>,
    /// The product's name, meant to be displayable to the customer. Applicable to both `service` and `good` types.
    #[serde(rename = "name")]
    pub name: String,
    /// The type of the product. The product is either of type `good`, which is eligible for use with Orders and SKUs, or `service`, which is eligible for use with Subscriptions and Plans.  * `good` - Good * `service` - Service
    #[serde(rename = "type")]
    pub _type: Option<Box<crate::models::StripeProductType>>,
    /// Whether the product is currently available for purchase. Only applicable to products of `type=good`.
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    /// A list of up to 5 attributes that each SKU can provide values for (e.g., `[\"color\", \"size\"]`). Only applicable to products of `type=good`.
    #[serde(rename = "attributes", skip_serializing_if = "Option::is_none")]
    pub attributes: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// A short one-line description of the product, meant to be displayableto the customer. Only applicable to products of `type=good`.
    #[serde(rename = "caption", skip_serializing_if = "Option::is_none")]
    pub caption: Option<String>,
    /// An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`.
    #[serde(rename = "deactivate_on", skip_serializing_if = "Option::is_none")]
    pub deactivate_on: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of `type=good`.
    #[serde(rename = "images", skip_serializing_if = "Option::is_none")]
    pub images: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The dimensions of this product for shipping purposes. A SKU associated with this product can override this value by having its own `package_dimensions`. Only applicable to products of `type=good`.
    #[serde(rename = "package_dimensions", skip_serializing_if = "Option::is_none")]
    pub package_dimensions: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Whether this product is a shipped good. Only applicable to products of `type=good`.
    #[serde(rename = "shippable", skip_serializing_if = "Option::is_none")]
    pub shippable: Option<bool>,
    /// A URL of a publicly-accessible webpage for this product. Only applicable to products of `type=good`.
    #[serde(rename = "url", skip_serializing_if = "Option::is_none")]
    pub url: Option<String>,
    /// Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only available on products of type=`service`.
    #[serde(rename = "statement_descriptor", skip_serializing_if = "Option::is_none")]
    pub statement_descriptor: Option<String>,
    #[serde(rename = "unit_label", skip_serializing_if = "Option::is_none")]
    pub unit_label: Option<String>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
}

impl DjStripeProduct {
    pub fn new(djstripe_id: i32, djstripe_created: String, djstripe_updated: String, id: String, name: String, _type: Option<crate::models::StripeProductType>) -> DjStripeProduct {
        DjStripeProduct {
            djstripe_id,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            description: None,
            name,
            _type: _type.map(Box::new),
            active: None,
            attributes: None,
            caption: None,
            deactivate_on: None,
            images: None,
            package_dimensions: None,
            shippable: None,
            url: None,
            statement_descriptor: None,
            unit_label: None,
            djstripe_owner_account: None,
        }
    }
}


