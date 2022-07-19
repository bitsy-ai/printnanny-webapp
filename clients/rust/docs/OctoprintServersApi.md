# \OctoprintServersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octoprint_servers_partial_update**](OctoprintServersApi.md#octoprint_servers_partial_update) | **PATCH** /api/octoprint-servers/{id}/ | 



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

