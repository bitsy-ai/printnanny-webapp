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
pub enum TelemetryEventPolymorphicRequest {
    #[serde(rename="OctoPrintEvent")]
    OctoPrintEventRequest {
        #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
        ts: Option<f32>,
        #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
        event_source: Option<Box<crate::models::OneOfEventSourceEnumNullEnum>>,
        #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
        event_type: Option<Box<crate::models::OctoGenericEvent>>,
        #[serde(rename = "octoprint_environment")]
        octoprint_environment: Box<crate::models::OctoprintEnvironmentRequest>,
        #[serde(rename = "octoprint_printer_data")]
        octoprint_printer_data: Box<crate::models::OctoprintPrinterDataRequest>,
        #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
        event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
        temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "print_nanny_plugin_version")]
        print_nanny_plugin_version: String,
        #[serde(rename = "print_nanny_client_version")]
        print_nanny_client_version: String,
        #[serde(rename = "print_nanny_beta_client_version", skip_serializing_if = "Option::is_none")]
        print_nanny_beta_client_version: Option<String>,
        #[serde(rename = "octoprint_version")]
        octoprint_version: String,
        #[serde(rename = "octoprint_device")]
        octoprint_device: i32,
        #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
        print_session: Option<i32>,
    },
    #[serde(rename="PrintJobEvent")]
    PrintJobEventRequest {
        #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
        ts: Option<f32>,
        #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
        event_source: Option<Box<crate::models::OneOfEventSourceEnumNullEnum>>,
        #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
        event_type: Option<Box<crate::models::OctoJobEvent>>,
        #[serde(rename = "octoprint_environment")]
        octoprint_environment: Box<crate::models::OctoprintEnvironmentRequest>,
        #[serde(rename = "octoprint_printer_data")]
        octoprint_printer_data: Box<crate::models::OctoprintPrinterDataRequest>,
        #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
        event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
        temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "print_nanny_plugin_version")]
        print_nanny_plugin_version: String,
        #[serde(rename = "print_nanny_client_version")]
        print_nanny_client_version: String,
        #[serde(rename = "print_nanny_beta_client_version", skip_serializing_if = "Option::is_none")]
        print_nanny_beta_client_version: Option<String>,
        #[serde(rename = "octoprint_version")]
        octoprint_version: String,
        #[serde(rename = "octoprint_device")]
        octoprint_device: i32,
        #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
        print_session: Option<i32>,
    },
    #[serde(rename="PrintNannyPluginEvent")]
    PrintNannyPluginEventRequest {
        #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
        ts: Option<f32>,
        #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
        event_source: Option<Box<crate::models::OneOfEventSourceEnumNullEnum>>,
        #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
        event_type: Option<Box<crate::models::OctoPrintNannyEvent>>,
        #[serde(rename = "octoprint_environment")]
        octoprint_environment: Box<crate::models::OctoprintEnvironmentRequest>,
        #[serde(rename = "octoprint_printer_data")]
        octoprint_printer_data: Box<crate::models::OctoprintPrinterDataRequest>,
        #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
        event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
        temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "print_nanny_plugin_version")]
        print_nanny_plugin_version: String,
        #[serde(rename = "print_nanny_client_version")]
        print_nanny_client_version: String,
        #[serde(rename = "print_nanny_beta_client_version", skip_serializing_if = "Option::is_none")]
        print_nanny_beta_client_version: Option<String>,
        #[serde(rename = "octoprint_version")]
        octoprint_version: String,
        #[serde(rename = "octoprint_device")]
        octoprint_device: i32,
        #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
        print_session: Option<i32>,
    },
    #[serde(rename="PrinterEvent")]
    PrinterEventRequest {
        #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
        ts: Option<f32>,
        #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
        event_source: Option<Box<crate::models::OneOfEventSourceEnumNullEnum>>,
        #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
        event_type: Option<Box<crate::models::OctoPrinterEvent>>,
        #[serde(rename = "octoprint_environment")]
        octoprint_environment: Box<crate::models::OctoprintEnvironmentRequest>,
        #[serde(rename = "octoprint_printer_data")]
        octoprint_printer_data: Box<crate::models::OctoprintPrinterDataRequest>,
        #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
        event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
        temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "print_nanny_plugin_version")]
        print_nanny_plugin_version: String,
        #[serde(rename = "print_nanny_client_version")]
        print_nanny_client_version: String,
        #[serde(rename = "print_nanny_beta_client_version", skip_serializing_if = "Option::is_none")]
        print_nanny_beta_client_version: Option<String>,
        #[serde(rename = "octoprint_version")]
        octoprint_version: String,
        #[serde(rename = "printer_state", skip_serializing_if = "Option::is_none")]
        printer_state: Option<crate::models::OctoPrinterEvent>,
        #[serde(rename = "octoprint_device")]
        octoprint_device: i32,
        #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
        print_session: Option<i32>,
    },
    #[serde(rename="RemoteCommandEvent")]
    RemoteCommandEventRequest {
        #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
        ts: Option<f32>,
        #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
        event_source: Option<Box<crate::models::OneOfEventSourceEnumNullEnum>>,
        #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
        event_type: Option<Box<crate::models::RemoteCommandEventEventTypeEnum>>,
        #[serde(rename = "octoprint_environment")]
        octoprint_environment: Box<crate::models::OctoprintEnvironmentRequest>,
        #[serde(rename = "octoprint_printer_data")]
        octoprint_printer_data: Box<crate::models::OctoprintPrinterDataRequest>,
        #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
        event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
        temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "print_nanny_plugin_version")]
        print_nanny_plugin_version: String,
        #[serde(rename = "print_nanny_client_version")]
        print_nanny_client_version: String,
        #[serde(rename = "print_nanny_beta_client_version", skip_serializing_if = "Option::is_none")]
        print_nanny_beta_client_version: Option<String>,
        #[serde(rename = "octoprint_version")]
        octoprint_version: String,
        #[serde(rename = "octoprint_device")]
        octoprint_device: i32,
        #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
        print_session: Option<i32>,
    },
    #[serde(rename="TelemetryEvent")]
    TelemetryEventRequest {
        #[serde(rename = "ts", skip_serializing_if = "Option::is_none")]
        ts: Option<f32>,
        #[serde(rename = "event_source", skip_serializing_if = "Option::is_none")]
        event_source: Option<Box<crate::models::OneOfEventSourceEnumNullEnum>>,
        #[serde(rename = "event_type", skip_serializing_if = "Option::is_none")]
        event_type: Option<Box<crate::models::OctoTelemetryEvent>>,
        #[serde(rename = "octoprint_environment")]
        octoprint_environment: Box<crate::models::OctoprintEnvironmentRequest>,
        #[serde(rename = "octoprint_printer_data")]
        octoprint_printer_data: Box<crate::models::OctoprintPrinterDataRequest>,
        #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
        event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
        temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
        #[serde(rename = "print_nanny_plugin_version")]
        print_nanny_plugin_version: String,
        #[serde(rename = "print_nanny_client_version")]
        print_nanny_client_version: String,
        #[serde(rename = "print_nanny_beta_client_version", skip_serializing_if = "Option::is_none")]
        print_nanny_beta_client_version: Option<String>,
        #[serde(rename = "octoprint_version")]
        octoprint_version: String,
        #[serde(rename = "octoprint_device")]
        octoprint_device: i32,
        #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
        print_session: Option<i32>,
    },
}




