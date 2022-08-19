/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.103.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct MemberBadge {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "type")]
    pub _type: String,
    #[serde(rename = "label")]
    pub label: String,
    #[serde(rename = "user")]
    pub user: i32,
}

impl MemberBadge {
    pub fn new(id: i32, created_dt: String, updated_dt: String, _type: String, label: String, user: i32) -> MemberBadge {
        MemberBadge {
            id,
            created_dt,
            updated_dt,
            _type,
            label,
            user,
        }
    }
}


