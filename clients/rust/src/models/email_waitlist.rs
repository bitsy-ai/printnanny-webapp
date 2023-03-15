/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.128.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct EmailWaitlist {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "email")]
    pub email: String,
}

impl EmailWaitlist {
    pub fn new(id: i32, created_dt: String, email: String) -> EmailWaitlist {
        EmailWaitlist {
            id,
            created_dt,
            email,
        }
    }
}


