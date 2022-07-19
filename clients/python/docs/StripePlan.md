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
**amount** | **str** | Amount (as decimal) to be charged on the interval specified. | [optional] 
**amount_decimal** | **str** | The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. | [optional] 
**currency** | **str** | Three-letter ISO currency code | 
**interval** | [**IntervalEnum**](IntervalEnum.md) | The frequency with which a subscription should be billed. | 
**interval_count** | **int** | The number of intervals (specified in the interval property) between each subscription billing. | [optional] 
**nickname** | **str** | A brief description of the plan, hidden from customers. | [optional] 
**tiers** | **dict(str, object)** | Each element represents a pricing tier. This parameter requires &#x60;billing_scheme&#x60; to be set to &#x60;tiered&#x60;. | [optional] 
**transform_usage** | **dict(str, object)** | Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with &#x60;tiers&#x60;. | [optional] 
**trial_period_days** | **int** | Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period. | [optional] 
**usage_type** | [**UsageTypeEnum**](UsageTypeEnum.md) | Configures how the quantity per period should be determined, can be either &#x60;metered&#x60; or &#x60;licensed&#x60;. &#x60;licensed&#x60; will automatically bill the &#x60;quantity&#x60; set for a plan when adding it to a subscription, &#x60;metered&#x60; will aggregate the total usage based on usage records. Defaults to &#x60;licensed&#x60;. | [optional] 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 
**product** | **str** | The product whose pricing this plan determines. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


