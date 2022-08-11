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
pub enum OctoPrintServerStatusSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.octoprint.server")]
    PiPiIdOctoprintServer,

}

impl ToString for OctoPrintServerStatusSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdOctoprintServer => String::from("pi.{pi_id}.octoprint.server"),
        }
    }
}

impl Default for OctoPrintServerStatusSubjectPatternEnum {
    fn default() -> OctoPrintServerStatusSubjectPatternEnum {
        Self::PiPiIdOctoprintServer
    }
}



