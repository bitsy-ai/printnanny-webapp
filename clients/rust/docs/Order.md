# Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_dt** | **String** |  | [readonly]
**djstripe_checkout_session** | Option<[**crate::models::DjStripeCheckoutSession**](DjStripeCheckoutSession.md)> |  | [readonly]
**djstripe_customer** | Option<[**crate::models::DjStripeCustomer**](DjStripeCustomer.md)> |  | [readonly]
**djstripe_payment_intent** | Option<[**crate::models::DjStripePaymentIntent**](DjStripePaymentIntent.md)> |  | [readonly]
**email** | **String** |  | 
**id** | **String** |  | [readonly]
**is_shippable** | **bool** |  | [readonly]
**is_subscription** | **bool** |  | [readonly]
**last_status** | [**crate::models::OrderStatus**](OrderStatus.md) |  | 
**products** | [**Vec<crate::models::Product>**](Product.md) |  | [readonly]
**status_history** | [**Vec<crate::models::OrderStatus>**](OrderStatus.md) |  | 
**stripe_checkout_redirect_url** | **String** |  | [readonly]
**stripe_checkout_session_data** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) |  | [readonly]
**user** | Option<[**crate::models::User**](User.md)> |  | [optional]
**receipt_url** | Option<**String**> |  | [readonly]
**portal_url** | Option<**String**> |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


