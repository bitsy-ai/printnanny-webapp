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
pub struct PrintNannyApiConfig {
    #[serde(rename = "bearer_access_token")]
    pub bearer_access_token: String,
    #[serde(rename = "base_path")]
    pub base_path: String,
    #[serde(rename = "device_id")]
    pub device_id: i32,
    #[serde(rename = "user_id")]
    pub user_id: String,
    #[serde(rename = "user_email")]
    pub user_email: String,
}

impl PrintNannyApiConfig {
    pub fn new(bearer_access_token: String, base_path: String, device_id: i32, user_id: String, user_email: String) -> PrintNannyApiConfig {
        PrintNannyApiConfig {
            bearer_access_token,
            base_path,
            device_id,
            user_id,
            user_email,
        }
    }
}


