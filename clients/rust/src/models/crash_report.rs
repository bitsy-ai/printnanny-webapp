/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct CrashReport {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "email", skip_serializing_if = "Option::is_none")]
    pub email: Option<String>,
    #[serde(rename = "os_version", skip_serializing_if = "Option::is_none")]
    pub os_version: Option<String>,
    #[serde(rename = "os_logs", skip_serializing_if = "Option::is_none")]
    pub os_logs: Option<String>,
    #[serde(rename = "browser_version", skip_serializing_if = "Option::is_none")]
    pub browser_version: Option<String>,
    #[serde(rename = "browser_logs", skip_serializing_if = "Option::is_none")]
    pub browser_logs: Option<String>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
    #[serde(rename = "pi", skip_serializing_if = "Option::is_none")]
    pub pi: Option<i32>,
}

impl CrashReport {
    pub fn new(id: String, created_dt: String) -> CrashReport {
        CrashReport {
            id,
            created_dt,
            email: None,
            os_version: None,
            os_logs: None,
            browser_version: None,
            browser_logs: None,
            user: None,
            pi: None,
        }
    }
}

