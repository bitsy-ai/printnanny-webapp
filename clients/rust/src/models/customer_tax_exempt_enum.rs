/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.0.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum CustomerTaxExemptEnum {
    #[serde(rename = "exempt")]
    Exempt,
    #[serde(rename = "none")]
    None,
    #[serde(rename = "reverse")]
    Reverse,

}

impl ToString for CustomerTaxExemptEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Exempt => String::from("exempt"),
            Self::None => String::from("none"),
            Self::Reverse => String::from("reverse"),
        }
    }
}

impl Default for CustomerTaxExemptEnum {
    fn default() -> CustomerTaxExemptEnum {
        Self::Exempt
    }
}




