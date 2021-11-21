# DeviceState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**deleted** | **String** |  | [readonly]
**status** | Option<[**crate::models::StatusEnum**](StatusEnum.md)> |  | [optional]
**command** | Option<[**crate::models::DeviceStateCommandEnum**](DeviceStateCommandEnum.md)> |  | [optional]
**ansible_facts** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**ansible_extra_vars** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**created_dt** | **String** |  | [readonly]
**device** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


