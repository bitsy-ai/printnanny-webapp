# AlertPolymorphic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_dt** | **datetime** |  | [optional] [readonly] 
**updated_dt** | **datetime** |  | [optional] [readonly] 
**user** | **int** |  | [optional] [readonly] 
**time** | **str** |  | [optional] [readonly] 
**seen** | **bool** |  | [optional] 
**octoprint_device** | **int** |  | [optional] [readonly] 
**alert_subtype** | [**PrintSessionAlertAlertSubtypeEnum**](PrintSessionAlertAlertSubtypeEnum.md) |  | 
**alert_method** | [**AlertMethodEnum**](AlertMethodEnum.md) |  | [optional] [readonly] 
**alert_type** | [**AlertTypeEnum**](AlertTypeEnum.md) |  | [readonly] 
**color** | **str** |  | 
**dashboard_url** | **str** |  | [optional] [readonly] 
**metadata** | **str** |  | [optional] [readonly] 
**icon** | **str** |  | 
**id** | **int** |  | [optional] [readonly] 
**description** | **str** |  | 
**title** | **str** |  | 
**sent** | **bool** |  | [optional] 
**progress_percent** | **int** | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress | [optional] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**device** | **int** |  | 
**needs_review** | **bool** |  | [optional] 
**annotated_video** | **str** |  | 
**print_session** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


