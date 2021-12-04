/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum TaskStatusType {
    #[serde(rename = "failed")]
    Failed,
    #[serde(rename = "requested")]
    Requested,
    #[serde(rename = "started")]
    Started,
    #[serde(rename = "success")]
    Success,
    #[serde(rename = "timeout")]
    Timeout,

}

impl ToString for TaskStatusType {
    fn to_string(&self) -> String {
        match self {
            Self::Failed => String::from("failed"),
            Self::Requested => String::from("requested"),
            Self::Started => String::from("started"),
            Self::Success => String::from("success"),
            Self::Timeout => String::from("timeout"),
        }
    }
}

impl Default for TaskStatusType {
    fn default() -> TaskStatusType {
        Self::Failed
    }
}




