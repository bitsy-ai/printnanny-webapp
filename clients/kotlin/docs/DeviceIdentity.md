
# DeviceIdentity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **kotlin.String** |  | 
**osVersion** | **kotlin.String** |  | 
**os** | **kotlin.String** |  | 
**kernelVersion** | **kotlin.String** |  | 
**cores** | **kotlin.Int** |  | 
**ram** | **kotlin.Long** |  | 
**cpuFlags** | **kotlin.collections.List&lt;kotlin.String&gt;** |  | 
**id** | **kotlin.Int** |  |  [optional] [readonly]
**deleted** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] [readonly]
**createdDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] [readonly]
**updatedDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] [readonly]
**user** | **kotlin.Int** |  |  [optional] [readonly]
**publicKey** | **kotlin.String** |  |  [optional] [readonly]
**fingerprint** | **kotlin.String** |  |  [optional] [readonly]
**cloudiotDevice** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional] [readonly]
**cloudiotDeviceName** | **kotlin.String** |  |  [optional] [readonly]
**cloudiotDevicePath** | **kotlin.String** |  |  [optional] [readonly]
**cloudiotDeviceNumId** | **kotlin.Int** |  |  [optional] [readonly]
**hardware** | **kotlin.String** |  |  [optional]
**revision** | **kotlin.String** |  |  [optional]
**model** | **kotlin.String** |  |  [optional]
**serial** | **kotlin.String** |  |  [optional]
**url** | [**java.net.URI**](java.net.URI.md) |  |  [optional] [readonly]
**privateKey** | **kotlin.String** |  |  [optional] [readonly]
**privateKeyChecksum** | **kotlin.String** |  |  [optional] [readonly]
**publicKeyChecksum** | **kotlin.String** |  |  [optional] [readonly]
**cloudiotDeviceConfigs** | **kotlin.String** |  |  [optional] [readonly]
**caCerts** | [**DeviceIdentityCaCerts**](DeviceIdentityCaCerts.md) |  |  [optional]
**manageUrl** | [**java.net.URI**](java.net.URI.md) |  |  [optional] [readonly]



