/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.133.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct EmailWaitlistRequest {
    #[serde(rename = "email")]
    pub email: String,
    #[serde(rename = "interest", skip_serializing_if = "Option::is_none")]
    pub interest: Option<crate::models::InterestEnum>,
}

impl EmailWaitlistRequest {
    pub fn new(email: String) -> EmailWaitlistRequest {
        EmailWaitlistRequest {
            email,
            interest: None,
        }
    }
}


