# PrintJobEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**ts** | **float** |  | [optional] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] 
**event_type** | [**PrintJobEventType**](PrintJobEventType.md) |  | [optional] 
**octoprint_environment** | [**OctoprintEnvironment**](OctoprintEnvironment.md) |  | 
**octoprint_printer_data** | [**OctoprintPrinterData**](OctoprintPrinterData.md) |  | 
**event_data** | **dict(str, object)** |  | [optional] 
**temperature** | **dict(str, object)** |  | [optional] 
**print_nanny_plugin_version** | **str** |  | 
**print_nanny_client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**polymorphic_ctype** | **int** |  | [readonly] 
**octoprint_device** | **int** |  | 
**user** | **int** |  | [readonly] 
**print_session** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


