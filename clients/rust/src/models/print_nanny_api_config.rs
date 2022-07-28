/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.97.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PrintNannyApiConfig {
    #[serde(rename = "bearer_access_token")]
    pub bearer_access_token: Option<String>,
    #[serde(rename = "base_path")]
    pub base_path: String,
    #[serde(rename = "static_url")]
    pub static_url: String,
    #[serde(rename = "dashboard_url")]
    pub dashboard_url: String,
}

impl PrintNannyApiConfig {
    pub fn new(bearer_access_token: Option<String>, base_path: String, static_url: String, dashboard_url: String) -> PrintNannyApiConfig {
        PrintNannyApiConfig {
            bearer_access_token,
            base_path,
            static_url,
            dashboard_url,
        }
    }
}


