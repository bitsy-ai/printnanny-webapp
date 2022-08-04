/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// TokenResponse : Our default response serializer.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct TokenResponse {
    #[serde(rename = "token")]
    pub token: String,
}

impl TokenResponse {
    /// Our default response serializer.
    pub fn new(token: String) -> TokenResponse {
        TokenResponse {
            token,
        }
    }
}


