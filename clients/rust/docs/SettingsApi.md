# \SettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_settings_email_create**](SettingsApi.md#alert_settings_email_create) | **POST** /api/alert-settings/email/ | 
[**alert_settings_email_list**](SettingsApi.md#alert_settings_email_list) | **GET** /api/alert-settings/email/ | 
[**alert_settings_email_partial_update**](SettingsApi.md#alert_settings_email_partial_update) | **PATCH** /api/alert-settings/email/{id}/ | 
[**alert_settings_email_retrieve**](SettingsApi.md#alert_settings_email_retrieve) | **GET** /api/alert-settings/email/{id}/ | 
[**alert_settings_email_update**](SettingsApi.md#alert_settings_email_update) | **PUT** /api/alert-settings/email/{id}/ | 



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

