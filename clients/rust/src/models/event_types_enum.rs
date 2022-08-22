/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.103.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum EventTypesEnum {
    #[serde(rename = "PrintQuality")]
    PrintQuality,
    #[serde(rename = "PrintStarted")]
    PrintStarted,
    #[serde(rename = "PrintDone")]
    PrintDone,
    #[serde(rename = "PrintProgress")]
    PrintProgress,
    #[serde(rename = "PrintPaused")]
    PrintPaused,
    #[serde(rename = "PrintCancelled")]
    PrintCancelled,

}

impl ToString for EventTypesEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PrintQuality => String::from("PrintQuality"),
            Self::PrintStarted => String::from("PrintStarted"),
            Self::PrintDone => String::from("PrintDone"),
            Self::PrintProgress => String::from("PrintProgress"),
            Self::PrintPaused => String::from("PrintPaused"),
            Self::PrintCancelled => String::from("PrintCancelled"),
        }
    }
}

impl Default for EventTypesEnum {
    fn default() -> EventTypesEnum {
        Self::PrintQuality
    }
}




