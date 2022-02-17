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
pub struct JanusTaskRequest {
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "tasktype")]
pub enum PolymorphicTaskRequest {
    #[serde(rename="JanusTask")]
    JanusTaskRequest(JanusTaskRequest),
}




