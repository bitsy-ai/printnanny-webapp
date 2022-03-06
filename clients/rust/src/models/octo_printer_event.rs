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
pub enum OctoPrinterEvent {
    #[serde(rename = "Operational")]
    Operational,
    #[serde(rename = "Paused")]
    Paused,
    #[serde(rename = "Cancelling")]
    Cancelling,
    #[serde(rename = "Printing")]
    Printing,
    #[serde(rename = "Pausing")]
    Pausing,
    #[serde(rename = "sdReady")]
    SdReady,
    #[serde(rename = "Error")]
    Error,
    #[serde(rename = "ReadyPrinter Ready")]
    ReadyPrinterReady,
    #[serde(rename = "closedOrError")]
    ClosedOrError,
    #[serde(rename = "Offline")]
    Offline,
    #[serde(rename = "Opening serial connection")]
    OpeningSerialConnection,
    #[serde(rename = "Connection")]
    Connection,
    #[serde(rename = "Resuming")]
    Resuming,
    #[serde(rename = "Finishing")]
    Finishing,
    #[serde(rename = "PrinterStateChanged")]
    PrinterStateChanged,
    #[serde(rename = "Connected")]
    Connected,
    #[serde(rename = "Disconnected")]
    Disconnected,
    #[serde(rename = "PrinterReset")]
    PrinterReset,
    #[serde(rename = "FirmwareData")]
    FirmwareData,

}

impl ToString for OctoPrinterEvent {
    fn to_string(&self) -> String {
        match self {
            Self::Operational => String::from("Operational"),
            Self::Paused => String::from("Paused"),
            Self::Cancelling => String::from("Cancelling"),
            Self::Printing => String::from("Printing"),
            Self::Pausing => String::from("Pausing"),
            Self::SdReady => String::from("sdReady"),
            Self::Error => String::from("Error"),
            Self::ReadyPrinterReady => String::from("ReadyPrinter Ready"),
            Self::ClosedOrError => String::from("closedOrError"),
            Self::Offline => String::from("Offline"),
            Self::OpeningSerialConnection => String::from("Opening serial connection"),
            Self::Connection => String::from("Connection"),
            Self::Resuming => String::from("Resuming"),
            Self::Finishing => String::from("Finishing"),
            Self::PrinterStateChanged => String::from("PrinterStateChanged"),
            Self::Connected => String::from("Connected"),
            Self::Disconnected => String::from("Disconnected"),
            Self::PrinterReset => String::from("PrinterReset"),
            Self::FirmwareData => String::from("FirmwareData"),
        }
    }
}

impl Default for OctoPrinterEvent {
    fn default() -> OctoPrinterEvent {
        Self::Operational
    }
}




