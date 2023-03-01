/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.127.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OrderCheckoutRequest {
    #[serde(rename = "items")]
    pub items: Vec<crate::models::OrderItemRequest>,
    #[serde(rename = "email")]
    pub email: String,
}

impl OrderCheckoutRequest {
    pub fn new(items: Vec<crate::models::OrderItemRequest>, email: String) -> OrderCheckoutRequest {
        OrderCheckoutRequest {
            items,
            email,
        }
    }
}


