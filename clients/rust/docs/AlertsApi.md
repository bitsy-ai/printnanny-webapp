# \AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_print_job_create**](AlertsApi.md#alerts_print_job_create) | **POST** /api/alerts/print-job/ | 
[**alerts_print_job_list**](AlertsApi.md#alerts_print_job_list) | **GET** /api/alerts/print-job/ | 
[**alerts_print_job_partial_update**](AlertsApi.md#alerts_print_job_partial_update) | **PATCH** /api/alerts/print-job/{id}/ | 
[**alerts_print_job_retrieve**](AlertsApi.md#alerts_print_job_retrieve) | **GET** /api/alerts/print-job/{id}/ | 
[**alerts_print_job_update**](AlertsApi.md#alerts_print_job_update) | **PUT** /api/alerts/print-job/{id}/ | 
[**email_alert_settings_create**](AlertsApi.md#email_alert_settings_create) | **POST** /api/email-alert-settings/ | 
[**email_alert_settings_partial_update**](AlertsApi.md#email_alert_settings_partial_update) | **PATCH** /api/email-alert-settings/{id} | 
[**email_alert_settings_retrieve**](AlertsApi.md#email_alert_settings_retrieve) | **GET** /api/email-alert-settings/ | 
[**email_alert_settings_update**](AlertsApi.md#email_alert_settings_update) | **PUT** /api/email-alert-settings/{id} | 



## alerts_print_job_create

> crate::models::PrintJobAlert alerts_print_job_create(print_job_alert_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**print_job_alert_request** | [**PrintJobAlertRequest**](PrintJobAlertRequest.md) |  | [required] |

### Return type

[**crate::models::PrintJobAlert**](PrintJobAlert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alerts_print_job_list

> crate::models::PaginatedPrintJobAlertList alerts_print_job_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedPrintJobAlertList**](PaginatedPrintJobAlertList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alerts_print_job_partial_update

> crate::models::PrintJobAlert alerts_print_job_partial_update(id, patched_print_job_alert_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this print job alert. | [required] |
**patched_print_job_alert_request** | Option<[**PatchedPrintJobAlertRequest**](PatchedPrintJobAlertRequest.md)> |  |  |

### Return type

[**crate::models::PrintJobAlert**](PrintJobAlert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alerts_print_job_retrieve

> crate::models::PrintJobAlert alerts_print_job_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this print job alert. | [required] |

### Return type

[**crate::models::PrintJobAlert**](PrintJobAlert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alerts_print_job_update

> crate::models::PrintJobAlert alerts_print_job_update(id, print_job_alert_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this print job alert. | [required] |
**print_job_alert_request** | [**PrintJobAlertRequest**](PrintJobAlertRequest.md) |  | [required] |

### Return type

[**crate::models::PrintJobAlert**](PrintJobAlert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## email_alert_settings_create

> crate::models::EmailAlertSettings email_alert_settings_create(email_alert_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**email_alert_settings_request** | Option<[**EmailAlertSettingsRequest**](EmailAlertSettingsRequest.md)> |  |  |

### Return type

[**crate::models::EmailAlertSettings**](EmailAlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## email_alert_settings_partial_update

> crate::models::EmailAlertSettings email_alert_settings_partial_update(id, patched_email_alert_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** |  | [required] |
**patched_email_alert_settings_request** | Option<[**PatchedEmailAlertSettingsRequest**](PatchedEmailAlertSettingsRequest.md)> |  |  |

### Return type

[**crate::models::EmailAlertSettings**](EmailAlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## email_alert_settings_retrieve

> crate::models::EmailAlertSettings email_alert_settings_retrieve()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::EmailAlertSettings**](EmailAlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## email_alert_settings_update

> crate::models::EmailAlertSettings email_alert_settings_update(id, email_alert_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** |  | [required] |
**email_alert_settings_request** | Option<[**EmailAlertSettingsRequest**](EmailAlertSettingsRequest.md)> |  |  |

### Return type

[**crate::models::EmailAlertSettings**](EmailAlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

