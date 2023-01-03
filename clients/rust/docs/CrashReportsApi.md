# \CrashReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crash_reports_create**](CrashReportsApi.md#crash_reports_create) | **POST** /api/crash-reports/ | 



## crash_reports_create

> crate::models::CrashReport crash_reports_create(description, email, os_version, os_logs, browser_version, browser_logs, serial, posthog_session, user, pi, related_crash_report)


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
**user** | Option<**i32**> |  |  |
**pi** | Option<**i32**> |  |  |
**related_crash_report** | Option<**String**> |  |  |

### Return type

[**crate::models::CrashReport**](CrashReport.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

