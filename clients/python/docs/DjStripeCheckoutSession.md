# DjStripeCheckoutSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **int** |  | [readonly] 
**billing_address_collection** | [**StripeSessionBillingAddressCollection**](StripeSessionBillingAddressCollection.md) |  | 
**mode** | [**StripeSessionMode**](StripeSessionMode.md) |  | 
**submit_type** | [**StripeSubmitTypeStatus**](StripeSubmitTypeStatus.md) |  | 
**djstripe_created** | **datetime** |  | [readonly] 
**djstripe_updated** | **datetime** |  | [readonly] 
**id** | **str** |  | 
**livemode** | **bool** | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional] 
**created** | **datetime** | The datetime this object was created in stripe. | [optional] 
**metadata** | **dict(str, object)** | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional] 
**description** | **str** | A description of this object. | [optional] 
**cancel_url** | **str** | The URL the customer will be directed to if theydecide to cancel payment and return to your website. | [optional] 
**client_reference_id** | **str** | A unique string to reference the Checkout Session.This can be a customer ID, a cart ID, or similar, andcan be used to reconcile the session with your internal systems. | [optional] 
**customer_email** | **str** | If provided, this value will be used when the Customer object is created. | [optional] 
**display_items** | **dict(str, object)** | The line items, plans, or SKUs purchased by the customer. | [optional] 
**locale** | **str** | The IETF language tag of the locale Checkout is displayed in.If blank or auto, the browser&#39;s locale is used. | [optional] 
**payment_method_types** | **dict(str, object)** | The list of payment method types (e.g. card) that this Checkout Session is allowed to accept. | 
**success_url** | **str** | The URL the customer will be directed to after the payment or subscriptioncreation is successful. | [optional] 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 
**customer** | **str** | Customer this Checkout is for if one exists. | [optional] 
**payment_intent** | **str** | PaymentIntent created if SKUs or line items were provided. | [optional] 
**subscription** | **str** | Subscription created if one or more plans were provided. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


