# RemoteCommandEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**ts** | **datetime** |  | [optional] [readonly] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] 
**event_data** | **dict(str, object)** |  | [optional] 
**print_nanny_plugin_version** | **str** |  | 
**print_nanny_client_version** | **str** |  | 
**octoprint_job** | **dict(str, object)** |  | [optional] 
**event_type** | [**RemoteCommandEventEventTypeEnum**](RemoteCommandEventEventTypeEnum.md) |  | 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**octoprint_device** | **int** |  | 
**user** | **int** |  | [optional] [readonly] 
**print_session** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


