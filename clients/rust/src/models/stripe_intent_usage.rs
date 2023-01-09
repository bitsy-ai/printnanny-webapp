/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.120.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeIntentUsage {
    #[serde(rename = "off_session")]
    OffSession,
    #[serde(rename = "on_session")]
    OnSession,

}

impl ToString for StripeIntentUsage {
    fn to_string(&self) -> String {
        match self {
            Self::OffSession => String::from("off_session"),
            Self::OnSession => String::from("on_session"),
        }
    }
}

impl Default for StripeIntentUsage {
    fn default() -> StripeIntentUsage {
        Self::OffSession
    }
}




