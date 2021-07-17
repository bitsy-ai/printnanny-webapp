# DeviceIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | Option<**i32**> |  | [optional][readonly]
**deleted** | Option<**String**> |  | [optional][readonly]
**created_dt** | Option<**String**> |  | [optional][readonly]
**updated_dt** | Option<**String**> |  | [optional][readonly]
**user** | Option<**i32**> |  | [optional][readonly]
**name** | **String** |  | 
**public_key** | Option<**String**> |  | [optional][readonly]
**fingerprint** | Option<**String**> |  | [optional][readonly]
**cloudiot_device** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional][readonly]
**cloudiot_device_name** | Option<**String**> |  | [optional][readonly]
**cloudiot_device_path** | Option<**String**> |  | [optional][readonly]
**cloudiot_device_num_id** | Option<**i32**> |  | [optional][readonly]
**os_version** | **String** |  | 
**os** | **String** |  | 
**kernel_version** | **String** |  | 
**hardware** | **String** |  | 
**revision** | **String** |  | 
**model** | **String** |  | 
**serial** | **String** |  | 
**cores** | **i32** |  | 
**ram** | **i64** |  | 
**cpu_flags** | **Vec<String>** |  | 
**url** | Option<**String**> |  | [optional][readonly]
**private_key** | Option<**String**> |  | [optional][readonly]
**private_key_checksum** | Option<**String**> |  | [optional][readonly]
**public_key_checksum** | Option<**String**> |  | [optional][readonly]
**cloudiot_device_configs** | Option<**String**> |  | [optional][readonly]
**ca_certs** | Option<[**crate::models::DeviceIdentityCaCerts**](DeviceIdentity_ca_certs.md)> |  | [optional]
**manage_url** | Option<**String**> |  | [optional][readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


