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
#[serde(tag = "resourcetype")]
pub enum PolymorphicEventRequest {
    #[serde(rename="TestEvent")]
    TestEventRequest {
        #[serde(rename = "type")]
        _type: crate::models::TestEventType,
        #[serde(rename = "status", skip_serializing_if = "Option::is_none")]
        status: Option<crate::models::EventStatus>,
    },
}




