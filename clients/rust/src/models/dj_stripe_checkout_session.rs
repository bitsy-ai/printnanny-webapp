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
pub struct DjStripeCheckoutSession {
    #[serde(rename = "djstripe_id")]
    pub djstripe_id: i32,
    #[serde(rename = "billing_address_collection")]
    pub billing_address_collection: crate::models::StripeSessionBillingAddressCollection,
    #[serde(rename = "mode")]
    pub mode: crate::models::StripeSessionMode,
    #[serde(rename = "submit_type")]
    pub submit_type: crate::models::StripeSubmitTypeStatus,
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
    /// The URL the customer will be directed to if theydecide to cancel payment and return to your website.
    #[serde(rename = "cancel_url", skip_serializing_if = "Option::is_none")]
    pub cancel_url: Option<String>,
    /// A unique string to reference the Checkout Session.This can be a customer ID, a cart ID, or similar, andcan be used to reconcile the session with your internal systems.
    #[serde(rename = "client_reference_id", skip_serializing_if = "Option::is_none")]
    pub client_reference_id: Option<String>,
    /// If provided, this value will be used when the Customer object is created.
    #[serde(rename = "customer_email", skip_serializing_if = "Option::is_none")]
    pub customer_email: Option<String>,
    /// The line items, plans, or SKUs purchased by the customer.
    #[serde(rename = "display_items", skip_serializing_if = "Option::is_none")]
    pub display_items: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The IETF language tag of the locale Checkout is displayed in.If blank or auto, the browser's locale is used.
    #[serde(rename = "locale", skip_serializing_if = "Option::is_none")]
    pub locale: Option<String>,
    /// The list of payment method types (e.g. card) that this Checkout Session is allowed to accept.
    #[serde(rename = "payment_method_types")]
    pub payment_method_types: ::std::collections::HashMap<String, serde_json::Value>,
    /// The URL the customer will be directed to after the payment or subscriptioncreation is successful.
    #[serde(rename = "success_url", skip_serializing_if = "Option::is_none")]
    pub success_url: Option<String>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
    /// Customer this Checkout is for if one exists.
    #[serde(rename = "customer", skip_serializing_if = "Option::is_none")]
    pub customer: Option<String>,
    /// PaymentIntent created if SKUs or line items were provided.
    #[serde(rename = "payment_intent", skip_serializing_if = "Option::is_none")]
    pub payment_intent: Option<String>,
    /// Subscription created if one or more plans were provided.
    #[serde(rename = "subscription", skip_serializing_if = "Option::is_none")]
    pub subscription: Option<String>,
}

impl DjStripeCheckoutSession {
    pub fn new(djstripe_id: i32, billing_address_collection: crate::models::StripeSessionBillingAddressCollection, mode: crate::models::StripeSessionMode, submit_type: crate::models::StripeSubmitTypeStatus, djstripe_created: String, djstripe_updated: String, id: String, payment_method_types: ::std::collections::HashMap<String, serde_json::Value>) -> DjStripeCheckoutSession {
        DjStripeCheckoutSession {
            djstripe_id,
            billing_address_collection,
            mode,
            submit_type,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            description: None,
            cancel_url: None,
            client_reference_id: None,
            customer_email: None,
            display_items: None,
            locale: None,
            payment_method_types,
            success_url: None,
            djstripe_owner_account: None,
            customer: None,
            payment_intent: None,
            subscription: None,
        }
    }
}


