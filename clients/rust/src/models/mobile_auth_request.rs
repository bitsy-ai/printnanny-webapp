/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.94.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// MobileAuthRequest : Abstract class that returns a callback token based on the field given Returns a token if valid, None or a message if not.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct MobileAuthRequest {
    #[serde(rename = "mobile")]
    pub mobile: String,
}

impl MobileAuthRequest {
    /// Abstract class that returns a callback token based on the field given Returns a token if valid, None or a message if not.
    pub fn new(mobile: String) -> MobileAuthRequest {
        MobileAuthRequest {
            mobile,
        }
    }
}


