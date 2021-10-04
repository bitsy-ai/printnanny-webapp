/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoprintHardwareRequest {
    #[serde(rename = "cores")]
    pub cores: i32,
    #[serde(rename = "freq")]
    pub freq: f32,
    #[serde(rename = "ram")]
    pub ram: i32,
}

impl OctoprintHardwareRequest {
    pub fn new(cores: i32, freq: f32, ram: i32) -> OctoprintHardwareRequest {
        OctoprintHardwareRequest {
            cores,
            freq,
            ram,
        }
    }
}


