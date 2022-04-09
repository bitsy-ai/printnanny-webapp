# Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**cloudiot_device** | Option<[**crate::models::CloudiotDevice**](CloudiotDevice.md)> |  | [readonly]
**cloud_url** | **String** |  | [readonly]
**edge_url** | **String** |  | [readonly]
**video_test_url** | **String** |  | [readonly]
**janus_auth** | Option<[**crate::models::JanusAuth**](JanusAuth.md)> |  | [readonly]
**janus_local_url** | **String** |  | [readonly]
**monitoring_active** | Option<**bool**> |  | [optional][default to false]
**setup_complete** | Option<**bool**> |  | [optional][default to false]
**user** | Option<[**crate::models::User**](User.md)> |  | [readonly]
**octoprint_url** | **String** |  | [readonly]
**release_channel** | Option<[**crate::models::DeviceReleaseChannel**](DeviceReleaseChannel.md)> |  | [optional]
**system_info** | Option<[**crate::models::SystemInfo**](SystemInfo.md)> |  | [readonly]
**public_key** | Option<[**crate::models::PublicKey**](PublicKey.md)> |  | [readonly]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


