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
pub struct SystemInfo {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    /// Populated from /etc/machine-id
    #[serde(rename = "machine_id")]
    pub machine_id: String,
    /// Populated from /proc/cpuinfo HARDWARE
    #[serde(rename = "hardware")]
    pub hardware: String,
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
    #[serde(rename = "device")]
    pub device: i32,
}

impl SystemInfo {
    pub fn new(id: i32, created_dt: String, updated_dt: String, machine_id: String, hardware: String, revision: String, model: String, serial: String, cores: i32, ram: i64, os_version_id: String, os_build_id: String, device: i32) -> SystemInfo {
        SystemInfo {
            id,
            created_dt,
            updated_dt,
            machine_id,
            hardware,
            revision,
            model,
            serial,
            cores,
            ram,
            os_version_id,
            os_build_id,
            device,
        }
    }
}


