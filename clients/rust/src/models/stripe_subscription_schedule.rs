/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct StripeSubscriptionSchedule {
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
    /// Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period.
    #[serde(rename = "billing_thresholds", skip_serializing_if = "Option::is_none")]
    pub billing_thresholds: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Time at which the subscription schedule was canceled.
    #[serde(rename = "canceled_at", skip_serializing_if = "Option::is_none")]
    pub canceled_at: Option<String>,
    /// Time at which the subscription schedule was completed.
    #[serde(rename = "completed_at", skip_serializing_if = "Option::is_none")]
    pub completed_at: Option<String>,
    /// Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`.
    #[serde(rename = "current_phase", skip_serializing_if = "Option::is_none")]
    pub current_phase: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Object representing the subscription schedule's default settings.
    #[serde(rename = "default_settings", skip_serializing_if = "Option::is_none")]
    pub default_settings: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Behavior of the subscription schedule and underlying subscription when it ends.
    #[serde(rename = "end_behavior")]
    pub end_behavior: Option<Box<crate::models::EndBehaviorEnum>>,
    /// Configuration for the subscription schedule's phases.
    #[serde(rename = "phases", skip_serializing_if = "Option::is_none")]
    pub phases: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Time at which the subscription schedule was released.
    #[serde(rename = "released_at", skip_serializing_if = "Option::is_none")]
    pub released_at: Option<String>,
    /// The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`.
    #[serde(rename = "status")]
    pub status: Option<Box<crate::models::StripeSubscriptionScheduleStatusEnum>>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
    /// The customer who owns the subscription schedule.
    #[serde(rename = "customer")]
    pub customer: i32,
    /// The subscription once managed by this subscription schedule (if it is released).
    #[serde(rename = "released_subscription", skip_serializing_if = "Option::is_none")]
    pub released_subscription: Option<i32>,
}

impl StripeSubscriptionSchedule {
    pub fn new(djstripe_id: i32, djstripe_created: String, djstripe_updated: String, id: String, end_behavior: Option<crate::models::EndBehaviorEnum>, status: Option<crate::models::StripeSubscriptionScheduleStatusEnum>, customer: i32) -> StripeSubscriptionSchedule {
        StripeSubscriptionSchedule {
            djstripe_id,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            description: None,
            billing_thresholds: None,
            canceled_at: None,
            completed_at: None,
            current_phase: None,
            default_settings: None,
            end_behavior: end_behavior.map(Box::new),
            phases: None,
            released_at: None,
            status: status.map(Box::new),
            djstripe_owner_account: None,
            customer,
            released_subscription: None,
        }
    }
}


