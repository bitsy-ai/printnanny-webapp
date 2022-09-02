/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.106.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintPrintJobStatusType {
    #[serde(rename = "PrintProgress")]
    PrintProgress,
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

impl ToString for OctoPrintPrintJobStatusType {
    fn to_string(&self) -> String {
        match self {
            Self::PrintProgress => String::from("PrintProgress"),
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

impl Default for OctoPrintPrintJobStatusType {
    fn default() -> OctoPrintPrintJobStatusType {
        Self::PrintProgress
    }
}




