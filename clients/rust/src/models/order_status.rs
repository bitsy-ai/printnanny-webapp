/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OrderStatus {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "deleted")]
    pub deleted: Option<String>,
    #[serde(rename = "deleted_by_cascade")]
    pub deleted_by_cascade: bool,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "status")]
    pub status: crate::models::OrderStatusType,
    #[serde(rename = "order")]
    pub order: String,
}

impl OrderStatus {
    pub fn new(id: i32, deleted: Option<String>, deleted_by_cascade: bool, created_dt: String, status: crate::models::OrderStatusType, order: String) -> OrderStatus {
        OrderStatus {
            id,
            deleted,
            deleted_by_cascade,
            created_dt,
            status,
            order,
        }
    }
}


