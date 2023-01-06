/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.119.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiBootCommand {
        #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
        pub id: Option<String>,
        #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
        pub created_dt: Option<String>,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiBootCommandType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiCamCommand {
        #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
        pub id: Option<String>,
        #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
        pub created_dt: Option<String>,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiCamCommandType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiSoftwareUpdateCommand {
        #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
        pub id: Option<String>,
        #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
        pub created_dt: Option<String>,
        #[serde(rename = "payload")]
        pub payload: Box<crate::models::PiSoftwareUpdatePayload>,
        #[serde(rename = "version")]
        pub version: String,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiSoftwareUpdateCommandType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiBootStatus {
        #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
        pub id: Option<String>,
        #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
        pub created_dt: Option<String>,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiBootStatusType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiCamStatus {
        #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
        pub id: Option<String>,
        #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
        pub created_dt: Option<String>,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiCamStatusType,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiSoftwareUpdateStatus {
        #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
        pub id: Option<String>,
        #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
        pub created_dt: Option<String>,
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
pub enum PolymorphicPiEvent {
    #[serde(rename="pi.{pi_id}.command.boot")]
    PiBootCommand(PiBootCommand),
    #[serde(rename="pi.{pi_id}.command.cam")]
    PiCamCommand(PiCamCommand),
    #[serde(rename="pi.{pi_id}.command.swupdate")]
    PiSoftwareUpdateCommand(PiSoftwareUpdateCommand),
    #[serde(rename="pi.{pi_id}.status.boot")]
    PiBootStatus(PiBootStatus),
    #[serde(rename="pi.{pi_id}.status.cam")]
    PiCamStatus(PiCamStatus),
    #[serde(rename="pi.{pi_id}.status.swupdate")]
    PiSoftwareUpdateStatus(PiSoftwareUpdateStatus),
}




