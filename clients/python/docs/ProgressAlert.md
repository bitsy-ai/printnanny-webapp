# ProgressAlert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**time** | **str** |  | [optional] [readonly] 
**alert_method** | [**AlertMethodEnum**](AlertMethodEnum.md) |  | [optional] [readonly] 
**alert_type** | [**AlertTypeEnum**](AlertTypeEnum.md) |  | [optional] [readonly] 
**created_dt** | **datetime** |  | [optional] [readonly] 
**updated_dt** | **datetime** |  | [optional] [readonly] 
**seen** | **bool** |  | [optional] 
**sent** | **bool** |  | [optional] 
**dismissed** | **bool** |  | [optional] 
**progress_percent** | **int** | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress | [optional] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**user** | **int** |  | [optional] [readonly] 
**octoprint_device** | **int** |  | [optional] 
**device** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


