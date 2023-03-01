/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.127.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// CallbackTokenAuth : Abstract class inspired by DRF's own token serializer. Returns a user if valid, None or a message if not.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct CallbackTokenAuth {
    #[serde(rename = "email", skip_serializing_if = "Option::is_none")]
    pub email: Option<String>,
    #[serde(rename = "mobile", skip_serializing_if = "Option::is_none")]
    pub mobile: Option<String>,
    #[serde(rename = "token")]
    pub token: String,
}

impl CallbackTokenAuth {
    /// Abstract class inspired by DRF's own token serializer. Returns a user if valid, None or a message if not.
    pub fn new(token: String) -> CallbackTokenAuth {
        CallbackTokenAuth {
            email: None,
            mobile: None,
            token,
        }
    }
}


