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
pub struct OctoprintPiSupport {
    #[serde(rename = "model")]
    pub model: String,
    #[serde(rename = "throttle_state")]
    pub throttle_state: String,
    #[serde(rename = "octopi_version", skip_serializing_if = "Option::is_none")]
    pub octopi_version: Option<String>,
}

impl OctoprintPiSupport {
    pub fn new(model: String, throttle_state: String) -> OctoprintPiSupport {
        OctoprintPiSupport {
            model,
            throttle_state,
            octopi_version: None,
        }
    }
}


