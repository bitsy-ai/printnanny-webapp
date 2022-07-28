/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.97.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Config {
    #[serde(rename = "api")]
    pub api: Option<Box<crate::models::PrintNannyApiConfig>>,
    #[serde(rename = "pi")]
    pub pi: Option<Box<crate::models::Pi>>,
}

impl Config {
    pub fn new(api: Option<crate::models::PrintNannyApiConfig>, pi: Option<crate::models::Pi>) -> Config {
        Config {
            api: api.map(Box::new),
            pi: pi.map(Box::new),
        }
    }
}


