/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.123.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum CrashReportStatusEnum {
    #[serde(rename = "Investigating")]
    Investigating,
    #[serde(rename = "Fixed")]
    Fixed,

}

impl ToString for CrashReportStatusEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Investigating => String::from("Investigating"),
            Self::Fixed => String::from("Fixed"),
        }
    }
}

impl Default for CrashReportStatusEnum {
    fn default() -> CrashReportStatusEnum {
        Self::Investigating
    }
}




