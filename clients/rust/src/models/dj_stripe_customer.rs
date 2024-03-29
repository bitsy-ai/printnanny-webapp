/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.135.1
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct DjStripeCustomer {
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
    /// A description of this object.
    #[serde(rename = "description", skip_serializing_if = "Option::is_none")]
    pub description: Option<String>,
    /// The customer's address.
    #[serde(rename = "address", skip_serializing_if = "Option::is_none")]
    pub address: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Current balance (in cents), if any, being stored on the customer's account. If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account for recurring billing purposes (i.e., subscriptions, invoices, invoice items).
    #[serde(rename = "balance", skip_serializing_if = "Option::is_none")]
    pub balance: Option<i64>,
    /// The currency the customer can be charged in for recurring billing purposes
    #[serde(rename = "currency", skip_serializing_if = "Option::is_none")]
    pub currency: Option<String>,
    /// Whether or not the latest charge for the customer's latest invoice has failed.
    #[serde(rename = "delinquent", skip_serializing_if = "Option::is_none")]
    pub delinquent: Option<bool>,
    /// Whether the Customer instance has been deleted upstream in Stripe or not.
    #[serde(rename = "deleted", skip_serializing_if = "Option::is_none")]
    pub deleted: Option<bool>,
    /// If a coupon is present, the date at which it was applied.
    #[serde(rename = "coupon_start")]
    pub coupon_start: Option<String>,
    /// If a coupon is present and has a limited duration, the date that the discount will end.
    #[serde(rename = "coupon_end")]
    pub coupon_end: Option<String>,
    #[serde(rename = "email", skip_serializing_if = "Option::is_none")]
    pub email: Option<String>,
    /// The prefix for the customer used to generate unique invoice numbers.
    #[serde(rename = "invoice_prefix", skip_serializing_if = "Option::is_none")]
    pub invoice_prefix: Option<String>,
    /// The customer's default invoice settings.
    #[serde(rename = "invoice_settings", skip_serializing_if = "Option::is_none")]
    pub invoice_settings: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The customer's full name or business name.
    #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    /// The customer's phone number.
    #[serde(rename = "phone", skip_serializing_if = "Option::is_none")]
    pub phone: Option<String>,
    /// The customer's preferred locales (languages), ordered by preference.
    #[serde(rename = "preferred_locales", skip_serializing_if = "Option::is_none")]
    pub preferred_locales: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Shipping information associated with the customer.
    #[serde(rename = "shipping", skip_serializing_if = "Option::is_none")]
    pub shipping: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Describes the customer's tax exemption status. When set to reverse, invoice and receipt PDFs include the text \"Reverse charge\".  * `exempt` - Exempt * `none` - None * `reverse` - Reverse
    #[serde(rename = "tax_exempt", skip_serializing_if = "Option::is_none")]
    pub tax_exempt: Option<Box<crate::models::StripeCustomerTaxExempt>>,
    #[serde(rename = "date_purged")]
    pub date_purged: Option<String>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account")]
    pub djstripe_owner_account: Option<String>,
    #[serde(rename = "default_source", skip_serializing_if = "Option::is_none")]
    pub default_source: Option<String>,
    #[serde(rename = "coupon", skip_serializing_if = "Option::is_none")]
    pub coupon: Option<i32>,
    /// default payment method used for subscriptions and invoices for the customer.
    #[serde(rename = "default_payment_method", skip_serializing_if = "Option::is_none")]
    pub default_payment_method: Option<String>,
    #[serde(rename = "subscriber")]
    pub subscriber: Option<i32>,
}

impl DjStripeCustomer {
    pub fn new(djstripe_id: i32, djstripe_created: String, djstripe_updated: String, id: String, coupon_start: Option<String>, coupon_end: Option<String>, date_purged: Option<String>, djstripe_owner_account: Option<String>, subscriber: Option<i32>) -> DjStripeCustomer {
        DjStripeCustomer {
            djstripe_id,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            description: None,
            address: None,
            balance: None,
            currency: None,
            delinquent: None,
            deleted: None,
            coupon_start,
            coupon_end,
            email: None,
            invoice_prefix: None,
            invoice_settings: None,
            name: None,
            phone: None,
            preferred_locales: None,
            shipping: None,
            tax_exempt: None,
            date_purged,
            djstripe_owner_account,
            default_source: None,
            coupon: None,
            default_payment_method: None,
            subscriber,
        }
    }
}


