# OctoPrintEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | Option<**i32**> |  | [optional][readonly]
**event_type** | [**crate::models::OctoPrintEventEventTypeEnum**](OctoPrintEventEventTypeEnum.md) |  | 
**ts** | Option<**String**> |  | [optional][readonly]
**event_source** | Option<[**crate::models::EventSourceEnum**](EventSourceEnum.md)> |  | [optional][readonly]
**event_data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**octoprint_environment** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**octoprint_printer_data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**temperature** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**print_nanny_plugin_version** | **String** |  | 
**print_nanny_client_version** | **String** |  | 
**octoprint_version** | **String** |  | 
**polymorphic_ctype** | Option<**i32**> |  | [optional][readonly]
**octoprint_device** | **i32** |  | 
**user** | Option<**i32**> |  | [optional][readonly]
**print_session** | Option<**i32**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


