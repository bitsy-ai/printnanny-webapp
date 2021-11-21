
# DeviceState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **kotlin.Int** |  |  [readonly]
**deleted** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**createdDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**device** | **kotlin.Int** |  | 
**status** | [**StatusEnum**](StatusEnum.md) |  |  [optional]
**command** | [**DeviceStateCommandEnum**](DeviceStateCommandEnum.md) |  |  [optional]
**ansibleFacts** | [**kotlin.collections.Map&lt;kotlin.String, kotlin.Any&gt;**](kotlin.Any.md) |  |  [optional]
**ansibleExtraVars** | [**kotlin.collections.Map&lt;kotlin.String, kotlin.Any&gt;**](kotlin.Any.md) |  |  [optional]



