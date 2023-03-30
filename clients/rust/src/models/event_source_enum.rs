/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.9
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// EventSourceEnum : * `octoprint` - Events originating from OctoPrint * `printnanny_os` - Event originating from PrintNanny OS * `printnanny_cloud` - Events originating from PrintNanny Cloud services * `mainsail` - Events originating from moonraker

/// * `octoprint` - Events originating from OctoPrint * `printnanny_os` - Event originating from PrintNanny OS * `printnanny_cloud` - Events originating from PrintNanny Cloud services * `mainsail` - Events originating from moonraker
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum EventSourceEnum {
    #[serde(rename = "octoprint")]
    Octoprint,
    #[serde(rename = "printnanny_os")]
    PrintnannyOs,
    #[serde(rename = "printnanny_cloud")]
    PrintnannyCloud,
    #[serde(rename = "mainsail")]
    Mainsail,

}

impl ToString for EventSourceEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Octoprint => String::from("octoprint"),
            Self::PrintnannyOs => String::from("printnanny_os"),
            Self::PrintnannyCloud => String::from("printnanny_cloud"),
            Self::Mainsail => String::from("mainsail"),
        }
    }
}

impl Default for EventSourceEnum {
    fn default() -> EventSourceEnum {
        Self::Octoprint
    }
}




