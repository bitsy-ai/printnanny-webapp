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
pub enum TasktypeEnum {
    #[serde(rename = "cloud_monitor_start")]
    CloudMonitorStart,
    #[serde(rename = "cloud_monitor_stop")]
    CloudMonitorStop,
    #[serde(rename = "system_check")]
    SystemCheck,
    #[serde(rename = "system_update")]
    SystemUpdate,

}

impl ToString for TasktypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::CloudMonitorStart => String::from("cloud_monitor_start"),
            Self::CloudMonitorStop => String::from("cloud_monitor_stop"),
            Self::SystemCheck => String::from("system_check"),
            Self::SystemUpdate => String::from("system_update"),
        }
    }
}

impl Default for TasktypeEnum {
    fn default() -> TasktypeEnum {
        Self::CloudMonitorStart
    }
}




