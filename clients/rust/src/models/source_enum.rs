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
pub enum SourceEnum {
    #[serde(rename = "octoprint")]
    Octoprint,
    #[serde(rename = "printnanny_os")]
    PrintnannyOs,
    #[serde(rename = "printnanny_cloud")]
    PrintnannyCloud,
    #[serde(rename = "mainsail")]
    Mainsail,

}

impl ToString for SourceEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Octoprint => String::from("octoprint"),
            Self::PrintnannyOs => String::from("printnanny_os"),
            Self::PrintnannyCloud => String::from("printnanny_cloud"),
            Self::Mainsail => String::from("mainsail"),
        }
    }
}

impl Default for SourceEnum {
    fn default() -> SourceEnum {
        Self::Octoprint
    }
}




