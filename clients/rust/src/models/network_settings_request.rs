/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct NetworkSettingsRequest {
    #[serde(rename = "preferred_dns", skip_serializing_if = "Option::is_none")]
    pub preferred_dns: Option<crate::models::PreferredDnsType>,
    #[serde(rename = "user")]
    pub user: i32,
}

impl NetworkSettingsRequest {
    pub fn new(user: i32) -> NetworkSettingsRequest {
        NetworkSettingsRequest {
            preferred_dns: None,
            user,
        }
    }
}


