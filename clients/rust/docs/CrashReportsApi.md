# \CrashReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crash_reports_create**](CrashReportsApi.md#crash_reports_create) | **POST** /api/crash-reports/ | 



## crash_reports_create

> crate::models::CrashReport crash_reports_create(email, os_version, os_logs, browser_version, browser_logs, user, pi)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**email** | Option<**String**> |  |  |
**os_version** | Option<**String**> |  |  |
**os_logs** | Option<**std::path::PathBuf**> |  |  |
**browser_version** | Option<**String**> |  |  |
**browser_logs** | Option<**std::path::PathBuf**> |  |  |
**user** | Option<**i32**> |  |  |
**pi** | Option<**i32**> |  |  |

### Return type

[**crate::models::CrashReport**](CrashReport.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

