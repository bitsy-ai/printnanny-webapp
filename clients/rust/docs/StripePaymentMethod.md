# StripePaymentMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **i32** |  | [readonly]
**djstripe_created** | **String** |  | [readonly]
**djstripe_updated** | **String** |  | [readonly]
**id** | **String** |  | 
**livemode** | Option<**bool**> | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional]
**created** | Option<**String**> | The datetime this object was created in stripe. | [optional]
**metadata** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional]
**billing_details** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) | Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods. | 
**_type** | Option<[**crate::models::StripePaymentMethodTypeEnum**](StripePaymentMethodTypeEnum.md)> | The type of the PaymentMethod. | 
**acss_debit** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `acss_debit` | [optional]
**afterpay_clearpay** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `afterpay_clearpay` | [optional]
**alipay** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `alipay` | [optional]
**au_becs_debit** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `au_becs_debit` | [optional]
**bacs_debit** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `bacs_debit` | [optional]
**bancontact** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `bancontact` | [optional]
**boleto** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `boleto` | [optional]
**card** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `card` | [optional]
**card_present** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `card_present` | [optional]
**eps** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `eps` | [optional]
**fpx** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `fpx` | [optional]
**giropay** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `giropay` | [optional]
**grabpay** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `grabpay` | [optional]
**ideal** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `ideal` | [optional]
**interac_present** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `interac_present` | [optional]
**oxxo** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `oxxo` | [optional]
**p24** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `p24` | [optional]
**sepa_debit** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `sepa_debit` | [optional]
**sofort** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `sofort` | [optional]
**wechat_pay** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Additional information for payment methods of type `wechat_pay` | [optional]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]
**customer** | Option<**String**> | Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


