/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.101.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiBootCommandRequest {
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiBootCommandType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiCamCommandRequest {
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiCamCommandType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiSoftwareUpdateCommandRequest {
        #[serde(rename = "payload")]
        pub payload: Box<crate::models::PiSoftwareUpdatePayloadRequest>,
        #[serde(rename = "version")]
        pub version: String,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiSoftwareUpdateCommandType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
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
pub enum PolymorphicPiEventRequest {
    #[serde(rename="pi.{pi_id}.command.boot")]
    PiBootCommandRequest(PiBootCommandRequest),
    #[serde(rename="pi.{pi_id}.command.cam")]
    PiCamCommandRequest(PiCamCommandRequest),
    #[serde(rename="pi.{pi_id}.command.swupdate")]
    PiSoftwareUpdateCommandRequest(PiSoftwareUpdateCommandRequest),
    #[serde(rename="pi.{pi_id}.status.boot")]
    PiBootStatusRequest(PiBootStatusRequest),
    #[serde(rename="pi.{pi_id}.status.cam")]
    PiCamStatusRequest(PiCamStatusRequest),
    #[serde(rename="pi.{pi_id}.status.swupdate")]
    PiSoftwareUpdateStatusRequest(PiSoftwareUpdateStatusRequest),
}




