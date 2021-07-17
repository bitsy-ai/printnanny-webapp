
# DeviceIdentity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**updatedDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**user** | **kotlin.Int** |  | 
**name** | **kotlin.String** |  | 
**fingerprint** | **kotlin.String** |  | 
**cloudiotDeviceName** | **kotlin.String** |  | 
**cloudiotDeviceNumId** | **kotlin.Long** |  | 
**cloudiotDevicePath** | **kotlin.String** |  | 
**osVersion** | **kotlin.String** |  | 
**os** | **kotlin.String** |  | 
**kernelVersion** | **kotlin.String** |  | 
**cores** | **kotlin.Int** |  | 
**ram** | **kotlin.Long** |  | 
**cpuFlags** | **kotlin.collections.List&lt;kotlin.String&gt;** |  | 
**url** | [**java.net.URI**](java.net.URI.md) |  |  [readonly]
**privateKey** | **kotlin.String** |  |  [readonly]
**privateKeyChecksum** | **kotlin.String** |  |  [readonly]
**publicKey** | **kotlin.String** |  |  [readonly]
**publicKeyChecksum** | **kotlin.String** |  |  [readonly]
**caCerts** | [**DeviceIdentityCaCerts**](DeviceIdentityCaCerts.md) |  | 
**hardware** | **kotlin.String** |  |  [optional]
**revision** | **kotlin.String** |  |  [optional]
**model** | **kotlin.String** |  |  [optional]
**serial** | **kotlin.String** |  |  [optional]



