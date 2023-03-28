# \VideosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_parts_create**](VideosApi.md#video_parts_create) | **POST** /api/video-parts/ | 
[**video_parts_list**](VideosApi.md#video_parts_list) | **GET** /api/video-parts/ | 
[**video_parts_retrieve**](VideosApi.md#video_parts_retrieve) | **GET** /api/video-parts/{id}/ | 
[**video_recordings_finalize**](VideosApi.md#video_recordings_finalize) | **POST** /api/videos/{id}/finalize/ | 
[**video_recordings_update_or_create**](VideosApi.md#video_recordings_update_or_create) | **POST** /api/videos/{id}/update-or-create/ | 
[**videos_create**](VideosApi.md#videos_create) | **POST** /api/videos/ | 
[**videos_list**](VideosApi.md#videos_list) | **GET** /api/videos/ | 
[**videos_partial_update**](VideosApi.md#videos_partial_update) | **PATCH** /api/videos/{id}/ | 
[**videos_retrieve**](VideosApi.md#videos_retrieve) | **GET** /api/videos/{id}/ | 
[**videos_update**](VideosApi.md#videos_update) | **PUT** /api/videos/{id}/ | 



## video_parts_create

> crate::models::VideoRecordingPart video_parts_create(id, size, buffer_index, buffer_runningtime, file_name, mp4_file, sync_start, video_recording)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** |  | [required] |
**size** | **i64** |  | [required] |
**buffer_index** | **i64** |  | [required] |
**buffer_runningtime** | **i64** |  | [required] |
**file_name** | **String** |  | [required] |
**mp4_file** | **std::path::PathBuf** |  | [required] |
**sync_start** | **String** |  | [required] |
**video_recording** | **String** |  | [required] |

### Return type

[**crate::models::VideoRecordingPart**](VideoRecordingPart.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_parts_list

> crate::models::PaginatedVideoRecordingPartList video_parts_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedVideoRecordingPartList**](PaginatedVideoRecordingPartList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_parts_retrieve

> crate::models::VideoRecordingPart video_parts_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A unique value identifying this video recording part. | [required] |

### Return type

[**crate::models::VideoRecordingPart**](VideoRecordingPart.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_recordings_finalize

> crate::models::VideoRecording video_recordings_finalize(id, video_recording_finalize_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this video recording. | [required] |
**video_recording_finalize_request** | [**VideoRecordingFinalizeRequest**](VideoRecordingFinalizeRequest.md) |  | [required] |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## video_recordings_update_or_create

> crate::models::VideoRecording video_recordings_update_or_create(id, video_recording_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this video recording. | [required] |
**video_recording_request** | Option<[**VideoRecordingRequest**](VideoRecordingRequest.md)> |  |  |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## videos_create

> crate::models::VideoRecording videos_create(video_recording_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**video_recording_request** | Option<[**VideoRecordingRequest**](VideoRecordingRequest.md)> |  |  |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## videos_list

> crate::models::PaginatedVideoRecordingList videos_list(page)


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


## videos_partial_update

> crate::models::VideoRecording videos_partial_update(id, patched_video_recording_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this video recording. | [required] |
**patched_video_recording_request** | Option<[**PatchedVideoRecordingRequest**](PatchedVideoRecordingRequest.md)> |  |  |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## videos_retrieve

> crate::models::VideoRecording videos_retrieve(id)


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


## videos_update

> crate::models::VideoRecording videos_update(id, video_recording_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this video recording. | [required] |
**video_recording_request** | Option<[**VideoRecordingRequest**](VideoRecordingRequest.md)> |  |  |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

