# OctoPrintEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**event_type** | [**OctoPrintEventEventTypeEnum**](OctoPrintEventEventTypeEnum.md) |  | 
**ts** | **datetime** |  | [optional] [readonly] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] [readonly] 
**event_data** | **dict(str, object)** |  | [optional] 
**octoprint_environment** | **dict(str, object)** |  | [optional] 
**octoprint_printer_data** | **dict(str, object)** |  | [optional] 
**temperature** | **dict(str, object)** |  | [optional] 
**print_nanny_plugin_version** | **str** |  | 
**print_nanny_client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**octoprint_device** | **int** |  | 
**user** | **int** |  | [optional] [readonly] 
**print_session** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


