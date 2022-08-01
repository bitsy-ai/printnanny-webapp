# Pi


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**last_boot** | **str** |  | [readonly] 
**settings** | [**PiSettings**](PiSettings.md) |  | [readonly] 
**cloudiot_device** | [**CloudiotDevice**](CloudiotDevice.md) |  | [readonly] 
**user** | [**User**](User.md) |  | [readonly] 
**system_info** | [**SystemInfo**](SystemInfo.md) |  | [readonly] 
**public_key** | [**PublicKey**](PublicKey.md) |  | [readonly] 
**webrtc_edge** | [**WebrtcStream**](WebrtcStream.md) |  | [readonly] 
**webrtc_cloud** | [**WebrtcStream**](WebrtcStream.md) |  | [readonly] 
**octoprint_server** | [**OctoPrintServer**](OctoPrintServer.md) |  | [readonly] 
**urls** | [**PiUrls**](PiUrls.md) |  | 
**sbc** | [**SbcEnum**](SbcEnum.md) |  | [optional] 
**edition** | [**OsEdition**](OsEdition.md) |  | [optional] 
**created_dt** | **datetime** |  | [readonly] 
**hostname** | **str** | Please enter the hostname you set in the Raspberry Pi Imager&#39;s Advanced Options menu (without .local extension) | [optional] 
**fqdn** | **str** |  | [optional] 
**favorite** | **bool** |  | [optional] 
**setup_finished** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


