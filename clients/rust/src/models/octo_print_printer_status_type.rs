/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.7
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintPrinterStatusType {
    #[serde(rename = "PrinterOffline")]
    PrinterOffline,
    #[serde(rename = "PrinterOpenSerial")]
    PrinterOpenSerial,
    #[serde(rename = "PrinterConnecting")]
    PrinterConnecting,
    #[serde(rename = "PrinterOperational")]
    PrinterOperational,
    #[serde(rename = "PrinterStarting")]
    PrinterStarting,
    #[serde(rename = "PrinterInProgress")]
    PrinterInProgress,
    #[serde(rename = "PrinterCancelling")]
    PrinterCancelling,
    #[serde(rename = "PrinterPausing")]
    PrinterPausing,
    #[serde(rename = "PrinterPaused")]
    PrinterPaused,
    #[serde(rename = "PrinterResuming")]
    PrinterResuming,
    #[serde(rename = "PrinterFinishing")]
    PrinterFinishing,
    #[serde(rename = "PrinterError")]
    PrinterError,

}

impl ToString for OctoPrintPrinterStatusType {
    fn to_string(&self) -> String {
        match self {
            Self::PrinterOffline => String::from("PrinterOffline"),
            Self::PrinterOpenSerial => String::from("PrinterOpenSerial"),
            Self::PrinterConnecting => String::from("PrinterConnecting"),
            Self::PrinterOperational => String::from("PrinterOperational"),
            Self::PrinterStarting => String::from("PrinterStarting"),
            Self::PrinterInProgress => String::from("PrinterInProgress"),
            Self::PrinterCancelling => String::from("PrinterCancelling"),
            Self::PrinterPausing => String::from("PrinterPausing"),
            Self::PrinterPaused => String::from("PrinterPaused"),
            Self::PrinterResuming => String::from("PrinterResuming"),
            Self::PrinterFinishing => String::from("PrinterFinishing"),
            Self::PrinterError => String::from("PrinterError"),
        }
    }
}

impl Default for OctoPrintPrinterStatusType {
    fn default() -> OctoPrintPrinterStatusType {
        Self::PrinterOffline
    }
}




