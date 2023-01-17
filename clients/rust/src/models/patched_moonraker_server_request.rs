/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedMoonrakerServerRequest {
    #[serde(rename = "base_path", skip_serializing_if = "Option::is_none")]
    pub base_path: Option<String>,
    #[serde(rename = "moonraker_version", skip_serializing_if = "Option::is_none")]
    pub moonraker_version: Option<String>,
    #[serde(rename = "pip_version", skip_serializing_if = "Option::is_none")]
    pub pip_version: Option<String>,
    #[serde(rename = "python_version", skip_serializing_if = "Option::is_none")]
    pub python_version: Option<String>,
    #[serde(rename = "api_key", skip_serializing_if = "Option::is_none")]
    pub api_key: Option<String>,
    #[serde(rename = "pi", skip_serializing_if = "Option::is_none")]
    pub pi: Option<i32>,
}

impl PatchedMoonrakerServerRequest {
    pub fn new() -> PatchedMoonrakerServerRequest {
        PatchedMoonrakerServerRequest {
            base_path: None,
            moonraker_version: None,
            pip_version: None,
            python_version: None,
            api_key: None,
            pi: None,
        }
    }
}


