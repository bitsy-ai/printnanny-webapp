# DeviceInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | Option<**i32**> |  | [optional][readonly]
**deleted** | Option<**String**> |  | [optional][readonly]
**machine_id** | **String** | Populated from /etc/machine-id | 
**hardware** | **String** | Populated from /proc/cpuinfo HARDWARE | 
**revision** | **String** | Populated from /proc/cpuinfo REVISION | 
**model** | **String** | Populated from /proc/cpuinfo MODEL | 
**serial** | **String** | Populated from /proc/cpuinfo SERIAL | 
**cores** | **i32** |  | 
**ram** | **i64** |  | 
**image_version** | **String** | Print Nanny OS version string from /boot/image_version.txt | 
**device** | **i32** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


