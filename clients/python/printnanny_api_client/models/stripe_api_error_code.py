# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.123.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class StripeApiErrorCode(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ACCOUNT_ALREADY_EXISTS = "account_already_exists"
    ACCOUNT_COUNTRY_INVALID_ADDRESS = "account_country_invalid_address"
    ACCOUNT_INVALID = "account_invalid"
    ACCOUNT_NUMBER_INVALID = "account_number_invalid"
    ALIPAY_UPGRADE_REQUIRED = "alipay_upgrade_required"
    AMOUNT_TOO_LARGE = "amount_too_large"
    AMOUNT_TOO_SMALL = "amount_too_small"
    API_KEY_EXPIRED = "api_key_expired"
    BALANCE_INSUFFICIENT = "balance_insufficient"
    BANK_ACCOUNT_EXISTS = "bank_account_exists"
    BANK_ACCOUNT_UNUSABLE = "bank_account_unusable"
    BANK_ACCOUNT_UNVERIFIED = "bank_account_unverified"
    BITCOIN_UPGRADE_REQUIRED = "bitcoin_upgrade_required"
    CARD_DECLINED = "card_declined"
    CHARGE_ALREADY_CAPTURED = "charge_already_captured"
    CHARGE_ALREADY_REFUNDED = "charge_already_refunded"
    CHARGE_DISPUTED = "charge_disputed"
    CHARGE_EXCEEDS_SOURCE_LIMIT = "charge_exceeds_source_limit"
    CHARGE_EXPIRED_FOR_CAPTURE = "charge_expired_for_capture"
    COUNTRY_UNSUPPORTED = "country_unsupported"
    COUPON_EXPIRED = "coupon_expired"
    CUSTOMER_MAX_SUBSCRIPTIONS = "customer_max_subscriptions"
    EMAIL_INVALID = "email_invalid"
    EXPIRED_CARD = "expired_card"
    IDEMPOTENCY_KEY_IN_USE = "idempotency_key_in_use"
    INCORRECT_ADDRESS = "incorrect_address"
    INCORRECT_CVC = "incorrect_cvc"
    INCORRECT_NUMBER = "incorrect_number"
    INCORRECT_ZIP = "incorrect_zip"
    INSTANT_PAYOUTS_UNSUPPORTED = "instant_payouts_unsupported"
    INVALID_CARD_TYPE = "invalid_card_type"
    INVALID_CHARGE_AMOUNT = "invalid_charge_amount"
    INVALID_CVC = "invalid_cvc"
    INVALID_EXPIRY_MONTH = "invalid_expiry_month"
    INVALID_EXPIRY_YEAR = "invalid_expiry_year"
    INVALID_NUMBER = "invalid_number"
    INVALID_SOURCE_USAGE = "invalid_source_usage"
    INVALID_SWIPE_DATA = "invalid_swipe_data"
    INVOICE_NO_CUSTOMER_LINE_ITEMS = "invoice_no_customer_line_items"
    INVOICE_NO_SUBSCRIPTION_LINE_ITEMS = "invoice_no_subscription_line_items"
    INVOICE_NOT_EDITABLE = "invoice_not_editable"
    INVOICE_UPCOMING_NONE = "invoice_upcoming_none"
    LIVEMODE_MISMATCH = "livemode_mismatch"
    MISSING = "missing"
    NOT_ALLOWED_ON_STANDARD_ACCOUNT = "not_allowed_on_standard_account"
    ORDER_CREATION_FAILED = "order_creation_failed"
    ORDER_REQUIRED_SETTINGS = "order_required_settings"
    ORDER_STATUS_INVALID = "order_status_invalid"
    ORDER_UPSTREAM_TIMEOUT = "order_upstream_timeout"
    OUT_OF_INVENTORY = "out_of_inventory"
    PARAMETER_INVALID_EMPTY = "parameter_invalid_empty"
    PARAMETER_INVALID_INTEGER = "parameter_invalid_integer"
    PARAMETER_INVALID_STRING_BLANK = "parameter_invalid_string_blank"
    PARAMETER_INVALID_STRING_EMPTY = "parameter_invalid_string_empty"
    PARAMETER_MISSING = "parameter_missing"
    PARAMETER_UNKNOWN = "parameter_unknown"
    PARAMETERS_EXCLUSIVE = "parameters_exclusive"
    PAYMENT_INTENT_AUTHENTICATION_FAILURE = "payment_intent_authentication_failure"
    PAYMENT_INTENT_INCOMPATIBLE_PAYMENT_METHOD = "payment_intent_incompatible_payment_method"
    PAYMENT_INTENT_INVALID_PARAMETER = "payment_intent_invalid_parameter"
    PAYMENT_INTENT_PAYMENT_ATTEMPT_FAILED = "payment_intent_payment_attempt_failed"
    PAYMENT_INTENT_UNEXPECTED_STATE = "payment_intent_unexpected_state"
    PAYMENT_METHOD_UNACTIVATED = "payment_method_unactivated"
    PAYMENT_METHOD_UNEXPECTED_STATE = "payment_method_unexpected_state"
    PAYOUTS_NOT_ALLOWED = "payouts_not_allowed"
    PLATFORM_API_KEY_EXPIRED = "platform_api_key_expired"
    POSTAL_CODE_INVALID = "postal_code_invalid"
    PROCESSING_ERROR = "processing_error"
    PRODUCT_INACTIVE = "product_inactive"
    RATE_LIMIT = "rate_limit"
    RESOURCE_ALREADY_EXISTS = "resource_already_exists"
    RESOURCE_MISSING = "resource_missing"
    ROUTING_NUMBER_INVALID = "routing_number_invalid"
    SECRET_KEY_REQUIRED = "secret_key_required"
    SEPA_UNSUPPORTED_ACCOUNT = "sepa_unsupported_account"
    SHIPPING_CALCULATION_FAILED = "shipping_calculation_failed"
    SKU_INACTIVE = "sku_inactive"
    STATE_UNSUPPORTED = "state_unsupported"
    TAX_ID_INVALID = "tax_id_invalid"
    TAXES_CALCULATION_FAILED = "taxes_calculation_failed"
    TESTMODE_CHARGES_ONLY = "testmode_charges_only"
    TLS_VERSION_UNSUPPORTED = "tls_version_unsupported"
    TOKEN_ALREADY_USED = "token_already_used"
    TOKEN_IN_USE = "token_in_use"
    TRANSFERS_NOT_ALLOWED = "transfers_not_allowed"
    UPSTREAM_ORDER_CREATION_FAILED = "upstream_order_creation_failed"
    URL_INVALID = "url_invalid"

    allowable_values = [ACCOUNT_ALREADY_EXISTS, ACCOUNT_COUNTRY_INVALID_ADDRESS, ACCOUNT_INVALID, ACCOUNT_NUMBER_INVALID, ALIPAY_UPGRADE_REQUIRED, AMOUNT_TOO_LARGE, AMOUNT_TOO_SMALL, API_KEY_EXPIRED, BALANCE_INSUFFICIENT, BANK_ACCOUNT_EXISTS, BANK_ACCOUNT_UNUSABLE, BANK_ACCOUNT_UNVERIFIED, BITCOIN_UPGRADE_REQUIRED, CARD_DECLINED, CHARGE_ALREADY_CAPTURED, CHARGE_ALREADY_REFUNDED, CHARGE_DISPUTED, CHARGE_EXCEEDS_SOURCE_LIMIT, CHARGE_EXPIRED_FOR_CAPTURE, COUNTRY_UNSUPPORTED, COUPON_EXPIRED, CUSTOMER_MAX_SUBSCRIPTIONS, EMAIL_INVALID, EXPIRED_CARD, IDEMPOTENCY_KEY_IN_USE, INCORRECT_ADDRESS, INCORRECT_CVC, INCORRECT_NUMBER, INCORRECT_ZIP, INSTANT_PAYOUTS_UNSUPPORTED, INVALID_CARD_TYPE, INVALID_CHARGE_AMOUNT, INVALID_CVC, INVALID_EXPIRY_MONTH, INVALID_EXPIRY_YEAR, INVALID_NUMBER, INVALID_SOURCE_USAGE, INVALID_SWIPE_DATA, INVOICE_NO_CUSTOMER_LINE_ITEMS, INVOICE_NO_SUBSCRIPTION_LINE_ITEMS, INVOICE_NOT_EDITABLE, INVOICE_UPCOMING_NONE, LIVEMODE_MISMATCH, MISSING, NOT_ALLOWED_ON_STANDARD_ACCOUNT, ORDER_CREATION_FAILED, ORDER_REQUIRED_SETTINGS, ORDER_STATUS_INVALID, ORDER_UPSTREAM_TIMEOUT, OUT_OF_INVENTORY, PARAMETER_INVALID_EMPTY, PARAMETER_INVALID_INTEGER, PARAMETER_INVALID_STRING_BLANK, PARAMETER_INVALID_STRING_EMPTY, PARAMETER_MISSING, PARAMETER_UNKNOWN, PARAMETERS_EXCLUSIVE, PAYMENT_INTENT_AUTHENTICATION_FAILURE, PAYMENT_INTENT_INCOMPATIBLE_PAYMENT_METHOD, PAYMENT_INTENT_INVALID_PARAMETER, PAYMENT_INTENT_PAYMENT_ATTEMPT_FAILED, PAYMENT_INTENT_UNEXPECTED_STATE, PAYMENT_METHOD_UNACTIVATED, PAYMENT_METHOD_UNEXPECTED_STATE, PAYOUTS_NOT_ALLOWED, PLATFORM_API_KEY_EXPIRED, POSTAL_CODE_INVALID, PROCESSING_ERROR, PRODUCT_INACTIVE, RATE_LIMIT, RESOURCE_ALREADY_EXISTS, RESOURCE_MISSING, ROUTING_NUMBER_INVALID, SECRET_KEY_REQUIRED, SEPA_UNSUPPORTED_ACCOUNT, SHIPPING_CALCULATION_FAILED, SKU_INACTIVE, STATE_UNSUPPORTED, TAX_ID_INVALID, TAXES_CALCULATION_FAILED, TESTMODE_CHARGES_ONLY, TLS_VERSION_UNSUPPORTED, TOKEN_ALREADY_USED, TOKEN_IN_USE, TRANSFERS_NOT_ALLOWED, UPSTREAM_ORDER_CREATION_FAILED, URL_INVALID]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """StripeApiErrorCode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StripeApiErrorCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StripeApiErrorCode):
            return True

        return self.to_dict() != other.to_dict()
