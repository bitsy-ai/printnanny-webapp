# Device


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**cloudiot_device** | [**CloudiotDevice**](CloudiotDevice.md) |  | [readonly] 
**cloud_url** | **str** |  | [readonly] 
**edge_url** | **str** |  | [readonly] 
**video_test_url** | **str** |  | [readonly] 
**janus_auth** | [**JanusAuth**](JanusAuth.md) |  | [readonly] 
**janus_local_url** | **str** |  | [readonly] 
**monitoring_active** | **bool** |  | [optional] [default to False]
**setup_complete** | **bool** |  | [optional] [default to False]
**user** | [**User**](User.md) |  | [readonly] 
**octoprint_url** | **str** |  | [readonly] 
**release_channel** | [**DeviceReleaseChannel**](DeviceReleaseChannel.md) |  | [optional] 
**system_info** | [**SystemInfo**](SystemInfo.md) |  | [readonly] 
**public_key** | [**PublicKey**](PublicKey.md) |  | [readonly] 
**created_dt** | **datetime** |  | [readonly] 
**updated_dt** | **datetime** |  | [readonly] 
**hostname** | **str** | Please enter the hostname you set in the Raspberry Pi Imager&#39;s Advanced Options menu (without .local extension) | [optional] 
**edition** | [**OsEdition**](OsEdition.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


