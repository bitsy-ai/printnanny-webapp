/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.123.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OrderCheckout {
    #[serde(rename = "products")]
    pub products: Vec<String>,
    #[serde(rename = "email")]
    pub email: String,
    #[serde(rename = "stripe_checkout_redirect_url")]
    pub stripe_checkout_redirect_url: String,
    #[serde(rename = "stripe_checkout_session_id")]
    pub stripe_checkout_session_id: String,
}

impl OrderCheckout {
    pub fn new(products: Vec<String>, email: String, stripe_checkout_redirect_url: String, stripe_checkout_session_id: String) -> OrderCheckout {
        OrderCheckout {
            products,
            email,
            stripe_checkout_redirect_url,
            stripe_checkout_session_id,
        }
    }
}


