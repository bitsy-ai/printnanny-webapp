/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.98.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct WebRtcCommandCreateRequest {
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::WebRtcCommandName,
        #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
        pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "pi")]
        pub pi: i32,
        #[serde(rename = "stream")]
        pub stream: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "model")]
pub enum PolymorphicCommandCreateRequest {
    #[serde(rename="WebRTCCommand")]
    WebRtcCommandCreateRequest(WebRtcCommandCreateRequest),
}




