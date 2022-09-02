# DjStripeCheckoutSession

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **i32** |  | [readonly]
**billing_address_collection** | [**crate::models::StripeSessionBillingAddressCollection**](StripeSessionBillingAddressCollection.md) |  | 
**mode** | [**crate::models::StripeSessionMode**](StripeSessionMode.md) |  | 
**submit_type** | [**crate::models::StripeSubmitTypeStatus**](StripeSubmitTypeStatus.md) |  | 
**djstripe_created** | **String** |  | [readonly]
**djstripe_updated** | **String** |  | [readonly]
**id** | **String** |  | 
**livemode** | Option<**bool**> | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional]
**created** | Option<**String**> | The datetime this object was created in stripe. | [optional]
**metadata** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional]
**description** | Option<**String**> | A description of this object. | [optional]
**cancel_url** | Option<**String**> | The URL the customer will be directed to if theydecide to cancel payment and return to your website. | [optional]
**client_reference_id** | Option<**String**> | A unique string to reference the Checkout Session.This can be a customer ID, a cart ID, or similar, andcan be used to reconcile the session with your internal systems. | [optional]
**customer_email** | Option<**String**> | If provided, this value will be used when the Customer object is created. | [optional]
**display_items** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | The line items, plans, or SKUs purchased by the customer. | [optional]
**locale** | Option<**String**> | The IETF language tag of the locale Checkout is displayed in.If blank or auto, the browser's locale is used. | [optional]
**payment_method_types** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) | The list of payment method types (e.g. card) that this Checkout Session is allowed to accept. | 
**success_url** | Option<**String**> | The URL the customer will be directed to after the payment or subscriptioncreation is successful. | [optional]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]
**customer** | Option<**String**> | Customer this Checkout is for if one exists. | [optional]
**payment_intent** | Option<**String**> | PaymentIntent created if SKUs or line items were provided. | [optional]
**subscription** | Option<**String**> | Subscription created if one or more plans were provided. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


