/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.102.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintPrintJobStatusSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.octoprint.print_job")]
    PiPiIdOctoprintPrintJob,

}

impl ToString for OctoPrintPrintJobStatusSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdOctoprintPrintJob => String::from("pi.{pi_id}.octoprint.print_job"),
        }
    }
}

impl Default for OctoPrintPrintJobStatusSubjectPatternEnum {
    fn default() -> OctoPrintPrintJobStatusSubjectPatternEnum {
        Self::PiPiIdOctoprintPrintJob
    }
}




