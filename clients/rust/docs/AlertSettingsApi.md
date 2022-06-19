# \AlertSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_settings_get_or_create_retrieve**](AlertSettingsApi.md#alert_settings_get_or_create_retrieve) | **GET** /api/alert-settings/get-or-create/ | 
[**alert_settings_partial_update**](AlertSettingsApi.md#alert_settings_partial_update) | **PATCH** /api/alert-settings/{id}/ | 
[**alert_settings_update**](AlertSettingsApi.md#alert_settings_update) | **PUT** /api/alert-settings/{id}/ | 



## alert_settings_get_or_create_retrieve

> crate::models::AlertSettings alert_settings_get_or_create_retrieve()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AlertSettings**](AlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alert_settings_partial_update

> crate::models::AlertSettings alert_settings_partial_update(id, patched_alert_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this alert settings. | [required] |
**patched_alert_settings_request** | Option<[**PatchedAlertSettingsRequest**](PatchedAlertSettingsRequest.md)> |  |  |

### Return type

[**crate::models::AlertSettings**](AlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## alert_settings_update

> crate::models::AlertSettings alert_settings_update(id, alert_settings_request)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **i32** | A unique integer value identifying this alert settings. | [required] |
**alert_settings_request** | Option<[**AlertSettingsRequest**](AlertSettingsRequest.md)> |  |  |

### Return type

[**crate::models::AlertSettings**](AlertSettings.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

