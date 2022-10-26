/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.109.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiSoftwareUpdateStatusSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.status.swupdate")]
    PiPiIdStatusSwupdate,

}

impl ToString for PiSoftwareUpdateStatusSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdStatusSwupdate => String::from("pi.{pi_id}.status.swupdate"),
        }
    }
}

impl Default for PiSoftwareUpdateStatusSubjectPatternEnum {
    fn default() -> PiSoftwareUpdateStatusSubjectPatternEnum {
        Self::PiPiIdStatusSwupdate
    }
}




