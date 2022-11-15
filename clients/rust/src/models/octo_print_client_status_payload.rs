/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.116.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintClientStatusPayload {
    #[serde(rename = "remoteAddress")]
    pub remote_address: String,
    #[serde(rename = "username", skip_serializing_if = "Option::is_none")]
    pub username: Option<String>,
}

impl OctoPrintClientStatusPayload {
    pub fn new(remote_address: String) -> OctoPrintClientStatusPayload {
        OctoPrintClientStatusPayload {
            remote_address,
            username: None,
        }
    }
}


