# PolymorphicEventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**TestEventModel**](TestEventModel.md) |  | 
**source** | [**EventSource**](EventSource.md) |  | 
**send_ws** | **bool** | Broadcast to events websocket: /ws/events | [optional] 
**event_name** | [**TestEventName**](TestEventName.md) |  | 
**payload** | **dict(str, object)** |  | [optional] 
**octoprint_install** | **int** |  | 
**device** | **int** |  | 
**data** | **dict(str, object)** |  | [optional] 
**stream** | **int** |  | 
**send_mqtt** | **bool** | Broadcast to mqtt topic: /devices/{device-id}/commands/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


