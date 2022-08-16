/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.101.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiBootStatusRequest {
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiBootStatusType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiCamStatusRequest {
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiCamStatusType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiSoftwareUpdateStatusRequest {
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "version")]
        pub version: String,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiSoftwareUpdateStatusType,
        #[serde(rename = "pi")]
        pub pi: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "subject_pattern")]
pub enum PolymorphicPiStatusRequest {
    #[serde(rename="PiBootStatus")]
    PiBootStatusRequest(PiBootStatusRequest),
    #[serde(rename="PiCamStatus")]
    PiCamStatusRequest(PiCamStatusRequest),
    #[serde(rename="PiSoftwareUpdateStatus")]
    PiSoftwareUpdateStatusRequest(PiSoftwareUpdateStatusRequest),
}




