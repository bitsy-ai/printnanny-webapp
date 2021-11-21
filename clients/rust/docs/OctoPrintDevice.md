# OctoPrintDevice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**created_dt** | **String** |  | [readonly]
**name** | **String** |  | 
**user** | **i32** |  | [readonly]
**public_key** | **String** |  | [readonly]
**fingerprint** | **String** |  | [readonly]
**cloudiot_device** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) |  | [readonly]
**cloudiot_device_name** | **String** |  | [readonly]
**cloudiot_device_path** | **String** |  | [readonly]
**cloudiot_device_num_id** | **i32** |  | [readonly]
**model** | **String** |  | 
**platform** | **String** |  | 
**cpu_flags** | Option<**Vec<String>**> |  | [optional]
**hardware** | Option<**String**> |  | [optional]
**revision** | Option<**String**> |  | [optional]
**serial** | **String** |  | 
**cores** | **i32** |  | 
**ram** | **i32** |  | 
**python_version** | **String** |  | 
**pip_version** | **String** |  | 
**virtualenv** | Option<**String**> |  | [optional]
**octoprint_version** | **String** |  | 
**plugin_version** | **String** |  | 
**print_nanny_client_version** | **String** |  | 
**cloudiot_device_configs** | **String** |  | [readonly]
**manage_url** | **String** |  | [readonly]
**monitoring_active** | **bool** |  | [readonly]
**active_session** | Option<[**crate::models::PrintSession**](PrintSession.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


