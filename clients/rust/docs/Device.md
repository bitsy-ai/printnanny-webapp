# Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | Option<**i32**> |  | [optional][readonly]
**cloudiot_device** | Option<[**crate::models::CloudiotDevice**](CloudiotDevice.md)> |  | [optional][readonly]
**cameras** | Option<[**Vec<crate::models::Camera>**](Camera.md)> |  | [optional][readonly]
**dashboard_url** | Option<**String**> |  | [optional][readonly]
**bootstrap_release** | Option<[**crate::models::Release**](Release.md)> |  | [optional][readonly]
**printer_controllers** | Option<[**Vec<crate::models::PrinterController>**](PrinterController.md)> |  | [optional][readonly]
**release_channel** | Option<[**crate::models::ReleaseChannelEnum**](ReleaseChannelEnum.md)> |  | [optional]
**user** | Option<[**crate::models::User**](User.md)> |  | [optional][readonly]
**license** | Option<[**crate::models::License**](License.md)> |  | [optional][readonly]
**deleted** | Option<**String**> |  | [optional][readonly]
**created_dt** | Option<**String**> |  | [optional][readonly]
**updated_dt** | Option<**String**> |  | [optional][readonly]
**hostname** | Option<**String**> | Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


