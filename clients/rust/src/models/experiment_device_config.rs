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
pub struct ExperimentDeviceConfig {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "created_dt")]
    pub created_dt: String,
    #[serde(rename = "experiment")]
    pub experiment: i32,
    #[serde(rename = "artifact")]
    pub artifact: i32,
}

impl ExperimentDeviceConfig {
    pub fn new(id: i32, created_dt: String, experiment: i32, artifact: i32) -> ExperimentDeviceConfig {
        ExperimentDeviceConfig {
            id,
            created_dt,
            experiment,
            artifact,
        }
    }
}


