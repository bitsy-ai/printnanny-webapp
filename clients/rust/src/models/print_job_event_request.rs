/*
 * print-nanny-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PrintJobEventRequest {
    #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
    pub ts: Option<f32>,
    #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
    pub event_source: Option<Box<crate::models::EventSourceEnum>>,
    #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
    pub event_type: Option<Box<crate::models::PrintJobEventType>>,
    #[serde(rename = "octoprint_environment")]
    pub octoprint_environment: Box<crate::models::OctoprintEnvironmentRequest>,
    #[serde(rename = "octoprint_printer_data")]
    pub octoprint_printer_data: Box<crate::models::OctoprintPrinterDataRequest>,
    #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
    pub event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
    pub temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "print_nanny_plugin_version")]
    pub print_nanny_plugin_version: String,
    #[serde(rename = "print_nanny_client_version")]
    pub print_nanny_client_version: String,
    #[serde(rename = "octoprint_version")]
    pub octoprint_version: String,
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: i32,
    #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
    pub print_session: Option<i32>,
}

impl PrintJobEventRequest {
    pub fn new(octoprint_environment: crate::models::OctoprintEnvironmentRequest, octoprint_printer_data: crate::models::OctoprintPrinterDataRequest, print_nanny_plugin_version: String, print_nanny_client_version: String, octoprint_version: String, octoprint_device: i32) -> PrintJobEventRequest {
        PrintJobEventRequest {
            ts: None,
            event_source: None,
            event_type: None,
            octoprint_environment: Box::new(octoprint_environment),
            octoprint_printer_data: Box::new(octoprint_printer_data),
            event_data: None,
            temperature: None,
            print_nanny_plugin_version,
            print_nanny_client_version,
            octoprint_version,
            octoprint_device,
            print_session: None,
        }
    }
}


