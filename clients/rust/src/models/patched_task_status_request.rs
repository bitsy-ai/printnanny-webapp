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
pub struct PatchedTaskStatusRequest {
    #[serde(rename = "detail", skip_serializing_if = "Option::is_none")]
    pub detail: Option<String>,
    #[serde(rename = "wiki_url", skip_serializing_if = "Option::is_none")]
    pub wiki_url: Option<String>,
    #[serde(rename = "status", skip_serializing_if = "Option::is_none")]
    pub status: Option<crate::models::TaskStatusType>,
    #[serde(rename = "task", skip_serializing_if = "Option::is_none")]
    pub task: Option<i32>,
}

impl PatchedTaskStatusRequest {
    pub fn new() -> PatchedTaskStatusRequest {
        PatchedTaskStatusRequest {
            detail: None,
            wiki_url: None,
            status: None,
            task: None,
        }
    }
}


