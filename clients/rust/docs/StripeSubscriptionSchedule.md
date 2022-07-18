# StripeSubscriptionSchedule

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
**billing_thresholds** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period. | [optional]
**canceled_at** | Option<**String**> | Time at which the subscription schedule was canceled. | [optional]
**completed_at** | Option<**String**> | Time at which the subscription schedule was completed. | [optional]
**current_phase** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`. | [optional]
**default_settings** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Object representing the subscription schedule's default settings. | [optional]
**end_behavior** | Option<[**crate::models::EndBehaviorEnum**](EndBehaviorEnum.md)> | Behavior of the subscription schedule and underlying subscription when it ends. | 
**phases** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Configuration for the subscription schedule's phases. | [optional]
**released_at** | Option<**String**> | Time at which the subscription schedule was released. | [optional]
**status** | Option<[**crate::models::StripeSubscriptionScheduleStatusEnum**](StripeSubscriptionScheduleStatusEnum.md)> | The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`. | 
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]
**customer** | **i32** | The customer who owns the subscription schedule. | 
**released_subscription** | Option<**i32**> | The subscription once managed by this subscription schedule (if it is released). | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


