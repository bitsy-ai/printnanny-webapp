# PrintStatusEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**print_session** | **str** |  | [optional] [readonly] 
**created_dt** | **datetime** |  | [optional] [readonly] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] 
**event_data** | **dict(str, object)** |  | [optional] 
**plugin_version** | **str** |  | 
**client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**metadata** | **dict(str, object)** |  | [optional] 
**octoprint_job** | **dict(str, object)** |  | [optional] 
**event_type** | [**PrintStatusEventEventTypeEnum**](PrintStatusEventEventTypeEnum.md) |  | 
**state** | **dict(str, object)** |  | [optional] 
**current_z** | **float** |  | [optional] 
**progress** | **dict(str, object)** |  | [optional] 
**job_data_file** | **str** |  | 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**octoprint_device** | **int** |  | 
**user** | **int** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


