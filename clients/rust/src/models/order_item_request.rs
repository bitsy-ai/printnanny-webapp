/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OrderItemRequest {
    #[serde(rename = "product")]
    pub product: String,
    #[serde(rename = "price")]
    pub price: String,
}

impl OrderItemRequest {
    pub fn new(product: String, price: String) -> OrderItemRequest {
        OrderItemRequest {
            product,
            price,
        }
    }
}


