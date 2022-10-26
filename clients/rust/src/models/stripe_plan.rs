/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.109.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct StripePlan {
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
    /// Whether the plan can be used for new purchases.
    #[serde(rename = "active")]
    pub active: bool,
    /// Amount (as decimal) to be charged on the interval specified.
    #[serde(rename = "amount", skip_serializing_if = "Option::is_none")]
    pub amount: Option<String>,
    /// The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places.
    #[serde(rename = "amount_decimal", skip_serializing_if = "Option::is_none")]
    pub amount_decimal: Option<String>,
    /// Three-letter ISO currency code
    #[serde(rename = "currency")]
    pub currency: String,
    /// The frequency with which a subscription should be billed.
    #[serde(rename = "interval")]
    pub interval: Option<Box<crate::models::StripePlanInterval>>,
    /// The number of intervals (specified in the interval property) between each subscription billing.
    #[serde(rename = "interval_count", skip_serializing_if = "Option::is_none")]
    pub interval_count: Option<i32>,
    /// A brief description of the plan, hidden from customers.
    #[serde(rename = "nickname", skip_serializing_if = "Option::is_none")]
    pub nickname: Option<String>,
    /// Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.
    #[serde(rename = "tiers", skip_serializing_if = "Option::is_none")]
    pub tiers: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
    #[serde(rename = "transform_usage", skip_serializing_if = "Option::is_none")]
    pub transform_usage: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period.
    #[serde(rename = "trial_period_days", skip_serializing_if = "Option::is_none")]
    pub trial_period_days: Option<i32>,
    /// Configures how the quantity per period should be determined, can be either `metered` or `licensed`. `licensed` will automatically bill the `quantity` set for a plan when adding it to a subscription, `metered` will aggregate the total usage based on usage records. Defaults to `licensed`.
    #[serde(rename = "usage_type", skip_serializing_if = "Option::is_none")]
    pub usage_type: Option<Box<crate::models::StripePriceUsageType>>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
    /// The product whose pricing this plan determines.
    #[serde(rename = "product", skip_serializing_if = "Option::is_none")]
    pub product: Option<String>,
}

impl StripePlan {
    pub fn new(djstripe_id: i32, djstripe_created: String, djstripe_updated: String, id: String, active: bool, currency: String, interval: Option<crate::models::StripePlanInterval>) -> StripePlan {
        StripePlan {
            djstripe_id,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            description: None,
            active,
            amount: None,
            amount_decimal: None,
            currency,
            interval: interval.map(Box::new),
            interval_count: None,
            nickname: None,
            tiers: None,
            transform_usage: None,
            trial_period_days: None,
            usage_type: None,
            djstripe_owner_account: None,
            product: None,
        }
    }
}


