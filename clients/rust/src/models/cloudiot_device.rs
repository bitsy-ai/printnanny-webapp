/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.9
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct CloudiotDevice {
    #[serde(rename = "num_id")]
    pub num_id: i64,
    #[serde(rename = "command_topic")]
    pub command_topic: String,
    #[serde(rename = "event_topic")]
    pub event_topic: String,
    #[serde(rename = "config_topic")]
    pub config_topic: String,
    #[serde(rename = "state_topic")]
    pub state_topic: String,
    #[serde(rename = "gcp_resource")]
    pub gcp_resource: String,
    #[serde(rename = "gcp_project_id")]
    pub gcp_project_id: String,
    #[serde(rename = "gcp_region")]
    pub gcp_region: String,
    #[serde(rename = "gcp_cloudiot_pi_registry")]
    pub gcp_cloudiot_pi_registry: String,
    #[serde(rename = "mqtt_bridge_hostname")]
    pub mqtt_bridge_hostname: String,
    #[serde(rename = "mqtt_bridge_port")]
    pub mqtt_bridge_port: i32,
    #[serde(rename = "mqtt_client_id")]
    pub mqtt_client_id: String,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "updated_dt")]
    pub updated_dt: String,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "pi")]
    pub pi: i32,
    #[serde(rename = "public_key")]
    pub public_key: i32,
}

impl CloudiotDevice {
    pub fn new(num_id: i64, command_topic: String, event_topic: String, config_topic: String, state_topic: String, gcp_resource: String, gcp_project_id: String, gcp_region: String, gcp_cloudiot_pi_registry: String, mqtt_bridge_hostname: String, mqtt_bridge_port: i32, mqtt_client_id: String, created_dt: String, updated_dt: String, name: String, id: String, pi: i32, public_key: i32) -> CloudiotDevice {
        CloudiotDevice {
            num_id,
            command_topic,
            event_topic,
            config_topic,
            state_topic,
            gcp_resource,
            gcp_project_id,
            gcp_region,
            gcp_cloudiot_pi_registry,
            mqtt_bridge_hostname,
            mqtt_bridge_port,
            mqtt_client_id,
            created_dt,
            updated_dt,
            name,
            id,
            pi,
            public_key,
        }
    }
}


