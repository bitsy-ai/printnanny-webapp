/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintDeviceRequest {
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "model")]
    pub model: String,
    #[serde(rename = "platform")]
    pub platform: String,
    #[serde(rename = "cpu_flags", skip_serializing_if = "Option::is_none")]
    pub cpu_flags: Option<Vec<String>>,
    #[serde(rename = "hardware", skip_serializing_if = "Option::is_none")]
    pub hardware: Option<String>,
    #[serde(rename = "revision", skip_serializing_if = "Option::is_none")]
    pub revision: Option<String>,
    #[serde(rename = "serial")]
    pub serial: String,
    #[serde(rename = "cores")]
    pub cores: i32,
    #[serde(rename = "ram")]
    pub ram: i32,
    #[serde(rename = "python_version")]
    pub python_version: String,
    #[serde(rename = "pip_version")]
    pub pip_version: String,
    #[serde(rename = "virtualenv", skip_serializing_if = "Option::is_none")]
    pub virtualenv: Option<String>,
    #[serde(rename = "octoprint_version")]
    pub octoprint_version: String,
    #[serde(rename = "plugin_version")]
    pub plugin_version: String,
    #[serde(rename = "print_nanny_client_version")]
    pub print_nanny_client_version: String,
    #[serde(rename = "active_session", skip_serializing_if = "Option::is_none")]
    pub active_session: Option<Box<crate::models::PrintSessionRequest>>,
}

impl OctoPrintDeviceRequest {
    pub fn new(name: String, model: String, platform: String, serial: String, cores: i32, ram: i32, python_version: String, pip_version: String, octoprint_version: String, plugin_version: String, print_nanny_client_version: String) -> OctoPrintDeviceRequest {
        OctoPrintDeviceRequest {
            name,
            model,
            platform,
            cpu_flags: None,
            hardware: None,
            revision: None,
            serial,
            cores,
            ram,
            python_version,
            pip_version,
            virtualenv: None,
            octoprint_version,
            plugin_version,
            print_nanny_client_version,
            active_session: None,
        }
    }
}


