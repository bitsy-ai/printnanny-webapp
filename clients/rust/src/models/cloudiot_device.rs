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
pub struct CloudiotDevice {
    #[serde(rename = "num_id")]
    pub num_id: i64,
    #[serde(rename = "desired_config_topic", skip_serializing_if = "Option::is_none")]
    pub desired_config_topic: Option<String>,
    #[serde(rename = "current_state_topic", skip_serializing_if = "Option::is_none")]
    pub current_state_topic: Option<String>,
    #[serde(rename = "gcp_project_id", skip_serializing_if = "Option::is_none")]
    pub gcp_project_id: Option<String>,
    #[serde(rename = "gcp_region", skip_serializing_if = "Option::is_none")]
    pub gcp_region: Option<String>,
    #[serde(rename = "gcp_cloudiot_device_registry", skip_serializing_if = "Option::is_none")]
    pub gcp_cloudiot_device_registry: Option<String>,
    #[serde(rename = "mqtt_bridge_hostname", skip_serializing_if = "Option::is_none")]
    pub mqtt_bridge_hostname: Option<String>,
    #[serde(rename = "mqtt_bridge_port", skip_serializing_if = "Option::is_none")]
    pub mqtt_bridge_port: Option<i32>,
    #[serde(rename = "mqtt_client_id", skip_serializing_if = "Option::is_none")]
    pub mqtt_client_id: Option<String>,
    #[serde(rename = "deleted", skip_serializing_if = "Option::is_none")]
    pub deleted: Option<String>,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "device")]
    pub device: i32,
}

impl CloudiotDevice {
    pub fn new(num_id: i64, name: String, id: String, device: i32) -> CloudiotDevice {
        CloudiotDevice {
            num_id,
            desired_config_topic: None,
            current_state_topic: None,
            gcp_project_id: None,
            gcp_region: None,
            gcp_cloudiot_device_registry: None,
            mqtt_bridge_hostname: None,
            mqtt_bridge_port: None,
            mqtt_client_id: None,
            deleted: None,
            name,
            id,
            device,
        }
    }
}


