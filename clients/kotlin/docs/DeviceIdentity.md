
# DeviceIdentity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **kotlin.Int** |  |  [readonly]
**deleted** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**createdDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**updatedDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**user** | **kotlin.Int** |  |  [readonly]
**name** | **kotlin.String** |  | 
**publicKey** | **kotlin.String** |  |  [readonly]
**fingerprint** | **kotlin.String** |  |  [readonly]
**cloudiotDevice** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [readonly]
**cloudiotDeviceName** | **kotlin.String** |  |  [readonly]
**cloudiotDevicePath** | **kotlin.String** |  |  [readonly]
**cloudiotDeviceNumId** | **kotlin.Int** |  |  [readonly]
**osVersion** | **kotlin.String** |  | 
**os** | **kotlin.String** |  | 
**kernelVersion** | **kotlin.String** |  | 
**cores** | **kotlin.Int** |  | 
**ram** | **kotlin.Long** |  | 
**cpuFlags** | **kotlin.collections.List&lt;kotlin.String&gt;** |  | 
**url** | [**java.net.URI**](java.net.URI.md) |  |  [readonly]
**privateKey** | **kotlin.String** |  |  [readonly]
**privateKeyChecksum** | **kotlin.String** |  |  [readonly]
**publicKeyChecksum** | **kotlin.String** |  |  [readonly]
**cloudiotDeviceConfigs** | **kotlin.String** |  |  [readonly]
**caCerts** | [**DeviceIdentityCaCerts**](DeviceIdentityCaCerts.md) |  | 
**hardware** | **kotlin.String** |  |  [optional]
**revision** | **kotlin.String** |  |  [optional]
**model** | **kotlin.String** |  |  [optional]
**serial** | **kotlin.String** |  |  [optional]



