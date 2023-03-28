# PrintJobAlert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [readonly]
**created_dt** | **String** |  | [readonly]
**event_type** | [**crate::models::EventTypeEnum**](EventTypeEnum.md) |  | 
**event_source** | [**crate::models::EventSourceEnum**](EventSourceEnum.md) |  | 
**payload** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**email_message_id** | Option<**String**> |  | [optional]
**celery_task_id** | Option<**String**> |  | [optional]
**image** | Option<**String**> |  | [optional]
**user** | **i32** |  | [readonly]
**pi** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


