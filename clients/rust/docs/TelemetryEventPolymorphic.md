# TelemetryEventPolymorphic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**ts** | Option<**f32**> |  | [optional]
**event_source** | Option<[**crate::models::AlphaEventSource**](AlphaEventSource.md)> |  | [readonly]
**event_type** | Option<[**crate::models::OctoPrintNannyEvent**](OctoPrintNannyEvent.md)> |  | [optional]
**octoprint_environment** | [**crate::models::OctoprintEnvironment**](OctoprintEnvironment.md) |  | 
**octoprint_printer_data** | [**crate::models::OctoprintPrinterData**](OctoprintPrinterData.md) |  | 
**event_data** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**temperature** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**print_nanny_plugin_version** | **String** |  | 
**print_nanny_client_version** | **String** |  | 
**print_nanny_beta_client_version** | Option<**String**> |  | [optional]
**octoprint_version** | **String** |  | 
**polymorphic_ctype** | **i32** |  | [readonly]
**octoprint_device** | **i32** |  | 
**user** | **i32** |  | [readonly]
**print_session** | Option<**i32**> |  | [optional]
**printer_state** | Option<[**crate::models::OctoPrinterEvent**](OctoPrinterEvent.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


