/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.123.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiBootCommandRequest {
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
pub struct PiCamCommandRequest {
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
pub struct PiSoftwareUpdateCommandRequest {
        #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
        pub id: Option<String>,
        #[serde(rename = "created_dt", skip_serializing_if = "Option::is_none")]
        pub created_dt: Option<String>,
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
#[serde(tag = "subject_pattern")]
pub enum PolymorphicPiCommandRequest {
    #[serde(rename="PiBootCommand")]
    PiBootCommandRequest(PiBootCommandRequest),
    #[serde(rename="PiCamCommand")]
    PiCamCommandRequest(PiCamCommandRequest),
    #[serde(rename="PiSoftwareUpdateCommand")]
    PiSoftwareUpdateCommandRequest(PiSoftwareUpdateCommandRequest),
}




