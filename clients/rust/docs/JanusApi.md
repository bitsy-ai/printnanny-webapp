# \JanusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pis_webrtc_streams_create**](JanusApi.md#pis_webrtc_streams_create) | **POST** /api/pis/{pi_id}/webrtc-streams/ | 
[**pis_webrtc_streams_list**](JanusApi.md#pis_webrtc_streams_list) | **GET** /api/pis/{pi_id}/webrtc-streams/ | 
[**pis_webrtc_streams_partial_update**](JanusApi.md#pis_webrtc_streams_partial_update) | **PATCH** /api/pis/{pi_id}/webrtc-streams/{id}/ | 
[**pis_webrtc_streams_retrieve**](JanusApi.md#pis_webrtc_streams_retrieve) | **GET** /api/pis/{pi_id}/webrtc-streams/{id}/ | 
[**pis_webrtc_streams_update**](JanusApi.md#pis_webrtc_streams_update) | **PUT** /api/pis/{pi_id}/webrtc-streams/{id}/ | 



## pis_webrtc_streams_create

> crate::models::WebrtcStream pis_webrtc_streams_create(pi_id, webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**webrtc_stream_request** | Option<[**WebrtcStreamRequest**](WebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_list

> crate::models::PaginatedWebrtcStreamList pis_webrtc_streams_list(pi_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedWebrtcStreamList**](PaginatedWebrtcStreamList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_partial_update

> crate::models::WebrtcStream pis_webrtc_streams_partial_update(id, pi_id, patched_webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |
**pi_id** | **i32** |  | [required] |
**patched_webrtc_stream_request** | Option<[**PatchedWebrtcStreamRequest**](PatchedWebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_retrieve

> crate::models::WebrtcStream pis_webrtc_streams_retrieve(id, pi_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |
**pi_id** | **i32** |  | [required] |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_webrtc_streams_update

> crate::models::WebrtcStream pis_webrtc_streams_update(id, pi_id, webrtc_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this webrtc stream. | [required] |
**pi_id** | **i32** |  | [required] |
**webrtc_stream_request** | Option<[**WebrtcStreamRequest**](WebrtcStreamRequest.md)> |  |  |

### Return type

[**crate::models::WebrtcStream**](WebrtcStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

