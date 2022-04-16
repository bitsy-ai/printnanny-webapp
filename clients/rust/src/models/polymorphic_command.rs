/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct WebRtcCommand {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "source")]
        pub source: crate::models::EventSource,
        #[serde(rename = "event_name")]
        pub event_name: crate::models::WebRtcCommandName,
        #[serde(rename = "data", skip_serializing_if = "Option::is_none")]
        pub data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "user")]
        pub user: i32,
        #[serde(rename = "device")]
        pub device: i32,
        #[serde(rename = "stream")]
        pub stream: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "model")]
pub enum PolymorphicCommand {
    #[serde(rename="WebRTCCommand")]
    WebRtcCommand(WebRtcCommand),
}




