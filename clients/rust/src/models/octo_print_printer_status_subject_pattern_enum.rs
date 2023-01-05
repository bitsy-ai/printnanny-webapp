/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.119.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintPrinterStatusSubjectPatternEnum {
    #[serde(rename = "pi.{pi_id}.octoprint.printer")]
    PiPiIdOctoprintPrinter,

}

impl ToString for OctoPrintPrinterStatusSubjectPatternEnum {
    fn to_string(&self) -> String {
        match self {
            Self::PiPiIdOctoprintPrinter => String::from("pi.{pi_id}.octoprint.printer"),
        }
    }
}

impl Default for OctoPrintPrinterStatusSubjectPatternEnum {
    fn default() -> OctoPrintPrinterStatusSubjectPatternEnum {
        Self::PiPiIdOctoprintPrinter
    }
}




