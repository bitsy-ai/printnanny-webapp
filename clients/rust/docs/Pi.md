# Pi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**last_boot** | Option<**String**> |  | [readonly]
**settings** | Option<[**crate::models::PiSettings**](PiSettings.md)> |  | [readonly]
**user** | Option<[**crate::models::User**](User.md)> |  | [readonly]
**system_info** | Option<[**crate::models::SystemInfo**](SystemInfo.md)> |  | [readonly]
**webrtc_edge** | Option<[**crate::models::WebrtcStream**](WebrtcStream.md)> |  | [readonly]
**webrtc_cloud** | Option<[**crate::models::WebrtcStream**](WebrtcStream.md)> |  | [readonly]
**octoprint_server** | Option<[**crate::models::OctoPrintServer**](OctoPrintServer.md)> |  | [readonly]
**urls** | [**crate::models::PiUrls**](Pi_urls.md) |  | 
**nats_app** | Option<[**crate::models::PiNatsApp**](PiNatsApp.md)> |  | [readonly]
**sbc** | Option<[**crate::models::SbcEnum**](SbcEnum.md)> |  | [optional]
**created_dt** | **String** |  | [readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]
**fqdn** | Option<**String**> |  | [optional]
**favorite** | Option<**bool**> |  | [optional]
**setup_finished** | Option<**bool**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


