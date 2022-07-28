# PatchedSystemInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **str** | Populated from /etc/machine-id | [optional] 
**revision** | **str** | Populated from /proc/cpuinfo REVISION | [optional] 
**model** | **str** | Populated from /proc/cpuinfo MODEL | [optional] 
**serial** | **str** | Populated from /proc/cpuinfo SERIAL | [optional] 
**cores** | **int** |  | [optional] 
**ram** | **int** |  | [optional] 
**os_version_id** | **str** | PrintNanny OS VERSION_ID from /etc/os-release | [optional] 
**os_build_id** | **datetime** | PrintNanny OS BUILD_ID from /etc/os-release | [optional] 
**os_variant_id** | **str** | PrintNanny OS VARIANT_ID from /etc/os-release | [optional] 
**os_release_json** | **dict(str, object)** | Full contents of /etc/os-release in key:value format | [optional] 
**pi** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


