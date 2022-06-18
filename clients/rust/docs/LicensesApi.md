# \LicensesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**license_activate**](LicensesApi.md#license_activate) | **POST** /api/license/{id}/activate/ | 
[**license_verify**](LicensesApi.md#license_verify) | **POST** /api/license/verify/ | 



## license_activate

> crate::models::License license_activate(id, license_request)


Marks License as activated (by setting Device fkey relation)

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | A UUID string identifying this license. | [required] |
**license_request** | [**LicenseRequest**](LicenseRequest.md) |  | [required] |

### Return type

[**crate::models::License**](License.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


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

