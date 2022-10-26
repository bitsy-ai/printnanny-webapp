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
pub struct DjStripePaymentIntent {
    #[serde(rename = "djstripe_id")]
    pub djstripe_id: i32,
    #[serde(rename = "cancellation_reason")]
    pub cancellation_reason: crate::models::StripePaymentIntentCancellationReason,
    #[serde(rename = "charges")]
    pub charges: Vec<crate::models::DjStripeCharge>,
    #[serde(rename = "setup_future_usage")]
    pub setup_future_usage: crate::models::StripeIntentUsage,
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
    /// Amount (in cents) intended to be collected by this PaymentIntent.
    #[serde(rename = "amount")]
    pub amount: i64,
    /// Amount (in cents) that can be captured from this PaymentIntent.
    #[serde(rename = "amount_capturable")]
    pub amount_capturable: i64,
    /// Amount (in cents) that was collected by this PaymentIntent.
    #[serde(rename = "amount_received")]
    pub amount_received: i64,
    /// Populated when status is canceled, this is the time at which the PaymentIntent was canceled. Measured in seconds since the Unix epoch.
    #[serde(rename = "canceled_at", skip_serializing_if = "Option::is_none")]
    pub canceled_at: Option<String>,
    /// Capture method of this PaymentIntent, one of automatic or manual.
    #[serde(rename = "capture_method")]
    pub capture_method: Option<Box<crate::models::StripeConfirmationMethod>>,
    /// The client secret of this PaymentIntent. Used for client-side retrieval using a publishable key.
    #[serde(rename = "client_secret")]
    pub client_secret: String,
    /// Confirmation method of this PaymentIntent, one of manual or automatic.
    #[serde(rename = "confirmation_method")]
    pub confirmation_method: Option<Box<crate::models::StripeConfirmationMethod>>,
    /// Three-letter ISO currency code
    #[serde(rename = "currency")]
    pub currency: String,
    /// An arbitrary string attached to the object. Often useful for displaying to users.
    #[serde(rename = "description", skip_serializing_if = "Option::is_none")]
    pub description: Option<String>,
    /// The payment error encountered in the previous PaymentIntent confirmation.
    #[serde(rename = "last_payment_error", skip_serializing_if = "Option::is_none")]
    pub last_payment_error: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// If present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source.
    #[serde(rename = "next_action", skip_serializing_if = "Option::is_none")]
    pub next_action: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The list of payment method types (e.g. card) that this PaymentIntent is allowed to use.
    #[serde(rename = "payment_method_types")]
    pub payment_method_types: ::std::collections::HashMap<String, serde_json::Value>,
    /// Email address that the receipt for the resulting payment will be sent to.
    #[serde(rename = "receipt_email", skip_serializing_if = "Option::is_none")]
    pub receipt_email: Option<String>,
    /// Shipping information for this PaymentIntent.
    #[serde(rename = "shipping", skip_serializing_if = "Option::is_none")]
    pub shipping: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// For non-card charges, you can use this value as the complete description that appears on your customers' statements. Must contain at least one letter, maximum 22 characters.
    #[serde(rename = "statement_descriptor", skip_serializing_if = "Option::is_none")]
    pub statement_descriptor: Option<String>,
    /// Status of this PaymentIntent, one of requires_payment_method, requires_confirmation, requires_action, processing, requires_capture, canceled, or succeeded. You can read more about PaymentIntent statuses here.
    #[serde(rename = "status")]
    pub status: Option<Box<crate::models::StripePaymentIntentStatus>>,
    /// The data with which to automatically create a Transfer when the payment is finalized. See the PaymentIntents Connect usage guide for details.
    #[serde(rename = "transfer_data", skip_serializing_if = "Option::is_none")]
    pub transfer_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// A string that identifies the resulting payment as part of a group. See the PaymentIntents Connect usage guide for details.
    #[serde(rename = "transfer_group", skip_serializing_if = "Option::is_none")]
    pub transfer_group: Option<String>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
    /// Customer this PaymentIntent is for if one exists.
    #[serde(rename = "customer", skip_serializing_if = "Option::is_none")]
    pub customer: Option<String>,
    /// The account (if any) for which the funds of the PaymentIntent are intended.
    #[serde(rename = "on_behalf_of", skip_serializing_if = "Option::is_none")]
    pub on_behalf_of: Option<String>,
    /// Payment method used in this PaymentIntent.
    #[serde(rename = "payment_method", skip_serializing_if = "Option::is_none")]
    pub payment_method: Option<String>,
}

impl DjStripePaymentIntent {
    pub fn new(djstripe_id: i32, cancellation_reason: crate::models::StripePaymentIntentCancellationReason, charges: Vec<crate::models::DjStripeCharge>, setup_future_usage: crate::models::StripeIntentUsage, djstripe_created: String, djstripe_updated: String, id: String, amount: i64, amount_capturable: i64, amount_received: i64, capture_method: Option<crate::models::StripeConfirmationMethod>, client_secret: String, confirmation_method: Option<crate::models::StripeConfirmationMethod>, currency: String, payment_method_types: ::std::collections::HashMap<String, serde_json::Value>, status: Option<crate::models::StripePaymentIntentStatus>) -> DjStripePaymentIntent {
        DjStripePaymentIntent {
            djstripe_id,
            cancellation_reason,
            charges,
            setup_future_usage,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            amount,
            amount_capturable,
            amount_received,
            canceled_at: None,
            capture_method: capture_method.map(Box::new),
            client_secret,
            confirmation_method: confirmation_method.map(Box::new),
            currency,
            description: None,
            last_payment_error: None,
            next_action: None,
            payment_method_types,
            receipt_email: None,
            shipping: None,
            statement_descriptor: None,
            status: status.map(Box::new),
            transfer_data: None,
            transfer_group: None,
            djstripe_owner_account: None,
            customer: None,
            on_behalf_of: None,
            payment_method: None,
        }
    }
}


