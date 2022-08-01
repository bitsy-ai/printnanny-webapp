/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiBootEventType {
    #[serde(rename = "BootStart")]
    BootStart,
    #[serde(rename = "BootSuccess")]
    BootSuccess,
    #[serde(rename = "BootDegraded")]
    BootDegraded,

}

impl ToString for PiBootEventType {
    fn to_string(&self) -> String {
        match self {
            Self::BootStart => String::from("BootStart"),
            Self::BootSuccess => String::from("BootSuccess"),
            Self::BootDegraded => String::from("BootDegraded"),
        }
    }
}

impl Default for PiBootEventType {
    fn default() -> PiBootEventType {
        Self::BootStart
    }
}




