# PolymorphicEventRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**crate::models::TestEventEventTypeEnum**](TestEventEventTypeEnum.md) |  | 
**source** | [**crate::models::EventSource**](EventSource.md) |  | 
**send_ws** | Option<**bool**> | Broadcast to events websocket: /ws/events | [optional]
**event_name** | [**crate::models::TestEventName**](TestEventName.md) |  | 
**data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**send_mqtt** | Option<**bool**> | Broadcast to mqtt topic: /devices/{device-id}/commands/ | [optional]
**device** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


