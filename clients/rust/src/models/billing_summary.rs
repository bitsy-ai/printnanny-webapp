/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.100.5
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct BillingSummary {
    #[serde(rename = "subscription")]
    pub subscription: Box<crate::models::StripeSubscription>,
    #[serde(rename = "customer")]
    pub customer: Box<crate::models::StripeCustomer>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<Box<crate::models::User>>,
    #[serde(rename = "billing_portal_url")]
    pub billing_portal_url: String,
}

impl BillingSummary {
    pub fn new(subscription: crate::models::StripeSubscription, customer: crate::models::StripeCustomer, billing_portal_url: String) -> BillingSummary {
        BillingSummary {
            subscription: Box::new(subscription),
            customer: Box::new(customer),
            user: None,
            billing_portal_url,
        }
    }
}


