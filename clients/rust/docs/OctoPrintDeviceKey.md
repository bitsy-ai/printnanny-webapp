# OctoPrintDeviceKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | Option<**i32**> |  | [optional][readonly]
**deleted** | Option<**String**> |  | [optional][readonly]
**created_dt** | Option<**String**> |  | [optional][readonly]
**name** | **String** |  | 
**user** | Option<**i32**> |  | [optional][readonly]
**public_key** | Option<**String**> |  | [optional][readonly]
**fingerprint** | Option<**String**> |  | [optional][readonly]
**cloudiot_device** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional][readonly]
**cloudiot_device_name** | Option<**String**> |  | [optional][readonly]
**cloudiot_device_path** | Option<**String**> |  | [optional][readonly]
**cloudiot_device_num_id** | Option<**i32**> |  | [optional][readonly]
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
**url** | Option<**String**> |  | [optional][readonly]
**private_key** | Option<**String**> |  | [optional][readonly]
**private_key_checksum** | Option<**String**> |  | [optional][readonly]
**public_key_checksum** | **String** |  | 
**cloudiot_device_configs** | Option<**String**> |  | [optional][readonly]
**ca_certs** | **::std::collections::HashMap<String, String>** |  | 
**manage_url** | Option<**String**> |  | [optional][readonly]
**monitoring_active** | Option<**bool**> |  | [optional][readonly]
**active_session** | Option<[**crate::models::PrintSession**](PrintSession.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


