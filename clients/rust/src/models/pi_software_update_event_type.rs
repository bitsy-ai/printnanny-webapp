/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiSoftwareUpdateEventType {
    #[serde(rename = "Started")]
    Started,
    #[serde(rename = "Success")]
    Success,
    #[serde(rename = "Error")]
    Error,

}

impl ToString for PiSoftwareUpdateEventType {
    fn to_string(&self) -> String {
        match self {
            Self::Started => String::from("Started"),
            Self::Success => String::from("Success"),
            Self::Error => String::from("Error"),
        }
    }
}

impl Default for PiSoftwareUpdateEventType {
    fn default() -> PiSoftwareUpdateEventType {
        Self::Started
    }
}




