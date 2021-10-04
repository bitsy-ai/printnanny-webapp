/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct PrintNannyPluginEvent {
    #[serde(rename = "id")]
    pub id: i32,
    #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
    pub ts: Option<f32>,
    #[serde(rename = "event_type")]
    pub event_type: crate::models::PrintNannyPluginEventEventTypeEnum,
    #[serde(rename = "octoprint_environment")]
    pub octoprint_environment: Box<crate::models::OctoprintEnvironment>,
    #[serde(rename = "octoprint_printer_data")]
    pub octoprint_printer_data: Box<crate::models::OctoprintPrinterData>,
    #[serde(rename = "event_source")]
    pub event_source: Option<Box<crate::models::EventSourceEnum>>,
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
    #[serde(rename = "polymorphic_ctype")]
    pub polymorphic_ctype: i32,
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: i32,
    #[serde(rename = "user")]
    pub user: i32,
    #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
    pub print_session: Option<i32>,
}

impl PrintNannyPluginEvent {
    pub fn new(id: i32, event_type: crate::models::PrintNannyPluginEventEventTypeEnum, octoprint_environment: crate::models::OctoprintEnvironment, octoprint_printer_data: crate::models::OctoprintPrinterData, event_source: Option<crate::models::EventSourceEnum>, print_nanny_plugin_version: String, print_nanny_client_version: String, octoprint_version: String, polymorphic_ctype: i32, octoprint_device: i32, user: i32) -> PrintNannyPluginEvent {
        PrintNannyPluginEvent {
            id,
            ts: None,
            event_type,
            octoprint_environment: Box::new(octoprint_environment),
            octoprint_printer_data: Box::new(octoprint_printer_data),
            event_source: Box::new(event_source),
            event_data: None,
            temperature: None,
            print_nanny_plugin_version,
            print_nanny_client_version,
            octoprint_version,
            polymorphic_ctype,
            octoprint_device,
            user,
            print_session: None,
        }
    }
}


