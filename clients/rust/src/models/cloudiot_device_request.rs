/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct CloudiotDeviceRequest {
    #[serde(rename = "public_key")]
    pub public_key: i32,
}

impl CloudiotDeviceRequest {
    pub fn new(public_key: i32) -> CloudiotDeviceRequest {
        CloudiotDeviceRequest {
            public_key,
        }
    }
}


