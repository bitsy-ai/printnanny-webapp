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
pub struct Config {
    #[serde(rename = "api")]
    pub api: Option<Box<crate::models::PrintNannyApiConfig>>,
    #[serde(rename = "device")]
    pub device: Option<Box<crate::models::Device>>,
}

impl Config {
    pub fn new(api: Option<crate::models::PrintNannyApiConfig>, device: Option<crate::models::Device>) -> Config {
        Config {
            api: api.map(Box::new),
            device: device.map(Box::new),
        }
    }
}

