/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiBootStatusType {
    #[serde(rename = "SystemctlShow")]
    SystemctlShow,
    #[serde(rename = "RebootStarted")]
    RebootStarted,
    #[serde(rename = "RebootError")]
    RebootError,
    #[serde(rename = "ShutdownStarted")]
    ShutdownStarted,
    #[serde(rename = "ShutdownError")]
    ShutdownError,
    #[serde(rename = "BootStarted")]
    BootStarted,
    #[serde(rename = "BootSuccess")]
    BootSuccess,
    #[serde(rename = "BootDegraded")]
    BootDegraded,
    #[serde(rename = "SyncSettingsStarted")]
    SyncSettingsStarted,
    #[serde(rename = "SyncSettingsSuccess")]
    SyncSettingsSuccess,
    #[serde(rename = "SyncSettingsError")]
    SyncSettingsError,

}

impl ToString for PiBootStatusType {
    fn to_string(&self) -> String {
        match self {
            Self::SystemctlShow => String::from("SystemctlShow"),
            Self::RebootStarted => String::from("RebootStarted"),
            Self::RebootError => String::from("RebootError"),
            Self::ShutdownStarted => String::from("ShutdownStarted"),
            Self::ShutdownError => String::from("ShutdownError"),
            Self::BootStarted => String::from("BootStarted"),
            Self::BootSuccess => String::from("BootSuccess"),
            Self::BootDegraded => String::from("BootDegraded"),
            Self::SyncSettingsStarted => String::from("SyncSettingsStarted"),
            Self::SyncSettingsSuccess => String::from("SyncSettingsSuccess"),
            Self::SyncSettingsError => String::from("SyncSettingsError"),
        }
    }
}

impl Default for PiBootStatusType {
    fn default() -> PiBootStatusType {
        Self::SystemctlShow
    }
}




