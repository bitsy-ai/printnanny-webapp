/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.118.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeSessionBillingAddressCollection {
    #[serde(rename = "auto")]
    Auto,
    #[serde(rename = "required")]
    Required,

}

impl ToString for StripeSessionBillingAddressCollection {
    fn to_string(&self) -> String {
        match self {
            Self::Auto => String::from("auto"),
            Self::Required => String::from("required"),
        }
    }
}

impl Default for StripeSessionBillingAddressCollection {
    fn default() -> StripeSessionBillingAddressCollection {
        Self::Auto
    }
}




