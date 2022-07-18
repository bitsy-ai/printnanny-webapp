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
**aggregate_usage** | Option<[**crate::models::OneOfAggregateUsageEnumBlankEnum**](oneOf<AggregateUsageEnum,BlankEnum>.md)> | Specifies a usage aggregation strategy for plans of usage_type=metered. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for picking the last usage record reported within a period, `last_ever` for picking the last usage record ever (across period bounds) or max which picks the usage record with the maximum reported usage during a period. Defaults to `sum`. | [optional]
**amount** | Option<**String**> | Amount (as decimal) to be charged on the interval specified. | [optional]
**amount_decimal** | Option<**String**> | The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. | [optional]
**billing_scheme** | Option<[**crate::models::OneOfBillingSchemeEnumBlankEnum**](oneOf<BillingSchemeEnum,BlankEnum>.md)> | Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in amount) will be charged per unit in quantity (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the tiers and tiers_mode attributes. | [optional]
**currency** | **String** | Three-letter ISO currency code | 
**interval** | Option<[**crate::models::IntervalEnum**](IntervalEnum.md)> | The frequency with which a subscription should be billed. | 
**interval_count** | Option<**i32**> | The number of intervals (specified in the interval property) between each subscription billing. | [optional]
**nickname** | Option<**String**> | A brief description of the plan, hidden from customers. | [optional]
**tiers** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. | [optional]
**tiers_mode** | Option<[**crate::models::OneOfTiersModeEnumBlankEnumNullEnum**](oneOf<TiersModeEnum,BlankEnum,NullEnum>.md)> | Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows. | [optional]
**transform_usage** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`. | [optional]
**trial_period_days** | Option<**i32**> | Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period. | [optional]
**usage_type** | Option<[**crate::models::UsageTypeEnum**](UsageTypeEnum.md)> | Configures how the quantity per period should be determined, can be either `metered` or `licensed`. `licensed` will automatically bill the `quantity` set for a plan when adding it to a subscription, `metered` will aggregate the total usage based on usage records. Defaults to `licensed`. | [optional]
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]
**product** | Option<**String**> | The product whose pricing this plan determines. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


