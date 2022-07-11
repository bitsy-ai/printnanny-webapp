# \JanusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_janus_streams_list**](JanusApi.md#devices_janus_streams_list) | **GET** /api/devices/{device_id}/janus-streams/ | 
[**devices_janus_streams_retrieve**](JanusApi.md#devices_janus_streams_retrieve) | **GET** /api/devices/{device_id}/janus-streams/{id}/ | 



## devices_janus_streams_list

> crate::models::PaginatedJanusStreamList devices_janus_streams_list(device_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedJanusStreamList**](PaginatedJanusStreamList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## devices_janus_streams_retrieve

> crate::models::JanusStream devices_janus_streams_retrieve(device_id, id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this janus stream. | [required] |

### Return type

[**crate::models::JanusStream**](JanusStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

