# DjStripeProduct

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
**name** | **String** | The product's name, meant to be displayable to the customer. Applicable to both `service` and `good` types. | 
**_type** | Option<[**crate::models::StripeProductType**](StripeProductType.md)> | The type of the product. The product is either of type `good`, which is eligible for use with Orders and SKUs, or `service`, which is eligible for use with Subscriptions and Plans.  * `good` - Good * `service` - Service | 
**active** | Option<**bool**> | Whether the product is currently available for purchase. Only applicable to products of `type=good`. | [optional]
**attributes** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | A list of up to 5 attributes that each SKU can provide values for (e.g., `[\"color\", \"size\"]`). Only applicable to products of `type=good`. | [optional]
**caption** | Option<**String**> | A short one-line description of the product, meant to be displayableto the customer. Only applicable to products of `type=good`. | [optional]
**deactivate_on** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`. | [optional]
**images** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of `type=good`. | [optional]
**package_dimensions** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | The dimensions of this product for shipping purposes. A SKU associated with this product can override this value by having its own `package_dimensions`. Only applicable to products of `type=good`. | [optional]
**shippable** | Option<**bool**> | Whether this product is a shipped good. Only applicable to products of `type=good`. | [optional]
**url** | Option<**String**> | A URL of a publicly-accessible webpage for this product. Only applicable to products of `type=good`. | [optional]
**statement_descriptor** | Option<**String**> | Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only available on products of type=`service`. | [optional]
**unit_label** | Option<**String**> |  | [optional]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


