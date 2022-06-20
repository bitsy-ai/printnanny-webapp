# \OctoprintServersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octoprint_servers_create**](OctoprintServersApi.md#octoprint_servers_create) | **POST** /api/octoprint-servers/ | 
[**octoprint_servers_list**](OctoprintServersApi.md#octoprint_servers_list) | **GET** /api/octoprint-servers/ | 
[**octoprint_servers_partial_update**](OctoprintServersApi.md#octoprint_servers_partial_update) | **PATCH** /api/octoprint-servers/{id}/ | 
[**octoprint_servers_update**](OctoprintServersApi.md#octoprint_servers_update) | **PUT** /api/octoprint-servers/{id}/ | 



## octoprint_servers_create

> crate::models::OctoPrintServer octoprint_servers_create(octo_print_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**octo_print_server_request** | [**OctoPrintServerRequest**](OctoPrintServerRequest.md) |  | [required] |

### Return type

[**crate::models::OctoPrintServer**](OctoPrintServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_servers_list

> crate::models::PaginatedOctoPrintServerList octoprint_servers_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedOctoPrintServerList**](PaginatedOctoPrintServerList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_servers_partial_update

> crate::models::OctoPrintServer octoprint_servers_partial_update(id, patched_octo_print_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print server. | [required] |
**patched_octo_print_server_request** | Option<[**PatchedOctoPrintServerRequest**](PatchedOctoPrintServerRequest.md)> |  |  |

### Return type

[**crate::models::OctoPrintServer**](OctoPrintServer.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## octoprint_servers_update

> octoprint_servers_update(id, octo_print_server_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this octo print server. | [required] |
**octo_print_server_request** | [**OctoPrintServerRequest**](OctoPrintServerRequest.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

