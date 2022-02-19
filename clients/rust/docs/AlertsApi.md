# \AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_list**](AlertsApi.md#alerts_list) | **GET** /api/alerts/ | 
[**alerts_partial_update**](AlertsApi.md#alerts_partial_update) | **PATCH** /api/alerts/{id}/ | 
[**alerts_recent**](AlertsApi.md#alerts_recent) | **GET** /api/alerts/recent/ | 
[**alerts_retrieve**](AlertsApi.md#alerts_retrieve) | **GET** /api/alerts/{id}/ | 
[**alerts_seen**](AlertsApi.md#alerts_seen) | **PATCH** /api/alerts/seen/ | 
[**alerts_unread**](AlertsApi.md#alerts_unread) | **GET** /api/alerts/unread/ | 
[**alerts_update**](AlertsApi.md#alerts_update) | **PUT** /api/alerts/{id}/ | 



## alerts_list

> crate::models::PaginatedAlertList alerts_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedAlertList**](PaginatedAlertList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alerts_partial_update

> crate::models::Alert alerts_partial_update(id, patched_alert_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this alert message. | [required] |
**patched_alert_request** | Option<[**PatchedAlertRequest**](PatchedAlertRequest.md)> |  |  |

### Return type

[**crate::models::Alert**](Alert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


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


## alerts_retrieve

> crate::models::Alert alerts_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this alert message. | [required] |

### Return type

[**crate::models::Alert**](Alert.md)

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


## alerts_update

> crate::models::Alert alerts_update(id, alert_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this alert message. | [required] |
**alert_request** | Option<[**AlertRequest**](AlertRequest.md)> |  |  |

### Return type

[**crate::models::Alert**](Alert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

