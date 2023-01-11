# SystemInfoRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **String** | Populated from /etc/machine-id | 
**revision** | **String** | Populated from /proc/cpuinfo REVISION | 
**model** | **String** | Populated from /proc/cpuinfo MODEL | 
**serial** | **String** | Populated from /proc/cpuinfo SERIAL | 
**cores** | **i32** |  | 
**ram** | **i64** |  | 
**os_version_id** | Option<**String**> | PrintNanny OS VERSION_ID from /etc/os-release | [optional]
**os_build_id** | Option<**String**> | PrintNanny OS BUILD_ID from /etc/os-release | [optional]
**os_release_json** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Full contents of /etc/os-release in key:value format | [optional]
**uptime** | **i64** | system uptime (in seconds) | 
**rootfs_size** | **i64** | Size of /dev/root filesystem in bytes | 
**rootfs_used** | **i64** | Space used in /dev/root filesystem in bytes | 
**bootfs_size** | **i64** | Size of /dev/mmcblk0p1 filesystem in bytes | 
**bootfs_used** | **i64** | Space used in /dev/mmcblk0p1 filesystem in bytes | 
**datafs_size** | **i64** | Size of /dev/mmcblk0p4 filesystem in bytes | 
**datafs_used** | **i64** | Space used in /dev/mmcblk0p4 filesystem in bytes | 
**pi** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


