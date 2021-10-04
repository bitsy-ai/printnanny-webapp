
# PrintSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **kotlin.Int** |  |  [readonly]
**createdDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  | 
**updatedDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [readonly]
**octoprintDevice** | **kotlin.Int** |  | 
**session** | **kotlin.String** |  | 
**user** | **kotlin.Int** |  |  [readonly]
**url** | [**java.net.URI**](java.net.URI.md) |  |  [readonly]
**datesegment** | **kotlin.String** |  |  [readonly]
**active** | **kotlin.Boolean** |  |  [optional]
**filepos** | **kotlin.Int** |  |  [optional]
**printProgress** | **kotlin.Int** |  |  [optional]
**timeElapsed** | **kotlin.Int** |  |  [optional]
**timeRemaining** | **kotlin.Int** |  |  [optional]
**printerProfile** | **kotlin.Int** |  |  [optional]
**gcodeFile** | **kotlin.Int** |  |  [optional]
**gcodeFilename** | **kotlin.String** |  |  [optional]
**octoprintJob** | [**kotlin.collections.Map&lt;kotlin.String, kotlin.Any&gt;**](kotlin.Any.md) |  |  [optional]
**printJobStatus** | [**PrintJobStatusEnum**](PrintJobStatusEnum.md) |  |  [optional]



