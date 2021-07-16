/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct DeviceRequest {
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "public_key")]
    pub public_key: String,
    #[serde(rename = "fingerprint")]
    pub fingerprint: String,
    #[serde(rename = "cloudiot_device")]
    pub cloudiot_device: ::std::collections::HashMap<String, serde_json::Value>,
    #[serde(rename = "cloudiot_device_name")]
    pub cloudiot_device_name: String,
    #[serde(rename = "cloudiot_device_path")]
    pub cloudiot_device_path: String,
    #[serde(rename = "cloudiot_device_num_id")]
    pub cloudiot_device_num_id: i64,
    #[serde(rename = "os_version")]
    pub os_version: String,
    #[serde(rename = "os")]
    pub os: String,
    #[serde(rename = "kernel_version")]
    pub kernel_version: String,
    #[serde(rename = "hardware")]
    pub hardware: String,
    #[serde(rename = "revision")]
    pub revision: String,
    #[serde(rename = "model")]
    pub model: String,
    #[serde(rename = "serial")]
    pub serial: String,
    #[serde(rename = "cores")]
    pub cores: i32,
    #[serde(rename = "ram")]
    pub ram: i32,
    #[serde(rename = "cpu_flags")]
    pub cpu_flags: String,
}

impl DeviceRequest {
    pub fn new(user: i32, name: String, public_key: String, fingerprint: String, cloudiot_device: ::std::collections::HashMap<String, serde_json::Value>, cloudiot_device_name: String, cloudiot_device_path: String, cloudiot_device_num_id: i64, os_version: String, os: String, kernel_version: String, hardware: String, revision: String, model: String, serial: String, cores: i32, ram: i32, cpu_flags: String) -> DeviceRequest {
        DeviceRequest {
            user,
            name,
            public_key,
            fingerprint,
            cloudiot_device,
            cloudiot_device_name,
            cloudiot_device_path,
            cloudiot_device_num_id,
            os_version,
            os,
            kernel_version,
            hardware,
            revision,
            model,
            serial,
            cores,
            ram,
            cpu_flags,
        }
    }
}


