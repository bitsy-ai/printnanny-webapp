/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct SystemInfoRequest {
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
    /// PrintNanny OS image version string from /boot/image_version.txt
    #[serde(rename = "image_version")]
    pub image_version: String,
    /// PrintNanny OS ansible collection version string. Releaes: https://github.com/bitsy-ai/ansible-collection-printnanny
    #[serde(rename = "ansible_collection_version")]
    pub ansible_collection_version: String,
    #[serde(rename = "device")]
    pub device: i32,
}

impl SystemInfoRequest {
    pub fn new(machine_id: String, hardware: String, revision: String, model: String, serial: String, cores: i32, ram: i64, image_version: String, ansible_collection_version: String, device: i32) -> SystemInfoRequest {
        SystemInfoRequest {
            machine_id,
            hardware,
            revision,
            model,
            serial,
            cores,
            ram,
            image_version,
            ansible_collection_version,
            device,
        }
    }
}


