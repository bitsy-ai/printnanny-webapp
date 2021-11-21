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
pub struct OctoprintHardware {
    #[serde(rename = "cores")]
    pub cores: i32,
    #[serde(rename = "freq")]
    pub freq: f32,
    #[serde(rename = "ram")]
    pub ram: i32,
}

impl OctoprintHardware {
    pub fn new(cores: i32, freq: f32, ram: i32) -> OctoprintHardware {
        OctoprintHardware {
            cores,
            freq,
            ram,
        }
    }
}


