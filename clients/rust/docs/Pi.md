# Pi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**last_boot** | **String** |  | [readonly]
**alert_settings** | Option<[**crate::models::AlertSettings**](AlertSettings.md)> |  | [readonly]
**settings** | Option<[**crate::models::PiSettings**](PiSettings.md)> |  | [readonly]
**cloudiot_device** | Option<[**crate::models::CloudiotDevice**](CloudiotDevice.md)> |  | [readonly]
**user** | Option<[**crate::models::User**](User.md)> |  | [readonly]
**system_info** | Option<[**crate::models::SystemInfo**](SystemInfo.md)> |  | [readonly]
**public_key** | Option<[**crate::models::PublicKey**](PublicKey.md)> |  | [readonly]
**webrtc_edge** | Option<[**crate::models::WebrtcStream**](WebrtcStream.md)> |  | [readonly]
**webrtc_cloud** | Option<[**crate::models::WebrtcStream**](WebrtcStream.md)> |  | [readonly]
**octoprint_server** | Option<[**crate::models::OctoPrintServer**](OctoPrintServer.md)> |  | [readonly]
**urls** | [**crate::models::PiUrls**](Pi_urls.md) |  | 
**created_dt** | **String** |  | [readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]
**fqdn** | Option<**String**> |  | [optional]
**favorite** | Option<**bool**> |  | [optional]
**ws_connected** | Option<**bool**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

