/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.109.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct DjStripePrice {
    #[serde(rename = "djstripe_id")]
    pub djstripe_id: i32,
    #[serde(rename = "billing_scheme")]
    pub billing_scheme: crate::models::StripeBillingScheme,
    #[serde(rename = "human_readable_price")]
    pub human_readable_price: String,
    #[serde(rename = "tiers_mode")]
    pub tiers_mode: crate::models::StripePriceTiersMode,
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
    /// Whether the price can be used for new purchases.
    #[serde(rename = "active")]
    pub active: bool,
    /// Three-letter ISO currency code
    #[serde(rename = "currency")]
    pub currency: String,
    /// A brief description of the plan, hidden from customers.
    #[serde(rename = "nickname", skip_serializing_if = "Option::is_none")]
    pub nickname: Option<String>,
    /// The recurring components of a price such as `interval` and `usage_type`.
    #[serde(rename = "recurring", skip_serializing_if = "Option::is_none")]
    pub recurring: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Whether the price is for a one-time purchase or a recurring (subscription) purchase.
    #[serde(rename = "type")]
    pub _type: Option<Box<crate::models::StripePriceType>>,
    /// The unit amount in cents to be charged, represented as a whole integer if possible. Null if a sub-cent precision is required.
    #[serde(rename = "unit_amount", skip_serializing_if = "Option::is_none")]
    pub unit_amount: Option<i64>,
    /// The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places.
    #[serde(rename = "unit_amount_decimal", skip_serializing_if = "Option::is_none")]
    pub unit_amount_decimal: Option<String>,
    /// A lookup key used to retrieve prices dynamically from a static string.
    #[serde(rename = "lookup_key", skip_serializing_if = "Option::is_none")]
    pub lookup_key: Option<String>,
    /// Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.
    #[serde(rename = "tiers", skip_serializing_if = "Option::is_none")]
    pub tiers: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.
    #[serde(rename = "transform_quantity", skip_serializing_if = "Option::is_none")]
    pub transform_quantity: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
    /// The product this price is associated with.
    #[serde(rename = "product")]
    pub product: String,
}

impl DjStripePrice {
    pub fn new(djstripe_id: i32, billing_scheme: crate::models::StripeBillingScheme, human_readable_price: String, tiers_mode: crate::models::StripePriceTiersMode, djstripe_created: String, djstripe_updated: String, id: String, active: bool, currency: String, _type: Option<crate::models::StripePriceType>, product: String) -> DjStripePrice {
        DjStripePrice {
            djstripe_id,
            billing_scheme,
            human_readable_price,
            tiers_mode,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            description: None,
            active,
            currency,
            nickname: None,
            recurring: None,
            _type: _type.map(Box::new),
            unit_amount: None,
            unit_amount_decimal: None,
            lookup_key: None,
            tiers: None,
            transform_quantity: None,
            djstripe_owner_account: None,
            product,
        }
    }
}


