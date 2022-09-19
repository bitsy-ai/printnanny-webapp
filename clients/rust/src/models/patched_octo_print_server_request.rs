/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.108.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedOctoPrintServerRequest {
    #[serde(rename = "base_path", skip_serializing_if = "Option::is_none")]
    pub base_path: Option<String>,
    #[serde(rename = "venv_path", skip_serializing_if = "Option::is_none")]
    pub venv_path: Option<String>,
    #[serde(rename = "pip_path", skip_serializing_if = "Option::is_none")]
    pub pip_path: Option<String>,
    #[serde(rename = "python_path", skip_serializing_if = "Option::is_none")]
    pub python_path: Option<String>,
    #[serde(rename = "octoprint_version", skip_serializing_if = "Option::is_none")]
    pub octoprint_version: Option<String>,
    #[serde(rename = "pip_version", skip_serializing_if = "Option::is_none")]
    pub pip_version: Option<String>,
    #[serde(rename = "python_version", skip_serializing_if = "Option::is_none")]
    pub python_version: Option<String>,
    #[serde(rename = "printnanny_plugin_version", skip_serializing_if = "Option::is_none")]
    pub printnanny_plugin_version: Option<String>,
    #[serde(rename = "pi", skip_serializing_if = "Option::is_none")]
    pub pi: Option<i32>,
}

impl PatchedOctoPrintServerRequest {
    pub fn new() -> PatchedOctoPrintServerRequest {
        PatchedOctoPrintServerRequest {
            base_path: None,
            venv_path: None,
            pip_path: None,
            python_path: None,
            octoprint_version: None,
            pip_version: None,
            python_version: None,
            printnanny_plugin_version: None,
            pi: None,
        }
    }
}


