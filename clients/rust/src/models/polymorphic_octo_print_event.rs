/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.106.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintClientStatus {
        #[serde(rename = "id")]
        pub id: String,
        #[serde(rename = "payload")]
        pub payload: Box<crate::models::OctoPrintClientStatusPayload>,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::OctoPrintClientStatusType,
        #[serde(rename = "octoprint_server")]
        pub octoprint_server: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintPrintJobStatus {
        #[serde(rename = "id")]
        pub id: String,
        #[serde(rename = "payload")]
        pub payload: Box<crate::models::OctoPrintPrintJobPayload>,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
        #[serde(rename = "event_type")]
        pub event_type: crate::models::OctoPrintPrintJobStatusType,
        #[serde(rename = "octoprint_server")]
        pub octoprint_server: i32,
        #[serde(rename = "pi")]
        pub pi: i32,
}
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintPrinterStatus {
        #[serde(rename = "id")]
        pub id: String,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
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
pub struct OctoPrintServerStatus {
        #[serde(rename = "id")]
        pub id: String,
        #[serde(rename = "created_dt")]
        pub created_dt: String,
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
pub enum PolymorphicOctoPrintEvent {
    #[serde(rename="pi.{pi_id}.octoprint.client")]
    OctoPrintClientStatus(OctoPrintClientStatus),
    #[serde(rename="pi.{pi_id}.octoprint.print_job")]
    OctoPrintPrintJobStatus(OctoPrintPrintJobStatus),
    #[serde(rename="pi.{pi_id}.octoprint.printer")]
    OctoPrintPrinterStatus(OctoPrintPrinterStatus),
    #[serde(rename="pi.{pi_id}.octoprint.server")]
    OctoPrintServerStatus(OctoPrintServerStatus),
}




