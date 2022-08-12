/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.9
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintClientStatusSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.octoprint.client")]
    PiPiIdOctoprintClient,

}

impl ToString for OctoPrintClientStatusSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdOctoprintClient => String::from("pi.{pi_id}.octoprint.client"),
        }
    }
}

impl Default for OctoPrintClientStatusSubjectPatternEnum {
    fn default() -> OctoPrintClientStatusSubjectPatternEnum {
        Self::PiPiIdOctoprintClient
    }
}




