# WebRtcEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**model** | [**crate::models::WebRtcEventModel**](WebRTCEventModel.md) |  | 
**stream** | Option<[**crate::models::JanusStream**](JanusStream.md)> |  | [readonly]
**created_dt** | **String** |  | [readonly]
**source** | [**crate::models::EventSource**](EventSource.md) |  | 
**send_ws** | Option<**bool**> | Broadcast to events websocket: /ws/events | [optional]
**event_name** | [**crate::models::WebRtcEventName**](WebRTCEventName.md) |  | 
**data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**send_mqtt** | Option<**bool**> | Broadcast to mqtt topic: /devices/{device-id}/commands/ | [optional]
**polymorphic_ctype** | **i32** |  | [readonly]
**user** | **i32** |  | [readonly]
**device** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


