# SystemInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **str** | Populated from /etc/machine-id | 
**revision** | **str** | Populated from /proc/cpuinfo REVISION | 
**model** | **str** | Populated from /proc/cpuinfo MODEL | 
**serial** | **str** | Populated from /proc/cpuinfo SERIAL | 
**cores** | **int** |  | 
**ram** | **int** |  | 
**os_version_id** | **str** | PrintNanny OS VERSION_ID from /etc/os-release | 
**os_build_id** | **datetime** | PrintNanny OS BUILD_ID from /etc/os-release | 
**os_variant_id** | **str** | PrintNanny OS VARIANT_ID from /etc/os-release | 
**os_release_json** | **dict(str, object)** | Full contents of /etc/os-release in key:value format | [optional] 
**pi** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


