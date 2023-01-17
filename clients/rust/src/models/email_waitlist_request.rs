/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct EmailWaitlistRequest {
    #[serde(rename = "email")]
    pub email: String,
}

impl EmailWaitlistRequest {
    pub fn new(email: String) -> EmailWaitlistRequest {
        EmailWaitlistRequest {
            email,
        }
    }
}


