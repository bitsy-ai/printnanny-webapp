/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PatchedCloudiotDeviceRequest {
    #[serde(rename = "public_key", skip_serializing_if = "Option::is_none")]
    pub public_key: Option<i32>,
}

impl PatchedCloudiotDeviceRequest {
    pub fn new() -> PatchedCloudiotDeviceRequest {
        PatchedCloudiotDeviceRequest {
            public_key: None,
        }
    }
}


