/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.127.4
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct DjStripeCharge {
    #[serde(rename = "djstripe_id")]
    pub djstripe_id: i32,
    #[serde(rename = "failure_code")]
    pub failure_code: crate::models::StripeApiErrorCode,
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
    /// Amount charged (as decimal).
    #[serde(rename = "amount")]
    pub amount: String,
    /// Amount (as decimal) captured (can be less than the amount attribute on the charge if a partial capture was issued).
    #[serde(rename = "amount_captured", skip_serializing_if = "Option::is_none")]
    pub amount_captured: Option<String>,
    /// Amount (as decimal) refunded (can be less than the amount attribute on the charge if a partial refund was issued).
    #[serde(rename = "amount_refunded")]
    pub amount_refunded: String,
    /// ID of the Connect application that created the charge.
    #[serde(rename = "application", skip_serializing_if = "Option::is_none")]
    pub application: Option<String>,
    /// The amount (as decimal) of the application fee (if any) requested for the charge.
    #[serde(rename = "application_fee_amount", skip_serializing_if = "Option::is_none")]
    pub application_fee_amount: Option<String>,
    /// Billing information associated with the PaymentMethod at the time of the transaction.
    #[serde(rename = "billing_details", skip_serializing_if = "Option::is_none")]
    pub billing_details: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The full statement descriptor that is passed to card networks, and that is displayed on your customers' credit card and bank statements. Allows you to see what the statement descriptor looks like after the static and dynamic portions are combined.
    #[serde(rename = "calculated_statement_descriptor", skip_serializing_if = "Option::is_none")]
    pub calculated_statement_descriptor: Option<String>,
    /// If the charge was created without capturing, this boolean represents whether or not it is still uncaptured or has since been captured.
    #[serde(rename = "captured", skip_serializing_if = "Option::is_none")]
    pub captured: Option<bool>,
    /// The currency in which the charge was made.
    #[serde(rename = "currency")]
    pub currency: String,
    /// Whether the charge has been disputed.
    #[serde(rename = "disputed", skip_serializing_if = "Option::is_none")]
    pub disputed: Option<bool>,
    /// Message to user further explaining reason for charge failure if available.
    #[serde(rename = "failure_message", skip_serializing_if = "Option::is_none")]
    pub failure_message: Option<String>,
    /// Hash with information on fraud assessments for the charge.
    #[serde(rename = "fraud_details", skip_serializing_if = "Option::is_none")]
    pub fraud_details: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// Details about whether or not the payment was accepted, and why.
    #[serde(rename = "outcome", skip_serializing_if = "Option::is_none")]
    pub outcome: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// True if the charge succeeded, or was successfully authorized for later capture, False otherwise.
    #[serde(rename = "paid", skip_serializing_if = "Option::is_none")]
    pub paid: Option<bool>,
    /// Details about the payment method at the time of the transaction.
    #[serde(rename = "payment_method_details", skip_serializing_if = "Option::is_none")]
    pub payment_method_details: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// The email address that the receipt for this charge was sent to.
    #[serde(rename = "receipt_email", skip_serializing_if = "Option::is_none")]
    pub receipt_email: Option<String>,
    /// The transaction number that appears on email receipts sent for this charge.
    #[serde(rename = "receipt_number", skip_serializing_if = "Option::is_none")]
    pub receipt_number: Option<String>,
    /// This is the URL to view the receipt for this charge. The receipt is kept up-to-date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt.
    #[serde(rename = "receipt_url", skip_serializing_if = "Option::is_none")]
    pub receipt_url: Option<String>,
    /// Whether or not the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.
    #[serde(rename = "refunded", skip_serializing_if = "Option::is_none")]
    pub refunded: Option<bool>,
    /// Shipping information for the charge
    #[serde(rename = "shipping", skip_serializing_if = "Option::is_none")]
    pub shipping: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// For card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers' statements. Must contain at least one letter, maximum 22 characters.
    #[serde(rename = "statement_descriptor", skip_serializing_if = "Option::is_none")]
    pub statement_descriptor: Option<String>,
    /// Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
    #[serde(rename = "statement_descriptor_suffix", skip_serializing_if = "Option::is_none")]
    pub statement_descriptor_suffix: Option<String>,
    /// The status of the payment.
    #[serde(rename = "status")]
    pub status: Option<Box<crate::models::StripeSourceCodeVerificationStatus>>,
    /// An optional dictionary including the account to automatically transfer to as part of a destination charge.
    #[serde(rename = "transfer_data", skip_serializing_if = "Option::is_none")]
    pub transfer_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
    /// A string that identifies this transaction as part of a group.
    #[serde(rename = "transfer_group", skip_serializing_if = "Option::is_none")]
    pub transfer_group: Option<String>,
    /// The Stripe Account this object belongs to.
    #[serde(rename = "djstripe_owner_account", skip_serializing_if = "Option::is_none")]
    pub djstripe_owner_account: Option<String>,
    /// The application fee (if any) for the charge.
    #[serde(rename = "application_fee", skip_serializing_if = "Option::is_none")]
    pub application_fee: Option<String>,
    /// The balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).
    #[serde(rename = "balance_transaction", skip_serializing_if = "Option::is_none")]
    pub balance_transaction: Option<String>,
    /// The customer associated with this charge.
    #[serde(rename = "customer", skip_serializing_if = "Option::is_none")]
    pub customer: Option<String>,
    /// Details about the dispute if the charge has been disputed.
    #[serde(rename = "dispute", skip_serializing_if = "Option::is_none")]
    pub dispute: Option<String>,
    /// The invoice this charge is for if one exists.
    #[serde(rename = "invoice", skip_serializing_if = "Option::is_none")]
    pub invoice: Option<String>,
    /// The account (if any) the charge was made on behalf of without triggering an automatic transfer.
    #[serde(rename = "on_behalf_of", skip_serializing_if = "Option::is_none")]
    pub on_behalf_of: Option<String>,
    /// PaymentIntent associated with this charge, if one exists.
    #[serde(rename = "payment_intent", skip_serializing_if = "Option::is_none")]
    pub payment_intent: Option<String>,
    /// PaymentMethod used in this charge.
    #[serde(rename = "payment_method", skip_serializing_if = "Option::is_none")]
    pub payment_method: Option<String>,
    /// The source used for this charge.
    #[serde(rename = "source", skip_serializing_if = "Option::is_none")]
    pub source: Option<String>,
    /// The transfer which created this charge. Only present if the charge came from another Stripe account.
    #[serde(rename = "source_transfer", skip_serializing_if = "Option::is_none")]
    pub source_transfer: Option<String>,
    /// The transfer to the `destination` account (only applicable if the charge was created using the `destination` parameter).
    #[serde(rename = "transfer", skip_serializing_if = "Option::is_none")]
    pub transfer: Option<String>,
}

impl DjStripeCharge {
    pub fn new(djstripe_id: i32, failure_code: crate::models::StripeApiErrorCode, djstripe_created: String, djstripe_updated: String, id: String, amount: String, amount_refunded: String, currency: String, status: Option<crate::models::StripeSourceCodeVerificationStatus>) -> DjStripeCharge {
        DjStripeCharge {
            djstripe_id,
            failure_code,
            djstripe_created,
            djstripe_updated,
            id,
            livemode: None,
            created: None,
            metadata: None,
            description: None,
            amount,
            amount_captured: None,
            amount_refunded,
            application: None,
            application_fee_amount: None,
            billing_details: None,
            calculated_statement_descriptor: None,
            captured: None,
            currency,
            disputed: None,
            failure_message: None,
            fraud_details: None,
            outcome: None,
            paid: None,
            payment_method_details: None,
            receipt_email: None,
            receipt_number: None,
            receipt_url: None,
            refunded: None,
            shipping: None,
            statement_descriptor: None,
            statement_descriptor_suffix: None,
            status: status.map(Box::new),
            transfer_data: None,
            transfer_group: None,
            djstripe_owner_account: None,
            application_fee: None,
            balance_transaction: None,
            customer: None,
            dispute: None,
            invoice: None,
            on_behalf_of: None,
            payment_intent: None,
            payment_method: None,
            source: None,
            source_transfer: None,
            transfer: None,
        }
    }
}


