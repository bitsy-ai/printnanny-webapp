# Order

Djstripe's representation of Stripe Checkout model is missing a number of fields, like subtotal amount and shipping/tax charges  stripe_checkout_session_data is the raw JSON returned by stripe.checkout.Session.retrieve

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_dt** | **datetime** |  | [readonly] 
**djstripe_checkout_session** | [**DjStripeCheckoutSession**](DjStripeCheckoutSession.md) |  | [readonly] 
**djstripe_customer** | [**DjStripeCustomer**](DjStripeCustomer.md) |  | [readonly] 
**djstripe_payment_intent** | [**DjStripePaymentIntent**](DjStripePaymentIntent.md) |  | [readonly] 
**email** | **str** |  | 
**id** | **str** |  | [readonly] 
**is_shippable** | **bool** |  | [readonly] 
**is_subscription** | **bool** |  | [readonly] 
**last_status** | [**OrderStatus**](OrderStatus.md) |  | 
**products** | [**list[Product]**](Product.md) |  | [readonly] 
**status_history** | [**list[OrderStatus]**](OrderStatus.md) |  | 
**stripe_checkout_redirect_url** | **str** |  | [readonly] 
**stripe_checkout_session_data** | **dict(str, object)** |  | [readonly] 
**user** | [**User**](User.md) |  | [optional] 
**receipt_url** | **str** |  | [readonly] 
**portal_url** | **str** |  | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


