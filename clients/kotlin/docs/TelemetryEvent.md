
# TelemetryEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **kotlin.Int** |  |  [readonly]
**eventType** | [**TelemetryEventEventTypeEnum**](TelemetryEventEventTypeEnum.md) |  | 
**octoprintEnvironment** | [**OctoprintEnvironment**](OctoprintEnvironment.md) |  | 
**octoprintPrinterData** | [**OctoprintPrinterData**](OctoprintPrinterData.md) |  | 
**ts** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**eventSource** | [**EventSourceEnum**](EventSourceEnum.md) |  |  [readonly]
**printNannyPluginVersion** | **kotlin.String** |  | 
**printNannyClientVersion** | **kotlin.String** |  | 
**octoprintVersion** | **kotlin.String** |  | 
**polymorphicCtype** | **kotlin.Int** |  |  [readonly]
**octoprintDevice** | **kotlin.Int** |  | 
**user** | **kotlin.Int** |  |  [readonly]
**eventData** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**temperature** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**printSession** | **kotlin.Int** |  |  [optional]



