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
**os_build_id** | **str** | PrintNanny OS BUILD_ID from /etc/os-release | [optional] 
**os_release_json** | **dict(str, object)** | Full contents of /etc/os-release in key:value format | [optional] 
**uptime** | **int** | system uptime (in seconds) | [optional] 
**rootfs_size** | **int** | Size of /dev/root filesystem in bytes | [optional] 
**rootfs_used** | **int** | Space used in /dev/root filesystem in bytes | [optional] 
**bootfs_size** | **int** | Size of /dev/mmcblk0p1 filesystem in bytes | [optional] 
**bootfs_used** | **int** | Space used in /dev/mmcblk0p1 filesystem in bytes | [optional] 
**datafs_size** | **int** | Size of /dev/mmcblk0p4 filesystem in bytes | [optional] 
**datafs_used** | **int** | Space used in /dev/mmcblk0p4 filesystem in bytes | [optional] 
**pi** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


