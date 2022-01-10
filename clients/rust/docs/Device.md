# Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**cloudiot_device** | Option<[**crate::models::CloudiotDevice**](CloudiotDevice.md)> |  | [readonly]
**cameras** | [**Vec<crate::models::Camera>**](Camera.md) |  | [readonly]
**janus_local_url** | **String** |  | [readonly]
**dashboard_url** | **String** |  | [readonly]
**printer_controllers** | [**Vec<crate::models::PrinterController>**](PrinterController.md) |  | [readonly]
**release_channel** | Option<[**crate::models::ReleaseChannelEnum**](ReleaseChannelEnum.md)> |  | [optional]
**monitoring_active** | Option<**bool**> |  | [optional][default to false]
**user** | Option<[**crate::models::User**](User.md)> |  | [readonly]
**last_task** | Option<[**crate::models::Task**](Task.md)> |  | [readonly]
**active_tasks** | [**Vec<crate::models::Task>**](Task.md) |  | [readonly]
**active_cameras** | [**Vec<crate::models::Camera>**](Camera.md) |  | [readonly]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


