/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// DetailResponse : Generic auth response serializer



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct DetailResponse {
    #[serde(rename = "detail")]
    pub detail: String,
}

impl DetailResponse {
    /// Generic auth response serializer
    pub fn new(detail: String) -> DetailResponse {
        DetailResponse {
            detail,
        }
    }
}


