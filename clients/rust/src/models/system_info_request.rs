/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.101.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct SystemInfoRequest {
    /// Populated from /etc/machine-id
    #[serde(rename = "machine_id")]
    pub machine_id: String,
    /// Populated from /proc/cpuinfo REVISION
    #[serde(rename = "revision")]
    pub revision: String,
    /// Populated from /proc/cpuinfo MODEL
    #[serde(rename = "model")]
    pub model: String,
    /// Populated from /proc/cpuinfo SERIAL
    #[serde(rename = "serial")]
    pub serial: String,
    #[serde(rename = "cores")]
    pub cores: i32,
    #[serde(rename = "ram")]
    pub ram: i64,
    /// PrintNanny OS VERSION_ID from /etc/os-release
    #[serde(rename = "os_version_id")]
    pub os_version_id: String,
    /// PrintNanny OS BUILD_ID from /etc/os-release
    #[serde(rename = "os_build_id")]
    pub os_build_id: String,
    /// PrintNanny OS VARIANT_ID from /etc/os-release
    #[serde(rename = "os_variant_id")]
    pub os_variant_id: String,
    /// Full contents of /etc/os-release in key:value format
    #[serde(rename = "os_release_json", skip_serializing_if = "Option::is_none")]
    pub os_release_json: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl SystemInfoRequest {
    pub fn new(machine_id: String, revision: String, model: String, serial: String, cores: i32, ram: i64, os_version_id: String, os_build_id: String, os_variant_id: String, pi: i32) -> SystemInfoRequest {
        SystemInfoRequest {
            machine_id,
            revision,
            model,
            serial,
            cores,
            ram,
            os_version_id,
            os_build_id,
            os_variant_id,
            os_release_json: None,
            pi,
        }
    }
}


