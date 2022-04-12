# PolymorphicEventRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**crate::models::TestEventModel**](TestEventModel.md) |  | 
**source** | [**crate::models::EventSource**](EventSource.md) |  | 
**send_ws** | Option<**bool**> | Broadcast to events websocket: /ws/events | [optional]
**event_name** | [**crate::models::TestEventName**](TestEventName.md) |  | 
**payload** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**octoprint_install** | **i32** |  | 
**device** | **i32** |  | 
**data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**stream** | **i32** |  | 
**send_mqtt** | Option<**bool**> | Broadcast to mqtt topic: /devices/{device-id}/commands/ | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


