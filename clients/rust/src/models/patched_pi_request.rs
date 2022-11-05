/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.114.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedPiRequest {
    #[serde(rename = "sbc", skip_serializing_if = "Option::is_none")]
    pub sbc: Option<crate::models::SbcEnum>,
    /// Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)
    #[serde(rename = "hostname", skip_serializing_if = "Option::is_none")]
    pub hostname: Option<String>,
    #[serde(rename = "fqdn", skip_serializing_if = "Option::is_none")]
    pub fqdn: Option<String>,
    #[serde(rename = "favorite", skip_serializing_if = "Option::is_none")]
    pub favorite: Option<bool>,
    #[serde(rename = "setup_finished", skip_serializing_if = "Option::is_none")]
    pub setup_finished: Option<bool>,
}

impl PatchedPiRequest {
    pub fn new() -> PatchedPiRequest {
        PatchedPiRequest {
            sbc: None,
            hostname: None,
            fqdn: None,
            favorite: None,
            setup_finished: None,
        }
    }
}


