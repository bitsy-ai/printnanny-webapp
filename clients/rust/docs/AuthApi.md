# \AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_email_create**](AuthApi.md#auth_email_create) | **POST** /auth/email/ | 
[**auth_mobile_create**](AuthApi.md#auth_mobile_create) | **POST** /auth/mobile/ | 
[**auth_token_create**](AuthApi.md#auth_token_create) | **POST** /auth/token/ | 
[**auth_verify_create**](AuthApi.md#auth_verify_create) | **POST** /auth/verify/ | 
[**auth_verify_email_create**](AuthApi.md#auth_verify_email_create) | **POST** /auth/verify/email/ | 
[**auth_verify_mobile_create**](AuthApi.md#auth_verify_mobile_create) | **POST** /auth/verify/mobile/ | 



## auth_email_create

> crate::models::DetailResponse auth_email_create(email_auth_request)


This returns a 6-digit callback token we can trade for a user's Auth Token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**email_auth_request** | [**EmailAuthRequest**](EmailAuthRequest.md) |  | [required] |

### Return type

[**crate::models::DetailResponse**](DetailResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## auth_mobile_create

> crate::models::DetailResponse auth_mobile_create(mobile_auth_request)


This returns a 6-digit callback token we can trade for a user's Auth Token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**mobile_auth_request** | [**MobileAuthRequest**](MobileAuthRequest.md) |  | [required] |

### Return type

[**crate::models::DetailResponse**](DetailResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## auth_token_create

> crate::models::TokenResponse auth_token_create(callback_token_auth_request)


This is a duplicate of rest_framework's own ObtainAuthToken method. Instead, this returns an Auth Token based on our callback token and source.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**callback_token_auth_request** | [**CallbackTokenAuthRequest**](CallbackTokenAuthRequest.md) |  | [required] |

### Return type

[**crate::models::TokenResponse**](TokenResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## auth_verify_create

> crate::models::CallbackTokenVerification auth_verify_create(callback_token_verification_request)


This verifies an alias on correct callback token entry using the same logic as auth. Should be refactored at some point.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**callback_token_verification_request** | [**CallbackTokenVerificationRequest**](CallbackTokenVerificationRequest.md) |  | [required] |

### Return type

[**crate::models::CallbackTokenVerification**](CallbackTokenVerification.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## auth_verify_email_create

> crate::models::DetailResponse auth_verify_email_create()


This returns a 6-digit callback token we can trade for a user's Auth Token.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::DetailResponse**](DetailResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## auth_verify_mobile_create

> crate::models::DetailResponse auth_verify_mobile_create()


This returns a 6-digit callback token we can trade for a user's Auth Token.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::DetailResponse**](DetailResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

