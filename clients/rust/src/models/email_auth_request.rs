/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// EmailAuthRequest : Abstract class that returns a callback token based on the field given Returns a token if valid, None or a message if not.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct EmailAuthRequest {
    #[serde(rename = "email")]
    pub email: String,
}

impl EmailAuthRequest {
    /// Abstract class that returns a callback token based on the field given Returns a token if valid, None or a message if not.
    pub fn new(email: String) -> EmailAuthRequest {
        EmailAuthRequest {
            email,
        }
    }
}


