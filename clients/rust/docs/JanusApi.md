# \JanusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_janus_streams_create**](JanusApi.md#devices_janus_streams_create) | **POST** /api/devices/{device_id}/janus-streams/ | 
[**devices_janus_streams_list**](JanusApi.md#devices_janus_streams_list) | **GET** /api/devices/{device_id}/janus-streams/ | 
[**devices_janus_streams_retrieve**](JanusApi.md#devices_janus_streams_retrieve) | **GET** /api/devices/{device_id}/janus-streams/{id}/ | 
[**devices_janus_streams_update**](JanusApi.md#devices_janus_streams_update) | **PUT** /api/devices/{device_id}/janus-streams/{id}/ | 
[**users_janus_auth_create**](JanusApi.md#users_janus_auth_create) | **POST** /api/users/{user_id}/janus-auth/ | 
[**users_janus_auth_list**](JanusApi.md#users_janus_auth_list) | **GET** /api/users/{user_id}/janus-auth/ | 
[**users_janus_auth_retrieve**](JanusApi.md#users_janus_auth_retrieve) | **GET** /api/users/{user_id}/janus-auth/{id}/ | 
[**users_janus_auth_update_or_create**](JanusApi.md#users_janus_auth_update_or_create) | **POST** /api/users/{user_id}/janus-auth/update-or-create/ | 



## devices_janus_streams_create

> crate::models::JanusStream devices_janus_streams_create(device_id, janus_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**janus_stream_request** | [**JanusStreamRequest**](JanusStreamRequest.md) |  | [required] |

### Return type

[**crate::models::JanusStream**](JanusStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


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


## devices_janus_streams_update

> crate::models::JanusStream devices_janus_streams_update(device_id, id, janus_stream_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**device_id** | **i32** |  | [required] |
**id** | **i32** | A unique integer value identifying this janus stream. | [required] |
**janus_stream_request** | [**JanusStreamRequest**](JanusStreamRequest.md) |  | [required] |

### Return type

[**crate::models::JanusStream**](JanusStream.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_janus_auth_create

> crate::models::JanusAuth users_janus_auth_create(user_id, janus_auth_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**user_id** | **i32** |  | [required] |
**janus_auth_request** | [**JanusAuthRequest**](JanusAuthRequest.md) |  | [required] |

### Return type

[**crate::models::JanusAuth**](JanusAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_janus_auth_list

> crate::models::PaginatedJanusAuthList users_janus_auth_list(user_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**user_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedJanusAuthList**](PaginatedJanusAuthList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_janus_auth_retrieve

> crate::models::JanusAuth users_janus_auth_retrieve(id, user_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this janus auth. | [required] |
**user_id** | **i32** |  | [required] |

### Return type

[**crate::models::JanusAuth**](JanusAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## users_janus_auth_update_or_create

> crate::models::JanusAuth users_janus_auth_update_or_create(user_id, janus_auth_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**user_id** | **i32** |  | [required] |
**janus_auth_request** | [**JanusAuthRequest**](JanusAuthRequest.md) |  | [required] |

### Return type

[**crate::models::JanusAuth**](JanusAuth.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

