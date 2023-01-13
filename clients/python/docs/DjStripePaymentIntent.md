# DjStripePaymentIntent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **int** |  | [readonly] 
**cancellation_reason** | [**StripePaymentIntentCancellationReason**](StripePaymentIntentCancellationReason.md) |  | 
**charges** | [**list[DjStripeCharge]**](DjStripeCharge.md) |  | [readonly] 
**setup_future_usage** | [**StripeIntentUsage**](StripeIntentUsage.md) |  | 
**djstripe_created** | **datetime** |  | [readonly] 
**djstripe_updated** | **datetime** |  | [readonly] 
**id** | **str** |  | 
**livemode** | **bool** | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional] 
**created** | **datetime** | The datetime this object was created in stripe. | [optional] 
**metadata** | **dict(str, object)** | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional] 
**amount** | **int** | Amount (in cents) intended to be collected by this PaymentIntent. | 
**amount_capturable** | **int** | Amount (in cents) that can be captured from this PaymentIntent. | 
**amount_received** | **int** | Amount (in cents) that was collected by this PaymentIntent. | 
**canceled_at** | **datetime** | Populated when status is canceled, this is the time at which the PaymentIntent was canceled. Measured in seconds since the Unix epoch. | [optional] 
**capture_method** | [**StripeConfirmationMethod**](StripeConfirmationMethod.md) | Capture method of this PaymentIntent, one of automatic or manual. | 
**client_secret** | **str** | The client secret of this PaymentIntent. Used for client-side retrieval using a publishable key. | 
**confirmation_method** | [**StripeConfirmationMethod**](StripeConfirmationMethod.md) | Confirmation method of this PaymentIntent, one of manual or automatic. | 
**currency** | **str** | Three-letter ISO currency code | 
**description** | **str** | An arbitrary string attached to the object. Often useful for displaying to users. | [optional] 
**last_payment_error** | **dict(str, object)** | The payment error encountered in the previous PaymentIntent confirmation. | [optional] 
**next_action** | **dict(str, object)** | If present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source. | [optional] 
**payment_method_types** | **dict(str, object)** | The list of payment method types (e.g. card) that this PaymentIntent is allowed to use. | 
**receipt_email** | **str** | Email address that the receipt for the resulting payment will be sent to. | [optional] 
**shipping** | **dict(str, object)** | Shipping information for this PaymentIntent. | [optional] 
**statement_descriptor** | **str** | For non-card charges, you can use this value as the complete description that appears on your customers&#39; statements. Must contain at least one letter, maximum 22 characters. | [optional] 
**status** | [**StripePaymentIntentStatus**](StripePaymentIntentStatus.md) | Status of this PaymentIntent, one of requires_payment_method, requires_confirmation, requires_action, processing, requires_capture, canceled, or succeeded. You can read more about PaymentIntent statuses here. | 
**transfer_data** | **dict(str, object)** | The data with which to automatically create a Transfer when the payment is finalized. See the PaymentIntents Connect usage guide for details. | [optional] 
**transfer_group** | **str** | A string that identifies the resulting payment as part of a group. See the PaymentIntents Connect usage guide for details. | [optional] 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 
**customer** | **str** | Customer this PaymentIntent is for if one exists. | [optional] 
**on_behalf_of** | **str** | The account (if any) for which the funds of the PaymentIntent are intended. | [optional] 
**payment_method** | **str** | Payment method used in this PaymentIntent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


