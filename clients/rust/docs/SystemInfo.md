# SystemInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**machine_id** | **String** | Populated from /etc/machine-id | 
**revision** | **String** | Populated from /proc/cpuinfo REVISION | 
**model** | **String** | Populated from /proc/cpuinfo MODEL | 
**serial** | **String** | Populated from /proc/cpuinfo SERIAL | 
**cores** | **i32** |  | 
**ram** | **i64** |  | 
**os_version_id** | **String** | PrintNanny OS VERSION_ID from /etc/os-release | 
**os_build_id** | **String** | PrintNanny OS BUILD_ID from /etc/os-release | 
**os_variant_id** | **String** | PrintNanny OS VARIANT_ID from /etc/os-release | 
**os_release_json** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Full contents of /etc/os-release in key:value format | [optional]
**device** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


