/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.131.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// StripeCustomerTaxExempt : * `exempt` - Exempt * `none` - None * `reverse` - Reverse

/// * `exempt` - Exempt * `none` - None * `reverse` - Reverse
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeCustomerTaxExempt {
    #[serde(rename = "exempt")]
    Exempt,
    #[serde(rename = "none")]
    None,
    #[serde(rename = "reverse")]
    Reverse,

}

impl ToString for StripeCustomerTaxExempt {
    fn to_string(&self) -> String {
        match self {
            Self::Exempt => String::from("exempt"),
            Self::None => String::from("none"),
            Self::Reverse => String::from("reverse"),
        }
    }
}

impl Default for StripeCustomerTaxExempt {
    fn default() -> StripeCustomerTaxExempt {
        Self::Exempt
    }
}




