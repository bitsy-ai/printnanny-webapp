# DeviceIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**deleted** | **String** |  | [readonly]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**user** | **i32** |  | [readonly]
**name** | **String** |  | 
**public_key** | **String** |  | [readonly]
**fingerprint** | **String** |  | [readonly]
**cloudiot_device** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) |  | [readonly]
**cloudiot_device_name** | **String** |  | [readonly]
**cloudiot_device_path** | **String** |  | [readonly]
**cloudiot_device_num_id** | **i32** |  | [readonly]
**os_version** | **String** |  | 
**os** | **String** |  | 
**kernel_version** | **String** |  | 
**hardware** | Option<**String**> |  | [optional]
**revision** | Option<**String**> |  | [optional]
**model** | Option<**String**> |  | [optional]
**serial** | Option<**String**> |  | [optional]
**cores** | **i32** |  | 
**ram** | **i64** |  | 
**cpu_flags** | **Vec<String>** |  | 
**url** | **String** |  | [readonly]
**private_key** | **String** |  | [readonly]
**private_key_checksum** | **String** |  | [readonly]
**public_key_checksum** | **String** |  | [readonly]
**cloudiot_device_configs** | **String** |  | [readonly]
**ca_certs** | [**crate::models::DeviceIdentityCaCerts**](DeviceIdentity_ca_certs.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


