/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.120.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedPiSettingsRequest {
    #[serde(rename = "preferred_dns", skip_serializing_if = "Option::is_none")]
    pub preferred_dns: Option<crate::models::PreferredDnsEnum>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
}

impl PatchedPiSettingsRequest {
    pub fn new() -> PatchedPiSettingsRequest {
        PatchedPiSettingsRequest {
            preferred_dns: None,
            user: None,
        }
    }
}


