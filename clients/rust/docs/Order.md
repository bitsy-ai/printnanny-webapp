# Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [readonly]
**created_dt** | **String** |  | [readonly]
**products** | [**Vec<crate::models::Product>**](Product.md) |  | [readonly]
**djstripe_customer** | Option<[**crate::models::DjStripeCustomer**](DjStripeCustomer.md)> |  | [readonly]
**djstripe_checkout_session** | Option<[**crate::models::DjStripeCheckoutSession**](DjStripeCheckoutSession.md)> |  | [readonly]
**djstripe_payment_intent** | Option<[**crate::models::DjStripePaymentIntent**](DjStripePaymentIntent.md)> |  | [readonly]
**last_status** | [**crate::models::OrderStatus**](OrderStatus.md) |  | 
**status_history** | [**Vec<crate::models::OrderStatus>**](OrderStatus.md) |  | 
**email** | **String** |  | 
**stripe_checkout_redirect_url** | **String** |  | [readonly]
**stripe_checkout_session_data** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


