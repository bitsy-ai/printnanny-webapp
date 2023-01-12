/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.122.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PaginatedPolymorphicOctoPrintEventList {
    #[serde(rename = "count", skip_serializing_if = "Option::is_none")]
    pub count: Option<i32>,
    #[serde(rename = "next", skip_serializing_if = "Option::is_none")]
    pub next: Option<String>,
    #[serde(rename = "previous", skip_serializing_if = "Option::is_none")]
    pub previous: Option<String>,
    #[serde(rename = "results", skip_serializing_if = "Option::is_none")]
    pub results: Option<Vec<crate::models::PolymorphicOctoPrintEvent>>,
}

impl PaginatedPolymorphicOctoPrintEventList {
    pub fn new() -> PaginatedPolymorphicOctoPrintEventList {
        PaginatedPolymorphicOctoPrintEventList {
            count: None,
            next: None,
            previous: None,
            results: None,
        }
    }
}


