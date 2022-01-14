/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct OctoPrintEvent {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
    pub ts: Option<f32>,
    #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
    pub event_source: Option<Box<crate::models::OneOfAlphaEventSourceNullEnum>>,
    #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
    pub event_type: Option<Box<crate::models::OctoGenericEvent>>,
    #[serde(rename = "octoprint_environment")]
    pub octoprint_environment: Box<crate::models::OctoprintEnvironment>,
    #[serde(rename = "octoprint_printer_data")]
    pub octoprint_printer_data: Box<crate::models::OctoprintPrinterData>,
    #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
    pub event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
    pub temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "print_nanny_plugin_version")]
    pub print_nanny_plugin_version: String,
    #[serde(rename = "print_nanny_client_version")]
    pub print_nanny_client_version: String,
    #[serde(rename = "print_nanny_beta_client_version", skip_serializing_if = "Option::is_none")]
    pub print_nanny_beta_client_version: Option<String>,
    #[serde(rename = "octoprint_version")]
    pub octoprint_version: String,
    #[serde(rename = "polymorphic_ctype")]
    pub polymorphic_ctype: i32,
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: i32,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
    pub print_session: Option<i32>,
}

impl OctoPrintEvent {
    pub fn new(id: i32, octoprint_environment: crate::models::OctoprintEnvironment, octoprint_printer_data: crate::models::OctoprintPrinterData, print_nanny_plugin_version: String, print_nanny_client_version: String, octoprint_version: String, polymorphic_ctype: i32, octoprint_device: i32, user: i32) -> OctoPrintEvent {
        OctoPrintEvent {
            id,
            ts: None,
            event_source: None,
            event_type: None,
            octoprint_environment: Box::new(octoprint_environment),
            octoprint_printer_data: Box::new(octoprint_printer_data),
            event_data: None,
            temperature: None,
            print_nanny_plugin_version,
            print_nanny_client_version,
            print_nanny_beta_client_version: None,
            octoprint_version,
            polymorphic_ctype,
            octoprint_device,
            user,
            print_session: None,
        }
    }
}


