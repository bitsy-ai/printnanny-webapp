/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// Order : Djstripe's representation of Stripe Checkout model is missing a number of fields, like subtotal amount and shipping/tax charges  stripe_checkout_session_data is the raw JSON returned by stripe.checkout.Session.retrieve



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Order {
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "djstripe_checkout_session")]
    pub djstripe_checkout_session: Option<Box<crate::models::DjStripeCheckoutSession>>,
    #[serde(rename = "djstripe_customer")]
    pub djstripe_customer: Option<Box<crate::models::DjStripeCustomer>>,
    #[serde(rename = "djstripe_payment_intent")]
    pub djstripe_payment_intent: Option<Box<crate::models::DjStripePaymentIntent>>,
    #[serde(rename = "email")]
    pub email: String,
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "is_shippable")]
    pub is_shippable: bool,
    #[serde(rename = "is_subscription")]
    pub is_subscription: bool,
    #[serde(rename = "last_status")]
    pub last_status: Box<crate::models::OrderStatus>,
    #[serde(rename = "products")]
    pub products: Vec<crate::models::Product>,
    #[serde(rename = "status_history")]
    pub status_history: Vec<crate::models::OrderStatus>,
    #[serde(rename = "stripe_checkout_session_data")]
    pub stripe_checkout_session_data: ::std::collections::HashMap<String, serde_json::Value>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<Box<crate::models::User>>,
    #[serde(rename = "receipt_url")]
    pub receipt_url: Option<String>,
    #[serde(rename = "portal_url")]
    pub portal_url: Option<String>,
}

impl Order {
    /// Djstripe's representation of Stripe Checkout model is missing a number of fields, like subtotal amount and shipping/tax charges  stripe_checkout_session_data is the raw JSON returned by stripe.checkout.Session.retrieve
    pub fn new(created_dt: String, djstripe_checkout_session: Option<crate::models::DjStripeCheckoutSession>, djstripe_customer: Option<crate::models::DjStripeCustomer>, djstripe_payment_intent: Option<crate::models::DjStripePaymentIntent>, email: String, id: String, is_shippable: bool, is_subscription: bool, last_status: crate::models::OrderStatus, products: Vec<crate::models::Product>, status_history: Vec<crate::models::OrderStatus>, stripe_checkout_session_data: ::std::collections::HashMap<String, serde_json::Value>, receipt_url: Option<String>, portal_url: Option<String>) -> Order {
        Order {
            created_dt,
            djstripe_checkout_session: djstripe_checkout_session.map(Box::new),
            djstripe_customer: djstripe_customer.map(Box::new),
            djstripe_payment_intent: djstripe_payment_intent.map(Box::new),
            email,
            id,
            is_shippable,
            is_subscription,
            last_status: Box::new(last_status),
            products,
            status_history,
            stripe_checkout_session_data,
            user: None,
            receipt_url,
            portal_url,
        }
    }
}


