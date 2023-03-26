/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.8
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiSoftwareUpdateCommandSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.command.swupdate")]
    PiPiIdCommandSwupdate,

}

impl ToString for PiSoftwareUpdateCommandSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdCommandSwupdate => String::from("pi.{pi_id}.command.swupdate"),
        }
    }
}

impl Default for PiSoftwareUpdateCommandSubjectPatternEnum {
    fn default() -> PiSoftwareUpdateCommandSubjectPatternEnum {
        Self::PiPiIdCommandSwupdate
    }
}




