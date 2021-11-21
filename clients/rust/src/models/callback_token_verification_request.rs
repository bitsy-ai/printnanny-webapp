/*
 * print-nanny-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */

/// CallbackTokenVerificationRequest : Takes a user and a token, verifies the token belongs to the user and validates the alias that the token was sent from.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct CallbackTokenVerificationRequest {
    #[serde(rename = "email", skip_serializing_if = "Option::is_none")]
    pub email: Option<String>,
    #[serde(rename = "mobile", skip_serializing_if = "Option::is_none")]
    pub mobile: Option<String>,
    #[serde(rename = "token")]
    pub token: String,
}

impl CallbackTokenVerificationRequest {
    /// Takes a user and a token, verifies the token belongs to the user and validates the alias that the token was sent from.
    pub fn new(token: String) -> CallbackTokenVerificationRequest {
        CallbackTokenVerificationRequest {
            email: None,
            mobile: None,
            token,
        }
    }
}


