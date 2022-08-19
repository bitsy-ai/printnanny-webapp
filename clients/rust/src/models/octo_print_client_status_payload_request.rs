/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.102.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintClientStatusPayloadRequest {
    #[serde(rename = "remoteAddress")]
    pub remote_address: String,
    #[serde(rename = "username", skip_serializing_if = "Option::is_none")]
    pub username: Option<String>,
}

impl OctoPrintClientStatusPayloadRequest {
    pub fn new(remote_address: String) -> OctoPrintClientStatusPayloadRequest {
        OctoPrintClientStatusPayloadRequest {
            remote_address,
            username: None,
        }
    }
}


