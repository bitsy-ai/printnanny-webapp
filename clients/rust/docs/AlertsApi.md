# \AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_settings_email_create**](AlertsApi.md#alert_settings_email_create) | **POST** /api/alert-settings/email/ | 
[**alert_settings_email_list**](AlertsApi.md#alert_settings_email_list) | **GET** /api/alert-settings/email/ | 
[**alert_settings_email_partial_update**](AlertsApi.md#alert_settings_email_partial_update) | **PATCH** /api/alert-settings/email/{id}/ | 
[**alert_settings_email_retrieve**](AlertsApi.md#alert_settings_email_retrieve) | **GET** /api/alert-settings/email/{id}/ | 
[**alert_settings_email_update**](AlertsApi.md#alert_settings_email_update) | **PUT** /api/alert-settings/email/{id}/ | 
[**alerts_print_job_create**](AlertsApi.md#alerts_print_job_create) | **POST** /api/alerts/print-job/ | 
[**alerts_print_job_list**](AlertsApi.md#alerts_print_job_list) | **GET** /api/alerts/print-job/ | 
[**alerts_print_job_partial_update**](AlertsApi.md#alerts_print_job_partial_update) | **PATCH** /api/alerts/print-job/{id}/ | 
[**alerts_print_job_retrieve**](AlertsApi.md#alerts_print_job_retrieve) | **GET** /api/alerts/print-job/{id}/ | 
[**alerts_print_job_update**](AlertsApi.md#alerts_print_job_update) | **PUT** /api/alerts/print-job/{id}/ | 



## alert_settings_email_create

> crate::models::EmailAlertSettings alert_settings_email_create(email_alert_settings_request)


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


## alert_settings_email_list

> crate::models::PaginatedEmailAlertSettingsList alert_settings_email_list(page)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**page** | Option<**i32**> | A page number within the paginated result set. |  |

### Return type

[**crate::models::PaginatedEmailAlertSettingsList**](PaginatedEmailAlertSettingsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alert_settings_email_partial_update

> crate::models::EmailAlertSettings alert_settings_email_partial_update(id, patched_email_alert_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this email alert settings. | [required] |
**patched_email_alert_settings_request** | Option<[**PatchedEmailAlertSettingsRequest**](PatchedEmailAlertSettingsRequest.md)> |  |  |

### Return type

[**crate::models::EmailAlertSettings**](EmailAlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alert_settings_email_retrieve

> crate::models::EmailAlertSettings alert_settings_email_retrieve(id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this email alert settings. | [required] |

### Return type

[**crate::models::EmailAlertSettings**](EmailAlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alert_settings_email_update

> crate::models::EmailAlertSettings alert_settings_email_update(id, email_alert_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this email alert settings. | [required] |
**email_alert_settings_request** | Option<[**EmailAlertSettingsRequest**](EmailAlertSettingsRequest.md)> |  |  |

### Return type

[**crate::models::EmailAlertSettings**](EmailAlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alerts_print_job_create

> crate::models::PrintJobAlert alerts_print_job_create(event_type, event_source, pi, image)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**event_type** | [**crate::models::EventTypeEnum**](EventTypeEnum.md) |  | [required] |
**event_source** | [**crate::models::EventSourceEnum**](EventSourceEnum.md) |  | [required] |
**pi** | **i32** |  | [required] |
**image** | Option<**std::path::PathBuf**> |  |  |

### Return type

[**crate::models::PrintJobAlert**](PrintJobAlert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
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

> crate::models::PrintJobAlert alerts_print_job_partial_update(id, event_type, event_source, image, pi)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this print job alert. | [required] |
**event_type** | Option<[**crate::models::EventTypeEnum**](EventTypeEnum.md)> |  |  |
**event_source** | Option<[**crate::models::EventSourceEnum**](EventSourceEnum.md)> |  |  |
**image** | Option<**std::path::PathBuf**> |  |  |
**pi** | Option<**i32**> |  |  |

### Return type

[**crate::models::PrintJobAlert**](PrintJobAlert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
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

> crate::models::PrintJobAlert alerts_print_job_update(id, event_type, event_source, pi, image)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this print job alert. | [required] |
**event_type** | [**crate::models::EventTypeEnum**](EventTypeEnum.md) |  | [required] |
**event_source** | [**crate::models::EventSourceEnum**](EventSourceEnum.md) |  | [required] |
**pi** | **i32** |  | [required] |
**image** | Option<**std::path::PathBuf**> |  |  |

### Return type

[**crate::models::PrintJobAlert**](PrintJobAlert.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

