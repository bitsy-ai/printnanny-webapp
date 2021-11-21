/*
 * print-nanny-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintDevice {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<i32>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
    #[serde(rename = "public_key", skip_serializing_if = "Option::is_none")]
    pub public_key: Option<String>,
    #[serde(rename = "fingerprint", skip_serializing_if = "Option::is_none")]
    pub fingerprint: Option<String>,
    #[serde(rename = "cloudiot_device", skip_serializing_if = "Option::is_none")]
    pub cloudiot_device: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "cloudiot_device_name", skip_serializing_if = "Option::is_none")]
    pub cloudiot_device_name: Option<String>,
    #[serde(rename = "cloudiot_device_path", skip_serializing_if = "Option::is_none")]
    pub cloudiot_device_path: Option<String>,
    #[serde(rename = "cloudiot_device_num_id", skip_serializing_if = "Option::is_none")]
    pub cloudiot_device_num_id: Option<i32>,
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
    #[serde(rename = "cloudiot_device_configs", skip_serializing_if = "Option::is_none")]
    pub cloudiot_device_configs: Option<String>,
    #[serde(rename = "manage_url", skip_serializing_if = "Option::is_none")]
    pub manage_url: Option<String>,
    #[serde(rename = "monitoring_active", skip_serializing_if = "Option::is_none")]
    pub monitoring_active: Option<bool>,
    #[serde(rename = "active_session", skip_serializing_if = "Option::is_none")]
    pub active_session: Option<Box<crate::models::PrintSession>>,
}

impl OctoPrintDevice {
    pub fn new(name: String, model: String, platform: String, serial: String, cores: i32, ram: i32, python_version: String, pip_version: String, octoprint_version: String, plugin_version: String, print_nanny_client_version: String) -> OctoPrintDevice {
        OctoPrintDevice {
            id: None,
            created_dt: None,
            name,
            user: None,
            public_key: None,
            fingerprint: None,
            cloudiot_device: None,
            cloudiot_device_name: None,
            cloudiot_device_path: None,
            cloudiot_device_num_id: None,
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
            cloudiot_device_configs: None,
            manage_url: None,
            monitoring_active: None,
            active_session: None,
        }
    }
}


