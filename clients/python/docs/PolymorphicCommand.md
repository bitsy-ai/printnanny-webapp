# PolymorphicCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**model** | [**WebRTCCommandModel**](WebRTCCommandModel.md) |  | 
**created_dt** | **datetime** |  | [readonly] 
**source** | [**EventSource**](EventSource.md) |  | 
**send_ws** | **bool** | Broadcast to events websocket: /ws/events | [optional] 
**event_name** | [**WebRTCCommandName**](WebRTCCommandName.md) |  | 
**data** | **dict(str, object)** |  | [optional] 
**polymorphic_ctype** | **int** |  | [readonly] 
**user** | **int** |  | [readonly] 
**device** | **int** |  | 
**stream** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

