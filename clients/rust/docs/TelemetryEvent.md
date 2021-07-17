# TelemetryEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**event_type** | [**crate::models::TelemetryEventEventTypeEnum**](TelemetryEventEventTypeEnum.md) |  | 
**octoprint_environment** | [**crate::models::OctoprintEnvironment**](OctoprintEnvironment.md) |  | 
**octoprint_printer_data** | [**crate::models::OctoprintPrinterData**](OctoprintPrinterData.md) |  | 
**ts** | **String** |  | [readonly]
**event_source** | [**crate::models::EventSourceEnum**](EventSourceEnum.md) |  | [readonly]
**event_data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**temperature** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**print_nanny_plugin_version** | **String** |  | 
**print_nanny_client_version** | **String** |  | 
**octoprint_version** | **String** |  | 
**polymorphic_ctype** | **i32** |  | [readonly]
**octoprint_device** | **i32** |  | 
**user** | **i32** |  | [readonly]
**print_session** | Option<**i32**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


