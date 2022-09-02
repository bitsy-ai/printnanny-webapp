# DjStripePrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**djstripe_id** | **int** |  | [readonly] 
**human_readable_price** | **str** |  | 
**djstripe_created** | **datetime** |  | [readonly] 
**djstripe_updated** | **datetime** |  | [readonly] 
**id** | **str** |  | 
**livemode** | **bool** | Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation. | [optional] 
**created** | **datetime** | The datetime this object was created in stripe. | [optional] 
**metadata** | **dict(str, object)** | A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format. | [optional] 
**description** | **str** | A description of this object. | [optional] 
**active** | **bool** | Whether the price can be used for new purchases. | 
**currency** | **str** | Three-letter ISO currency code | 
**nickname** | **str** | A brief description of the plan, hidden from customers. | [optional] 
**recurring** | **dict(str, object)** | The recurring components of a price such as &#x60;interval&#x60; and &#x60;usage_type&#x60;. | [optional] 
**type** | [**DjStripePriceTypeEnum**](DjStripePriceTypeEnum.md) | Whether the price is for a one-time purchase or a recurring (subscription) purchase. | 
**unit_amount** | **int** | The unit amount in cents to be charged, represented as a whole integer if possible. Null if a sub-cent precision is required. | [optional] 
**unit_amount_decimal** | **str** | The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. | [optional] 
**billing_scheme** | [**OneOfBillingSchemeEnumBlankEnum**](OneOfBillingSchemeEnumBlankEnum.md) | Describes how to compute the price per period. Either &#x60;per_unit&#x60; or &#x60;tiered&#x60;. &#x60;per_unit&#x60; indicates that the fixed amount (specified in &#x60;unit_amount&#x60; or &#x60;unit_amount_decimal&#x60;) will be charged per unit in &#x60;quantity&#x60; (for prices with &#x60;usage_type&#x3D;licensed&#x60;), or per unit of total usage (for prices with &#x60;usage_type&#x3D;metered&#x60;). &#x60;tiered&#x60; indicates that the unit pricing will be computed using a tiering strategy as defined using the &#x60;tiers&#x60; and &#x60;tiers_mode&#x60; attributes. | [optional] 
**lookup_key** | **str** | A lookup key used to retrieve prices dynamically from a static string. | [optional] 
**tiers** | **dict(str, object)** | Each element represents a pricing tier. This parameter requires &#x60;billing_scheme&#x60; to be set to &#x60;tiered&#x60;. | [optional] 
**tiers_mode** | [**OneOfTiersModeEnumBlankEnumNullEnum**](OneOfTiersModeEnumBlankEnumNullEnum.md) | Defines if the tiering price should be &#x60;graduated&#x60; or &#x60;volume&#x60; based. In &#x60;volume&#x60;-based tiering, the maximum quantity within a period determines the per unit price, in &#x60;graduated&#x60; tiering pricing can successively change as the quantity grows. | [optional] 
**transform_quantity** | **dict(str, object)** | Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with &#x60;tiers&#x60;. | [optional] 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 
**product** | **str** | The product this price is associated with. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


