# DjStripePrice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **i32** |  | [readonly]
**billing_scheme** | [**crate::models::StripeBillingScheme**](StripeBillingScheme.md) |  | 
**human_readable_price** | **String** |  | 
**tiers_mode** | [**crate::models::StripePriceTiersMode**](StripePriceTiersMode.md) |  | 
**djstripe_created** | **String** |  | [readonly]
**djstripe_updated** | **String** |  | [readonly]
**id** | **String** |  | 
**livemode** | Option<**bool**> | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional]
**created** | Option<**String**> | The datetime this object was created in stripe. | [optional]
**metadata** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional]
**description** | Option<**String**> | A description of this object. | [optional]
**active** | **bool** | Whether the price can be used for new purchases. | 
**currency** | **String** | Three-letter ISO currency code | 
**nickname** | Option<**String**> | A brief description of the plan, hidden from customers. | [optional]
**recurring** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | The recurring components of a price such as `interval` and `usage_type`. | [optional]
**_type** | Option<[**crate::models::StripePriceType**](StripePriceType.md)> | Whether the price is for a one-time purchase or a recurring (subscription) purchase. | 
**unit_amount** | Option<**i64**> | The unit amount in cents to be charged, represented as a whole integer if possible. Null if a sub-cent precision is required. | [optional]
**unit_amount_decimal** | Option<**String**> | The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. | [optional]
**lookup_key** | Option<**String**> | A lookup key used to retrieve prices dynamically from a static string. | [optional]
**tiers** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. | [optional]
**transform_quantity** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`. | [optional]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]
**product** | **String** | The product this price is associated with. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


