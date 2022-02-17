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
pub struct MonitorStartTaskRequest {
        #[serde(rename = "janus_media_stream")]
        janus_media_stream: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct MonitorStopTaskRequest {
        #[serde(rename = "janus_media_stream")]
        janus_media_stream: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "model")]
pub enum PolymorphicTaskRequest {
    #[serde(rename="MonitorStartTask")]
    MonitorStartTaskRequest(MonitorStartTaskRequest),
    #[serde(rename="MonitorStopTask")]
    MonitorStopTaskRequest(MonitorStopTaskRequest),
}




