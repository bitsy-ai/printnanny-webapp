# Pi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**last_boot** | Option<**String**> |  | [readonly]
**network_settings** | Option<[**crate::models::NetworkSettings**](NetworkSettings.md)> |  | [readonly]
**user** | Option<[**crate::models::User**](User.md)> |  | [readonly]
**system_info** | Option<[**crate::models::SystemInfo**](SystemInfo.md)> |  | [readonly]
**webrtc_edge** | Option<[**crate::models::WebrtcStream**](WebrtcStream.md)> |  | [readonly]
**webrtc_cloud** | Option<[**crate::models::WebrtcStream**](WebrtcStream.md)> |  | [readonly]
**octoprint_server** | Option<[**crate::models::OctoPrintServer**](OctoPrintServer.md)> |  | [readonly]
**nats_app** | Option<[**crate::models::PiNatsApp**](PiNatsApp.md)> |  | [readonly]
**urls** | [**crate::models::PiUrls**](Pi_urls.md) |  | 
**shortname_urls** | [**crate::models::PiUrls**](Pi_urls.md) |  | 
**mdns_urls** | [**crate::models::PiUrls**](Pi_urls.md) |  | 
**sbc** | Option<[**crate::models::SbcEnum**](SbcEnum.md)> |  | [optional]
**created_dt** | **String** |  | [readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]
**favorite** | Option<**bool**> |  | [optional]
**setup_finished** | Option<**bool**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


