# \MoonrakerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**moonraker_create**](MoonrakerApi.md#moonraker_create) | **POST** /api/moonraker/ | 
[**moonraker_list**](MoonrakerApi.md#moonraker_list) | **GET** /api/moonraker/ | 
[**moonraker_partial_update**](MoonrakerApi.md#moonraker_partial_update) | **PATCH** /api/moonraker/{id}/ | 
[**moonraker_retrieve**](MoonrakerApi.md#moonraker_retrieve) | **GET** /api/moonraker/{id}/ | 
[**moonraker_server_update_or_create**](MoonrakerApi.md#moonraker_server_update_or_create) | **POST** /api/moonraker/update-or-create/ | 
[**moonraker_update**](MoonrakerApi.md#moonraker_update) | **PUT** /api/moonraker/{id}/ | 
[**pis_moonraker_server_list**](MoonrakerApi.md#pis_moonraker_server_list) | **GET** /api/pis/{pi_id}/moonraker-server/ | 



## moonraker_create

> crate::models::MoonrakerServer moonraker_create(moonraker_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**moonraker_server_request** | [**MoonrakerServerRequest**](MoonrakerServerRequest.md) |  | [required] |

### Return type

[**crate::models::MoonrakerServer**](MoonrakerServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## moonraker_list

> crate::models::PaginatedMoonrakerServerList moonraker_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedMoonrakerServerList**](PaginatedMoonrakerServerList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## moonraker_partial_update

> crate::models::MoonrakerServer moonraker_partial_update(id, patched_moonraker_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this moonraker server. | [required] |
**patched_moonraker_server_request** | Option<[**PatchedMoonrakerServerRequest**](PatchedMoonrakerServerRequest.md)> |  |  |

### Return type

[**crate::models::MoonrakerServer**](MoonrakerServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## moonraker_retrieve

> crate::models::MoonrakerServer moonraker_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this moonraker server. | [required] |

### Return type

[**crate::models::MoonrakerServer**](MoonrakerServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## moonraker_server_update_or_create

> crate::models::MoonrakerServer moonraker_server_update_or_create(moonraker_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**moonraker_server_request** | [**MoonrakerServerRequest**](MoonrakerServerRequest.md) |  | [required] |

### Return type

[**crate::models::MoonrakerServer**](MoonrakerServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## moonraker_update

> crate::models::MoonrakerServer moonraker_update(id, moonraker_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this moonraker server. | [required] |
**moonraker_server_request** | [**MoonrakerServerRequest**](MoonrakerServerRequest.md) |  | [required] |

### Return type

[**crate::models::MoonrakerServer**](MoonrakerServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## pis_moonraker_server_list

> crate::models::PaginatedMoonrakerServerList pis_moonraker_server_list(pi_id, page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**pi_id** | **i32** |  | [required] |
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedMoonrakerServerList**](PaginatedMoonrakerServerList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

