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
pub struct VerifyEmailRequest {
    #[serde(rename = "key")]
    pub key: String,
}

impl VerifyEmailRequest {
    pub fn new(key: String) -> VerifyEmailRequest {
        VerifyEmailRequest {
            key,
        }
    }
}


