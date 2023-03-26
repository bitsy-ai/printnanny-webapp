/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.129.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripePaymentIntentStatus {
    #[serde(rename = "canceled")]
    Canceled,
    #[serde(rename = "processing")]
    Processing,
    #[serde(rename = "requires_action")]
    RequiresAction,
    #[serde(rename = "requires_capture")]
    RequiresCapture,
    #[serde(rename = "requires_confirmation")]
    RequiresConfirmation,
    #[serde(rename = "requires_payment_method")]
    RequiresPaymentMethod,
    #[serde(rename = "succeeded")]
    Succeeded,

}

impl ToString for StripePaymentIntentStatus {
    fn to_string(&self) -> String {
        match self {
            Self::Canceled => String::from("canceled"),
            Self::Processing => String::from("processing"),
            Self::RequiresAction => String::from("requires_action"),
            Self::RequiresCapture => String::from("requires_capture"),
            Self::RequiresConfirmation => String::from("requires_confirmation"),
            Self::RequiresPaymentMethod => String::from("requires_payment_method"),
            Self::Succeeded => String::from("succeeded"),
        }
    }
}

impl Default for StripePaymentIntentStatus {
    fn default() -> StripePaymentIntentStatus {
        Self::Canceled
    }
}




