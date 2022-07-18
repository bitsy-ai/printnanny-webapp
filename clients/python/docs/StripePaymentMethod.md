# StripePaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **int** |  | [readonly] 
**djstripe_created** | **datetime** |  | [readonly] 
**djstripe_updated** | **datetime** |  | [readonly] 
**id** | **str** |  | 
**livemode** | **bool** | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional] 
**created** | **datetime** | The datetime this object was created in stripe. | [optional] 
**metadata** | **dict(str, object)** | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional] 
**billing_details** | **dict(str, object)** | Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods. | 
**type** | [**TypeEnum**](TypeEnum.md) | The type of the PaymentMethod. | 
**acss_debit** | **dict(str, object)** | Additional information for payment methods of type &#x60;acss_debit&#x60; | [optional] 
**afterpay_clearpay** | **dict(str, object)** | Additional information for payment methods of type &#x60;afterpay_clearpay&#x60; | [optional] 
**alipay** | **dict(str, object)** | Additional information for payment methods of type &#x60;alipay&#x60; | [optional] 
**au_becs_debit** | **dict(str, object)** | Additional information for payment methods of type &#x60;au_becs_debit&#x60; | [optional] 
**bacs_debit** | **dict(str, object)** | Additional information for payment methods of type &#x60;bacs_debit&#x60; | [optional] 
**bancontact** | **dict(str, object)** | Additional information for payment methods of type &#x60;bancontact&#x60; | [optional] 
**boleto** | **dict(str, object)** | Additional information for payment methods of type &#x60;boleto&#x60; | [optional] 
**card** | **dict(str, object)** | Additional information for payment methods of type &#x60;card&#x60; | [optional] 
**card_present** | **dict(str, object)** | Additional information for payment methods of type &#x60;card_present&#x60; | [optional] 
**eps** | **dict(str, object)** | Additional information for payment methods of type &#x60;eps&#x60; | [optional] 
**fpx** | **dict(str, object)** | Additional information for payment methods of type &#x60;fpx&#x60; | [optional] 
**giropay** | **dict(str, object)** | Additional information for payment methods of type &#x60;giropay&#x60; | [optional] 
**grabpay** | **dict(str, object)** | Additional information for payment methods of type &#x60;grabpay&#x60; | [optional] 
**ideal** | **dict(str, object)** | Additional information for payment methods of type &#x60;ideal&#x60; | [optional] 
**interac_present** | **dict(str, object)** | Additional information for payment methods of type &#x60;interac_present&#x60; | [optional] 
**oxxo** | **dict(str, object)** | Additional information for payment methods of type &#x60;oxxo&#x60; | [optional] 
**p24** | **dict(str, object)** | Additional information for payment methods of type &#x60;p24&#x60; | [optional] 
**sepa_debit** | **dict(str, object)** | Additional information for payment methods of type &#x60;sepa_debit&#x60; | [optional] 
**sofort** | **dict(str, object)** | Additional information for payment methods of type &#x60;sofort&#x60; | [optional] 
**wechat_pay** | **dict(str, object)** | Additional information for payment methods of type &#x60;wechat_pay&#x60; | [optional] 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 
**customer** | **str** | Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


