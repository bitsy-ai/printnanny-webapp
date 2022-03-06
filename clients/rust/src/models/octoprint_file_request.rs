/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoprintFileRequest {
    #[serde(rename = "name")]
    pub name: Option<String>,
    #[serde(rename = "path")]
    pub path: Option<String>,
    #[serde(rename = "display", skip_serializing_if = "Option::is_none")]
    pub display: Option<String>,
    #[serde(rename = "origin")]
    pub origin: Option<String>,
    #[serde(rename = "size")]
    pub size: Option<i32>,
    #[serde(rename = "date")]
    pub date: Option<i32>,
}

impl OctoprintFileRequest {
    pub fn new(name: Option<String>, path: Option<String>, origin: Option<String>, size: Option<i32>, date: Option<i32>) -> OctoprintFileRequest {
        OctoprintFileRequest {
            name,
            path,
            display: None,
            origin,
            size,
            date,
        }
    }
}


