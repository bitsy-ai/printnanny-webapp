/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
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
            nameSome(Some(,
            pathSome(Some(,
            display: NoneSome(,
            originSome(Some(,
            sizeSome(Some(,
            dateSome(Some(,
        }
    }
}


