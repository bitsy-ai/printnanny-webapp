
# PatchedDeviceInfoRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machineId** | **kotlin.String** | Populated from /etc/machine-id |  [optional]
**hardware** | **kotlin.String** | Populated from /proc/cpuinfo HARDWARE |  [optional]
**revision** | **kotlin.String** | Populated from /proc/cpuinfo REVISION |  [optional]
**model** | **kotlin.String** | Populated from /proc/cpuinfo MODEL |  [optional]
**serial** | **kotlin.String** | Populated from /proc/cpuinfo SERIAL |  [optional]
**cores** | **kotlin.Int** |  |  [optional]
**ram** | **kotlin.Long** |  |  [optional]
**imageVersion** | **kotlin.String** | Print Nanny OS version string from /boot/image_version.txt |  [optional]
**device** | **kotlin.Int** |  |  [optional]



