# StripePlan


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
**active** | **bool** | Whether the plan can be used for new purchases. | 
**aggregate_usage** | [**OneOfAggregateUsageEnumBlankEnum**](OneOfAggregateUsageEnumBlankEnum.md) | Specifies a usage aggregation strategy for plans of usage_type&#x3D;metered. Allowed values are &#x60;sum&#x60; for summing up all usage during a period, &#x60;last_during_period&#x60; for picking the last usage record reported within a period, &#x60;last_ever&#x60; for picking the last usage record ever (across period bounds) or max which picks the usage record with the maximum reported usage during a period. Defaults to &#x60;sum&#x60;. | [optional] 
**amount** | **str** | Amount (as decimal) to be charged on the interval specified. | [optional] 
**amount_decimal** | **str** | The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. | [optional] 
**billing_scheme** | [**OneOfBillingSchemeEnumBlankEnum**](OneOfBillingSchemeEnumBlankEnum.md) | Describes how to compute the price per period. Either &#x60;per_unit&#x60; or &#x60;tiered&#x60;. &#x60;per_unit&#x60; indicates that the fixed amount (specified in amount) will be charged per unit in quantity (for plans with &#x60;usage_type&#x3D;licensed&#x60;), or per unit of total usage (for plans with &#x60;usage_type&#x3D;metered&#x60;). &#x60;tiered&#x60; indicates that the unit pricing will be computed using a tiering strategy as defined using the tiers and tiers_mode attributes. | [optional] 
**currency** | **str** | Three-letter ISO currency code | 
**interval** | [**IntervalEnum**](IntervalEnum.md) | The frequency with which a subscription should be billed. | 
**interval_count** | **int** | The number of intervals (specified in the interval property) between each subscription billing. | [optional] 
**nickname** | **str** | A brief description of the plan, hidden from customers. | [optional] 
**tiers** | **dict(str, object)** | Each element represents a pricing tier. This parameter requires &#x60;billing_scheme&#x60; to be set to &#x60;tiered&#x60;. | [optional] 
**tiers_mode** | [**OneOfTiersModeEnumBlankEnumNullEnum**](OneOfTiersModeEnumBlankEnumNullEnum.md) | Defines if the tiering price should be &#x60;graduated&#x60; or &#x60;volume&#x60; based. In &#x60;volume&#x60;-based tiering, the maximum quantity within a period determines the per unit price, in &#x60;graduated&#x60; tiering pricing can successively change as the quantity grows. | [optional] 
**transform_usage** | **dict(str, object)** | Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with &#x60;tiers&#x60;. | [optional] 
**trial_period_days** | **int** | Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period. | [optional] 
**usage_type** | [**UsageTypeEnum**](UsageTypeEnum.md) | Configures how the quantity per period should be determined, can be either &#x60;metered&#x60; or &#x60;licensed&#x60;. &#x60;licensed&#x60; will automatically bill the &#x60;quantity&#x60; set for a plan when adding it to a subscription, &#x60;metered&#x60; will aggregate the total usage based on usage records. Defaults to &#x60;licensed&#x60;. | [optional] 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 
**product** | **str** | The product whose pricing this plan determines. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


