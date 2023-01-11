/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.121.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiBootCommandSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.command.boot")]
    PiPiIdCommandBoot,

}

impl ToString for PiBootCommandSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdCommandBoot => String::from("pi.{pi_id}.command.boot"),
        }
    }
}

impl Default for PiBootCommandSubjectPatternEnum {
    fn default() -> PiBootCommandSubjectPatternEnum {
        Self::PiPiIdCommandBoot
    }
}




