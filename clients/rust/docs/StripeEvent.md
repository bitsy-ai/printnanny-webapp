# StripeEvent

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
**api_version** | Option<**String**> | the API version at which the event data was rendered. Blank for old entries only, all new entries will have this value | [optional]
**data** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) | data received at webhook. data should be considered to be garbage until validity check is run and valid flag is set | 
**request_id** | Option<**String**> | Information about the request that triggered this event, for traceability purposes. If empty string then this is an old entry without that data. If Null then this is not an old entry, but a Stripe 'automated' event with no associated request. | [optional]
**idempotency_key** | Option<**String**> |  | [optional]
**_type** | **String** | Stripe's event description code | 
**djstripe_owner_account** | Option<**String**> | The Stripe Account this object belongs to. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


