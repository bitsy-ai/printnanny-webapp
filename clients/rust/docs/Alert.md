# Alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**time** | **String** |  | [readonly]
**gcode_file** | **String** |  | [readonly]
**print_progress** | **String** |  | [readonly]
**time_elapsed** | **String** |  | [readonly]
**time_remaining** | **String** |  | [readonly]
**manage_device_url** | Option<**String**> |  | [readonly]
**user** | **i32** |  | [readonly]
**octoprint_device** | Option<**i32**> |  | [optional]
**alert_method** | [**crate::models::AlertMethodEnum**](AlertMethodEnum.md) |  | 
**event_type** | Option<[**crate::models::AlertEventTypeEnum**](AlertEventTypeEnum.md)> |  | [optional]
**seen** | Option<**bool**> |  | [optional]
**sent** | Option<**bool**> |  | [optional]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**message** | **String** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


