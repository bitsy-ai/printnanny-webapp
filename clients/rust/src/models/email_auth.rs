/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// EmailAuth : Abstract class that returns a callback token based on the field given Returns a token if valid, None or a message if not.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct EmailAuth {
    #[serde(rename = "email")]
    pub email: String,
}

impl EmailAuth {
    /// Abstract class that returns a callback token based on the field given Returns a token if valid, None or a message if not.
    pub fn new(email: String) -> EmailAuth {
        EmailAuth {
            email,
        }
    }
}


