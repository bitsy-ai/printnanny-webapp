# StripeEvent


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
**api_version** | **str** | the API version at which the event data was rendered. Blank for old entries only, all new entries will have this value | [optional] 
**data** | **dict(str, object)** | data received at webhook. data should be considered to be garbage until validity check is run and valid flag is set | 
**request_id** | **str** | Information about the request that triggered this event, for traceability purposes. If empty string then this is an old entry without that data. If Null then this is not an old entry, but a Stripe &#39;automated&#39; event with no associated request. | [optional] 
**idempotency_key** | **str** |  | [optional] 
**type** | **str** | Stripe&#39;s event description code | 
**djstripe_owner_account** | **str** | The Stripe Account this object belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


