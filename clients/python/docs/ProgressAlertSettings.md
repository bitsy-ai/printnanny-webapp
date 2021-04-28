# ProgressAlertSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_dt** | **datetime** |  | [optional] [readonly] 
**updated_dt** | **datetime** |  | [optional] [readonly] 
**alert_type** | [**AlertTypeEnum**](AlertTypeEnum.md) |  | 
**alert_methods** | [**list[AlertMethodsEnum]**](AlertMethodsEnum.md) |  | [optional] 
**enabled** | **bool** | Enable or disable this alert type | [optional] 
**on_progress_percent** | **int** | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress | [optional] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**user** | **int** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


