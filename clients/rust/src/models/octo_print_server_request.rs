/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintServerRequest {
    #[serde(rename = "base_path")]
    pub base_path: String,
    #[serde(rename = "venv_path")]
    pub venv_path: String,
    #[serde(rename = "pip_path")]
    pub pip_path: String,
    #[serde(rename = "python_path")]
    pub python_path: String,
    #[serde(rename = "octoprint_version", skip_serializing_if = "Option::is_none")]
    pub octoprint_version: Option<String>,
    #[serde(rename = "pip_version", skip_serializing_if = "Option::is_none")]
    pub pip_version: Option<String>,
    #[serde(rename = "python_version", skip_serializing_if = "Option::is_none")]
    pub python_version: Option<String>,
    #[serde(rename = "printnanny_plugin_version", skip_serializing_if = "Option::is_none")]
    pub printnanny_plugin_version: Option<String>,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintServerRequest {
    pub fn new(base_path: String, venv_path: String, pip_path: String, python_path: String, pi: i32) -> OctoPrintServerRequest {
        OctoPrintServerRequest {
            base_path,
            venv_path,
            pip_path,
            python_path,
            octoprint_version: None,
            pip_version: None,
            python_version: None,
            printnanny_plugin_version: None,
            pi,
        }
    }
}


