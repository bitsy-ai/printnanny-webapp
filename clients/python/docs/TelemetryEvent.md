# TelemetryEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**print_session** | **str** |  | [optional] [readonly] 
**event_type** | [**TelemetryEventEventTypeEnum**](TelemetryEventEventTypeEnum.md) |  | 
**environment** | [**OctoPrintEnvironment**](OctoPrintEnvironment.md) |  | 
**octoprint_job** | [**OctoPrintJob**](OctoPrintJob.md) |  | [optional] 
**created_dt** | **datetime** |  | [optional] [readonly] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] 
**event_data** | **dict(str, object)** |  | [optional] 
**plugin_version** | **str** |  | 
**client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**metadata** | **dict(str, object)** |  | [optional] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**octoprint_device** | **int** |  | 
**user** | **int** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


