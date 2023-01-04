/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.119.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum GcodeEventType {
    #[serde(rename = "M300")]
    M300,
    #[serde(rename = "M245")]
    M245,
    #[serde(rename = "G4")]
    G4,
    #[serde(rename = "M112")]
    M112,
    #[serde(rename = "M600")]
    M600,
    #[serde(rename = "M701")]
    M701,
    #[serde(rename = "M702")]
    M702,
    #[serde(rename = "G28")]
    G28,
    #[serde(rename = "M81")]
    M81,
    #[serde(rename = "M80")]
    M80,

}

impl ToString for GcodeEventType {
    fn to_string(&self) -> String {
        match self {
            Self::M300 => String::from("M300"),
            Self::M245 => String::from("M245"),
            Self::G4 => String::from("G4"),
            Self::M112 => String::from("M112"),
            Self::M600 => String::from("M600"),
            Self::M701 => String::from("M701"),
            Self::M702 => String::from("M702"),
            Self::G28 => String::from("G28"),
            Self::M81 => String::from("M81"),
            Self::M80 => String::from("M80"),
        }
    }
}

impl Default for GcodeEventType {
    fn default() -> GcodeEventType {
        Self::M300
    }
}




