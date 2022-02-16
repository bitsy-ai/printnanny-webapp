# Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**active_cameras** | [**Vec<crate::models::Camera>**](Camera.md) |  | [readonly]
**active_tasks** | [**Vec<crate::models::Task>**](Task.md) |  | [readonly]
**cameras** | [**Vec<crate::models::Camera>**](Camera.md) |  | [readonly]
**cloudiot_device** | Option<[**crate::models::CloudiotDevice**](CloudiotDevice.md)> |  | [readonly]
**dashboard_url** | **String** |  | [readonly]
**video_test_url** | **String** |  | [readonly]
**janus_auth** | Option<[**crate::models::JanusCloudAuth**](JanusCloudAuth.md)> |  | [readonly]
**janus_local_url** | **String** |  | [readonly]
**last_task** | Option<[**crate::models::Task**](Task.md)> |  | [readonly]
**monitoring_active** | Option<**bool**> |  | [optional][default to false]
**setup_complete** | Option<**bool**> |  | [optional][default to false]
**printer_controllers** | [**Vec<crate::models::PrinterController>**](PrinterController.md) |  | [readonly]
**user** | Option<[**crate::models::User**](User.md)> |  | [readonly]
**release_channel** | Option<[**crate::models::ReleaseChannelEnum**](ReleaseChannelEnum.md)> |  | [optional]
**system_info** | Option<[**crate::models::SystemInfo**](SystemInfo.md)> |  | [readonly]
**public_key** | Option<[**crate::models::PublicKey**](PublicKey.md)> |  | [readonly]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


