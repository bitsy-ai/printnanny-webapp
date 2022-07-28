# PolymorphicEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**model** | [**crate::models::TestEventModel**](TestEventModel.md) |  | 
**created_dt** | **String** |  | [readonly]
**source** | [**crate::models::EventSource**](EventSource.md) |  | 
**event_name** | [**crate::models::TestEventName**](TestEventName.md) |  | 
**payload** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**polymorphic_ctype** | **i32** |  | [readonly]
**user** | **i32** |  | [readonly]
**octoprint_server** | **i32** |  | 
**pi** | **i32** |  | 
**data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**stream** | Option<[**crate::models::WebrtcStream**](WebrtcStream.md)> |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


