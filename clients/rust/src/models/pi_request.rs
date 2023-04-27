/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.133.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PiRequest {
    #[serde(rename = "hostname")]
    pub hostname: String,
    #[serde(rename = "favorite")]
    pub favorite: bool,
    #[serde(rename = "sbc")]
    pub sbc: crate::models::SbcEnum,
    #[serde(rename = "setup_finished")]
    pub setup_finished: bool,
}

impl PiRequest {
    pub fn new(hostname: String, favorite: bool, sbc: crate::models::SbcEnum, setup_finished: bool) -> PiRequest {
        PiRequest {
            hostname,
            favorite,
            sbc,
            setup_finished,
        }
    }
}


