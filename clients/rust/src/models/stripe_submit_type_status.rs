/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeSubmitTypeStatus {
    #[serde(rename = "auto")]
    Auto,
    #[serde(rename = "book")]
    Book,
    #[serde(rename = "donate")]
    Donate,
    #[serde(rename = "pay")]
    Pay,

}

impl ToString for StripeSubmitTypeStatus {
    fn to_string(&self) -> String {
        match self {
            Self::Auto => String::from("auto"),
            Self::Book => String::from("book"),
            Self::Donate => String::from("donate"),
            Self::Pay => String::from("pay"),
        }
    }
}

impl Default for StripeSubmitTypeStatus {
    fn default() -> StripeSubmitTypeStatus {
        Self::Auto
    }
}




