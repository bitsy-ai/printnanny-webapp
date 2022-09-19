/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.108.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OrderStatus {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "status")]
    pub status: crate::models::OrderStatusType,
    #[serde(rename = "order")]
    pub order: String,
}

impl OrderStatus {
    pub fn new(id: i32, deleted: String, created_dt: String, status: crate::models::OrderStatusType, order: String) -> OrderStatus {
        OrderStatus {
            id,
            deleted,
            created_dt,
            status,
            order,
        }
    }
}


