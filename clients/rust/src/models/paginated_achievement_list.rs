/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.110.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PaginatedAchievementList {
    #[serde(rename = "count", skip_serializing_if = "Option::is_none")]
    pub count: Option<i32>,
    #[serde(rename = "next", skip_serializing_if = "Option::is_none")]
    pub next: Option<String>,
    #[serde(rename = "previous", skip_serializing_if = "Option::is_none")]
    pub previous: Option<String>,
    #[serde(rename = "results", skip_serializing_if = "Option::is_none")]
    pub results: Option<Vec<crate::models::Achievement>>,
}

impl PaginatedAchievementList {
    pub fn new() -> PaginatedAchievementList {
        PaginatedAchievementList {
            count: None,
            next: None,
            previous: None,
            results: None,
        }
    }
}

