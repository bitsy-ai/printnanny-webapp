/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PasswordChangeRequest {
    #[serde(rename = "new_password1")]
    pub new_password1: String,
    #[serde(rename = "new_password2")]
    pub new_password2: String,
}

impl PasswordChangeRequest {
    pub fn new(new_password1: String, new_password2: String) -> PasswordChangeRequest {
        PasswordChangeRequest {
            new_password1,
            new_password2,
        }
    }
}


