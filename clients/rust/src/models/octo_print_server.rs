/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.133.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintServer {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "settings")]
    pub settings: Option<Box<crate::models::OctoPrintSettings>>,
    #[serde(rename = "base_url")]
    pub base_url: String,
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
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "api_key", skip_serializing_if = "Option::is_none")]
    pub api_key: Option<String>,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl OctoPrintServer {
    pub fn new(id: i32, settings: Option<crate::models::OctoPrintSettings>, base_url: String, base_path: String, venv_path: String, pip_path: String, python_path: String, created_dt: String, updated_dt: String, user: i32, pi: i32) -> OctoPrintServer {
        OctoPrintServer {
            id,
            settings: settings.map(Box::new),
            base_url,
            base_path,
            venv_path,
            pip_path,
            python_path,
            octoprint_version: None,
            pip_version: None,
            python_version: None,
            printnanny_plugin_version: None,
            created_dt,
            updated_dt,
            api_key: None,
            user,
            pi,
        }
    }
}


