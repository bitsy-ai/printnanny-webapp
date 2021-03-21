# AlertPolymorphic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_dt** | **datetime** |  | [optional] [readonly] 
**updated_dt** | **datetime** |  | [optional] [readonly] 
**user** | **int** |  | [readonly] 
**dismissed** | **bool** |  | [optional] 
**time** | **str** |  | [optional] [readonly] 
**alert_subtype** | [**AlertSubtypeEnum**](AlertSubtypeEnum.md) |  | 
**alert_method** | [**AlertMethodEnum**](AlertMethodEnum.md) |  | [readonly] 
**alert_type** | [**AlertTypeEnum**](AlertTypeEnum.md) |  | [readonly] 
**color** | **str** |  | 
**dashboard_url** | **str** |  | [optional] [readonly] 
**metadata** | **str** |  | [optional] [readonly] 
**icon** | **str** |  | 
**id** | **int** |  | [optional] [readonly] 
**description** | **str** |  | 
**seen** | **bool** |  | [optional] 
**snapshot_url** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 
**print_session** | **str** |  | 
**monitoring_mode** | [**DefectAlertMonitoringModeEnum**](DefectAlertMonitoringModeEnum.md) |  | 
**octoprint_device** | **int** |  | [optional] 
**print_job** | **int** |  | [optional] [readonly] 
**progress_percent** | **int** | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress | [optional] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**device** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


