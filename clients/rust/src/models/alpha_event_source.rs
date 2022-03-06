/*
 * printnanny-api-client
 *
 * Official API client library forprintnanny.ai print-nanny.com
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum AlphaEventSource {
    #[serde(rename = "octoprint")]
    Octoprint,
    #[serde(rename = "plugin_octoprint_nanny")]
    PluginOctoprintNanny,
    #[serde(rename = "remote_command")]
    RemoteCommand,

}

impl ToString for AlphaEventSource {
    fn to_string(&self) -> String {
        match self {
            Self::Octoprint => String::from("octoprint"),
            Self::PluginOctoprintNanny => String::from("plugin_octoprint_nanny"),
            Self::RemoteCommand => String::from("remote_command"),
        }
    }
}

impl Default for AlphaEventSource {
    fn default() -> AlphaEventSource {
        Self::Octoprint
    }
}




