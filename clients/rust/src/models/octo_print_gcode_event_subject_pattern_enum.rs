/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.122.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintGcodeEventSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.octoprint.gcode")]
    PiPiIdOctoprintGcode,

}

impl ToString for OctoPrintGcodeEventSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdOctoprintGcode => String::from("pi.{pi_id}.octoprint.gcode"),
        }
    }
}

impl Default for OctoPrintGcodeEventSubjectPatternEnum {
    fn default() -> OctoPrintGcodeEventSubjectPatternEnum {
        Self::PiPiIdOctoprintGcode
    }
}




