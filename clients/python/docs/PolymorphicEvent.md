# PolymorphicEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**model** | [**TestEventModel**](TestEventModel.md) |  | 
**created_dt** | **datetime** |  | [readonly] 
**source** | [**EventSource**](EventSource.md) |  | 
**event_name** | [**TestEventName**](TestEventName.md) |  | 
**payload** | **dict(str, object)** |  | [optional] 
**polymorphic_ctype** | **int** |  | [readonly] 
**user** | **int** |  | [readonly] 
**octoprint_server** | **int** |  | 
**device** | **int** |  | 
**data** | **dict(str, object)** |  | [optional] 
**stream** | [**WebrtcStream**](WebrtcStream.md) |  | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


