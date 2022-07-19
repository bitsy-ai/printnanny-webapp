/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.94.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintEventName {
    #[serde(rename = "Startup")]
    Startup,
    #[serde(rename = "Shutdown")]
    Shutdown,
    #[serde(rename = "PrintProgress")]
    PrintProgress,
    #[serde(rename = "Connecting")]
    Connecting,
    #[serde(rename = "Connected")]
    Connected,
    #[serde(rename = "Disconnecting")]
    Disconnecting,
    #[serde(rename = "Disconnected")]
    Disconnected,
    #[serde(rename = "Error")]
    Error,
    #[serde(rename = "PrintStarted")]
    PrintStarted,
    #[serde(rename = "PrintFailed")]
    PrintFailed,
    #[serde(rename = "PrintDone")]
    PrintDone,
    #[serde(rename = "PrintCancelling")]
    PrintCancelling,
    #[serde(rename = "PrintCancelled")]
    PrintCancelled,
    #[serde(rename = "PrintPaused")]
    PrintPaused,
    #[serde(rename = "PrintResumed")]
    PrintResumed,

}

impl ToString for OctoPrintEventName {
    fn to_string(&self) -> String {
        match self {
            Self::Startup => String::from("Startup"),
            Self::Shutdown => String::from("Shutdown"),
            Self::PrintProgress => String::from("PrintProgress"),
            Self::Connecting => String::from("Connecting"),
            Self::Connected => String::from("Connected"),
            Self::Disconnecting => String::from("Disconnecting"),
            Self::Disconnected => String::from("Disconnected"),
            Self::Error => String::from("Error"),
            Self::PrintStarted => String::from("PrintStarted"),
            Self::PrintFailed => String::from("PrintFailed"),
            Self::PrintDone => String::from("PrintDone"),
            Self::PrintCancelling => String::from("PrintCancelling"),
            Self::PrintCancelled => String::from("PrintCancelled"),
            Self::PrintPaused => String::from("PrintPaused"),
            Self::PrintResumed => String::from("PrintResumed"),
        }
    }
}

impl Default for OctoPrintEventName {
    fn default() -> OctoPrintEventName {
        Self::Startup
    }
}




