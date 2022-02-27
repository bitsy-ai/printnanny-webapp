# WebRTCEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**event_type** | [**WebRTCEventEventTypeEnum**](WebRTCEventEventTypeEnum.md) |  | 
**created_dt** | **datetime** |  | [readonly] 
**source** | [**EventSource**](EventSource.md) |  | 
**send_ws** | **bool** | Broadcast to events websocket: /ws/events | [optional] 
**event_name** | [**WebRTCEventName**](WebRTCEventName.md) |  | 
**data** | **dict(str, object)** |  | [optional] 
**mqtt** | **bool** | Broadcast to mqtt topic: /devices/{device-id}/commands/ | [optional] 
**polymorphic_ctype** | **int** |  | [readonly] 
**user** | **int** |  | [readonly] 
**device** | **int** |  | 
**stream** | **int** |  | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


