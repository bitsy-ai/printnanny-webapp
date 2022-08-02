/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiGstreamerCommandType {
    #[serde(rename = "Start")]
    Start,
    #[serde(rename = "Stop")]
    Stop,

}

impl ToString for PiGstreamerCommandType {
    fn to_string(&self) -> String {
        match self {
            Self::Start => String::from("Start"),
            Self::Stop => String::from("Stop"),
        }
    }
}

impl Default for PiGstreamerCommandType {
    fn default() -> PiGstreamerCommandType {
        Self::Start
    }
}




