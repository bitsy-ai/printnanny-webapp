# DjStripeCustomer

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
**description** | Option<**String**> | A description of this object. | [optional]
**address** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | The customer's address. | [optional]
**balance** | Option<**i64**> | Current balance (in cents), if any, being stored on the customer's account. If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account for recurring billing purposes (i.e., subscriptions, invoices, invoice items). | [optional]
**currency** | Option<**String**> | The currency the customer can be charged in for recurring billing purposes | [optional]
**delinquent** | Option<**bool**> | Whether or not the latest charge for the customer's latest invoice has failed. | [optional]
**deleted** | Option<**bool**> | Whether the Customer instance has been deleted upstream in Stripe or not. | [optional]
**coupon_start** | **String** | If a coupon is present, the date at which it was applied. | [readonly]
**coupon_end** | **String** | If a coupon is present and has a limited duration, the date that the discount will end. | [readonly]
**email** | Option<**String**> |  | [optional]
**invoice_prefix** | Option<**String**> | The prefix for the customer used to generate unique invoice numbers. | [optional]
**invoice_settings** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | The customer's default invoice settings. | [optional]
**name** | Option<**String**> | The customer's full name or business name. | [optional]
**phone** | Option<**String**> | The customer's phone number. | [optional]
**preferred_locales** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | The customer's preferred locales (languages), ordered by preference. | [optional]
**shipping** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Shipping information associated with the customer. | [optional]
**tax_exempt** | Option<[**crate::models::StripeCustomerTaxExempt**](StripeCustomerTaxExempt.md)> | Describes the customer's tax exemption status. When set to reverse, invoice and receipt PDFs include the text \"Reverse charge\". | [optional]
**date_purged** | **String** |  | [readonly]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | 
**default_source** | Option<**String**> |  | [optional]
**coupon** | Option<**i32**> |  | [optional]
**default_payment_method** | Option<**String**> | default payment method used for subscriptions and invoices for the customer. | [optional]
**subscriber** | Option<**i32**> |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


