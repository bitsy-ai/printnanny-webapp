/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.134.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedPiRequest {
    #[serde(rename = "hostname", skip_serializing_if = "Option::is_none")]
    pub hostname: Option<String>,
    #[serde(rename = "favorite", skip_serializing_if = "Option::is_none")]
    pub favorite: Option<bool>,
    #[serde(rename = "sbc", skip_serializing_if = "Option::is_none")]
    pub sbc: Option<crate::models::SbcEnum>,
    #[serde(rename = "setup_finished", skip_serializing_if = "Option::is_none")]
    pub setup_finished: Option<bool>,
}

impl PatchedPiRequest {
    pub fn new() -> PatchedPiRequest {
        PatchedPiRequest {
            hostname: None,
            favorite: None,
            sbc: None,
            setup_finished: None,
        }
    }
}


