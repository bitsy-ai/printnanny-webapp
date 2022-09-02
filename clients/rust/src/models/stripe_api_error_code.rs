/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.106.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, clap::ValueEnum, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum StripeApiErrorCode {
    #[serde(rename = "account_already_exists")]
    AccountAlreadyExists,
    #[serde(rename = "account_country_invalid_address")]
    AccountCountryInvalidAddress,
    #[serde(rename = "account_invalid")]
    AccountInvalid,
    #[serde(rename = "account_number_invalid")]
    AccountNumberInvalid,
    #[serde(rename = "alipay_upgrade_required")]
    AlipayUpgradeRequired,
    #[serde(rename = "amount_too_large")]
    AmountTooLarge,
    #[serde(rename = "amount_too_small")]
    AmountTooSmall,
    #[serde(rename = "api_key_expired")]
    ApiKeyExpired,
    #[serde(rename = "balance_insufficient")]
    BalanceInsufficient,
    #[serde(rename = "bank_account_exists")]
    BankAccountExists,
    #[serde(rename = "bank_account_unusable")]
    BankAccountUnusable,
    #[serde(rename = "bank_account_unverified")]
    BankAccountUnverified,
    #[serde(rename = "bitcoin_upgrade_required")]
    BitcoinUpgradeRequired,
    #[serde(rename = "card_declined")]
    CardDeclined,
    #[serde(rename = "charge_already_captured")]
    ChargeAlreadyCaptured,
    #[serde(rename = "charge_already_refunded")]
    ChargeAlreadyRefunded,
    #[serde(rename = "charge_disputed")]
    ChargeDisputed,
    #[serde(rename = "charge_exceeds_source_limit")]
    ChargeExceedsSourceLimit,
    #[serde(rename = "charge_expired_for_capture")]
    ChargeExpiredForCapture,
    #[serde(rename = "country_unsupported")]
    CountryUnsupported,
    #[serde(rename = "coupon_expired")]
    CouponExpired,
    #[serde(rename = "customer_max_subscriptions")]
    CustomerMaxSubscriptions,
    #[serde(rename = "email_invalid")]
    EmailInvalid,
    #[serde(rename = "expired_card")]
    ExpiredCard,
    #[serde(rename = "idempotency_key_in_use")]
    IdempotencyKeyInUse,
    #[serde(rename = "incorrect_address")]
    IncorrectAddress,
    #[serde(rename = "incorrect_cvc")]
    IncorrectCvc,
    #[serde(rename = "incorrect_number")]
    IncorrectNumber,
    #[serde(rename = "incorrect_zip")]
    IncorrectZip,
    #[serde(rename = "instant_payouts_unsupported")]
    InstantPayoutsUnsupported,
    #[serde(rename = "invalid_card_type")]
    InvalidCardType,
    #[serde(rename = "invalid_charge_amount")]
    InvalidChargeAmount,
    #[serde(rename = "invalid_cvc")]
    InvalidCvc,
    #[serde(rename = "invalid_expiry_month")]
    InvalidExpiryMonth,
    #[serde(rename = "invalid_expiry_year")]
    InvalidExpiryYear,
    #[serde(rename = "invalid_number")]
    InvalidNumber,
    #[serde(rename = "invalid_source_usage")]
    InvalidSourceUsage,
    #[serde(rename = "invalid_swipe_data")]
    InvalidSwipeData,
    #[serde(rename = "invoice_no_customer_line_items")]
    InvoiceNoCustomerLineItems,
    #[serde(rename = "invoice_no_subscription_line_items")]
    InvoiceNoSubscriptionLineItems,
    #[serde(rename = "invoice_not_editable")]
    InvoiceNotEditable,
    #[serde(rename = "invoice_upcoming_none")]
    InvoiceUpcomingNone,
    #[serde(rename = "livemode_mismatch")]
    LivemodeMismatch,
    #[serde(rename = "missing")]
    Missing,
    #[serde(rename = "not_allowed_on_standard_account")]
    NotAllowedOnStandardAccount,
    #[serde(rename = "order_creation_failed")]
    OrderCreationFailed,
    #[serde(rename = "order_required_settings")]
    OrderRequiredSettings,
    #[serde(rename = "order_status_invalid")]
    OrderStatusInvalid,
    #[serde(rename = "order_upstream_timeout")]
    OrderUpstreamTimeout,
    #[serde(rename = "out_of_inventory")]
    OutOfInventory,
    #[serde(rename = "parameter_invalid_empty")]
    ParameterInvalidEmpty,
    #[serde(rename = "parameter_invalid_integer")]
    ParameterInvalidInteger,
    #[serde(rename = "parameter_invalid_string_blank")]
    ParameterInvalidStringBlank,
    #[serde(rename = "parameter_invalid_string_empty")]
    ParameterInvalidStringEmpty,
    #[serde(rename = "parameter_missing")]
    ParameterMissing,
    #[serde(rename = "parameter_unknown")]
    ParameterUnknown,
    #[serde(rename = "parameters_exclusive")]
    ParametersExclusive,
    #[serde(rename = "payment_intent_authentication_failure")]
    PaymentIntentAuthenticationFailure,
    #[serde(rename = "payment_intent_incompatible_payment_method")]
    PaymentIntentIncompatiblePaymentMethod,
    #[serde(rename = "payment_intent_invalid_parameter")]
    PaymentIntentInvalidParameter,
    #[serde(rename = "payment_intent_payment_attempt_failed")]
    PaymentIntentPaymentAttemptFailed,
    #[serde(rename = "payment_intent_unexpected_state")]
    PaymentIntentUnexpectedState,
    #[serde(rename = "payment_method_unactivated")]
    PaymentMethodUnactivated,
    #[serde(rename = "payment_method_unexpected_state")]
    PaymentMethodUnexpectedState,
    #[serde(rename = "payouts_not_allowed")]
    PayoutsNotAllowed,
    #[serde(rename = "platform_api_key_expired")]
    PlatformApiKeyExpired,
    #[serde(rename = "postal_code_invalid")]
    PostalCodeInvalid,
    #[serde(rename = "processing_error")]
    ProcessingError,
    #[serde(rename = "product_inactive")]
    ProductInactive,
    #[serde(rename = "rate_limit")]
    RateLimit,
    #[serde(rename = "resource_already_exists")]
    ResourceAlreadyExists,
    #[serde(rename = "resource_missing")]
    ResourceMissing,
    #[serde(rename = "routing_number_invalid")]
    RoutingNumberInvalid,
    #[serde(rename = "secret_key_required")]
    SecretKeyRequired,
    #[serde(rename = "sepa_unsupported_account")]
    SepaUnsupportedAccount,
    #[serde(rename = "shipping_calculation_failed")]
    ShippingCalculationFailed,
    #[serde(rename = "sku_inactive")]
    SkuInactive,
    #[serde(rename = "state_unsupported")]
    StateUnsupported,
    #[serde(rename = "tax_id_invalid")]
    TaxIdInvalid,
    #[serde(rename = "taxes_calculation_failed")]
    TaxesCalculationFailed,
    #[serde(rename = "testmode_charges_only")]
    TestmodeChargesOnly,
    #[serde(rename = "tls_version_unsupported")]
    TlsVersionUnsupported,
    #[serde(rename = "token_already_used")]
    TokenAlreadyUsed,
    #[serde(rename = "token_in_use")]
    TokenInUse,
    #[serde(rename = "transfers_not_allowed")]
    TransfersNotAllowed,
    #[serde(rename = "upstream_order_creation_failed")]
    UpstreamOrderCreationFailed,
    #[serde(rename = "url_invalid")]
    UrlInvalid,

}

impl ToString for StripeApiErrorCode {
    fn to_string(&self) -> String {
        match self {
            Self::AccountAlreadyExists => String::from("account_already_exists"),
            Self::AccountCountryInvalidAddress => String::from("account_country_invalid_address"),
            Self::AccountInvalid => String::from("account_invalid"),
            Self::AccountNumberInvalid => String::from("account_number_invalid"),
            Self::AlipayUpgradeRequired => String::from("alipay_upgrade_required"),
            Self::AmountTooLarge => String::from("amount_too_large"),
            Self::AmountTooSmall => String::from("amount_too_small"),
            Self::ApiKeyExpired => String::from("api_key_expired"),
            Self::BalanceInsufficient => String::from("balance_insufficient"),
            Self::BankAccountExists => String::from("bank_account_exists"),
            Self::BankAccountUnusable => String::from("bank_account_unusable"),
            Self::BankAccountUnverified => String::from("bank_account_unverified"),
            Self::BitcoinUpgradeRequired => String::from("bitcoin_upgrade_required"),
            Self::CardDeclined => String::from("card_declined"),
            Self::ChargeAlreadyCaptured => String::from("charge_already_captured"),
            Self::ChargeAlreadyRefunded => String::from("charge_already_refunded"),
            Self::ChargeDisputed => String::from("charge_disputed"),
            Self::ChargeExceedsSourceLimit => String::from("charge_exceeds_source_limit"),
            Self::ChargeExpiredForCapture => String::from("charge_expired_for_capture"),
            Self::CountryUnsupported => String::from("country_unsupported"),
            Self::CouponExpired => String::from("coupon_expired"),
            Self::CustomerMaxSubscriptions => String::from("customer_max_subscriptions"),
            Self::EmailInvalid => String::from("email_invalid"),
            Self::ExpiredCard => String::from("expired_card"),
            Self::IdempotencyKeyInUse => String::from("idempotency_key_in_use"),
            Self::IncorrectAddress => String::from("incorrect_address"),
            Self::IncorrectCvc => String::from("incorrect_cvc"),
            Self::IncorrectNumber => String::from("incorrect_number"),
            Self::IncorrectZip => String::from("incorrect_zip"),
            Self::InstantPayoutsUnsupported => String::from("instant_payouts_unsupported"),
            Self::InvalidCardType => String::from("invalid_card_type"),
            Self::InvalidChargeAmount => String::from("invalid_charge_amount"),
            Self::InvalidCvc => String::from("invalid_cvc"),
            Self::InvalidExpiryMonth => String::from("invalid_expiry_month"),
            Self::InvalidExpiryYear => String::from("invalid_expiry_year"),
            Self::InvalidNumber => String::from("invalid_number"),
            Self::InvalidSourceUsage => String::from("invalid_source_usage"),
            Self::InvalidSwipeData => String::from("invalid_swipe_data"),
            Self::InvoiceNoCustomerLineItems => String::from("invoice_no_customer_line_items"),
            Self::InvoiceNoSubscriptionLineItems => String::from("invoice_no_subscription_line_items"),
            Self::InvoiceNotEditable => String::from("invoice_not_editable"),
            Self::InvoiceUpcomingNone => String::from("invoice_upcoming_none"),
            Self::LivemodeMismatch => String::from("livemode_mismatch"),
            Self::Missing => String::from("missing"),
            Self::NotAllowedOnStandardAccount => String::from("not_allowed_on_standard_account"),
            Self::OrderCreationFailed => String::from("order_creation_failed"),
            Self::OrderRequiredSettings => String::from("order_required_settings"),
            Self::OrderStatusInvalid => String::from("order_status_invalid"),
            Self::OrderUpstreamTimeout => String::from("order_upstream_timeout"),
            Self::OutOfInventory => String::from("out_of_inventory"),
            Self::ParameterInvalidEmpty => String::from("parameter_invalid_empty"),
            Self::ParameterInvalidInteger => String::from("parameter_invalid_integer"),
            Self::ParameterInvalidStringBlank => String::from("parameter_invalid_string_blank"),
            Self::ParameterInvalidStringEmpty => String::from("parameter_invalid_string_empty"),
            Self::ParameterMissing => String::from("parameter_missing"),
            Self::ParameterUnknown => String::from("parameter_unknown"),
            Self::ParametersExclusive => String::from("parameters_exclusive"),
            Self::PaymentIntentAuthenticationFailure => String::from("payment_intent_authentication_failure"),
            Self::PaymentIntentIncompatiblePaymentMethod => String::from("payment_intent_incompatible_payment_method"),
            Self::PaymentIntentInvalidParameter => String::from("payment_intent_invalid_parameter"),
            Self::PaymentIntentPaymentAttemptFailed => String::from("payment_intent_payment_attempt_failed"),
            Self::PaymentIntentUnexpectedState => String::from("payment_intent_unexpected_state"),
            Self::PaymentMethodUnactivated => String::from("payment_method_unactivated"),
            Self::PaymentMethodUnexpectedState => String::from("payment_method_unexpected_state"),
            Self::PayoutsNotAllowed => String::from("payouts_not_allowed"),
            Self::PlatformApiKeyExpired => String::from("platform_api_key_expired"),
            Self::PostalCodeInvalid => String::from("postal_code_invalid"),
            Self::ProcessingError => String::from("processing_error"),
            Self::ProductInactive => String::from("product_inactive"),
            Self::RateLimit => String::from("rate_limit"),
            Self::ResourceAlreadyExists => String::from("resource_already_exists"),
            Self::ResourceMissing => String::from("resource_missing"),
            Self::RoutingNumberInvalid => String::from("routing_number_invalid"),
            Self::SecretKeyRequired => String::from("secret_key_required"),
            Self::SepaUnsupportedAccount => String::from("sepa_unsupported_account"),
            Self::ShippingCalculationFailed => String::from("shipping_calculation_failed"),
            Self::SkuInactive => String::from("sku_inactive"),
            Self::StateUnsupported => String::from("state_unsupported"),
            Self::TaxIdInvalid => String::from("tax_id_invalid"),
            Self::TaxesCalculationFailed => String::from("taxes_calculation_failed"),
            Self::TestmodeChargesOnly => String::from("testmode_charges_only"),
            Self::TlsVersionUnsupported => String::from("tls_version_unsupported"),
            Self::TokenAlreadyUsed => String::from("token_already_used"),
            Self::TokenInUse => String::from("token_in_use"),
            Self::TransfersNotAllowed => String::from("transfers_not_allowed"),
            Self::UpstreamOrderCreationFailed => String::from("upstream_order_creation_failed"),
            Self::UrlInvalid => String::from("url_invalid"),
        }
    }
}

impl Default for StripeApiErrorCode {
    fn default() -> StripeApiErrorCode {
        Self::AccountAlreadyExists
    }
}




