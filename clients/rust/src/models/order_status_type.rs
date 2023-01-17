/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.124.3
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OrderStatusType {
    #[serde(rename = "checkout_session_created")]
    CheckoutSessionCreated,
    #[serde(rename = "checkout_session_completed")]
    CheckoutSessionCompleted,
    #[serde(rename = "checkout_session_expired")]
    CheckoutSessionExpired,
    #[serde(rename = "processing")]
    Processing,
    #[serde(rename = "ready_to_ship")]
    ReadyToShip,
    #[serde(rename = "shipped")]
    Shipped,
    #[serde(rename = "goods_fulfilled")]
    GoodsFulfilled,
    #[serde(rename = "service_fulfilled")]
    ServiceFulfilled,
    #[serde(rename = "refund_requested")]
    RefundRequested,
    #[serde(rename = "refund_granted")]
    RefundGranted,

}

impl ToString for OrderStatusType {
    fn to_string(&self) -> String {
        match self {
            Self::CheckoutSessionCreated => String::from("checkout_session_created"),
            Self::CheckoutSessionCompleted => String::from("checkout_session_completed"),
            Self::CheckoutSessionExpired => String::from("checkout_session_expired"),
            Self::Processing => String::from("processing"),
            Self::ReadyToShip => String::from("ready_to_ship"),
            Self::Shipped => String::from("shipped"),
            Self::GoodsFulfilled => String::from("goods_fulfilled"),
            Self::ServiceFulfilled => String::from("service_fulfilled"),
            Self::RefundRequested => String::from("refund_requested"),
            Self::RefundGranted => String::from("refund_granted"),
        }
    }
}

impl Default for OrderStatusType {
    fn default() -> OrderStatusType {
        Self::CheckoutSessionCreated
    }
}




