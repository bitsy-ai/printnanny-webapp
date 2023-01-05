# \CrashReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crash_reports_create**](CrashReportsApi.md#crash_reports_create) | **POST** /api/crash-reports/ | 
[**crash_reports_list**](CrashReportsApi.md#crash_reports_list) | **GET** /api/crash-reports/ | 
[**crash_reports_partial_update**](CrashReportsApi.md#crash_reports_partial_update) | **PATCH** /api/crash-reports/{id}/ | 
[**crash_reports_retrieve**](CrashReportsApi.md#crash_reports_retrieve) | **GET** /api/crash-reports/{id}/ | 
[**crash_reports_update**](CrashReportsApi.md#crash_reports_update) | **PUT** /api/crash-reports/{id}/ | 



## crash_reports_create

> crate::models::CrashReport crash_reports_create(description, email, os_version, os_logs, browser_version, browser_logs, serial, posthog_session, status, support_comment, user, pi)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**description** | Option<**String**> |  |  |
**email** | Option<**String**> |  |  |
**os_version** | Option<**String**> |  |  |
**os_logs** | Option<**std::path::PathBuf**> |  |  |
**browser_version** | Option<**String**> |  |  |
**browser_logs** | Option<**std::path::PathBuf**> |  |  |
**serial** | Option<**String**> |  |  |
**posthog_session** | Option<**String**> |  |  |
**status** | Option<[**crate::models::CrashReportStatusEnum**](CrashReportStatusEnum.md)> |  |  |
**support_comment** | Option<**String**> |  |  |
**user** | Option<**i32**> |  |  |
**pi** | Option<**i32**> |  |  |

### Return type

[**crate::models::CrashReport**](CrashReport.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## crash_reports_list

> crate::models::PaginatedCrashReportList crash_reports_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedCrashReportList**](PaginatedCrashReportList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## crash_reports_partial_update

> crate::models::CrashReport crash_reports_partial_update(id, description, email, os_version, os_logs, browser_version, browser_logs, serial, posthog_session, status, support_comment, user, pi)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this crash report. | [required] |
**description** | Option<**String**> |  |  |
**email** | Option<**String**> |  |  |
**os_version** | Option<**String**> |  |  |
**os_logs** | Option<**std::path::PathBuf**> |  |  |
**browser_version** | Option<**String**> |  |  |
**browser_logs** | Option<**std::path::PathBuf**> |  |  |
**serial** | Option<**String**> |  |  |
**posthog_session** | Option<**String**> |  |  |
**status** | Option<[**crate::models::CrashReportStatusEnum**](CrashReportStatusEnum.md)> |  |  |
**support_comment** | Option<**String**> |  |  |
**user** | Option<**i32**> |  |  |
**pi** | Option<**i32**> |  |  |

### Return type

[**crate::models::CrashReport**](CrashReport.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## crash_reports_retrieve

> crate::models::CrashReport crash_reports_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this crash report. | [required] |

### Return type

[**crate::models::CrashReport**](CrashReport.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## crash_reports_update

> crate::models::CrashReport crash_reports_update(id, description, email, os_version, os_logs, browser_version, browser_logs, serial, posthog_session, status, support_comment, user, pi)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this crash report. | [required] |
**description** | Option<**String**> |  |  |
**email** | Option<**String**> |  |  |
**os_version** | Option<**String**> |  |  |
**os_logs** | Option<**std::path::PathBuf**> |  |  |
**browser_version** | Option<**String**> |  |  |
**browser_logs** | Option<**std::path::PathBuf**> |  |  |
**serial** | Option<**String**> |  |  |
**posthog_session** | Option<**String**> |  |  |
**status** | Option<[**crate::models::CrashReportStatusEnum**](CrashReportStatusEnum.md)> |  |  |
**support_comment** | Option<**String**> |  |  |
**user** | Option<**i32**> |  |  |
**pi** | Option<**i32**> |  |  |

### Return type

[**crate::models::CrashReport**](CrashReport.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

