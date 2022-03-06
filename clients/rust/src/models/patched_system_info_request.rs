/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedSystemInfoRequest {
    /// Populated from /etc/machine-id
    #[serde(rename = "machine_id", skip_serializing_if = "Option::is_none")]
    pub machine_id: Option<String>,
    /// Populated from /proc/cpuinfo HARDWARE
    #[serde(rename = "hardware", skip_serializing_if = "Option::is_none")]
    pub hardware: Option<String>,
    /// Populated from /proc/cpuinfo REVISION
    #[serde(rename = "revision", skip_serializing_if = "Option::is_none")]
    pub revision: Option<String>,
    /// Populated from /proc/cpuinfo MODEL
    #[serde(rename = "model", skip_serializing_if = "Option::is_none")]
    pub model: Option<String>,
    /// Populated from /proc/cpuinfo SERIAL
    #[serde(rename = "serial", skip_serializing_if = "Option::is_none")]
    pub serial: Option<String>,
    #[serde(rename = "cores", skip_serializing_if = "Option::is_none")]
    pub cores: Option<i32>,
    #[serde(rename = "ram", skip_serializing_if = "Option::is_none")]
    pub ram: Option<i64>,
    /// PrintNanny OS image version string from /boot/image_version.txt
    #[serde(rename = "image_version", skip_serializing_if = "Option::is_none")]
    pub image_version: Option<String>,
    /// PrintNanny OS ansible collection version string. Releaes: https://github.com/bitsy-ai/ansible-collection-printnanny
    #[serde(rename = "ansible_collection_version", skip_serializing_if = "Option::is_none")]
    pub ansible_collection_version: Option<String>,
    #[serde(rename = "device", skip_serializing_if = "Option::is_none")]
    pub device: Option<i32>,
}

impl PatchedSystemInfoRequest {
    pub fn new() -> PatchedSystemInfoRequest {
        PatchedSystemInfoRequest {
            machine_id: None,
            hardware: None,
            revision: None,
            model: None,
            serial: None,
            cores: None,
            ram: None,
            image_version: None,
            ansible_collection_version: None,
            device: None,
        }
    }
}


