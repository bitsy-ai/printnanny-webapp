/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.8
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiBootCommand {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "subject")]
        pub subject: String,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiBootCommandType,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiBootEvent {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "subject")]
        pub subject: String,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiBootEventType,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiGstreamerCommand {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "subject")]
        pub subject: String,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiGstreamerCommandType,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PiSoftwareUpdateEvent {
        #[serde(rename = "id")]
        pub id: i32,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "subject")]
        pub subject: String,
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "version")]
        pub version: String,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::PiSoftwareUpdateEventType,
        #[serde(rename = "polymorphic_ctype")]
        pub polymorphic_ctype: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "__class__")]
pub enum PolymorphicPiEvent {
    #[serde(rename="PiBootCommand")]
    PiBootCommand(PiBootCommand),
    #[serde(rename="PiBootEvent")]
    PiBootEvent(PiBootEvent),
    #[serde(rename="PiGstreamerCommand")]
    PiGstreamerCommand(PiGstreamerCommand),
    #[serde(rename="PiSoftwareUpdateEvent")]
    PiSoftwareUpdateEvent(PiSoftwareUpdateEvent),
}




