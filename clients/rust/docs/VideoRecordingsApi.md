# \VideoRecordingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_recordings_retrieve**](VideoRecordingsApi.md#video_recordings_retrieve) | **GET** /api/video-recordings/{id}/ | 



## video_recordings_retrieve

> crate::models::VideoRecording video_recordings_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this video recording. | [required] |

### Return type

[**crate::models::VideoRecording**](VideoRecording.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

