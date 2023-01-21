# \VideosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_recordings_create**](VideosApi.md#video_recordings_create) | **POST** /api/video-recordings/ | 
[**video_recordings_list**](VideosApi.md#video_recordings_list) | **GET** /api/video-recordings/ | 
[**video_recordings_partial_update**](VideosApi.md#video_recordings_partial_update) | **PATCH** /api/video-recordings/{id}/ | 
[**video_recordings_retrieve**](VideosApi.md#video_recordings_retrieve) | **GET** /api/video-recordings/{id}/ | 
[**video_recordings_update**](VideosApi.md#video_recordings_update) | **PUT** /api/video-recordings/{id}/ | 
[**video_recordings_update_or_create**](VideosApi.md#video_recordings_update_or_create) | **POST** /api/video-recordings/update-or-create/ | 



## video_recordings_create

> crate::models::VideoRecording video_recordings_create(id, recording_start, recording_end, recording_status, cloud_sync_start, cloud_sync_end, cloud_sync_status, gcode_file_name, mp4_file)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | Option<**String**> |  |  |
**recording_start** | Option<**String**> |  |  |
**recording_end** | Option<**String**> |  |  |
**recording_status** | Option<[**crate::models::RecordingStatusEnum**](RecordingStatusEnum.md)> |  |  |
**cloud_sync_start** | Option<**String**> |  |  |
**cloud_sync_end** | Option<**String**> |  |  |
**cloud_sync_status** | Option<[**crate::models::CloudSyncStatusEnum**](CloudSyncStatusEnum.md)> |  |  |
**gcode_file_name** | Option<**String**> |  |  |
**mp4_file** | Option<**std::path::PathBuf**> |  |  |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_recordings_list

> crate::models::PaginatedVideoRecordingList video_recordings_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedVideoRecordingList**](PaginatedVideoRecordingList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_recordings_partial_update

> crate::models::VideoRecording video_recordings_partial_update(id, id2, recording_start, recording_end, recording_status, cloud_sync_start, cloud_sync_end, cloud_sync_status, gcode_file_name, mp4_file)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this video recording. | [required] |
**id2** | Option<**String**> |  |  |
**recording_start** | Option<**String**> |  |  |
**recording_end** | Option<**String**> |  |  |
**recording_status** | Option<[**crate::models::RecordingStatusEnum**](RecordingStatusEnum.md)> |  |  |
**cloud_sync_start** | Option<**String**> |  |  |
**cloud_sync_end** | Option<**String**> |  |  |
**cloud_sync_status** | Option<[**crate::models::CloudSyncStatusEnum**](CloudSyncStatusEnum.md)> |  |  |
**gcode_file_name** | Option<**String**> |  |  |
**mp4_file** | Option<**std::path::PathBuf**> |  |  |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_recordings_retrieve

> crate::models::VideoRecording video_recordings_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this video recording. | [required] |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_recordings_update

> crate::models::VideoRecording video_recordings_update(id, id2, recording_start, recording_end, recording_status, cloud_sync_start, cloud_sync_end, cloud_sync_status, gcode_file_name, mp4_file)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this video recording. | [required] |
**id2** | Option<**String**> |  |  |
**recording_start** | Option<**String**> |  |  |
**recording_end** | Option<**String**> |  |  |
**recording_status** | Option<[**crate::models::RecordingStatusEnum**](RecordingStatusEnum.md)> |  |  |
**cloud_sync_start** | Option<**String**> |  |  |
**cloud_sync_end** | Option<**String**> |  |  |
**cloud_sync_status** | Option<[**crate::models::CloudSyncStatusEnum**](CloudSyncStatusEnum.md)> |  |  |
**gcode_file_name** | Option<**String**> |  |  |
**mp4_file** | Option<**std::path::PathBuf**> |  |  |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_recordings_update_or_create

> crate::models::VideoRecording video_recordings_update_or_create(id, recording_start, recording_end, recording_status, cloud_sync_start, cloud_sync_end, cloud_sync_status, gcode_file_name, mp4_file)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | Option<**String**> |  |  |
**recording_start** | Option<**String**> |  |  |
**recording_end** | Option<**String**> |  |  |
**recording_status** | Option<[**crate::models::RecordingStatusEnum**](RecordingStatusEnum.md)> |  |  |
**cloud_sync_start** | Option<**String**> |  |  |
**cloud_sync_end** | Option<**String**> |  |  |
**cloud_sync_status** | Option<[**crate::models::CloudSyncStatusEnum**](CloudSyncStatusEnum.md)> |  |  |
**gcode_file_name** | Option<**String**> |  |  |
**mp4_file** | Option<**std::path::PathBuf**> |  |  |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

