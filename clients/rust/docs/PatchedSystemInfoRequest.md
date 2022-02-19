# PatchedSystemInfoRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | Option<**String**> | Populated from /etc/machine-id | [optional]
**hardware** | Option<**String**> | Populated from /proc/cpuinfo HARDWARE | [optional]
**revision** | Option<**String**> | Populated from /proc/cpuinfo REVISION | [optional]
**model** | Option<**String**> | Populated from /proc/cpuinfo MODEL | [optional]
**serial** | Option<**String**> | Populated from /proc/cpuinfo SERIAL | [optional]
**cores** | Option<**i32**> |  | [optional]
**ram** | Option<**i64**> |  | [optional]
**image_version** | Option<**String**> | Print Nanny OS version string from /boot/image_version.txt | [optional]
**device** | Option<**i32**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


