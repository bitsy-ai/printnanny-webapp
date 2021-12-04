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
pub struct TaskStatus {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "detail", skip_serializing_if = "Option::is_none")]
    pub detail: Option<String>,
    #[serde(rename = "wiki_url", skip_serializing_if = "Option::is_none")]
    pub wiki_url: Option<String>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "status", skip_serializing_if = "Option::is_none")]
    pub status: Option<crate::models::TaskStatusType>,
    #[serde(rename = "task")]
    pub task: i32,
}

impl TaskStatus {
    pub fn new(id: i32, created_dt: String, task: i32) -> TaskStatus {
        TaskStatus {
            id,
            detail: None,
            wiki_url: None,
            created_dt,
            status: None,
            task,
        }
    }
}


