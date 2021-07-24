# TelemetryEventPolymorphicRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ts** | **int** |  | [optional] 
**event_type** | [**PrintNannyPluginEventEventTypeEnum**](PrintNannyPluginEventEventTypeEnum.md) |  | 
**octoprint_environment** | [**OctoprintEnvironmentRequest**](OctoprintEnvironmentRequest.md) |  | 
**octoprint_printer_data** | [**OctoprintPrinterDataRequest**](OctoprintPrinterDataRequest.md) |  | 
**event_data** | **dict(str, object)** |  | [optional] 
**temperature** | **dict(str, object)** |  | [optional] 
**print_nanny_plugin_version** | **str** |  | 
**print_nanny_client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**octoprint_device** | **int** |  | 
**print_session** | **int** |  | [optional] 
**printer_state** | [**PrinterStateEnum**](PrinterStateEnum.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


