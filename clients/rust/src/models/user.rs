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
pub struct User {
    #[serde(rename = "email")]
    pub email: String,
    #[serde(rename = "id")]
    pub id: i32,
}

impl User {
    pub fn new(email: String, id: i32) -> User {
        User {
            email,
            id,
        }
    }
}


