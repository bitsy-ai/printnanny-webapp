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
pub struct Device {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "cloudiot_device")]
    pub cloudiot_device: Option<Box<crate::models::CloudiotDevice>>,
    #[serde(rename = "user")]
    pub user: Option<Box<crate::models::User>>,
    #[serde(rename = "system_info")]
    pub system_info: Option<Box<crate::models::SystemInfo>>,
    #[serde(rename = "public_key")]
    pub public_key: Option<Box<crate::models::PublicKey>>,
    #[serde(rename = "urls")]
    pub urls: Box<crate::models::DeviceUrls>,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    /// Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)
    #[serde(rename = "hostname", skip_serializing_if = "Option::is_none")]
    pub hostname: Option<String>,
}

impl Device {
    pub fn new(id: i32, cloudiot_device: Option<crate::models::CloudiotDevice>, user: Option<crate::models::User>, system_info: Option<crate::models::SystemInfo>, public_key: Option<crate::models::PublicKey>, urls: crate::models::DeviceUrls, created_dt: String) -> Device {
        Device {
            id,
            cloudiot_device: cloudiot_device.map(Box::new),
            user: user.map(Box::new),
            system_info: system_info.map(Box::new),
            public_key: public_key.map(Box::new),
            urls: Box::new(urls),
            created_dt,
            hostname: None,
        }
    }
}


