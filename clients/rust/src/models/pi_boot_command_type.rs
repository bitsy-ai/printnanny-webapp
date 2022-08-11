/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiBootCommandType {
    #[serde(rename = "Reboot")]
    Reboot,
    #[serde(rename = "Shutdown")]
    Shutdown,
    #[serde(rename = "SyncSettings")]
    SyncSettings,

}

impl ToString for PiBootCommandType {
    fn to_string(&self) -> String {
        match self {
            Self::Reboot => String::from("Reboot"),
            Self::Shutdown => String::from("Shutdown"),
            Self::SyncSettings => String::from("SyncSettings"),
        }
    }
}

impl Default for PiBootCommandType {
    fn default() -> PiBootCommandType {
        Self::Reboot
    }
}




