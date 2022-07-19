# StripePlan

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
**active** | **bool** | Whether the plan can be used for new purchases. | 
**amount** | Option<**String**> | Amount (as decimal) to be charged on the interval specified. | [optional]
**amount_decimal** | Option<**String**> | The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. | [optional]
**currency** | **String** | Three-letter ISO currency code | 
**interval** | Option<[**crate::models::IntervalEnum**](IntervalEnum.md)> | The frequency with which a subscription should be billed. | 
**interval_count** | Option<**i32**> | The number of intervals (specified in the interval property) between each subscription billing. | [optional]
**nickname** | Option<**String**> | A brief description of the plan, hidden from customers. | [optional]
**tiers** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. | [optional]
**transform_usage** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`. | [optional]
**trial_period_days** | Option<**i32**> | Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period. | [optional]
**usage_type** | Option<[**crate::models::UsageTypeEnum**](UsageTypeEnum.md)> | Configures how the quantity per period should be determined, can be either `metered` or `licensed`. `licensed` will automatically bill the `quantity` set for a plan when adding it to a subscription, `metered` will aggregate the total usage based on usage records. Defaults to `licensed`. | [optional]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]
**product** | Option<**String**> | The product whose pricing this plan determines. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

