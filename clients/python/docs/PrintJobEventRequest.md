# PrintJobEventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ts** | **float** |  | [optional] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] 
**event_type** | [**PrintJobEventType**](PrintJobEventType.md) |  | [optional] 
**octoprint_environment** | [**OctoprintEnvironmentRequest**](OctoprintEnvironmentRequest.md) |  | 
**octoprint_printer_data** | [**OctoprintPrinterDataRequest**](OctoprintPrinterDataRequest.md) |  | 
**event_data** | **dict(str, object)** |  | [optional] 
**temperature** | **dict(str, object)** |  | [optional] 
**print_nanny_plugin_version** | **str** |  | 
**print_nanny_client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**octoprint_device** | **int** |  | 
**print_session** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


