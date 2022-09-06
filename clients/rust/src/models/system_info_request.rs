/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.107.2
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
    /// system uptime (in seconds)
    #[serde(rename = "uptime")]
    pub uptime: i64,
    /// Size of /dev/root filesystem in bytes
    #[serde(rename = "rootfs_size")]
    pub rootfs_size: i64,
    /// Space used in /dev/root filesystem in bytes
    #[serde(rename = "rootfs_used")]
    pub rootfs_used: i64,
    /// Size of /dev/mmcblk0p1 filesystem in bytes
    #[serde(rename = "bootfs_size")]
    pub bootfs_size: i64,
    /// Space used in /dev/mmcblk0p1 filesystem in bytes
    #[serde(rename = "bootfs_used")]
    pub bootfs_used: i64,
    /// Size of /dev/mmcblk0p4 filesystem in bytes
    #[serde(rename = "datafs_size")]
    pub datafs_size: i64,
    /// Space used in /dev/mmcblk0p4 filesystem in bytes
    #[serde(rename = "datafs_used")]
    pub datafs_used: i64,
    #[serde(rename = "pi")]
    pub pi: i32,
}

impl SystemInfoRequest {
    pub fn new(machine_id: String, revision: String, model: String, serial: String, cores: i32, ram: i64, os_version_id: String, os_build_id: String, os_variant_id: String, uptime: i64, rootfs_size: i64, rootfs_used: i64, bootfs_size: i64, bootfs_used: i64, datafs_size: i64, datafs_used: i64, pi: i32) -> SystemInfoRequest {
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
            uptime,
            rootfs_size,
            rootfs_used,
            bootfs_size,
            bootfs_used,
            datafs_size,
            datafs_used,
            pi,
        }
    }
}


