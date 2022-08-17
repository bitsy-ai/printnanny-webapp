/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.102.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedSystemInfoRequest {
    /// Populated from /etc/machine-id
    #[serde(rename = "machine_id", skip_serializing_if = "Option::is_none")]
    pub machine_id: Option<String>,
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
    /// PrintNanny OS VERSION_ID from /etc/os-release
    #[serde(rename = "os_version_id", skip_serializing_if = "Option::is_none")]
    pub os_version_id: Option<String>,
    /// PrintNanny OS BUILD_ID from /etc/os-release
    #[serde(rename = "os_build_id", skip_serializing_if = "Option::is_none")]
    pub os_build_id: Option<String>,
    /// PrintNanny OS VARIANT_ID from /etc/os-release
    #[serde(rename = "os_variant_id", skip_serializing_if = "Option::is_none")]
    pub os_variant_id: Option<String>,
    /// Full contents of /etc/os-release in key:value format
    #[serde(rename = "os_release_json", skip_serializing_if = "Option::is_none")]
    pub os_release_json: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "pi", skip_serializing_if = "Option::is_none")]
    pub pi: Option<i32>,
}

impl PatchedSystemInfoRequest {
    pub fn new() -> PatchedSystemInfoRequest {
        PatchedSystemInfoRequest {
            machine_id: None,
            revision: None,
            model: None,
            serial: None,
            cores: None,
            ram: None,
            os_version_id: None,
            os_build_id: None,
            os_variant_id: None,
            os_release_json: None,
            pi: None,
        }
    }
}


