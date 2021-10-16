/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoprintPlatform {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "platform")]
    pub platform: String,
    #[serde(rename = "bits")]
    pub bits: String,
}

impl OctoprintPlatform {
    pub fn new(id: String, platform: String, bits: String) -> OctoprintPlatform {
        OctoprintPlatform {
            id,
            platform,
            bits,
        }
    }
}


