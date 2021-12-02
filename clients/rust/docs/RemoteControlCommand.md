# RemoteControlCommand

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**created_dt** | **String** |  | [readonly]
**command** | Option<[**crate::models::CommandEnum**](CommandEnum.md)> |  | [optional]
**user** | **i32** |  | 
**device** | **i32** |  | 
**received** | Option<**bool**> |  | [optional]
**success** | Option<**bool**> |  | [optional]
**iotcore_response** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**metadata** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**url** | **String** |  | [readonly]
**octoprint_event_type** | **String** |  | [readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


