/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.6
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// PasswordResetConfirmRequest : Serializer for confirming a password reset attempt.



#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PasswordResetConfirmRequest {
    #[serde(rename = "new_password1")]
    pub new_password1: String,
    #[serde(rename = "new_password2")]
    pub new_password2: String,
    #[serde(rename = "uid")]
    pub uid: String,
    #[serde(rename = "token")]
    pub token: String,
}

impl PasswordResetConfirmRequest {
    /// Serializer for confirming a password reset attempt.
    pub fn new(new_password1: String, new_password2: String, uid: String, token: String) -> PasswordResetConfirmRequest {
        PasswordResetConfirmRequest {
            new_password1,
            new_password2,
            uid,
            token,
        }
    }
}


