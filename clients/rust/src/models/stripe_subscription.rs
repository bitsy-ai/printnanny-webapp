/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct StripeSubscription {
    #[serde(rename = "djstripe_id")]
    pub djstripe_id: i32,
    #[serde(rename = "plan")]
    pub plan: Box<crate::models::StripePlan>,
    #[serde(rename = "default_payment_method")]
    pub default_payment_method: Box<crate::models::StripePaymentMethod>,
    #[serde(rename = "schedule")]
    pub schedule: Box<crate::models::StripeSubscriptionSchedule>,
    #[serde(rename = "is_period_current")]
    pub is_period_current: bool,
    #[serde(rename = "is_status_current")]
    pub is_status_current: bool,
    #[serde(rename = "is_status_temporarily_current")]
    pub is_status_temporarily_current: bool,
    #[serde(rename = "is_valid")]
    pub is_valid: bool,
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
    /// A positive decimal that represents the fee percentage of the subscription invoice amount that will be transferred to the application owner's Stripe account each billing period.
    #[serde(rename = "application_fee_percent", skip_serializing_if = "Option::is_none")]
    pub application_fee_percent: Option<String>,
    /// Determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices.
    #[serde(rename = "billing_cycle_anchor", skip_serializing_if = "Option::is_none")]
    pub billing_cycle_anchor: Option<String>,
    /// Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period.
    #[serde(rename = "billing_thresholds", skip_serializing_if = "Option::is_none")]
    pub billing_thresholds: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// A date in the future at which the subscription will automatically get canceled.
    #[serde(rename = "cancel_at", skip_serializing_if = "Option::is_none")]
    pub cancel_at: Option<String>,
    /// If the subscription has been canceled with the ``at_period_end`` flag set to true, ``cancel_at_period_end`` on the subscription will be true. You can use this attribute to determine whether a subscription that has a status of active is scheduled to be canceled at the end of the current period.
    #[serde(rename = "cancel_at_period_end", skip_serializing_if = "Option::is_none")]
    pub cancel_at_period_end: Option<bool>,
    /// If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with ``cancel_at_period_end``, canceled_at will still reflect the date of the initial cancellation request, not the end of the subscription period when the subscription is automatically moved to a canceled state.
    #[serde(rename = "canceled_at", skip_serializing_if = "Option::is_none")]
    pub canceled_at: Option<String>,
    /// Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions.
    #[serde(rename = "collection_method")]
    pub collection_method: Option<Box<crate::models::CollectionMethodEnum>>,
    /// End of the current period for which the subscription has been invoiced. At the end of this period, a new invoice will be created.
    #[serde(rename = "current_period_end")]
    pub current_period_end: String,
    /// Start of the current period for which the subscription has been invoiced.
    #[serde(rename = "current_period_start")]
    pub current_period_start: String,
    /// Number of days a customer has to pay invoices generated by this subscription. This value will be `null` for subscriptions where `billing=charge_automatically`.
    #[serde(rename = "days_until_due", skip_serializing_if = "Option::is_none")]
    pub days_until_due: Option<i32>,
    #[serde(rename = "discount", skip_serializing_if = "Option::is_none")]
    pub discount: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// If the subscription has ended (either because it was canceled or because the customer was switched to a subscription to a new plan), the date the subscription ended.
    #[serde(rename = "ended_at", skip_serializing_if = "Option::is_none")]
    pub ended_at: Option<String>,
    /// Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at pending_invoice_item_interval.
    #[serde(rename = "next_pending_invoice_item_invoice", skip_serializing_if = "Option::is_none")]
    pub next_pending_invoice_item_invoice: Option<String>,
    /// Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling Create an invoice for the given subscription at the specified interval.
    #[serde(rename = "pending_invoice_item_interval", skip_serializing_if = "Option::is_none")]
    pub pending_invoice_item_interval: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// If specified, pending updates that will be applied to the subscription once the latest_invoice has been paid.
    #[serde(rename = "pending_update", skip_serializing_if = "Option::is_none")]
    pub pending_update: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The quantity applied to this subscription. This value will be `null` for multi-plan subscriptions
    #[serde(rename = "quantity", skip_serializing_if = "Option::is_none")]
    pub quantity: Option<i32>,
    /// Date when the subscription was first created. The date might differ from the created date due to backdating.
    #[serde(rename = "start_date", skip_serializing_if = "Option::is_none")]
    pub start_date: Option<String>,
    /// The status of this subscription.
    #[serde(rename = "status")]
    pub status: Option<Box<crate::models::StripeSubscriptionStatusEnum>>,
    /// If the subscription has a trial, the end of that trial.
    #[serde(rename = "trial_end", skip_serializing_if = "Option::is_none")]
    pub trial_end: Option<String>,
    /// If the subscription has a trial, the beginning of that trial.
    #[serde(rename = "trial_start", skip_serializing_if = "Option::is_none")]
    pub trial_start: Option<String>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
    /// The customer associated with this subscription.
    #[serde(rename = "customer")]
    pub customer: String,
    /// The default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If not set, defaults to the customer's default source.
    #[serde(rename = "default_source", skip_serializing_if = "Option::is_none")]
    pub default_source: Option<String>,
    /// The most recent invoice this subscription has generated.
    #[serde(rename = "latest_invoice", skip_serializing_if = "Option::is_none")]
    pub latest_invoice: Option<String>,
    /// We can use this SetupIntent to collect user authentication when creating a subscription without immediate payment or updating a subscription's payment method, allowing you to optimize for off-session payments.
    #[serde(rename = "pending_setup_intent", skip_serializing_if = "Option::is_none")]
    pub pending_setup_intent: Option<String>,
    /// The tax rates that will apply to any subscription item that does not have tax_rates set. Invoices created will have their default_tax_rates populated from the subscription.
    #[serde(rename = "default_tax_rates", skip_serializing_if = "Option::is_none")]
    pub default_tax_rates: Option<Vec<i32>>,
}

impl StripeSubscription {
    pub fn new(djstripe_id: i32, plan: crate::models::StripePlan, default_payment_method: crate::models::StripePaymentMethod, schedule: crate::models::StripeSubscriptionSchedule, is_period_current: bool, is_status_current: bool, is_status_temporarily_current: bool, is_valid: bool, djstripe_created: String, djstripe_updated: String, id: String, collection_method: Option<crate::models::CollectionMethodEnum>, current_period_end: String, current_period_start: String, status: Option<crate::models::StripeSubscriptionStatusEnum>, customer: String) -> StripeSubscription {
        StripeSubscription {
            djstripe_id,
            plan: Box::new(plan),
            default_payment_method: Box::new(default_payment_method),
            schedule: Box::new(schedule),
            is_period_current,
            is_status_current,
            is_status_temporarily_current,
            is_valid,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            description: None,
            application_fee_percent: None,
            billing_cycle_anchor: None,
            billing_thresholds: None,
            cancel_at: None,
            cancel_at_period_end: None,
            canceled_at: None,
            collection_method: collection_method.map(Box::new),
            current_period_end,
            current_period_start,
            days_until_due: None,
            discount: None,
            ended_at: None,
            next_pending_invoice_item_invoice: None,
            pending_invoice_item_interval: None,
            pending_update: None,
            quantity: None,
            start_date: None,
            status: status.map(Box::new),
            trial_end: None,
            trial_start: None,
            djstripe_owner_account: None,
            customer,
            default_source: None,
            latest_invoice: None,
            pending_setup_intent: None,
            default_tax_rates: None,
        }
    }
}


