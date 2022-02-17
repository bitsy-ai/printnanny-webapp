/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Task {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "tasktype")]
    pub tasktype: crate::models::TasktypeEnum,
    #[serde(rename = "deleted")]
    pub deleted: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "polymorphic_ctype")]
    pub polymorphic_ctype: i32,
    #[serde(rename = "device")]
    pub device: i32,
}

impl Task {
    pub fn new(id: i32, tasktype: crate::models::TasktypeEnum, deleted: String, created_dt: String, polymorphic_ctype: i32, device: i32) -> Task {
        Task {
            id,
            tasktype,
            deleted,
            created_dt,
            polymorphic_ctype,
            device,
        }
    }
}


