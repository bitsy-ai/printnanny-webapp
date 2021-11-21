# Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **i32** |  | [readonly]
**cloudiot_device** | Option<[**crate::models::CloudiotDevice**](CloudiotDevice.md)> |  | [readonly]
**cameras** | [**Vec<crate::models::Camera>**](Camera.md) |  | [readonly][default to []]
**dashboard_url** | **String** |  | [readonly]
**bootstrap_release** | Option<[**crate::models::Release**](Release.md)> |  | [readonly]
**printer_controllers** | [**Vec<crate::models::PrinterController>**](PrinterController.md) |  | [readonly]
**release_channel** | Option<[**crate::models::ReleaseChannelEnum**](ReleaseChannelEnum.md)> |  | [optional]
**user** | Option<[**crate::models::User**](User.md)> |  | [readonly]
**active_license** | Option<[**crate::models::License**](License.md)> |  | [readonly]
**deleted** | **String** |  | [readonly]
**created_dt** | **String** |  | [readonly]
**updated_dt** | **String** |  | [readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


