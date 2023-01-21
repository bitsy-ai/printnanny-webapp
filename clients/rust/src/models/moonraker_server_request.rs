/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct MoonrakerServerRequest {
    #[serde(rename = "base_path")]
    pub base_path: String,
    #[serde(rename = "moonraker_version", skip_serializing_if = "Option::is_none")]
    pub moonraker_version: Option<String>,
    #[serde(rename = "pip_version", skip_serializing_if = "Option::is_none")]
    pub pip_version: Option<String>,
    #[serde(rename = "python_version", skip_serializing_if = "Option::is_none")]
    pub python_version: Option<String>,
    #[serde(rename = "api_key", skip_serializing_if = "Option::is_none")]
    pub api_key: Option<String>,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl MoonrakerServerRequest {
    pub fn new(base_path: String, pi: i32) -> MoonrakerServerRequest {
        MoonrakerServerRequest {
            base_path,
            moonraker_version: None,
            pip_version: None,
            python_version: None,
            api_key: None,
            pi,
        }
    }
}


