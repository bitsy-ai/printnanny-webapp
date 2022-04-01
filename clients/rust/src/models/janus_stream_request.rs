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
pub struct JanusStreamRequest {
    #[serde(rename = "ws_port", skip_serializing_if = "Option::is_none")]
    pub ws_port: Option<i32>,
}

impl JanusStreamRequest {
    pub fn new() -> JanusStreamRequest {
        JanusStreamRequest {
            ws_port: None,
        }
    }
}


