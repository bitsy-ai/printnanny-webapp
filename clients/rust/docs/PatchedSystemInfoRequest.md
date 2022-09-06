# PatchedSystemInfoRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | Option<**String**> | Populated from /etc/machine-id | [optional]
**revision** | Option<**String**> | Populated from /proc/cpuinfo REVISION | [optional]
**model** | Option<**String**> | Populated from /proc/cpuinfo MODEL | [optional]
**serial** | Option<**String**> | Populated from /proc/cpuinfo SERIAL | [optional]
**cores** | Option<**i32**> |  | [optional]
**ram** | Option<**i64**> |  | [optional]
**os_version_id** | Option<**String**> | PrintNanny OS VERSION_ID from /etc/os-release | [optional]
**os_build_id** | Option<**String**> | PrintNanny OS BUILD_ID from /etc/os-release | [optional]
**os_variant_id** | Option<**String**> | PrintNanny OS VARIANT_ID from /etc/os-release | [optional]
**os_release_json** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> | Full contents of /etc/os-release in key:value format | [optional]
**uptime** | Option<**i64**> | system uptime (in seconds) | [optional]
**rootfs_size** | Option<**i64**> | Size of /dev/root filesystem in bytes | [optional]
**rootfs_used** | Option<**i64**> | Space used in /dev/root filesystem in bytes | [optional]
**bootfs_size** | Option<**i64**> | Size of /dev/mmcblk0p1 filesystem in bytes | [optional]
**bootfs_used** | Option<**i64**> | Space used in /dev/mmcblk0p1 filesystem in bytes | [optional]
**datafs_size** | Option<**i64**> | Size of /dev/mmcblk0p4 filesystem in bytes | [optional]
**datafs_used** | Option<**i64**> | Space used in /dev/mmcblk0p4 filesystem in bytes | [optional]
**pi** | Option<**i32**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


