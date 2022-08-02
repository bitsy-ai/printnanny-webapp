/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.99.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum CollectionMethodEnum {
    #[serde(rename = "charge_automatically")]
    ChargeAutomatically,
    #[serde(rename = "send_invoice")]
    SendInvoice,

}

impl ToString for CollectionMethodEnum {
    fn to_string(&self) -> String {
        match self {
            Self::ChargeAutomatically => String::from("charge_automatically"),
            Self::SendInvoice => String::from("send_invoice"),
        }
    }
}

impl Default for CollectionMethodEnum {
    fn default() -> CollectionMethodEnum {
        Self::ChargeAutomatically
    }
}




