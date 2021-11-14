/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Device {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<i32>,
    #[serde(rename = "cloudiot_device", skip_serializing_if = "Option::is_none")]
    pub cloudiot_device: Option<Box<crate::models::CloudiotDevice>>,
    #[serde(rename = "cameras", skip_serializing_if = "Option::is_none")]
    pub cameras: Option<Vec<crate::models::Camera>>,
    #[serde(rename = "dashboard_url", skip_serializing_if = "Option::is_none")]
    pub dashboard_url: Option<String>,
    #[serde(rename = "bootstrap_release", skip_serializing_if = "Option::is_none")]
    pub bootstrap_release: Option<Box<crate::models::Release>>,
    #[serde(rename = "printer_controllers", skip_serializing_if = "Option::is_none")]
    pub printer_controllers: Option<Vec<crate::models::PrinterController>>,
    #[serde(rename = "release_channel", skip_serializing_if = "Option::is_none")]
    pub release_channel: Option<Box<crate::models::ReleaseChannelEnum>>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<Box<crate::models::User>>,
    #[serde(rename = "license", skip_serializing_if = "Option::is_none")]
    pub license: Option<Box<crate::models::License>>,
    #[serde(rename = "deleted", skip_serializing_if = "Option::is_none")]
    pub deleted: Option<String>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "updated_dt", skip_serializing_if = "Option::is_none")]
    pub updated_dt: Option<String>,
    /// Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)
    #[serde(rename = "hostname", skip_serializing_if = "Option::is_none")]
    pub hostname: Option<String>,
}

impl Device {
    pub fn new() -> Device {
        Device {
            id: None,
            cloudiot_device: None,
            cameras: None,
            dashboard_url: None,
            bootstrap_release: None,
            printer_controllers: None,
            release_channel: None,
            user: None,
            license: None,
            deleted: None,
            created_dt: None,
            updated_dt: None,
            hostname: None,
        }
    }
}


