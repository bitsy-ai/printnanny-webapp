/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct UserRequest {
    #[serde(rename = "email")]
    pub email: String,
}

impl UserRequest {
    pub fn new(email: String) -> UserRequest {
        UserRequest {
            email,
        }
    }
}


