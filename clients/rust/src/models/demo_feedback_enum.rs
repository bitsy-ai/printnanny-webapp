/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// DemoFeedbackEnum : * `pass` - Submission received positive (thumbs up) feedback * `fail` - Submission received negative (thumbs down) feedback * `na` - Submission received N/A (not applicable)

/// * `pass` - Submission received positive (thumbs up) feedback * `fail` - Submission received negative (thumbs down) feedback * `na` - Submission received N/A (not applicable)
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum DemoFeedbackEnum {
    #[serde(rename = "pass")]
    Pass,
    #[serde(rename = "fail")]
    Fail,
    #[serde(rename = "na")]
    Na,

}

impl ToString for DemoFeedbackEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Pass => String::from("pass"),
            Self::Fail => String::from("fail"),
            Self::Na => String::from("na"),
        }
    }
}

impl Default for DemoFeedbackEnum {
    fn default() -> DemoFeedbackEnum {
        Self::Pass
    }
}




