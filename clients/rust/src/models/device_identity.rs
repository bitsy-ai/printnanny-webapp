/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct DeviceIdentity {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<i32>,
    #[serde(rename = "deleted", skip_serializing_if = "Option::is_none")]
    pub deleted: Option<String>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "updated_dt", skip_serializing_if = "Option::is_none")]
    pub updated_dt: Option<String>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
    #[serde(rename = "name")]
    pub name: String,
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
    #[serde(rename = "os_version")]
    pub os_version: String,
    #[serde(rename = "os")]
    pub os: String,
    #[serde(rename = "kernel_version")]
    pub kernel_version: String,
    #[serde(rename = "hardware", skip_serializing_if = "Option::is_none")]
    pub hardware: Option<String>,
    #[serde(rename = "revision", skip_serializing_if = "Option::is_none")]
    pub revision: Option<String>,
    #[serde(rename = "model", skip_serializing_if = "Option::is_none")]
    pub model: Option<String>,
    #[serde(rename = "serial", skip_serializing_if = "Option::is_none")]
    pub serial: Option<String>,
    #[serde(rename = "cores")]
    pub cores: i32,
    #[serde(rename = "ram")]
    pub ram: i64,
    #[serde(rename = "cpu_flags")]
    pub cpu_flags: Vec<String>,
    #[serde(rename = "url", skip_serializing_if = "Option::is_none")]
    pub url: Option<String>,
    #[serde(rename = "private_key", skip_serializing_if = "Option::is_none")]
    pub private_key: Option<String>,
    #[serde(rename = "private_key_checksum", skip_serializing_if = "Option::is_none")]
    pub private_key_checksum: Option<String>,
    #[serde(rename = "public_key_checksum", skip_serializing_if = "Option::is_none")]
    pub public_key_checksum: Option<String>,
    #[serde(rename = "cloudiot_device_configs", skip_serializing_if = "Option::is_none")]
    pub cloudiot_device_configs: Option<String>,
    #[serde(rename = "ca_certs", skip_serializing_if = "Option::is_none")]
    pub ca_certs: Option<Box<crate::models::DeviceIdentityCaCerts>>,
}

impl DeviceIdentity {
    pub fn new(name: String, os_version: String, os: String, kernel_version: String, cores: i32, ram: i64, cpu_flags: Vec<String>) -> DeviceIdentity {
        DeviceIdentity {
            id: None,
            deleted: None,
            created_dt: None,
            updated_dt: None,
            user: None,
            name,
            public_key: None,
            fingerprint: None,
            cloudiot_device: None,
            cloudiot_device_name: None,
            cloudiot_device_path: None,
            cloudiot_device_num_id: None,
            os_version,
            os,
            kernel_version,
            hardware: None,
            revision: None,
            model: None,
            serial: None,
            cores,
            ram,
            cpu_flags,
            url: None,
            private_key: None,
            private_key_checksum: None,
            public_key_checksum: None,
            cloudiot_device_configs: None,
            ca_certs: None,
        }
    }
}


