# PolymorphicEventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**TestEventEventTypeEnum**](TestEventEventTypeEnum.md) |  | 
**source** | [**EventSource**](EventSource.md) |  | 
**send_ws** | **bool** | Broadcast to events websocket: /ws/events | [optional] 
**event_name** | [**TestEventName**](TestEventName.md) |  | 
**data** | **dict(str, object)** |  | [optional] 
**mqtt** | **bool** | Broadcast to mqtt topic: /devices/{device-id}/commands/ | [optional] 
**device** | **int** |  | 
**send_mqtt** | **bool** | Broadcast to mqtt topic: /devices/{device-id}/commands/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


