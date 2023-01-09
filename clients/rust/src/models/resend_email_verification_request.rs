/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.121.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct ResendEmailVerificationRequest {
    #[serde(rename = "email")]
    pub email: String,
}

impl ResendEmailVerificationRequest {
    pub fn new(email: String) -> ResendEmailVerificationRequest {
        ResendEmailVerificationRequest {
            email,
        }
    }
}


