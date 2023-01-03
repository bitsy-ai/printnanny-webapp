/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OrderCheckoutRequest {
    #[serde(rename = "products")]
    pub products: Vec<String>,
    #[serde(rename = "email")]
    pub email: String,
}

impl OrderCheckoutRequest {
    pub fn new(products: Vec<String>, email: String) -> OrderCheckoutRequest {
        OrderCheckoutRequest {
            products,
            email,
        }
    }
}


