# OctoprintPrinterDataRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**crate::models::OctoprintJobRequest**](OctoprintJobRequest.md) |  | 
**state** | [**crate::models::OctoprintPrinterStateRequest**](OctoprintPrinterStateRequest.md) |  | 
**user** | Option<**String**> |  | [optional]
**current_z** | Option<**f32**> |  | [optional]
**progress** | [**crate::models::OctoprintProgressRequest**](OctoprintProgressRequest.md) |  | 
**resends** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) |  | 
**offsets** | [**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


