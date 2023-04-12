/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.132.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// StripeSourceCodeVerificationStatus : * `failed` - Failed * `pending` - Pending * `succeeded` - Succeeded

/// * `failed` - Failed * `pending` - Pending * `succeeded` - Succeeded
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeSourceCodeVerificationStatus {
    #[serde(rename = "failed")]
    Failed,
    #[serde(rename = "pending")]
    Pending,
    #[serde(rename = "succeeded")]
    Succeeded,

}

impl ToString for StripeSourceCodeVerificationStatus {
    fn to_string(&self) -> String {
        match self {
            Self::Failed => String::from("failed"),
            Self::Pending => String::from("pending"),
            Self::Succeeded => String::from("succeeded"),
        }
    }
}

impl Default for StripeSourceCodeVerificationStatus {
    fn default() -> StripeSourceCodeVerificationStatus {
        Self::Failed
    }
}




