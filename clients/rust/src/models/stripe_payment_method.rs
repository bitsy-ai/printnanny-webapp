/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.101.2
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct StripePaymentMethod {
    #[serde(rename = "djstripe_id")]
    pub djstripe_id: i32,
    #[serde(rename = "djstripe_created")]
    pub djstripe_created: String,
    #[serde(rename = "djstripe_updated")]
    pub djstripe_updated: String,
    #[serde(rename = "id")]
    pub id: String,
    /// Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.
    #[serde(rename = "livemode", skip_serializing_if = "Option::is_none")]
    pub livemode: Option<bool>,
    /// The datetime this object was created in stripe.
    #[serde(rename = "created", skip_serializing_if = "Option::is_none")]
    pub created: Option<String>,
    /// A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.
    #[serde(rename = "metadata", skip_serializing_if = "Option::is_none")]
    pub metadata: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    #[serde(rename = "billing_details")]
    pub billing_details: ::std::collections::HashMap<String, serde_json::Value>,
    /// The type of the PaymentMethod.
    #[serde(rename = "type")]
    pub _type: Option<Box<crate::models::TypeEnum>>,
    /// Additional information for payment methods of type `acss_debit`
    #[serde(rename = "acss_debit", skip_serializing_if = "Option::is_none")]
    pub acss_debit: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `afterpay_clearpay`
    #[serde(rename = "afterpay_clearpay", skip_serializing_if = "Option::is_none")]
    pub afterpay_clearpay: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `alipay`
    #[serde(rename = "alipay", skip_serializing_if = "Option::is_none")]
    pub alipay: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `au_becs_debit`
    #[serde(rename = "au_becs_debit", skip_serializing_if = "Option::is_none")]
    pub au_becs_debit: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `bacs_debit`
    #[serde(rename = "bacs_debit", skip_serializing_if = "Option::is_none")]
    pub bacs_debit: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `bancontact`
    #[serde(rename = "bancontact", skip_serializing_if = "Option::is_none")]
    pub bancontact: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `boleto`
    #[serde(rename = "boleto", skip_serializing_if = "Option::is_none")]
    pub boleto: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `card`
    #[serde(rename = "card", skip_serializing_if = "Option::is_none")]
    pub card: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `card_present`
    #[serde(rename = "card_present", skip_serializing_if = "Option::is_none")]
    pub card_present: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `eps`
    #[serde(rename = "eps", skip_serializing_if = "Option::is_none")]
    pub eps: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `fpx`
    #[serde(rename = "fpx", skip_serializing_if = "Option::is_none")]
    pub fpx: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `giropay`
    #[serde(rename = "giropay", skip_serializing_if = "Option::is_none")]
    pub giropay: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `grabpay`
    #[serde(rename = "grabpay", skip_serializing_if = "Option::is_none")]
    pub grabpay: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `ideal`
    #[serde(rename = "ideal", skip_serializing_if = "Option::is_none")]
    pub ideal: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `interac_present`
    #[serde(rename = "interac_present", skip_serializing_if = "Option::is_none")]
    pub interac_present: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `oxxo`
    #[serde(rename = "oxxo", skip_serializing_if = "Option::is_none")]
    pub oxxo: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `p24`
    #[serde(rename = "p24", skip_serializing_if = "Option::is_none")]
    pub p24: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `sepa_debit`
    #[serde(rename = "sepa_debit", skip_serializing_if = "Option::is_none")]
    pub sepa_debit: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `sofort`
    #[serde(rename = "sofort", skip_serializing_if = "Option::is_none")]
    pub sofort: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Additional information for payment methods of type `wechat_pay`
    #[serde(rename = "wechat_pay", skip_serializing_if = "Option::is_none")]
    pub wechat_pay: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
    /// Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.
    #[serde(rename = "customer", skip_serializing_if = "Option::is_none")]
    pub customer: Option<String>,
}

impl StripePaymentMethod {
    pub fn new(djstripe_id: i32, djstripe_created: String, djstripe_updated: String, id: String, billing_details: ::std::collections::HashMap<String, serde_json::Value>, _type: Option<crate::models::TypeEnum>) -> StripePaymentMethod {
        StripePaymentMethod {
            djstripe_id,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            billing_details,
            _type: _type.map(Box::new),
            acss_debit: None,
            afterpay_clearpay: None,
            alipay: None,
            au_becs_debit: None,
            bacs_debit: None,
            bancontact: None,
            boleto: None,
            card: None,
            card_present: None,
            eps: None,
            fpx: None,
            giropay: None,
            grabpay: None,
            ideal: None,
            interac_present: None,
            oxxo: None,
            p24: None,
            sepa_debit: None,
            sofort: None,
            wechat_pay: None,
            djstripe_owner_account: None,
            customer: None,
        }
    }
}


