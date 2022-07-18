# BillingSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**crate::models::StripeSubscription**](StripeSubscription.md) |  | 
**charges** | [**Vec<crate::models::StripeCharge>**](StripeCharge.md) |  | 
**events** | [**Vec<crate::models::StripeEvent>**](StripeEvent.md) |  | 
**next_invoice** | Option<[**crate::models::StripeNextInvoice**](StripeNextInvoice.md)> |  | [optional]
**customer** | [**crate::models::StripeCustomer**](StripeCustomer.md) |  | 
**user** | Option<[**crate::models::User**](User.md)> |  | [optional]
**billing_portal_url** | **String** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


