# PrintNannyPluginEventRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ts** | Option<**f32**> |  | [optional]
**event_source** | Option<[**crate::models::EventSourceEnum**](EventSourceEnum.md)> |  | [optional]
**event_type** | Option<[**crate::models::PrintNannyPluginEventEventTypeEnum**](PrintNannyPluginEventEventTypeEnum.md)> |  | [optional]
**octoprint_environment** | [**crate::models::OctoprintEnvironmentRequest**](OctoprintEnvironmentRequest.md) |  | 
**octoprint_printer_data** | [**crate::models::OctoprintPrinterDataRequest**](OctoprintPrinterDataRequest.md) |  | 
**event_data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**temperature** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**print_nanny_plugin_version** | **String** |  | 
**print_nanny_client_version** | **String** |  | 
**octoprint_version** | **String** |  | 
**octoprint_device** | **i32** |  | 
**print_session** | Option<**i32**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


