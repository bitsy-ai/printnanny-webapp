
# DeviceInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **kotlin.Int** |  |  [readonly]
**deleted** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**machineId** | **kotlin.String** | Populated from /etc/machine-id | 
**hardware** | **kotlin.String** | Populated from /proc/cpuinfo HARDWARE | 
**revision** | **kotlin.String** | Populated from /proc/cpuinfo REVISION | 
**model** | **kotlin.String** | Populated from /proc/cpuinfo MODEL | 
**serial** | **kotlin.String** | Populated from /proc/cpuinfo SERIAL | 
**cores** | **kotlin.Int** |  | 
**ram** | **kotlin.Long** |  | 
**imageVersion** | **kotlin.String** | Print Nanny OS version string from /boot/image_version.txt | 
**device** | **kotlin.Int** |  | 



