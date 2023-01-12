/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.122.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripePaymentIntentCancellationReason {
    #[serde(rename = "abandoned")]
    Abandoned,
    #[serde(rename = "automatic")]
    Automatic,
    #[serde(rename = "duplicate")]
    Duplicate,
    #[serde(rename = "failed_invoice")]
    FailedInvoice,
    #[serde(rename = "fraudulent")]
    Fraudulent,
    #[serde(rename = "requested_by_customer")]
    RequestedByCustomer,
    #[serde(rename = "void_invoice")]
    VoidInvoice,

}

impl ToString for StripePaymentIntentCancellationReason {
    fn to_string(&self) -> String {
        match self {
            Self::Abandoned => String::from("abandoned"),
            Self::Automatic => String::from("automatic"),
            Self::Duplicate => String::from("duplicate"),
            Self::FailedInvoice => String::from("failed_invoice"),
            Self::Fraudulent => String::from("fraudulent"),
            Self::RequestedByCustomer => String::from("requested_by_customer"),
            Self::VoidInvoice => String::from("void_invoice"),
        }
    }
}

impl Default for StripePaymentIntentCancellationReason {
    fn default() -> StripePaymentIntentCancellationReason {
        Self::Abandoned
    }
}




