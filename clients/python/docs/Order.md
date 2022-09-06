# Order

Djstripe's representation of Stripe Checkout model is missing a number of fields, like subtotal amount and shipping/tax charges  stripe_checkout_session_data is the raw JSON returned by stripe.checkout.Session.retrieve

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_dt** | **datetime** |  | [readonly] 
**products** | [**list[Product]**](Product.md) |  | [readonly] 
**djstripe_customer** | [**DjStripeCustomer**](DjStripeCustomer.md) |  | [readonly] 
**djstripe_checkout_session** | [**DjStripeCheckoutSession**](DjStripeCheckoutSession.md) |  | [readonly] 
**djstripe_payment_intent** | [**DjStripePaymentIntent**](DjStripePaymentIntent.md) |  | [readonly] 
**last_status** | [**OrderStatus**](OrderStatus.md) |  | 
**status_history** | [**list[OrderStatus]**](OrderStatus.md) |  | 
**email** | **str** |  | 
**stripe_checkout_redirect_url** | **str** |  | [readonly] 
**stripe_checkout_session_data** | **dict(str, object)** |  | [readonly] 
**user** | [**User**](User.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


