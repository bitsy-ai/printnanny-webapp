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
pub enum TaskType {
    #[serde(rename = "monitor_start")]
    MonitorStart,
    #[serde(rename = "monitor_stop")]
    MonitorStop,
    #[serde(rename = "check_license")]
    CheckLicense,
    #[serde(rename = "software_update")]
    SoftwareUpdate,

}

impl ToString for TaskType {
    fn to_string(&self) -> String {
        match self {
            Self::MonitorStart => String::from("monitor_start"),
            Self::MonitorStop => String::from("monitor_stop"),
            Self::CheckLicense => String::from("check_license"),
            Self::SoftwareUpdate => String::from("software_update"),
        }
    }
}

impl Default for TaskType {
    fn default() -> TaskType {
        Self::MonitorStart
    }
}




