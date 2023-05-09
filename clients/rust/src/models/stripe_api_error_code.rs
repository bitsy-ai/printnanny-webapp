/*
 * printnanny-api-client
 *
 * Official API client library for printnanny.ai
 *
 * The version of the OpenAPI document: 0.134.0
 * Contact: leigh@printnanny.ai
 * Generated by: https://openapi-generator.tech
 */

/// StripeApiErrorCode : * `account_already_exists` - Account already exists * `account_country_invalid_address` - Account country invalid address * `account_invalid` - Account invalid * `account_number_invalid` - Account number invalid * `alipay_upgrade_required` - Alipay upgrade required * `amount_too_large` - Amount too large * `amount_too_small` - Amount too small * `api_key_expired` - Api key expired * `balance_insufficient` - Balance insufficient * `bank_account_exists` - Bank account exists * `bank_account_unusable` - Bank account unusable * `bank_account_unverified` - Bank account unverified * `bitcoin_upgrade_required` - Bitcoin upgrade required * `card_declined` - Card was declined * `charge_already_captured` - Charge already captured * `charge_already_refunded` - Charge already refunded * `charge_disputed` - Charge disputed * `charge_exceeds_source_limit` - Charge exceeds source limit * `charge_expired_for_capture` - Charge expired for capture * `country_unsupported` - Country unsupported * `coupon_expired` - Coupon expired * `customer_max_subscriptions` - Customer max subscriptions * `email_invalid` - Email invalid * `expired_card` - Expired card * `idempotency_key_in_use` - Idempotency key in use * `incorrect_address` - Incorrect address * `incorrect_cvc` - Incorrect security code * `incorrect_number` - Incorrect number * `incorrect_zip` - ZIP code failed validation * `instant_payouts_unsupported` - Instant payouts unsupported * `invalid_card_type` - Invalid card type * `invalid_charge_amount` - Invalid charge amount * `invalid_cvc` - Invalid security code * `invalid_expiry_month` - Invalid expiration month * `invalid_expiry_year` - Invalid expiration year * `invalid_number` - Invalid number * `invalid_source_usage` - Invalid source usage * `invalid_swipe_data` - Invalid swipe data * `invoice_no_customer_line_items` - Invoice no customer line items * `invoice_no_subscription_line_items` - Invoice no subscription line items * `invoice_not_editable` - Invoice not editable * `invoice_upcoming_none` - Invoice upcoming none * `livemode_mismatch` - Livemode mismatch * `missing` - No card being charged * `not_allowed_on_standard_account` - Not allowed on standard account * `order_creation_failed` - Order creation failed * `order_required_settings` - Order required settings * `order_status_invalid` - Order status invalid * `order_upstream_timeout` - Order upstream timeout * `out_of_inventory` - Out of inventory * `parameter_invalid_empty` - Parameter invalid empty * `parameter_invalid_integer` - Parameter invalid integer * `parameter_invalid_string_blank` - Parameter invalid string blank * `parameter_invalid_string_empty` - Parameter invalid string empty * `parameter_missing` - Parameter missing * `parameter_unknown` - Parameter unknown * `parameters_exclusive` - Parameters exclusive * `payment_intent_authentication_failure` - Payment intent authentication failure * `payment_intent_incompatible_payment_method` - Payment intent incompatible payment method * `payment_intent_invalid_parameter` - Payment intent invalid parameter * `payment_intent_payment_attempt_failed` - Payment intent payment attempt failed * `payment_intent_unexpected_state` - Payment intent unexpected state * `payment_method_unactivated` - Payment method unactivated * `payment_method_unexpected_state` - Payment method unexpected state * `payouts_not_allowed` - Payouts not allowed * `platform_api_key_expired` - Platform api key expired * `postal_code_invalid` - Postal code invalid * `processing_error` - Processing error * `product_inactive` - Product inactive * `rate_limit` - Rate limit * `resource_already_exists` - Resource already exists * `resource_missing` - Resource missing * `routing_number_invalid` - Routing number invalid * `secret_key_required` - Secret key required * `sepa_unsupported_account` - SEPA unsupported account * `shipping_calculation_failed` - Shipping calculation failed * `sku_inactive` - SKU inactive * `state_unsupported` - State unsupported * `tax_id_invalid` - Tax id invalid * `taxes_calculation_failed` - Taxes calculation failed * `testmode_charges_only` - Testmode charges only * `tls_version_unsupported` - TLS version unsupported * `token_already_used` - Token already used * `token_in_use` - Token in use * `transfers_not_allowed` - Transfers not allowed * `upstream_order_creation_failed` - Upstream order creation failed * `url_invalid` - URL invalid

/// * `account_already_exists` - Account already exists * `account_country_invalid_address` - Account country invalid address * `account_invalid` - Account invalid * `account_number_invalid` - Account number invalid * `alipay_upgrade_required` - Alipay upgrade required * `amount_too_large` - Amount too large * `amount_too_small` - Amount too small * `api_key_expired` - Api key expired * `balance_insufficient` - Balance insufficient * `bank_account_exists` - Bank account exists * `bank_account_unusable` - Bank account unusable * `bank_account_unverified` - Bank account unverified * `bitcoin_upgrade_required` - Bitcoin upgrade required * `card_declined` - Card was declined * `charge_already_captured` - Charge already captured * `charge_already_refunded` - Charge already refunded * `charge_disputed` - Charge disputed * `charge_exceeds_source_limit` - Charge exceeds source limit * `charge_expired_for_capture` - Charge expired for capture * `country_unsupported` - Country unsupported * `coupon_expired` - Coupon expired * `customer_max_subscriptions` - Customer max subscriptions * `email_invalid` - Email invalid * `expired_card` - Expired card * `idempotency_key_in_use` - Idempotency key in use * `incorrect_address` - Incorrect address * `incorrect_cvc` - Incorrect security code * `incorrect_number` - Incorrect number * `incorrect_zip` - ZIP code failed validation * `instant_payouts_unsupported` - Instant payouts unsupported * `invalid_card_type` - Invalid card type * `invalid_charge_amount` - Invalid charge amount * `invalid_cvc` - Invalid security code * `invalid_expiry_month` - Invalid expiration month * `invalid_expiry_year` - Invalid expiration year * `invalid_number` - Invalid number * `invalid_source_usage` - Invalid source usage * `invalid_swipe_data` - Invalid swipe data * `invoice_no_customer_line_items` - Invoice no customer line items * `invoice_no_subscription_line_items` - Invoice no subscription line items * `invoice_not_editable` - Invoice not editable * `invoice_upcoming_none` - Invoice upcoming none * `livemode_mismatch` - Livemode mismatch * `missing` - No card being charged * `not_allowed_on_standard_account` - Not allowed on standard account * `order_creation_failed` - Order creation failed * `order_required_settings` - Order required settings * `order_status_invalid` - Order status invalid * `order_upstream_timeout` - Order upstream timeout * `out_of_inventory` - Out of inventory * `parameter_invalid_empty` - Parameter invalid empty * `parameter_invalid_integer` - Parameter invalid integer * `parameter_invalid_string_blank` - Parameter invalid string blank * `parameter_invalid_string_empty` - Parameter invalid string empty * `parameter_missing` - Parameter missing * `parameter_unknown` - Parameter unknown * `parameters_exclusive` - Parameters exclusive * `payment_intent_authentication_failure` - Payment intent authentication failure * `payment_intent_incompatible_payment_method` - Payment intent incompatible payment method * `payment_intent_invalid_parameter` - Payment intent invalid parameter * `payment_intent_payment_attempt_failed` - Payment intent payment attempt failed * `payment_intent_unexpected_state` - Payment intent unexpected state * `payment_method_unactivated` - Payment method unactivated * `payment_method_unexpected_state` - Payment method unexpected state * `payouts_not_allowed` - Payouts not allowed * `platform_api_key_expired` - Platform api key expired * `postal_code_invalid` - Postal code invalid * `processing_error` - Processing error * `product_inactive` - Product inactive * `rate_limit` - Rate limit * `resource_already_exists` - Resource already exists * `resource_missing` - Resource missing * `routing_number_invalid` - Routing number invalid * `secret_key_required` - Secret key required * `sepa_unsupported_account` - SEPA unsupported account * `shipping_calculation_failed` - Shipping calculation failed * `sku_inactive` - SKU inactive * `state_unsupported` - State unsupported * `tax_id_invalid` - Tax id invalid * `taxes_calculation_failed` - Taxes calculation failed * `testmode_charges_only` - Testmode charges only * `tls_version_unsupported` - TLS version unsupported * `token_already_used` - Token already used * `token_in_use` - Token in use * `transfers_not_allowed` - Transfers not allowed * `upstream_order_creation_failed` - Upstream order creation failed * `url_invalid` - URL invalid
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




