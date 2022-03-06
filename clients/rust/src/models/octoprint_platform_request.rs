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
pub struct OctoprintPlatformRequest {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "platform")]
    pub platform: String,
    #[serde(rename = "bits")]
    pub bits: String,
}

impl OctoprintPlatformRequest {
    pub fn new(id: String, platform: String, bits: String) -> OctoprintPlatformRequest {
        OctoprintPlatformRequest {
            id,
            platform,
            bits,
        }
    }
}


