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
pub struct TaskStatusRequest {
    #[serde(rename = "detail", skip_serializing_if = "Option::is_none")]
    pub detail: Option<String>,
    #[serde(rename = "wiki_url", skip_serializing_if = "Option::is_none")]
    pub wiki_url: Option<String>,
    #[serde(rename = "status")]
    pub status: crate::models::TaskStatusType,
    #[serde(rename = "status_display")]
    pub status_display: String,
    #[serde(rename = "css_class")]
    pub css_class: String,
    #[serde(rename = "task")]
    pub task: i32,
}

impl TaskStatusRequest {
    pub fn new(status: crate::models::TaskStatusType, status_display: String, css_class: String, task: i32) -> TaskStatusRequest {
        TaskStatusRequest {
            detail: None,
            wiki_url: None,
            status,
            status_display,
            css_class,
            task,
        }
    }
}


