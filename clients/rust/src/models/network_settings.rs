/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.121.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct NetworkSettings {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "preferred_dns", skip_serializing_if = "Option::is_none")]
    pub preferred_dns: Option<crate::models::PreferredDnsType>,
    #[serde(rename = "user")]
    pub user: i32,
}

impl NetworkSettings {
    pub fn new(id: i32, updated_dt: String, user: i32) -> NetworkSettings {
        NetworkSettings {
            id,
            updated_dt,
            preferred_dns: None,
            user,
        }
    }
}

