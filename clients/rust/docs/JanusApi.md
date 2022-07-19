# \JanusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_webrtc_streams_create**](JanusApi.md#devices_webrtc_streams_create) | **POST** /api/devices/{device_id}/webrtc-streams/ | 
[**devices_webrtc_streams_list**](JanusApi.md#devices_webrtc_streams_list) | **GET** /api/devices/{device_id}/webrtc-streams/ | 
[**devices_webrtc_streams_retrieve**](JanusApi.md#devices_webrtc_streams_retrieve) | **GET** /api/devices/{device_id}/webrtc-streams/{id}/ | 



## devices_webrtc_streams_create

> crate::models::WebrtcStream devices_webrtc_streams_create(device_id, webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**webrtc_stream_request** | Option<[**WebrtcStreamRequest**](WebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_webrtc_streams_list

> crate::models::PaginatedWebrtcStreamList devices_webrtc_streams_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedWebrtcStreamList**](PaginatedWebrtcStreamList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_webrtc_streams_retrieve

> crate::models::WebrtcStream devices_webrtc_streams_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

