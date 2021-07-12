# \AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_recent**](AlertsApi.md#alerts_recent) | **get** /api/alerts/recent/ | 
[**alerts_seen**](AlertsApi.md#alerts_seen) | **patch** /api/alerts/seen/ | 
[**alerts_unread**](AlertsApi.md#alerts_unread) | **get** /api/alerts/unread/ | 



## alerts_recent

> crate::models::AlertBulkResponse alerts_recent()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AlertBulkResponse**](AlertBulkResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alerts_seen

> crate::models::AlertBulkResponse alerts_seen(patched_alert_bulk_request_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**patched_alert_bulk_request_request** | Option<[**PatchedAlertBulkRequestRequest**](PatchedAlertBulkRequestRequest.md)> |  |  |

### Return type

[**crate::models::AlertBulkResponse**](AlertBulkResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alerts_unread

> crate::models::AlertBulkResponse alerts_unread()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AlertBulkResponse**](AlertBulkResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

