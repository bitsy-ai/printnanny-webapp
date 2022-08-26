/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.105.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum PiCamStatusSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.status.cam")]
    PiPiIdStatusCam,

}

impl ToString for PiCamStatusSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdStatusCam => String::from("pi.{pi_id}.status.cam"),
        }
    }
}

impl Default for PiCamStatusSubjectPatternEnum {
    fn default() -> PiCamStatusSubjectPatternEnum {
        Self::PiPiIdStatusCam
    }
}




