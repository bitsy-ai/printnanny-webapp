/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.6
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct CrashReport {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "url")]
    pub url: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "description", skip_serializing_if = "Option::is_none")]
    pub description: Option<String>,
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
    #[serde(rename = "serial", skip_serializing_if = "Option::is_none")]
    pub serial: Option<String>,
    #[serde(rename = "posthog_session", skip_serializing_if = "Option::is_none")]
    pub posthog_session: Option<String>,
    #[serde(rename = "status", skip_serializing_if = "Option::is_none")]
    pub status: Option<crate::models::CrashReportStatusEnum>,
    #[serde(rename = "support_comment", skip_serializing_if = "Option::is_none")]
    pub support_comment: Option<String>,
    #[serde(rename = "user")]
    pub user: Option<i32>,
    #[serde(rename = "pi", skip_serializing_if = "Option::is_none")]
    pub pi: Option<i32>,
}

impl CrashReport {
    pub fn new(id: String, url: String, created_dt: String, updated_dt: String, user: Option<i32>) -> CrashReport {
        CrashReport {
            id,
            url,
            created_dt,
            updated_dt,
            description: None,
            email: None,
            os_version: None,
            os_logs: None,
            browser_version: None,
            browser_logs: None,
            serial: None,
            posthog_session: None,
            status: None,
            support_comment: None,
            user,
            pi: None,
        }
    }
}


