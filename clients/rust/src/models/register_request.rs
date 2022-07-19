/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.94.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct RegisterRequest {
    #[serde(rename = "email")]
    pub email: String,
    #[serde(rename = "password1")]
    pub password1: String,
    #[serde(rename = "password2")]
    pub password2: String,
}

impl RegisterRequest {
    pub fn new(email: String, password1: String, password2: String) -> RegisterRequest {
        RegisterRequest {
            email,
            password1,
            password2,
        }
    }
}

