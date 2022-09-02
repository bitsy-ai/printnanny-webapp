# DjStripeProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **int** |  | [readonly] 
**djstripe_created** | **datetime** |  | [readonly] 
**djstripe_updated** | **datetime** |  | [readonly] 
**id** | **str** |  | 
**livemode** | **bool** | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional] 
**created** | **datetime** | The datetime this object was created in stripe. | [optional] 
**metadata** | **dict(str, object)** | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional] 
**description** | **str** | A description of this object. | [optional] 
**name** | **str** | The product&#39;s name, meant to be displayable to the customer. Applicable to both &#x60;service&#x60; and &#x60;good&#x60; types. | 
**type** | [**StripeProductType**](StripeProductType.md) | The type of the product. The product is either of type &#x60;good&#x60;, which is eligible for use with Orders and SKUs, or &#x60;service&#x60;, which is eligible for use with Subscriptions and Plans. | 
**active** | **bool** | Whether the product is currently available for purchase. Only applicable to products of &#x60;type&#x3D;good&#x60;. | [optional] 
**attributes** | **dict(str, object)** | A list of up to 5 attributes that each SKU can provide values for (e.g., &#x60;[\&quot;color\&quot;, \&quot;size\&quot;]&#x60;). Only applicable to products of &#x60;type&#x3D;good&#x60;. | [optional] 
**caption** | **str** | A short one-line description of the product, meant to be displayableto the customer. Only applicable to products of &#x60;type&#x3D;good&#x60;. | [optional] 
**deactivate_on** | **dict(str, object)** | An array of connect application identifiers that cannot purchase this product. Only applicable to products of &#x60;type&#x3D;good&#x60;. | [optional] 
**images** | **dict(str, object)** | A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of &#x60;type&#x3D;good&#x60;. | [optional] 
**package_dimensions** | **dict(str, object)** | The dimensions of this product for shipping purposes. A SKU associated with this product can override this value by having its own &#x60;package_dimensions&#x60;. Only applicable to products of &#x60;type&#x3D;good&#x60;. | [optional] 
**shippable** | **bool** | Whether this product is a shipped good. Only applicable to products of &#x60;type&#x3D;good&#x60;. | [optional] 
**url** | **str** | A URL of a publicly-accessible webpage for this product. Only applicable to products of &#x60;type&#x3D;good&#x60;. | [optional] 
**statement_descriptor** | **str** | Extra information about a product which will appear on your customer&#39;s credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only available on products of type&#x3D;&#x60;service&#x60;. | [optional] 
**unit_label** | **str** |  | [optional] 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


