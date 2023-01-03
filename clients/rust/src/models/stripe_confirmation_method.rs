/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeConfirmationMethod {
    #[serde(rename = "automatic")]
    Automatic,
    #[serde(rename = "manual")]
    Manual,

}

impl ToString for StripeConfirmationMethod {
    fn to_string(&self) -> String {
        match self {
            Self::Automatic => String::from("automatic"),
            Self::Manual => String::from("manual"),
        }
    }
}

impl Default for StripeConfirmationMethod {
    fn default() -> StripeConfirmationMethod {
        Self::Automatic
    }
}




