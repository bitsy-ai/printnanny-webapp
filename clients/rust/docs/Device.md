# Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**bootstrap_release** | Option<[**crate::models::Release**](Release.md)> |  | [readonly]
**cloudiot_device** | Option<[**crate::models::CloudiotDevice**](CloudiotDevice.md)> |  | [readonly]
**cameras** | [**Vec<crate::models::Camera>**](Camera.md) |  | [readonly]
**dashboard_url** | **String** |  | [readonly]
**printer_controllers** | [**Vec<crate::models::PrinterController>**](PrinterController.md) |  | [readonly]
**release_channel** | Option<[**crate::models::ReleaseChannelEnum**](ReleaseChannelEnum.md)> |  | [optional]
**user** | Option<[**crate::models::User**](User.md)> |  | [readonly]
**last_task** | Option<[**crate::models::Task**](Task.md)> |  | [readonly]
**active_tasks** | [**Vec<crate::models::Task>**](Task.md) |  | [readonly]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


