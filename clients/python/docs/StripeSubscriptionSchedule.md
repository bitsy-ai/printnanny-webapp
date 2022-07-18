# StripeSubscriptionSchedule


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
**billing_thresholds** | **dict(str, object)** | Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period. | [optional] 
**canceled_at** | **datetime** | Time at which the subscription schedule was canceled. | [optional] 
**completed_at** | **datetime** | Time at which the subscription schedule was completed. | [optional] 
**current_phase** | **dict(str, object)** | Object representing the start and end dates for the current phase of the subscription schedule, if it is &#x60;active&#x60;. | [optional] 
**default_settings** | **dict(str, object)** | Object representing the subscription schedule&#39;s default settings. | [optional] 
**end_behavior** | [**EndBehaviorEnum**](EndBehaviorEnum.md) | Behavior of the subscription schedule and underlying subscription when it ends. | 
**phases** | **dict(str, object)** | Configuration for the subscription schedule&#39;s phases. | [optional] 
**released_at** | **datetime** | Time at which the subscription schedule was released. | [optional] 
**status** | [**StripeSubscriptionScheduleStatusEnum**](StripeSubscriptionScheduleStatusEnum.md) | The present status of the subscription schedule. Possible values are &#x60;not_started&#x60;, &#x60;active&#x60;, &#x60;completed&#x60;, &#x60;released&#x60;, and &#x60;canceled&#x60;. | 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 
**customer** | **int** | The customer who owns the subscription schedule. | 
**released_subscription** | **int** | The subscription once managed by this subscription schedule (if it is released). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


