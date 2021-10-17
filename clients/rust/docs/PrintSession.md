# PrintSession

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | Option<**i32**> |  | [optional][readonly]
**created_dt** | **String** |  | 
**updated_dt** | Option<**String**> |  | [optional][readonly]
**octoprint_device** | **i32** |  | 
**active** | Option<**bool**> |  | [optional]
**session** | **String** |  | 
**filepos** | Option<**i32**> |  | [optional]
**print_progress** | Option<**i32**> |  | [optional]
**time_elapsed** | Option<**i32**> |  | [optional]
**time_remaining** | Option<**i32**> |  | [optional]
**user** | Option<**i32**> |  | [optional][readonly]
**printer_profile** | Option<**i32**> |  | [optional]
**gcode_file** | Option<**i32**> |  | [optional]
**gcode_filename** | Option<**String**> |  | [optional]
**octoprint_job** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**print_job_status** | Option<[**crate::models::PrintJobStatusEnum**](PrintJobStatusEnum.md)> |  | [optional]
**url** | Option<**String**> |  | [optional][readonly]
**datesegment** | Option<**String**> |  | [optional][readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


