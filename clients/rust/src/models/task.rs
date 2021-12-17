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
    #[serde(rename = "last_status")]
    pub last_status: Option<Box<crate::models::TaskStatus>>,
    #[serde(rename = "task_type")]
    pub task_type: crate::models::TaskType,
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<bool>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "device")]
    pub device: i32,
}

impl Task {
    pub fn new(id: i32, last_status: Option<crate::models::TaskStatus>, task_type: crate::models::TaskType, created_dt: String, device: i32) -> Task {
        Task {
            id,
            last_status: last_status.map(Box::new),
            task_type,
            active: None,
            created_dt,
            device,
        }
    }
}


