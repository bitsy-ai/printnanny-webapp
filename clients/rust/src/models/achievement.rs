/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Achievement {
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "type")]
    pub _type: crate::models::AchievementTypeEnum,
    #[serde(rename = "label")]
    pub label: String,
    #[serde(rename = "user")]
    pub user: i32,
}

impl Achievement {
    pub fn new(created_dt: String, _type: crate::models::AchievementTypeEnum, label: String, user: i32) -> Achievement {
        Achievement {
            created_dt,
            _type,
            label,
            user,
        }
    }
}


