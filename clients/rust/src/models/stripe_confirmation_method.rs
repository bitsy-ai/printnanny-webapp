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
pub enum StripeConfirmationMethod {

}

impl ToString for StripeConfirmationMethod {
    fn to_string(&self) -> String {
        match self {
        }
    }
}

impl Default for StripeConfirmationMethod {
    fn default() -> StripeConfirmationMethod {
        Self::
    }
}




