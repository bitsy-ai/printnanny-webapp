/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.6
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// Token : Serializer for Token model.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Token {
    #[serde(rename = "key")]
    pub key: String,
}

impl Token {
    /// Serializer for Token model.
    pub fn new(key: String) -> Token {
        Token {
            key,
        }
    }
}


