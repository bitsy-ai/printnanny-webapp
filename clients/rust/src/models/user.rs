/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.123.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct User {
    #[serde(rename = "email")]
    pub email: String,
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "first_name", skip_serializing_if = "Option::is_none")]
    pub first_name: Option<String>,
    #[serde(rename = "last_name", skip_serializing_if = "Option::is_none")]
    pub last_name: Option<String>,
    #[serde(rename = "is_beta_tester")]
    pub is_beta_tester: bool,
}

impl User {
    pub fn new(email: String, id: i32, is_beta_tester: bool) -> User {
        User {
            email,
            id,
            first_name: None,
            last_name: None,
            is_beta_tester,
        }
    }
}


