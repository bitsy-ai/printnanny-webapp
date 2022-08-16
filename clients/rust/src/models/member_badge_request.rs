/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.101.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct MemberBadgeRequest {
    #[serde(rename = "user")]
    pub user: i32,
}

impl MemberBadgeRequest {
    pub fn new(user: i32) -> MemberBadgeRequest {
        MemberBadgeRequest {
            user,
        }
    }
}


