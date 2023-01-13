/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.122.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct SystemInfo {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "bootfs_available")]
    pub bootfs_available: i64,
    #[serde(rename = "bootfs_available_pretty")]
    pub bootfs_available_pretty: String,
    #[serde(rename = "bootfs_used_pretty")]
    pub bootfs_used_pretty: String,
    #[serde(rename = "bootfs_size_pretty")]
    pub bootfs_size_pretty: String,
    #[serde(rename = "datafs_available")]
    pub datafs_available: i64,
    #[serde(rename = "datafs_available_pretty")]
    pub datafs_available_pretty: String,
    #[serde(rename = "datafs_used_pretty")]
    pub datafs_used_pretty: String,
    #[serde(rename = "datafs_size_pretty")]
    pub datafs_size_pretty: String,
    #[serde(rename = "rootfs_available")]
    pub rootfs_available: i64,
    #[serde(rename = "rootfs_available_pretty")]
    pub rootfs_available_pretty: String,
    #[serde(rename = "rootfs_size_pretty")]
    pub rootfs_size_pretty: String,
    #[serde(rename = "rootfs_used_pretty")]
    pub rootfs_used_pretty: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
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
    #[serde(rename = "os_version_id", skip_serializing_if = "Option::is_none")]
    pub os_version_id: Option<String>,
    /// PrintNanny OS BUILD_ID from /etc/os-release
    #[serde(rename = "os_build_id", skip_serializing_if = "Option::is_none")]
    pub os_build_id: Option<String>,
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

impl SystemInfo {
    pub fn new(id: i32, bootfs_available: i64, bootfs_available_pretty: String, bootfs_used_pretty: String, bootfs_size_pretty: String, datafs_available: i64, datafs_available_pretty: String, datafs_used_pretty: String, datafs_size_pretty: String, rootfs_available: i64, rootfs_available_pretty: String, rootfs_size_pretty: String, rootfs_used_pretty: String, created_dt: String, updated_dt: String, machine_id: String, revision: String, model: String, serial: String, cores: i32, ram: i64, uptime: i64, rootfs_size: i64, rootfs_used: i64, bootfs_size: i64, bootfs_used: i64, datafs_size: i64, datafs_used: i64, pi: i32) -> SystemInfo {
        SystemInfo {
            id,
            bootfs_available,
            bootfs_available_pretty,
            bootfs_used_pretty,
            bootfs_size_pretty,
            datafs_available,
            datafs_available_pretty,
            datafs_used_pretty,
            datafs_size_pretty,
            rootfs_available,
            rootfs_available_pretty,
            rootfs_size_pretty,
            rootfs_used_pretty,
            created_dt,
            updated_dt,
            machine_id,
            revision,
            model,
            serial,
            cores,
            ram,
            os_version_id: None,
            os_build_id: None,
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


