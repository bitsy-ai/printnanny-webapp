# OctoPrintEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**created_dt** | **datetime** |  | [optional] [readonly] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] 
**event_data** | **dict(str, object)** |  | [optional] 
**octoprint_device** | **int** |  | 
**user** | **int** |  | [optional] [readonly] 
**plugin_version** | **str** |  | 
**client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**metadata** | **dict(str, object)** |  | [optional] 
**octoprint_job** | **dict(str, object)** |  | [optional] 
**print_session** | **int** |  | [optional] 
**telemetryevent_ptr** | **int** |  | [optional] [readonly] 
**event_type** | [**OctoPrintEventEventTypeEnum**](OctoPrintEventEventTypeEnum.md) |  | 
**url** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


