/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.2
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
    /// Full contents of /etc/os-release in key:value format
    #[serde(rename = "os_release_json", skip_serializing_if = "Option::is_none")]
    pub os_release_json: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// system uptime (in seconds)
    #[serde(rename = "uptime", skip_serializing_if = "Option::is_none")]
    pub uptime: Option<i64>,
    /// Size of /dev/root filesystem in bytes
    #[serde(rename = "rootfs_size", skip_serializing_if = "Option::is_none")]
    pub rootfs_size: Option<i64>,
    /// Space used in /dev/root filesystem in bytes
    #[serde(rename = "rootfs_used", skip_serializing_if = "Option::is_none")]
    pub rootfs_used: Option<i64>,
    /// Size of /dev/mmcblk0p1 filesystem in bytes
    #[serde(rename = "bootfs_size", skip_serializing_if = "Option::is_none")]
    pub bootfs_size: Option<i64>,
    /// Space used in /dev/mmcblk0p1 filesystem in bytes
    #[serde(rename = "bootfs_used", skip_serializing_if = "Option::is_none")]
    pub bootfs_used: Option<i64>,
    /// Size of /dev/mmcblk0p4 filesystem in bytes
    #[serde(rename = "datafs_size", skip_serializing_if = "Option::is_none")]
    pub datafs_size: Option<i64>,
    /// Space used in /dev/mmcblk0p4 filesystem in bytes
    #[serde(rename = "datafs_used", skip_serializing_if = "Option::is_none")]
    pub datafs_used: Option<i64>,
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
            os_release_json: None,
            uptime: None,
            rootfs_size: None,
            rootfs_used: None,
            bootfs_size: None,
            bootfs_used: None,
            datafs_size: None,
            datafs_used: None,
            pi: None,
        }
    }
}


