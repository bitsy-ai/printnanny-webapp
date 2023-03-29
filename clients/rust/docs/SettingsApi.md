# \SettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_alert_settings_create**](SettingsApi.md#email_alert_settings_create) | **POST** /api/email-alert-settings/ | 
[**email_alert_settings_partial_update**](SettingsApi.md#email_alert_settings_partial_update) | **PATCH** /api/email-alert-settings//{id} | 
[**email_alert_settings_retrieve**](SettingsApi.md#email_alert_settings_retrieve) | **GET** /api/email-alert-settings/ | 
[**email_alert_settings_update**](SettingsApi.md#email_alert_settings_update) | **PUT** /api/email-alert-settings//{id} | 



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

