# \AuthTokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_token_create**](AuthTokenApi.md#auth_token_create) | **post** /api/auth-token/ | 



## auth_token_create

> crate::models::AuthToken auth_token_create(username, password)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** |  | [required] |
**password** | **String** |  | [required] |

### Return type

[**crate::models::AuthToken**](AuthToken.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, multipart/form-data, application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

