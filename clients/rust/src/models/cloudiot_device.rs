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
    #[serde(rename = "desired_config_topic")]
    pub desired_config_topic: String,
    #[serde(rename = "current_state_topic")]
    pub current_state_topic: String,
    #[serde(rename = "gcp_project_id")]
    pub gcp_project_id: String,
    #[serde(rename = "gcp_region")]
    pub gcp_region: String,
    #[serde(rename = "gcp_cloudiot_device_registry")]
    pub gcp_cloudiot_device_registry: String,
    #[serde(rename = "mqtt_bridge_hostname")]
    pub mqtt_bridge_hostname: String,
    #[serde(rename = "mqtt_bridge_port")]
    pub mqtt_bridge_port: i32,
    #[serde(rename = "mqtt_client_id")]
    pub mqtt_client_id: String,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "device")]
    pub device: i32,
}

impl CloudiotDevice {
    pub fn new(num_id: i64, desired_config_topic: String, current_state_topic: String, gcp_project_id: String, gcp_region: String, gcp_cloudiot_device_registry: String, mqtt_bridge_hostname: String, mqtt_bridge_port: i32, mqtt_client_id: String, name: String, id: String, device: i32) -> CloudiotDevice {
        CloudiotDevice {
            num_id,
            desired_config_topic,
            current_state_topic,
            gcp_project_id,
            gcp_region,
            gcp_cloudiot_device_registry,
            mqtt_bridge_hostname,
            mqtt_bridge_port,
            mqtt_client_id,
            name,
            id,
            device,
        }
    }
}


