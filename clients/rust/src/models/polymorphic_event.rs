/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct TestEvent {
        /// Indicates whether event should be sent to Device on command topic
        #[serde(rename = "command", skip_serializing_if = "Option::is_none")]
        command: Option<bool>,
        #[serde(rename = "created_dt")]
        created_dt: String,
        #[serde(rename = "device")]
        device: i32,
        #[serde(rename = "event_type")]
        event_type: crate::models::TestEventType,
        #[serde(rename = "id")]
        id: i32,
        #[serde(rename = "source")]
        source: crate::models::EventSource,
        #[serde(rename = "status", skip_serializing_if = "Option::is_none")]
        status: Option<crate::models::EventStatus>,
        #[serde(rename = "user")]
        user: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "model")]
pub enum PolymorphicEvent {
    #[serde(rename="TestEvent")]
    TestEvent(TestEvent),
}




