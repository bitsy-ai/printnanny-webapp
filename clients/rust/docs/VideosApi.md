# \VideosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**videos_retrieve**](VideosApi.md#videos_retrieve) | **GET** /api/videos/{id}/ | 



## videos_retrieve

> crate::models::VideoRecording videos_retrieve(id)


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

