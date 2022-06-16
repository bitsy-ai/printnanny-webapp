# \LicensesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**license_verify**](LicensesApi.md#license_verify) | **POST** /api/license/verify/ | 



## license_verify

> crate::models::PrintNannyApiConfig license_verify(license_request)


Verifies that license key and email match Returns API credentials if license is inactive

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**license_request** | [**LicenseRequest**](LicenseRequest.md) |  | [required] |

### Return type

[**crate::models::PrintNannyApiConfig**](PrintNannyApiConfig.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

