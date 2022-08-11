/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.6
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintClientStatusRequest {
        #[serde(rename = "payload")]
        pub payload: Box<crate::models::OctoPrintClientStatusPayloadRequest>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::OctoPrintClientStatusType,
        #[serde(rename = "octoprint_server")]
        pub octoprint_server: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintPrintJobStatusRequest {
        #[serde(rename = "payload")]
        pub payload: Box<crate::models::OctoPrintPrintJobPayloadRequest>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::OctoPrintPrintJobStatusEventTypeEnum,
        #[serde(rename = "octoprint_server")]
        pub octoprint_server: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintPrinterStatusRequest {
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::OctoPrintPrinterStatusType,
        #[serde(rename = "octoprint_server")]
        pub octoprint_server: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintServerStatusRequest {
        #[serde(rename = "payload", skip_serializing_if = "Option::is_none")]
        pub payload: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::OctoPrintServerStatusType,
        #[serde(rename = "octoprint_server")]
        pub octoprint_server: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
#[serde(tag = "subject_pattern")]
pub enum PolymorphicOctoPrintEventRequest {
    #[serde(rename="pi.{pi_id}.octoprint.client")]
    OctoPrintClientStatusRequest(OctoPrintClientStatusRequest),
    #[serde(rename="pi.{pi_id}.octoprint.print_job")]
    OctoPrintPrintJobStatusRequest(OctoPrintPrintJobStatusRequest),
    #[serde(rename="pi.{pi_id}.octoprint.printer")]
    OctoPrintPrinterStatusRequest(OctoPrintPrinterStatusRequest),
    #[serde(rename="pi.{pi_id}.octoprint.server")]
    OctoPrintServerStatusRequest(OctoPrintServerStatusRequest),
}




