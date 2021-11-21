/*
 * print-nanny-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct ExperimentDeviceConfig {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<i32>,
    #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
    pub created_dt: Option<String>,
    #[serde(rename = "experiment")]
    pub experiment: i32,
    #[serde(rename = "artifact")]
    pub artifact: i32,
}

impl ExperimentDeviceConfig {
    pub fn new(experiment: i32, artifact: i32) -> ExperimentDeviceConfig {
        ExperimentDeviceConfig {
            id: None,
            created_dt: None,
            experiment,
            artifact,
        }
    }
}


