
# TelemetryEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventType** | [**TelemetryEventEventTypeEnum**](TelemetryEventEventTypeEnum.md) |  | 
**environment** | [**OctoprintEnvironment**](OctoprintEnvironment.md) |  | 
**printerData** | [**OctoprintPrinterData**](OctoprintPrinterData.md) |  | 
**temperature** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  | 
**printNannyPluginVersion** | **kotlin.String** |  | 
**printNannyClientVersion** | **kotlin.String** |  | 
**octoprintVersion** | **kotlin.String** |  | 
**octoprintDevice** | **kotlin.Int** |  | 
**id** | **kotlin.Int** |  |  [optional] [readonly]
**printSession** | **kotlin.String** |  |  [optional] [readonly]
**createdDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] [readonly]
**eventSource** | [**EventSourceEnum**](EventSourceEnum.md) |  |  [optional]
**eventData** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**metadata** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**octoprintJob** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**polymorphicCtype** | **kotlin.Int** |  |  [optional] [readonly]
**user** | **kotlin.Int** |  |  [optional] [readonly]



