/*
 * printnanny-api-client
 *
 * Official API client library for print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@print-nanny.com
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintNannyEvent {
    #[serde(rename = "plugin_octoprint_nanny_monitoring_start")]
    MonitoringStart,
    #[serde(rename = "plugin_octoprint_nanny_monitoring_stop")]
    MonitoringStop,
    #[serde(rename = "plugin_octoprint_nanny_monitoring_reset")]
    MonitoringReset,
    #[serde(rename = "plugin_octoprint_nanny_device_register_start")]
    DeviceRegisterStart,
    #[serde(rename = "plugin_octoprint_nanny_device_register_done")]
    DeviceRegisterDone,
    #[serde(rename = "plugin_octoprint_nanny_device_register_failed")]
    DeviceRegisterFailed,
    #[serde(rename = "plugin_octoprint_nanny_device_reset")]
    DeviceReset,
    #[serde(rename = "plugin_octoprint_nanny_printer_profile_sync_start")]
    PrinterProfileSyncStart,
    #[serde(rename = "plugin_octoprint_nanny_printer_profile_sync_done")]
    PrinterProfileSyncDone,
    #[serde(rename = "plugin_octoprint_nanny_printer_profile_sync_failed")]
    PrinterProfileSyncFailed,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_rest_api")]
    ConnectTestRestApi,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_rest_api_failed")]
    ConnectTestRestApiFailed,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_rest_api_success")]
    ConnectTestRestApiSuccess,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_mqtt_ping")]
    ConnectTestMqttPing,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_mqtt_ping_failed")]
    ConnectTestMqttPingFailed,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_mqtt_ping_success")]
    ConnectTestMqttPingSuccess,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_mqtt_pong")]
    ConnectTestMqttPong,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_mqtt_pong_failed")]
    ConnectTestMqttPongFailed,
    #[serde(rename = "plugin_octoprint_nanny_connect_test_mqtt_pong_success")]
    ConnectTestMqttPongSuccess,

}

impl ToString for OctoPrintNannyEvent {
    fn to_string(&self) -> String {
        match self {
            Self::MonitoringStart => String::from("plugin_octoprint_nanny_monitoring_start"),
            Self::MonitoringStop => String::from("plugin_octoprint_nanny_monitoring_stop"),
            Self::MonitoringReset => String::from("plugin_octoprint_nanny_monitoring_reset"),
            Self::DeviceRegisterStart => String::from("plugin_octoprint_nanny_device_register_start"),
            Self::DeviceRegisterDone => String::from("plugin_octoprint_nanny_device_register_done"),
            Self::DeviceRegisterFailed => String::from("plugin_octoprint_nanny_device_register_failed"),
            Self::DeviceReset => String::from("plugin_octoprint_nanny_device_reset"),
            Self::PrinterProfileSyncStart => String::from("plugin_octoprint_nanny_printer_profile_sync_start"),
            Self::PrinterProfileSyncDone => String::from("plugin_octoprint_nanny_printer_profile_sync_done"),
            Self::PrinterProfileSyncFailed => String::from("plugin_octoprint_nanny_printer_profile_sync_failed"),
            Self::ConnectTestRestApi => String::from("plugin_octoprint_nanny_connect_test_rest_api"),
            Self::ConnectTestRestApiFailed => String::from("plugin_octoprint_nanny_connect_test_rest_api_failed"),
            Self::ConnectTestRestApiSuccess => String::from("plugin_octoprint_nanny_connect_test_rest_api_success"),
            Self::ConnectTestMqttPing => String::from("plugin_octoprint_nanny_connect_test_mqtt_ping"),
            Self::ConnectTestMqttPingFailed => String::from("plugin_octoprint_nanny_connect_test_mqtt_ping_failed"),
            Self::ConnectTestMqttPingSuccess => String::from("plugin_octoprint_nanny_connect_test_mqtt_ping_success"),
            Self::ConnectTestMqttPong => String::from("plugin_octoprint_nanny_connect_test_mqtt_pong"),
            Self::ConnectTestMqttPongFailed => String::from("plugin_octoprint_nanny_connect_test_mqtt_pong_failed"),
            Self::ConnectTestMqttPongSuccess => String::from("plugin_octoprint_nanny_connect_test_mqtt_pong_success"),
        }
    }
}

impl Default for OctoPrintNannyEvent {
    fn default() -> OctoPrintNannyEvent {
        Self::MonitoringStart
    }
}




