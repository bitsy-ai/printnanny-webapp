# Device


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**cloudiot_device** | [**CloudiotDevice**](CloudiotDevice.md) |  | [readonly] 
**cameras** | [**list[Camera]**](Camera.md) |  | [readonly] 
**janus_local_url** | **str** |  | [readonly] 
**dashboard_url** | **str** |  | [readonly] 
**printer_controllers** | [**list[PrinterController]**](PrinterController.md) |  | [readonly] 
**release_channel** | [**ReleaseChannelEnum**](ReleaseChannelEnum.md) |  | [optional] 
**monitoring_active** | **bool** |  | [optional] [default to False]
**user** | [**User**](User.md) |  | [readonly] 
**last_task** | [**Task**](Task.md) |  | [readonly] 
**active_tasks** | [**list[Task]**](Task.md) |  | [readonly] 
**active_cameras** | [**list[Camera]**](Camera.md) |  | [readonly] 
**created_dt** | **datetime** |  | [readonly] 
**updated_dt** | **datetime** |  | [readonly] 
**hostname** | **str** | Please enter the hostname you set in the Raspberry Pi Imager&#39;s Advanced Options menu (without .local extension) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


