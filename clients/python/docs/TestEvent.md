# TestEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**event_type** | [**TestEventEventTypeEnum**](TestEventEventTypeEnum.md) |  | 
**created_dt** | **datetime** |  | [readonly] 
**source** | [**EventSource**](EventSource.md) |  | 
**send_ws** | **bool** | Broadcast to events websocket: /ws/events | [optional] 
**event_name** | [**TestEventName**](TestEventName.md) |  | 
**send_mqtt** | **bool** | Broadcast to mqtt topic: /devices/{device-id}/commands/ | [optional] 
**polymorphic_ctype** | **int** |  | [readonly] 
**user** | **int** |  | [readonly] 
**device** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


