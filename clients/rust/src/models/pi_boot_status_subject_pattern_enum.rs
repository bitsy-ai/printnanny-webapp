/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiBootStatusSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.status.boot")]
    PiPiIdStatusBoot,

}

impl ToString for PiBootStatusSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdStatusBoot => String::from("pi.{pi_id}.status.boot"),
        }
    }
}

impl Default for PiBootStatusSubjectPatternEnum {
    fn default() -> PiBootStatusSubjectPatternEnum {
        Self::PiPiIdStatusBoot
    }
}




