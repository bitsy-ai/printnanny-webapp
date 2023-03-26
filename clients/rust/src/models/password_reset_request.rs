/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// PasswordResetRequest : Serializer for requesting a password reset e-mail.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PasswordResetRequest {
    #[serde(rename = "email")]
    pub email: String,
}

impl PasswordResetRequest {
    /// Serializer for requesting a password reset e-mail.
    pub fn new(email: String) -> PasswordResetRequest {
        PasswordResetRequest {
            email,
        }
    }
}


