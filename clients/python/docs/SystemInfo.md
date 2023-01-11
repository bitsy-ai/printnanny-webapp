# SystemInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**bootfs_available** | **int** |  | [readonly] 
**bootfs_available_pretty** | **str** |  | [readonly] 
**bootfs_used_pretty** | **str** |  | [readonly] 
**bootfs_size_pretty** | **str** |  | [readonly] 
**datafs_available** | **int** |  | [readonly] 
**datafs_available_pretty** | **str** |  | [readonly] 
**datafs_used_pretty** | **str** |  | [readonly] 
**datafs_size_pretty** | **str** |  | [readonly] 
**rootfs_available** | **int** |  | [readonly] 
**rootfs_available_pretty** | **str** |  | [readonly] 
**rootfs_size_pretty** | **str** |  | [readonly] 
**rootfs_used_pretty** | **str** |  | [readonly] 
**created_dt** | **datetime** |  | [readonly] 
**updated_dt** | **datetime** |  | [readonly] 
**machine_id** | **str** | Populated from /etc/machine-id | 
**revision** | **str** | Populated from /proc/cpuinfo REVISION | 
**model** | **str** | Populated from /proc/cpuinfo MODEL | 
**serial** | **str** | Populated from /proc/cpuinfo SERIAL | 
**cores** | **int** |  | 
**ram** | **int** |  | 
**os_version_id** | **str** | PrintNanny OS VERSION_ID from /etc/os-release | [optional] 
**os_build_id** | **str** | PrintNanny OS BUILD_ID from /etc/os-release | [optional] 
**os_release_json** | **dict(str, object)** | Full contents of /etc/os-release in key:value format | [optional] 
**uptime** | **int** | system uptime (in seconds) | 
**rootfs_size** | **int** | Size of /dev/root filesystem in bytes | 
**rootfs_used** | **int** | Space used in /dev/root filesystem in bytes | 
**bootfs_size** | **int** | Size of /dev/mmcblk0p1 filesystem in bytes | 
**bootfs_used** | **int** | Space used in /dev/mmcblk0p1 filesystem in bytes | 
**datafs_size** | **int** | Size of /dev/mmcblk0p4 filesystem in bytes | 
**datafs_used** | **int** | Space used in /dev/mmcblk0p4 filesystem in bytes | 
**pi** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


